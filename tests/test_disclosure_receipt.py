from contracts.tools.validate import FIXTURES, errors_for, load_json

VALID = FIXTURES / "valid" / "disclosure_receipt"
INVALID = FIXTURES / "invalid" / "disclosure_receipt"


def test_basic_receipt_validates():
    assert errors_for("disclosure_receipt", load_json(VALID / "basic.json")) == []


def test_pooling_opt_in_validates_when_text_version_named():
    doc = load_json(VALID / "pooling-opt-in.json")
    assert doc["consent_pooling"] is True
    assert errors_for("disclosure_receipt", doc) == []


def test_pooling_true_without_text_version_is_invalid():
    doc = load_json(INVALID / "pooling-without-text-version.json")
    errors = errors_for("disclosure_receipt", doc)
    assert any("consent_pooling_text_version" in message for message in errors), errors


def test_record_consent_false_is_invalid():
    doc = load_json(INVALID / "record-consent-false.json")
    errors = errors_for("disclosure_receipt", doc)
    assert any("True was expected" in message for message in errors), errors


def test_unknown_jurisdiction_hint_is_invalid():
    doc = load_json(VALID / "basic.json")
    doc["jurisdiction_hints"] = ["US-XX"]
    assert any("is not one of" in message for message in errors_for("disclosure_receipt", doc))
