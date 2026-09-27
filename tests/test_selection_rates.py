import pytest

from contracts.tools.selection_rates import FOUR_FIFTHS, impact_ratios


def _rows(category, group, applicants, selected):
    return [{"category": category, "group": group, "selected": index < selected} for index in range(applicants)]


def test_selected_must_be_a_bool():
    with pytest.raises(ValueError):
        impact_ratios([{"category": "sex", "group": "A", "selected": "no"}])


def test_group_must_be_a_non_empty_str():
    with pytest.raises(ValueError):
        impact_ratios([{"category": "sex", "group": "", "selected": True}])


def test_four_fifths_threshold():
    assert FOUR_FIFTHS == 0.8


def test_two_groups_one_flagged():
    result = impact_ratios(_rows("sex", "A", 20, 10) + _rows("sex", "B", 20, 4))
    by_group = {row["group"]: row for row in result}
    assert by_group["A"] == {
        "category": "sex", "group": "A", "applicants": 20, "selected": 10,
        "selection_rate": 0.5, "impact_ratio": 1.0, "flagged": False,
    }
    assert by_group["B"]["selection_rate"] == 0.2
    assert by_group["B"]["impact_ratio"] == 0.4
    assert by_group["B"]["flagged"] is True


def test_output_sorted_by_category_then_group():
    result = impact_ratios(_rows("race", "Z", 5, 1) + _rows("sex", "B", 5, 1) + _rows("race", "A", 5, 1))
    assert [(row["category"], row["group"]) for row in result] == [("race", "A"), ("race", "Z"), ("sex", "B")]


def test_no_selections_at_all_flags_nobody():
    result = impact_ratios(_rows("sex", "A", 5, 0) + _rows("sex", "B", 5, 0))
    assert all(row["impact_ratio"] == 0.0 and row["flagged"] is False for row in result)


def test_empty_input():
    assert impact_ratios([]) == []


def test_boundary_ratio_shows_0_8_and_still_flags():
    result = impact_ratios(_rows("sex", "A", 10, 10) + _rows("sex", "B", 100000, 79998))
    by_group = {row["group"]: row for row in result}
    assert by_group["A"]["selection_rate"] == 1.0
    assert by_group["B"]["impact_ratio"] == 0.8
    assert by_group["B"]["flagged"] is True
