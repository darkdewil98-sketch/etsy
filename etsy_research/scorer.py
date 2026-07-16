"""Deterministic, data-driven opportunity scoring. No estimation, no AI guesses."""


def compute_trend_growth_rate(interest_over_time: list[int]) -> float:
    """Ratio of second-half average to first-half average of a real interest series.

    >1.0 means rising interest, <1.0 means falling. If the series starts at zero,
    returns the raw second-half average (growth from nothing can't be a ratio).
    """
    if len(interest_over_time) < 2:
        return 0.0

    midpoint = len(interest_over_time) // 2
    first_half = interest_over_time[:midpoint]
    second_half = interest_over_time[midpoint:]
    first_avg = sum(first_half) / len(first_half)
    second_avg = sum(second_half) / len(second_half)

    if first_avg == 0:
        return float(second_avg)
    return second_avg / first_avg


def normalize_volume(volume: float, max_volume: float) -> float:
    """Scales a raw volume figure to a 0-1 range relative to the batch's max."""
    if max_volume == 0:
        return 0.0
    return volume / max_volume


def compute_opportunity_score(
    trend_growth_rate: float,
    trend_volume_normalized: float,
    competition_count: int | None = None,
) -> float:
    """Higher score = more growth and volume, divided by (competitors + 1) when known.

    Using +1 avoids division by zero and means zero known competitors yields the
    undiminished score (the best case), rather than being confused with "unknown".
    """
    score = trend_growth_rate * trend_volume_normalized
    if competition_count is not None:
        score = score / (competition_count + 1)
    return score
