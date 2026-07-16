"""Manual smoke test against real Google Trends. NOT run by the automated suite —
this filename deliberately matches neither of pytest's default discovery globs
(test_*.py or *_test.py), so it stays excluded even if a test_-prefixed function
is ever added here. Google Trends rate-limits aggressively, so this must never
run automatically in CI.

Run manually with: python tests/manual_smoke_check.py
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
