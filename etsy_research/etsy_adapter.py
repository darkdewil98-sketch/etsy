"""Etsy competition-data source.

Stub until the Etsy Developer API key/OAuth application is approved. Callers must
treat `None` as "competition data unavailable" and skip the competition adjustment
(see etsy_research.scorer.compute_opportunity_score). Swap the body of
get_competition_count for a real Etsy Open API call later without changing this
class's interface or any caller.
"""


class EtsyAdapter:
    def get_competition_count(self, keyword: str) -> int | None:
        return None
