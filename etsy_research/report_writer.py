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
