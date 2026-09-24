import pytest

from contracts.tools.panel import MIN_PANEL, aggregate
from contracts.tools.validate import FIXTURES, errors_for, load_json

VALID = FIXTURES / "valid" / "score_row"
INVALID = FIXTURES / "invalid" / "score_row"


def test_min_panel_is_three():
    assert MIN_PANEL == 3


def test_median_and_disagreement_three_raters():
    assert aggregate([4, 4, 5]) == (4.0, 1)


def test_median_and_disagreement_spread():
    assert aggregate([2, 5, 3]) == (3.0, 3)


def test_even_panel_uses_statistical_median():
    assert aggregate([3, 4, 4, 5]) == (4.0, 2)


def test_two_ratings_rejected():
    with pytest.raises(ValueError, match="at least 3"):
        aggregate([4, 5])


def test_out_of_range_rating_rejected():
    with pytest.raises(ValueError, match="out of range"):
        aggregate([1, 6, 3])


def test_score_row_fixture_validates():
    assert errors_for("score_row", load_json(VALID / "q01.json")) == []


def test_fixture_aggregate_is_consistent_with_tool():
    doc = load_json(VALID / "q01.json")
    score, disagreement = aggregate([rater["rating"] for rater in doc["panel"]])
    assert doc["aggregate"]["score"] == score
    assert doc["disagreement"] == disagreement


def test_two_rater_fixture_is_invalid():
    errors = errors_for("score_row", load_json(INVALID / "two-raters.json"))
    assert any("is too short" in message for message in errors), errors
