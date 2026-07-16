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

## Manual smoke test (real Google Trends)

`tests/manual_smoke_check.py` hits the real Google Trends API once to confirm live connectivity.
It is deliberately excluded from the automated suite: pytest's default discovery collects files
matching `test_*.py` or `*_test.py`, and this filename matches neither glob, so it stays excluded
regardless of what functions are added to it later. Google Trends rate-limits aggressively, so this
must never run automatically in CI — run it manually only:

```
python tests/manual_smoke_check.py
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
