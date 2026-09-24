from contracts.tools.validate import FIXTURES, errors_for, load_json

VALID = FIXTURES / "valid" / "interview_session"
INVALID = FIXTURES / "invalid" / "interview_session"


def test_completed_session_validates():
    assert errors_for("interview_session", load_json(VALID / "completed.json")) == []


def test_abandoned_session_validates_without_result():
    doc = load_json(VALID / "abandoned.json")
    assert "result" not in doc
    assert errors_for("interview_session", doc) == []


def test_completed_session_requires_result():
    errors = errors_for("interview_session", load_json(INVALID / "completed-without-result.json"))
    assert "'result' is a required property" in errors, errors


def test_abandoned_session_must_not_carry_result():
    errors = errors_for("interview_session", load_json(INVALID / "abandoned-with-result.json"))
    assert any("should not be valid under" in message for message in errors), errors


def test_candidate_ref_must_be_pseudonymous():
    doc = load_json(VALID / "completed.json")
    doc["candidate_ref"] = "jane.doe@example.com"
    assert any("does not match" in message for message in errors_for("interview_session", doc))


def test_recording_retention_policy_is_constrained():
    doc = load_json(VALID / "completed.json")
    doc["recording_retention"]["policy"] = "forever"
    assert any("is not one of" in message for message in errors_for("interview_session", doc))
