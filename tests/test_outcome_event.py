import pytest

from contracts.tools.validate import FIXTURES, errors_for, load_json
from contracts.tools.webhook_sign import PREFIX, sign, verify

VALID = FIXTURES / "valid" / "outcome_event"
INVALID = FIXTURES / "invalid" / "outcome_event"
SECRET = b"whsec_test_0123456789"


def test_sign_produces_prefixed_hex():
    signature = sign(SECRET, b"1759760000." + b'{"a":1}')
    assert signature.startswith(PREFIX)
    assert len(signature) == len(PREFIX) + 64


def test_verify_roundtrip():
    message = b"1759760000." + b'{"event_id":"x"}'
    assert verify(SECRET, message, sign(SECRET, message)) is True


def test_verify_rejects_tampered_body():
    message = b"1759760000." + b'{"event_id":"x"}'
    assert verify(SECRET, message + b" ", sign(SECRET, message)) is False


def test_verify_rejects_missing_prefix():
    message = b"1759760000.{}"
    assert verify(SECRET, message, sign(SECRET, message)[len(PREFIX):]) is False


@pytest.mark.parametrize("name", ["application_decision", "hired", "retained_90", "separated", "performance_rating"])
def test_valid_event_fixtures(name):
    assert errors_for("outcome_event", load_json(VALID / f"{name}.json")) == []


def test_bad_decision_is_invalid():
    errors = errors_for("outcome_event", load_json(INVALID / "bad-decision.json"))
    assert any("is not one of" in message for message in errors), errors


def test_unknown_event_type_is_invalid():
    errors = errors_for("outcome_event", load_json(INVALID / "unknown-type.json"))
    assert any("is not one of" in message for message in errors), errors


def test_hired_payload_must_be_empty():
    errors = errors_for("outcome_event", load_json(INVALID / "hired-with-payload.json"))
    assert any("Additional properties are not allowed" in message for message in errors), errors
