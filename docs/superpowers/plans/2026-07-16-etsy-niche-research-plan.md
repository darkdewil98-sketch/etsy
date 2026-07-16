# Etsy Niche Research Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a weekly, data-driven Etsy niche/opportunity research tool that pulls real Google
Trends signals, scores opportunities with a deterministic formula, and writes both a human-readable
CSV report and a machine-readable JSON file for the next pipeline stage (Canva mockup generation).

**Architecture:** A small set of single-responsibility Python modules (`scorer`, `etsy_adapter`,
`trends_client`, `report_writer`) with all external I/O behind injectable interfaces, orchestrated by
`run_research.py`. Every module with logic is unit-tested with fakes — no real network calls in the
automated test suite.

**Tech Stack:** Python 3.10+, `pytrends` (Google Trends client), `pandas` (pytrends dependency),
`PyYAML` (seed config), `pytest` (testing).

## Global Constraints

- Python 3.10+ required (plan uses `int | None` union type hints).
- All external I/O (Google Trends, Etsy data) must be dependency-injected so business logic is
  unit-testable without network access — per spec's "no automated network calls in CI" rule.
- Every run must produce both `reports/<week>.csv` (human) and `data/opportunities.json` (machine) —
  per spec's dual-output requirement.
- Scoring is 100% deterministic math on real fetched numbers — no AI/LLM estimation anywhere in the
  scoring path, per spec's "veriye dayalı, tahmini değil" principle.
- The Etsy data source is a swappable adapter (stub today, real Etsy API implementation later)
  without changing any caller — per spec's phased-Etsy-API-rollout decision.
- Google Trends calls must retry with exponential backoff on failure and skip-and-continue on a
  single keyword's permanent failure rather than aborting the whole run — per spec's error handling
  section.

---

### Task 1: Scorer module (pure scoring logic)

**Files:**
- Create: `requirements.txt`
- Create: `etsy_research/__init__.py`
- Create: `etsy_research/scorer.py`
- Test: `tests/test_scorer.py`

**Interfaces:**
- Produces: `compute_trend_growth_rate(interest_over_time: list[int]) -> float`
- Produces: `normalize_volume(volume: float, max_volume: float) -> float`
- Produces: `compute_opportunity_score(trend_growth_rate: float, trend_volume_normalized: float, competition_count: int | None = None) -> float`

- [ ] **Step 1: Create project scaffolding**

Create `requirements.txt`:
```
pytest>=7.4
```

Create `etsy_research/__init__.py` (empty file).

- [ ] **Step 2: Write the failing tests**

Create `tests/test_scorer.py`:
```python
from etsy_research.scorer import (
    compute_opportunity_score,
    compute_trend_growth_rate,
    normalize_volume,
)


def test_compute_trend_growth_rate_rising_trend():
    assert compute_trend_growth_rate([10, 10, 20, 30]) == 2.5


def test_compute_trend_growth_rate_falling_trend():
    assert compute_trend_growth_rate([40, 40, 10, 10]) == 0.25


def test_compute_trend_growth_rate_too_short():
    assert compute_trend_growth_rate([10]) == 0.0


def test_compute_trend_growth_rate_zero_baseline():
    assert compute_trend_growth_rate([0, 0, 5, 5]) == 5.0


def test_normalize_volume():
    assert normalize_volume(50, 100) == 0.5


def test_normalize_volume_zero_max():
    assert normalize_volume(0, 0) == 0.0


def test_compute_opportunity_score_no_competition():
    assert compute_opportunity_score(2.0, 0.5, None) == 1.0


def test_compute_opportunity_score_with_competition():
    assert compute_opportunity_score(2.0, 0.5, competition_count=5) == 0.2
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest tests/test_scorer.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'etsy_research.scorer'`

- [ ] **Step 4: Implement the scorer**

