from jsonschema import Draft202012Validator

from contracts.tools.selection_rates import impact_ratios
from contracts.tools.validate import FIXTURES, errors_for, load_json, load_schema

VALID = FIXTURES / "valid" / "audit_export"
INVALID = FIXTURES / "invalid" / "audit_export"


def test_ll144_export_validates():
    assert errors_for("audit_export", load_json(VALID / "nyc-ll144-q4.json")) == []


def test_tool_rows_validate_against_export_item_schema():
    item_schema = load_schema("audit_export")["properties"]["selection_rates"]["items"]
    validator = Draft202012Validator(item_schema)
    rows = [{"category": "sex", "group": "A", "selected": True}, {"category": "sex", "group": "B", "selected": False}]
    for row in impact_ratios(rows):
        assert sorted(error.message for error in validator.iter_errors(row)) == []


def test_deletion_log_entry_requires_completion():
    errors = errors_for("audit_export", load_json(INVALID / "deletion-missing-completed.json"))
    assert "'completed_at' is a required property" in errors, errors


def test_jurisdiction_is_constrained():
    doc = load_json(VALID / "nyc-ll144-q4.json")
    doc["jurisdiction"] = "US-FL"
    assert any("is not one of" in message for message in errors_for("audit_export", doc))
