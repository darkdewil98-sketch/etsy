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
                time.sleep(self._backoff_base_seconds * (2**attempt))
        raise TrendsClientError(f"Failed after {self._max_retries} retries: {last_error}")

    def get_interest_over_time(self, keyword: str) -> list[int]:
        def fetch():
            self._client.build_payload([keyword], timeframe="today 3-m")
            return self._client.interest_over_time()

        df = self._call_with_retry(fetch)
        if df.empty:
            return []
        return df[keyword].tolist()

    def get_rising_queries(self, keyword: str) -> list[str]:
        def fetch():
            self._client.build_payload([keyword], timeframe="today 3-m")
            return self._client.related_queries()

        related = self._call_with_retry(fetch)
        rising_df = related.get("rising")
        if rising_df is None or rising_df.empty:
            return []
        return rising_df["query"].tolist()
