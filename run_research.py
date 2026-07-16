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
