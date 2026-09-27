"""Panel aggregation: several model ratings per answer, median score, disagreement kept as a signal.

consistency_errors re-derives a score row's aggregate fields from its panel; JSON Schema cannot.
"""
from __future__ import annotations

from statistics import median

MIN_PANEL = 3
MAX_PANEL = 7


def aggregate(ratings: list[int]) -> tuple[float, int]:
    if len(ratings) < MIN_PANEL:
        raise ValueError(f"panel needs at least {MIN_PANEL} ratings, got {len(ratings)}")
    if len(ratings) > MAX_PANEL:
        raise ValueError(f"panel needs at most {MAX_PANEL} ratings, got {len(ratings)}")
    for rating in ratings:
        if isinstance(rating, bool) or not isinstance(rating, int) or not 1 <= rating <= 5:
            raise ValueError(f"rating out of range 1-5: {rating!r}")
    return float(median(ratings)), max(ratings) - min(ratings)


def consistency_errors(row: dict) -> list[str]:
    """Cross-field checks on a score row that already validates against score_row.schema.json."""
    errors: list[str] = []
    try:
        score, disagreement = aggregate([rater["rating"] for rater in row["panel"]])
    except ValueError as error:
        errors.append(f"panel: {error}")
    else:
        if row["aggregate"]["score"] != score:
            errors.append(f"aggregate.score {row['aggregate']['score']} is not the panel median {score}")
        if row["disagreement"] != disagreement:
            errors.append(f"disagreement {row['disagreement']} is not the panel max minus min {disagreement}")
    span = row["transcript_span"]
    if span["end_ms"] < span["start_ms"]:
        errors.append(f"transcript_span end_ms {span['end_ms']} is before start_ms {span['start_ms']}")
    return errors
