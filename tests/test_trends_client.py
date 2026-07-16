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
