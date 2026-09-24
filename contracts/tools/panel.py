"""Panel aggregation: several model ratings per answer, median score, disagreement kept as a signal."""
from __future__ import annotations

from statistics import median

MIN_PANEL = 3


def aggregate(ratings: list[int]) -> tuple[float, int]:
    if len(ratings) < MIN_PANEL:
        raise ValueError(f"panel needs at least {MIN_PANEL} ratings, got {len(ratings)}")
    for rating in ratings:
        if isinstance(rating, bool) or not isinstance(rating, int) or not 1 <= rating <= 5:
            raise ValueError(f"rating out of range 1-5: {rating!r}")
    return float(median(ratings)), max(ratings) - min(ratings)
