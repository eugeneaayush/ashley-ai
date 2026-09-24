import copy
import json

from contracts.tools.instrument_hash import canonical_hash, verify_hash
from contracts.tools.validate import INSTRUMENTS, FIXTURES, errors_for, load_json

RETAIL = INSTRUMENTS / "retail-associate.v1.json"


def test_retail_associate_v1_validates():
    assert errors_for("instrument", load_json(RETAIL)) == []


def test_retail_associate_v1_has_eight_questions_with_three_anchors():
    doc = load_json(RETAIL)
    assert len(doc["questions"]) == 8
    for question in doc["questions"]:
        assert set(question["anchors"]) == {"1", "3", "5"}


def test_stored_hash_matches_canonical_hash():
    doc = load_json(RETAIL)
    assert verify_hash(doc), f"expected {canonical_hash(doc)}"


def test_changing_question_text_changes_hash():
    doc = load_json(RETAIL)
    changed = copy.deepcopy(doc)
    changed["questions"][0]["text"] = changed["questions"][0]["text"] + " Also, why?"
    assert canonical_hash(changed) != canonical_hash(doc)
    assert not verify_hash(changed)


def test_status_change_does_not_change_hash():
    doc = load_json(RETAIL)
    retired = copy.deepcopy(doc)
    retired["status"] = "retired"
    assert canonical_hash(retired) == canonical_hash(doc)


def test_four_questions_is_invalid():
    doc = load_json(FIXTURES / "invalid" / "instrument" / "four-questions.json")
    errors = errors_for("instrument", doc)
    assert any("is too short" in message for message in errors), errors


def test_unknown_role_family_is_invalid():
    doc = load_json(RETAIL)
    doc["role_family"] = "astronaut"
    assert any("is not one of" in message for message in errors_for("instrument", doc))
