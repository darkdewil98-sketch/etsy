from etsy_research.etsy_adapter import EtsyAdapter


def test_get_competition_count_returns_none_until_etsy_api_is_wired_up():
    adapter = EtsyAdapter()
    assert adapter.get_competition_count("t-shirt design") is None