Create `etsy_research/scorer.py`:
```python
"""Deterministic, data-driven opportunity scoring. No estimation, no AI guesses."""


def compute_trend_growth_rate(interest_over_time: list[int]) -> float:
    """Ratio of second-half average to first-half average of a real interest series.

    >1.0 means rising interest, <1.0 means falling. If the series starts at zero,
    returns the raw second-half average (growth from nothing can't be a ratio).
    """
    if len(interest_over_time) < 2:
        return 0.0

    midpoint = len(interest_over_time) // 2
    first_half = interest_over_time[:midpoint]
    second_half = interest_over_time[midpoint:]
    first_avg = sum(first_half) / len(first_half)
    second_avg = sum(second_half) / len(second_half)

    if first_avg == 0:
        return float(second_avg)
    return second_avg / first_avg


def normalize_volume(volume: float, max_volume: float) -> float:
    """Scales a raw volume figure to a 0-1 range relative to the batch's max."""
    if max_volume == 0:
        return 0.0
    return volume / max_volume


def compute_opportunity_score(
    trend_growth_rate: float,
    trend_volume_normalized: float,
    competition_count: int | None = None,
) -> float:
    """Higher score = more growth and volume, divided by competition when known."""
    score = trend_growth_rate * trend_volume_normalized
    if competition_count:
        score = score / competition_count
    return score
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_scorer.py -v`
Expected: PASS (8 passed)

- [ ] **Step 6: Commit**

```bash
git add requirements.txt etsy_research/__init__.py etsy_research/scorer.py tests/test_scorer.py
git commit -m "feat: add deterministic opportunity scorer"
```

---

### Task 2: Etsy data adapter (stub interface)

**Files:**
- Create: `etsy_research/etsy_adapter.py`
- Test: `tests/test_etsy_adapter.py`

