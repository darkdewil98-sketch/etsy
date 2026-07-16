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
