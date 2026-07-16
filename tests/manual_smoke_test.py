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