**Interfaces:**
- Consumes: nothing
- Produces: `EtsyAdapter.get_competition_count(keyword: str) -> int | None` (used by Task 5's orchestrator)

- [ ] **Step 1: Write the failing test**

Create `tests/test_etsy_adapter.py`:
```python
from etsy_research.etsy_adapter import EtsyAdapter


def test_get_competition_count_returns_none_until_etsy_api_is_wired_up():
    adapter = EtsyAdapter()
    assert adapter.get_competition_count("t-shirt design") is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_etsy_adapter.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'etsy_research.etsy_adapter'`

- [ ] **Step 3: Implement the stub adapter**

Create `etsy_research/etsy_adapter.py`:
```python
"""Etsy competition-data source.

Stub until the Etsy Developer API key/OAuth application is approved. Callers must
treat `None` as "competition data unavailable" and skip the competition adjustment
(see etsy_research.scorer.compute_opportunity_score). Swap the body of
get_competition_count for a real Etsy Open API call later without changing this
class's interface or any caller.
"""


class EtsyAdapter:
    def get_competition_count(self, keyword: str) -> int | None:
        return None
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_etsy_adapter.py -v`
Expected: PASS (1 passed)

- [ ] **Step 5: Commit**

```bash
git add etsy_research/etsy_adapter.py tests/test_etsy_adapter.py
git commit -m "feat: add Etsy data adapter stub"
```

---

### Task 3: Google Trends client (with retry/backoff)

**Files:**
- Modify: `requirements.txt`
- Create: `etsy_research/trends_client.py`
- Test: `tests/test_trends_client.py`

**Interfaces:**
- Consumes: any object exposing `build_payload(keywords, timeframe)`, `interest_over_time()`,
  `related_queries()` (matches `pytrends.request.TrendReq`'s interface)
- Produces: `TrendsClient(pytrends_client, request_delay_seconds=1.0, max_retries=3, backoff_base_seconds=2.0)`
  with `.get_interest_over_time(keyword: str) -> list[int]` and
  `.get_rising_queries(keyword: str) -> list[str]`
- Produces: `TrendsClientError` exception, raised when all retries are exhausted (consumed by Task 5)

- [ ] **Step 1: Add dependencies**

Append to `requirements.txt`:
```
pandas>=2.0
pytrends>=4.9
```

Run: `pip install -r requirements.txt`

- [ ] **Step 2: Write the failing tests**

Create `tests/test_trends_client.py`:
```python
import pandas as pd
import pytest

from etsy_research.trends_client import TrendsClient, TrendsClientError


class FakePyTrends:
    def __init__(self, interest_frames=None, related_frames=None, fail_times=0):
        self.interest_frames = interest_frames or {}
        self.related_frames = related_frames or {}
        self.fail_times = fail_times
        self.calls = 0
        self.last_keywords = None

    def build_payload(self, keywords, timeframe):
        self.last_keywords = keywords

    def interest_over_time(self):
        self.calls += 1
        if self.calls <= self.fail_times:
            raise RuntimeError("429 rate limited")
        return self.interest_frames[self.last_keywords[0]]

    def related_queries(self):
        return self.related_frames[self.last_keywords[0]]


def test_get_interest_over_time_returns_values_from_dataframe():
    fake = FakePyTrends(interest_frames={"t-shirt design": pd.DataFrame({"t-shirt design": [10, 20, 30]})})
    client = TrendsClient(fake, request_delay_seconds=0)

    assert client.get_interest_over_time("t-shirt design") == [10, 20, 30]


def test_get_interest_over_time_returns_empty_list_for_empty_dataframe():
    fake = FakePyTrends(interest_frames={"obscure term": pd.DataFrame()})
    client = TrendsClient(fake, request_delay_seconds=0)

    assert client.get_interest_over_time("obscure term") == []


def test_get_interest_over_time_retries_then_succeeds():
    fake = FakePyTrends(
        interest_frames={"t-shirt design": pd.DataFrame({"t-shirt design": [5, 15]})},
        fail_times=2,
    )
    client = TrendsClient(fake, request_delay_seconds=0, max_retries=3, backoff_base_seconds=0)

    assert client.get_interest_over_time("t-shirt design") == [5, 15]
    assert fake.calls == 3


def test_get_interest_over_time_raises_after_exhausting_retries():
    fake = FakePyTrends(interest_frames={}, fail_times=5)
    client = TrendsClient(fake, request_delay_seconds=0, max_retries=3, backoff_base_seconds=0)

    with pytest.raises(TrendsClientError):
        client.get_interest_over_time("t-shirt design")


def test_get_rising_queries_returns_query_list():
    fake = FakePyTrends(
        related_frames={
            "t-shirt design": {"rising": pd.DataFrame({"query": ["funny cat shirt"], "value": [250]})}
        }
    )
    client = TrendsClient(fake, request_delay_seconds=0)

    assert client.get_rising_queries("t-shirt design") == ["funny cat shirt"]


def test_get_rising_queries_returns_empty_list_when_no_rising_data():
    fake = FakePyTrends(related_frames={"quiet term": {"rising": pd.DataFrame()}})
    client = TrendsClient(fake, request_delay_seconds=0)

    assert client.get_rising_queries("quiet term") == []
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest tests/test_trends_client.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'etsy_research.trends_client'`

- [ ] **Step 4: Implement the trends client**

Create `etsy_research/trends_client.py`:
```python
"""Thin, retrying wrapper around a pytrends-shaped client for real Google Trends data."""
import time


class TrendsClientError(Exception):
    """Raised when a Trends request fails after all retries are exhausted."""


class TrendsClient:
    def __init__(
        self,
        pytrends_client,
        request_delay_seconds: float = 1.0,
        max_retries: int = 3,
        backoff_base_seconds: float = 2.0,
    ):
        self._client = pytrends_client
        self._request_delay_seconds = request_delay_seconds
        self._max_retries = max_retries
        self._backoff_base_seconds = backoff_base_seconds

    def _call_with_retry(self, func):
        last_error: Exception | None = None
        for attempt in range(self._max_retries):
            try:
                result = func()
                time.sleep(self._request_delay_seconds)
                return result
            except Exception as error:  # noqa: BLE001 - pytrends raises plain Exceptions/HTTPError
                last_error = error
                time.sleep(self._backoff_base_seconds**attempt)
        raise TrendsClientError(f"Failed after {self._max_retries} retries: {last_error}")

    def get_interest_over_time(self, keyword: str) -> list[int]:
        self._client.build_payload([keyword], timeframe="today 3-m")
        df = self._call_with_retry(self._client.interest_over_time)
        if df.empty:
            return []
        return df[keyword].tolist()

    def get_rising_queries(self, keyword: str) -> list[str]:
        self._client.build_payload([keyword], timeframe="today 3-m")
        related = self._call_with_retry(self._client.related_queries)
        rising_df = related.get("rising")
        if rising_df is None or rising_df.empty:
            return []
        return rising_df["query"].tolist()
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_trends_client.py -v`
Expected: PASS (6 passed)

- [ ] **Step 6: Commit**

```bash
git add requirements.txt etsy_research/trends_client.py tests/test_trends_client.py
git commit -m "feat: add Google Trends client with retry/backoff"
```

---

### Task 4: Report writer (CSV + JSON dual output)

**Files:**
- Create: `etsy_research/report_writer.py`
- Test: `tests/test_report_writer.py`

**Interfaces:**
- Consumes: `list[dict]` where each dict has keys `keyword, category, score, trend_growth_rate,
  trend_volume, competition_count` (matches the shape Task 5 will produce)
- Produces: `write_reports(opportunities: list[dict], csv_path: Path, json_path: Path) -> None`

- [ ] **Step 1: Write the failing test**

Create `tests/test_report_writer.py`:
```python
import csv
import json

from etsy_research.report_writer import write_reports


def test_write_reports_creates_csv_and_json(tmp_path):
    opportunities = [
        {
            "keyword": "funny cat shirt",
            "category": "clothing",
            "score": 1.5,
            "trend_growth_rate": 2.0,
            "trend_volume": 80,
            "competition_count": None,
        },
        {
            "keyword": "wall art",
            "category": "home_decor",
            "score": 0.8,
            "trend_growth_rate": 1.2,
            "trend_volume": 40,
            "competition_count": 10,
        },
    ]
    csv_path = tmp_path / "reports" / "2026-W29.csv"
    json_path = tmp_path / "data" / "opportunities.json"

    write_reports(opportunities, csv_path, json_path)

    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert rows[0]["keyword"] == "funny cat shirt"
    assert rows[1]["keyword"] == "wall art"

    with open(json_path, encoding="utf-8") as f:
        loaded = json.load(f)
    assert loaded == opportunities
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_report_writer.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'etsy_research.report_writer'`

- [ ] **Step 3: Implement the report writer**

Create `etsy_research/report_writer.py`:
```python
"""Writes scored opportunities to both a human CSV report and a machine JSON file."""
import csv
import json
from pathlib import Path

FIELDNAMES = ["keyword", "category", "score", "trend_growth_rate", "trend_volume", "competition_count"]


def write_reports(opportunities: list[dict], csv_path: Path, json_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for opportunity in opportunities:
            writer.writerow(opportunity)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(opportunities, f, indent=2, ensure_ascii=False)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_report_writer.py -v`
Expected: PASS (1 passed)

- [ ] **Step 5: Commit**

```bash
git add etsy_research/report_writer.py tests/test_report_writer.py
git commit -m "feat: add CSV+JSON report writer"
```

---

### Task 5: Seeds config + orchestrator

**Files:**
- Modify: `requirements.txt`
- Create: `seeds.yaml`
- Create: `run_research.py`
- Test: `tests/test_run_research.py`

**Interfaces:**
- Consumes: `TrendsClient.get_interest_over_time`, `TrendsClient.get_rising_queries`,
  `TrendsClientError` (Task 3); `EtsyAdapter.get_competition_count` (Task 2);
  `compute_trend_growth_rate`, `normalize_volume`, `compute_opportunity_score` (Task 1);
  `write_reports` (Task 4)
- Produces: `build_opportunities(seeds: dict, trends_client, etsy_adapter) -> tuple[list[dict], dict]`
  where the summary dict has keys `seeds_scanned, opportunities_found, errors`; `main()` CLI entrypoint

- [ ] **Step 1: Add PyYAML dependency**

Append to `requirements.txt`:
```
PyYAML>=6.0
```

Run: `pip install -r requirements.txt`

- [ ] **Step 2: Create the seed keyword config**

Create `seeds.yaml`:
```yaml
clothing:
  - "t-shirt design"
  - "hoodie print"
home_decor:
  - "wall art"
  - "mug design"
digital_downloads:
  - "planner printable"
  - "svg bundle"
```

- [ ] **Step 3: Write the failing tests**

Create `tests/test_run_research.py`:
```python
from etsy_research.trends_client import TrendsClientError
from run_research import build_opportunities


class FakeTrendsClient:
    def __init__(self, interest_by_keyword, rising_by_keyword=None, fail_keywords=None):
        self.interest_by_keyword = interest_by_keyword
        self.rising_by_keyword = rising_by_keyword or {}
        self.fail_keywords = fail_keywords or set()

    def get_interest_over_time(self, keyword):
        if keyword in self.fail_keywords:
            raise TrendsClientError(f"simulated failure for {keyword}")
        return self.interest_by_keyword.get(keyword, [])

    def get_rising_queries(self, keyword):
        return self.rising_by_keyword.get(keyword, [])


class FakeEtsyAdapter:
    def get_competition_count(self, keyword):
        return None


def test_build_opportunities_scores_and_sorts_by_score_descending():
    seeds = {"clothing": ["t-shirt design"]}
    trends_client = FakeTrendsClient(
        interest_by_keyword={
            "t-shirt design": [10, 10, 20, 20],
            "funny cat shirt": [0, 0, 40, 40],
        },
        rising_by_keyword={"t-shirt design": ["funny cat shirt"]},
    )

    opportunities, summary = build_opportunities(seeds, trends_client, FakeEtsyAdapter())

    assert summary == {"seeds_scanned": 1, "opportunities_found": 2, "errors": 0}
    assert opportunities[0]["keyword"] == "funny cat shirt"
    assert opportunities[1]["keyword"] == "t-shirt design"


def test_build_opportunities_skips_failed_keyword_without_crashing():
    seeds = {"clothing": ["t-shirt design"], "home_decor": ["wall art"]}
    trends_client = FakeTrendsClient(
        interest_by_keyword={"wall art": [10, 10, 15, 15]},
        fail_keywords={"t-shirt design"},
    )

    opportunities, summary = build_opportunities(seeds, trends_client, FakeEtsyAdapter())

    assert summary == {"seeds_scanned": 2, "opportunities_found": 1, "errors": 1}
    assert opportunities[0]["keyword"] == "wall art"


def test_build_opportunities_does_not_duplicate_rising_keyword_seen_twice():
    seeds = {"clothing": ["t-shirt design"], "home_decor": ["hoodie print"]}
    trends_client = FakeTrendsClient(
        interest_by_keyword={
            "t-shirt design": [10, 10, 10, 10],
            "hoodie print": [10, 10, 10, 10],
            "funny cat shirt": [0, 0, 20, 20],
        },
        rising_by_keyword={
            "t-shirt design": ["funny cat shirt"],
            "hoodie print": ["funny cat shirt"],
        },
    )

    opportunities, summary = build_opportunities(seeds, trends_client, FakeEtsyAdapter())

    keywords = [o["keyword"] for o in opportunities]
    assert keywords.count("funny cat shirt") == 1
    assert summary["opportunities_found"] == 3
```

- [ ] **Step 4: Run tests to verify they fail**

Run: `python -m pytest tests/test_run_research.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'run_research'`

- [ ] **Step 5: Implement the orchestrator**

Create `run_research.py`:
```python
"""Weekly orchestrator: seeds -> Google Trends -> scoring -> CSV+JSON reports."""
import argparse
import logging
import time
from pathlib import Path

import yaml
from pytrends.request import TrendReq

from etsy_research.etsy_adapter import EtsyAdapter
from etsy_research.report_writer import write_reports
from etsy_research.scorer import (
    compute_opportunity_score,
    compute_trend_growth_rate,
    normalize_volume,
)
from etsy_research.trends_client import TrendsClient, TrendsClientError

logger = logging.getLogger(__name__)


def load_seeds(seeds_path: Path) -> dict:
    with open(seeds_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_opportunities(seeds: dict, trends_client, etsy_adapter) -> tuple[list[dict], dict]:
    candidates: list[tuple[str, str]] = [
        (category, keyword) for category, keywords in seeds.items() for keyword in keywords
    ]
    seen_keywords = {keyword for _, keyword in candidates}

    errors = 0
    raw_signals: list[dict] = []
    for category, keyword in candidates:
        try:
            interest = trends_client.get_interest_over_time(keyword)
            rising = trends_client.get_rising_queries(keyword)
        except TrendsClientError as error:
            logger.warning("Skipping %r after trends failure: %s", keyword, error)
            errors += 1
            continue

        raw_signals.append({"category": category, "keyword": keyword, "interest_over_time": interest})

        for rising_keyword in rising:
            if rising_keyword in seen_keywords:
                continue
            seen_keywords.add(rising_keyword)
            try:
                rising_interest = trends_client.get_interest_over_time(rising_keyword)
            except TrendsClientError as error:
                logger.warning("Skipping rising keyword %r after trends failure: %s", rising_keyword, error)
                errors += 1
                continue
            raw_signals.append(
                {"category": category, "keyword": rising_keyword, "interest_over_time": rising_interest}
            )

    current_volumes = [
        signal["interest_over_time"][-1] if signal["interest_over_time"] else 0 for signal in raw_signals
    ]
    max_volume = max(current_volumes, default=0)

    opportunities = []
    for signal, current_volume in zip(raw_signals, current_volumes):
        growth_rate = compute_trend_growth_rate(signal["interest_over_time"])
        volume_normalized = normalize_volume(current_volume, max_volume)
        competition_count = etsy_adapter.get_competition_count(signal["keyword"])
        score = compute_opportunity_score(growth_rate, volume_normalized, competition_count)
        opportunities.append(
            {
                "keyword": signal["keyword"],
                "category": signal["category"],
                "score": round(score, 4),
                "trend_growth_rate": round(growth_rate, 4),
                "trend_volume": current_volume,
                "competition_count": competition_count,
            }
        )

    opportunities.sort(key=lambda o: o["score"], reverse=True)
    summary = {
        "seeds_scanned": len(candidates),
        "opportunities_found": len(opportunities),
        "errors": errors,
    }
    return opportunities, summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", default="seeds.yaml")
    parser.add_argument("--reports-dir", default="reports")
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--logs-dir", default="logs")
    args = parser.parse_args()

    week_id = time.strftime("%G-W%V")
    logs_dir = Path(args.logs_dir)
    logs_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(filename=logs_dir / f"{week_id}.log", level=logging.INFO)

    seeds = load_seeds(Path(args.seeds))
    trends_client = TrendsClient(TrendReq(hl="en-US", tz=360))
    etsy_adapter = EtsyAdapter()

    opportunities, summary = build_opportunities(seeds, trends_client, etsy_adapter)

    write_reports(
        opportunities,
        csv_path=Path(args.reports_dir) / f"{week_id}.csv",
        json_path=Path(args.data_dir) / "opportunities.json",
    )

    logger.info("Run summary: %s", summary)


if __name__ == "__main__":
    main()
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `python -m pytest tests/test_run_research.py -v`
Expected: PASS (3 passed)

- [ ] **Step 7: Run the full test suite**

Run: `python -m pytest -v`
Expected: PASS (all tests from Tasks 1-5 pass, no network calls made)

- [ ] **Step 8: Commit**

```bash
git add requirements.txt seeds.yaml run_research.py tests/test_run_research.py
git commit -m "feat: add seeds config and research orchestrator"
```

---

### Task 6: Weekly scheduling + manual smoke test

**Files:**
- Create: `README.md`
- Create: `tests/manual_smoke_test.py`

**Interfaces:**
- Consumes: `run_research.main` indirectly via CLI invocation (documentation only, no new code interfaces)

- [ ] **Step 1: Create a manual (non-CI) smoke test against real Google Trends**

Create `tests/manual_smoke_test.py`:
```python
"""Manual smoke test against real Google Trends. NOT run by the automated suite
(no test_ prefix on the filename) because Google Trends rate-limits aggressively.

Run manually with: python tests/manual_smoke_test.py
"""
from pytrends.request import TrendReq

from etsy_research.trends_client import TrendsClient


def main() -> None:
    client = TrendsClient(TrendReq(hl="en-US", tz=360))
    interest = client.get_interest_over_time("t-shirt design")
    rising = client.get_rising_queries("t-shirt design")
    print(f"interest_over_time (last 5 points): {interest[-5:]}")
    print(f"rising queries: {rising}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the manual smoke test**

Run: `python tests/manual_smoke_test.py`
Expected: prints a non-empty list of numbers for interest and a (possibly empty) list of rising
queries, with no exception raised. If it fails with a 429, wait a few minutes and retry — this
confirms live Google Trends connectivity, it is not part of the automated suite.

- [ ] **Step 3: Document setup and weekly scheduling**

Create `README.md`:
```markdown
# Etsy Niche Research Engine

Weekly, data-driven Etsy niche opportunity research. Pulls real Google Trends signals, scores
opportunities with a deterministic formula (no AI estimation), and writes:

- `reports/<year>-W<week>.csv` — human-readable report
- `data/opportunities.json` — machine-readable, consumed by the next pipeline stage (Canva mockup
  generation)

## Setup

1. Install Python 3.10+.
2. `pip install -r requirements.txt`
3. Edit `seeds.yaml` to adjust starting keywords per category.

## Run manually

```
python run_research.py
```

## Run the test suite

```
python -m pytest -v
```

## Schedule weekly runs (Windows Task Scheduler)

Run once, from an elevated PowerShell prompt, adjusting the path to your Python and repo location:

```
schtasks /create /tn "EtsyNicheResearch" /tr "python C:\Users\HUAWEI\etsy\run_research.py" /sc weekly /d MON /st 09:00
```

Verify it was registered:

```
schtasks /query /tn "EtsyNicheResearch"
```

## Etsy API (not yet wired up)

`etsy_research/etsy_adapter.py` is a stub that always returns `None` for competition data. Once the
Etsy Developer API key/OAuth application is approved, replace its implementation with real Etsy
Open API calls — no other module needs to change.
```

- [ ] **Step 4: Commit**

```bash
git add README.md tests/manual_smoke_test.py
git commit -m "docs: add setup instructions, weekly scheduling, and manual smoke test"
```
