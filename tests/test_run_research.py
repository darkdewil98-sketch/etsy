from etsy_research.trends_client import TrendsClientError
from run_research import build_opportunities, load_seeds


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


def test_build_opportunities_handles_empty_seeds_dict():
    opportunities, summary = build_opportunities({}, FakeTrendsClient({}), FakeEtsyAdapter())

    assert opportunities == []
    assert summary == {"seeds_scanned": 0, "opportunities_found": 0, "errors": 0}


def test_load_seeds_returns_empty_dict_for_empty_yaml_file(tmp_path):
    seeds_path = tmp_path / "seeds.yaml"
    seeds_path.write_text("", encoding="utf-8")

    assert load_seeds(seeds_path) == {}
