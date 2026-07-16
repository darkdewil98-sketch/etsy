from etsy_research.scorer import (
    compute_opportunity_score,
    compute_trend_growth_rate,
    normalize_volume,
)


def test_compute_trend_growth_rate_rising_trend():
    assert compute_trend_growth_rate([10, 10, 20, 30]) == 2.5


def test_compute_trend_growth_rate_falling_trend():
    assert compute_trend_growth_rate([40, 40, 10, 10]) == 0.25


def test_compute_trend_growth_rate_too_short():
    assert compute_trend_growth_rate([10]) == 0.0


def test_compute_trend_growth_rate_zero_baseline():
    assert compute_trend_growth_rate([0, 0, 5, 5]) == 5.0


def test_normalize_volume():
    assert normalize_volume(50, 100) == 0.5


def test_normalize_volume_zero_max():
    assert normalize_volume(0, 0) == 0.0


def test_compute_opportunity_score_no_competition():
    assert compute_opportunity_score(2.0, 0.5, None) == 1.0


def test_compute_opportunity_score_with_competition():
    assert compute_opportunity_score(2.0, 0.5, competition_count=5) == 1.0 / 6


def test_compute_opportunity_score_zero_competition_is_undiminished():
    assert compute_opportunity_score(2.0, 0.5, competition_count=0) == 1.0
