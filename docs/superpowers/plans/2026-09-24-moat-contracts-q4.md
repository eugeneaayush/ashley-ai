# Moat Contracts and Q4 2026 Deliverables Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Pin, in this repository, the interface contracts and reference calculations that the moat design depends on (instrument, disclosure receipt, interview session, score row, outcome event, audit export), plus the non-code Q4 2026 deliverables, so the product team can implement against fixed, tested contracts.

**Architecture:** JSON Schema (draft 2020-12) documents under `contracts/schemas/`, exercised by pytest against valid and invalid fixtures under `contracts/fixtures/`. Small pure-Python reference implementations under `contracts/tools/` for instrument hashing, panel aggregation, webhook signing, and four-fifths selection-rate math, so behaviour is defined by runnable code rather than prose. Markdown deliverables (Company OS wiki page, flagship criteria, ATS check, audit RFQ, ISO 42001 skeleton) with header-presence tests so they cannot silently rot.

**Tech Stack:** Python 3.14 (the machine has 3.14.4), pytest 9, jsonschema 4.x, standard library only otherwise. No product code lives here; the product codebase is separate and gets its own code-level plan later.

**Spec:** `docs/superpowers/specs/2026-09-23-competitive-moat-design.md`

## Global Constraints

- Words-only scoring: no contract may carry expression, emotion, facial, appearance, accent, gaze, or posture features (spec 4.4, "Hard rule: never score expression").
- Consent to pool is separate from consent to record and is opt-in; a receipt may only mark pooling consent true when it names the pooling text version shown (spec 4.3, "Consent architecture for pooling").
- Instruments are versioned and immutable: "Fixed core question batteries and anchored rubrics ... versioned on every score row" (spec 4.2). Any change to question or anchor text is a new version with a new content hash.
- Rubric scale is 1 to 5 with anchors at 1, 3, and 5; six to ten hourly role families (spec 4.2).
- Every score row stamps instrument id and version, scoring prompt version, and model versions (spec 4.3, "Append-only event log").
- Panel scoring: at least three ratings per answer, aggregated by median, disagreement kept (spec 4.3, "Panel scoring by default").
- Deletion propagates to derived features and is logged in audit exports (spec 4.3 and 4.4).
- Outcome events are keyed to the interview session id: hire decision, 30, 90, and 365-day retention, and manager rating (spec 4.2, "Outcome webhooks coming in").
- Audit exports cover NYC Local Law 144, Illinois AIVIA and HB 3773, California automated-decision rules, and the EU AI Act (spec 4.4).
- Test runs use `PYTHONDONTWRITEBYTECODE=1` (repository convention) and run from the repository root.
- Commit after every task; never push (project safety guard).

---

## File Structure

```
pyproject.toml                          # pytest config: testpaths=tests, pythonpath=.
contracts/
  requirements.txt                      # pytest, jsonschema
  README.md                             # layout, versioning rules, how to validate (Task 8)
  WEBHOOKS.md                           # outcome webhook delivery and signing spec (Task 6)
  __init__.py
  schemas/
    instrument.schema.json              # Task 2
    disclosure_receipt.schema.json      # Task 3
    interview_session.schema.json       # Task 4
    score_row.schema.json               # Task 5
    outcome_event.schema.json           # Task 6
    audit_export.schema.json            # Task 7
  instruments/
    retail-associate.v1.json            # first real instrument (Task 2)
  fixtures/
    valid/<schema-name>/*.json          # must validate
    invalid/<schema-name>/*.json        # must fail validation
  tools/
    __init__.py
    validate.py                         # load schemas, errors_for(), CLI (Task 1)
    instrument_hash.py                  # canonical_hash(), verify_hash() (Task 2)
    panel.py                            # aggregate(ratings) -> (score, disagreement) (Task 5)
    webhook_sign.py                     # sign(), verify() HMAC-SHA256 (Task 6)
    selection_rates.py                  # impact_ratios(rows) four-fifths math (Task 7)
tests/
  test_validate_tool.py                 # Task 1
  test_instrument.py                    # Task 2
  test_disclosure_receipt.py            # Task 3
  test_interview_session.py             # Task 4
  test_score_row.py                     # Task 5
  test_outcome_event.py                 # Task 6
  test_selection_rates.py               # Task 7
  test_audit_export.py                  # Task 7
  test_fixture_sweep.py                 # Task 8: every fixture dir agrees with its schema
  test_words_only_guard.py              # Task 8: forbidden property names
  test_company_os_docs.py               # Task 9
  test_q4_docs.py                       # Tasks 10 and 11
blueprint/wiki/moat-decisions.md        # Company OS page (Task 9)
blueprint/INDEX.md                      # add one row (Task 9)
docs/moat/flagship-targets.md           # Task 10
docs/moat/ats-check.md                  # Task 10
docs/moat/audit-vendor-rfq.md           # Task 11
docs/moat/iso42001-skeleton.md          # Task 11
```

Conventions used by every schema: `$schema` is `https://json-schema.org/draft/2020-12/schema`; `additionalProperties` is `false` at every object level; identifiers use the patterns below, repeated inline in each schema so every schema is self-contained (no cross-file `$ref`).

- UUID: `^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$`
- Date-time (RFC 3339): `^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$`
- Date: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$`
- SHA-256 hash: `^sha256:[0-9a-f]{64}$`

---

### Task 1: Test tooling and the validator module

**Files:**
- Create: `pyproject.toml`
- Create: `contracts/requirements.txt`
- Create: `contracts/__init__.py` (empty)
- Create: `contracts/tools/__init__.py` (empty)
- Create: `contracts/tools/validate.py`
- Create: `tests/test_validate_tool.py`
- Modify: `.gitignore` (append three lines)

**Interfaces:**
- Consumes: nothing.
- Produces: `contracts.tools.validate.load_json(path: Path) -> dict`, `load_schema(name: str) -> dict` (reads `contracts/schemas/<name>.schema.json`), `errors_for(schema_name: str, doc: dict) -> list[str]` (sorted validation messages, empty when valid), `main(argv: list[str]) -> int` CLI. Every later test imports `errors_for`.

- [ ] **Step 1: Create the pytest configuration and requirements**

`pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]
addopts = "-q"
```

`contracts/requirements.txt`:

```
pytest>=8,<10
jsonschema>=4.18,<5
```

- [ ] **Step 2: Create the virtual environment and install**

Run:

```bash
python3 -m venv .venv && .venv/bin/pip install -q -r contracts/requirements.txt && .venv/bin/python -c "import jsonschema, pytest; print('ok')"
```

Expected: `ok`

- [ ] **Step 3: Ignore the environment and caches**

Append to `.gitignore`:

```
.venv/
__pycache__/
.pytest_cache/
```

- [ ] **Step 4: Write the failing test**

`tests/test_validate_tool.py`:

```python
from contracts.tools.validate import main


def test_usage_error_returns_2(capsys):
    assert main(["validate.py"]) == 2
    assert "usage" in capsys.readouterr().err


def test_draft_2020_12_validator_is_available():
    from jsonschema import Draft202012Validator

    validator = Draft202012Validator({"type": "integer"})
    assert sorted(e.message for e in validator.iter_errors("x")) == ["'x' is not of type 'integer'"]
```

- [ ] **Step 5: Run the test to verify it fails**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_validate_tool.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'contracts'` (or `contracts.tools.validate`)

- [ ] **Step 6: Write the validator module**

Create empty `contracts/__init__.py` and `contracts/tools/__init__.py`, then `contracts/tools/validate.py`:

```python
"""Validate JSON documents against the contract schemas in contracts/schemas."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "contracts" / "schemas"
FIXTURES = ROOT / "contracts" / "fixtures"
INSTRUMENTS = ROOT / "contracts" / "instruments"


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def load_schema(name: str) -> dict:
    return load_json(SCHEMAS / f"{name}.schema.json")


def errors_for(schema_name: str, doc: dict) -> list[str]:
    """Return sorted validation messages; an empty list means the document is valid."""
    validator = Draft202012Validator(load_schema(schema_name))
    return sorted(error.message for error in validator.iter_errors(doc))


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: validate.py <schema-name> <document.json>", file=sys.stderr)
        return 2
    errors = errors_for(argv[1], load_json(Path(argv[2])))
    for message in errors:
        print(message)
    print("VALID" if not errors else f"INVALID ({len(errors)} errors)")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 7: Run the test to verify it passes**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_validate_tool.py -v`
Expected: `2 passed`

- [ ] **Step 8: Commit**

```bash
git add pyproject.toml .gitignore contracts/requirements.txt contracts/__init__.py contracts/tools/__init__.py contracts/tools/validate.py tests/test_validate_tool.py
git commit -m "chore: add contract validation tooling"
```

---

### Task 2: Instrument schema, content hash, and the first real instrument

**Files:**
- Create: `contracts/schemas/instrument.schema.json`
- Create: `contracts/tools/instrument_hash.py`
- Create: `contracts/instruments/retail-associate.v1.json`
- Create: `contracts/fixtures/invalid/instrument/four-questions.json`
- Create: `tests/test_instrument.py`

**Interfaces:**
- Consumes: `errors_for`, `load_json`, `INSTRUMENTS` from Task 1.
- Produces: `contracts.tools.instrument_hash.canonical_hash(instrument: dict) -> str` (returns `sha256:<64 hex>` over every key except `content_hash` and `status`), `verify_hash(instrument: dict) -> bool`. The `instrument_id` and `version` fields are referenced by Tasks 4, 5, and 7.

- [ ] **Step 1: Write the failing tests**

`tests/test_instrument.py`:

```python
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
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_instrument.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'contracts.tools.instrument_hash'`

- [ ] **Step 3: Write the schema**

`contracts/schemas/instrument.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://tryashley.ai/contracts/instrument.schema.json",
  "title": "Instrument",
  "description": "A versioned, immutable interview instrument for one hourly role family: fixed core questions with anchored 1-5 rubrics. Any change to question or anchor text is a new version.",
  "type": "object",
  "additionalProperties": false,
  "required": ["instrument_id", "role_family", "version", "status", "rubric_scale", "questions", "content_hash"],
  "properties": {
    "instrument_id": {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"},
    "role_family": {
      "enum": [
        "retail-associate", "customer-support", "warehouse-associate", "delivery-driver",
        "food-service", "call-center", "hospitality-front-desk", "healthcare-aide",
        "sales-development", "general-labor"
      ]
    },
    "version": {"type": "integer", "minimum": 1},
    "status": {"enum": ["draft", "active", "retired"]},
    "rubric_scale": {
      "type": "object",
      "additionalProperties": false,
      "required": ["min", "max"],
      "properties": {"min": {"const": 1}, "max": {"const": 5}}
    },
    "questions": {
      "type": "array",
      "minItems": 5,
      "maxItems": 12,
      "items": {"$ref": "#/$defs/question"}
    },
    "content_hash": {"type": "string", "pattern": "^sha256:[0-9a-f]{64}$"}
  },
  "$defs": {
    "question": {
      "type": "object",
      "additionalProperties": false,
      "required": ["question_id", "text", "competency", "follow_up_allowed", "anchors"],
      "properties": {
        "question_id": {"type": "string", "pattern": "^q[0-9]{2}$"},
        "text": {"type": "string", "minLength": 15},
        "competency": {"type": "string", "pattern": "^[a-z]+(-[a-z]+)*$"},
        "follow_up_allowed": {"type": "boolean"},
        "anchors": {
          "type": "object",
          "additionalProperties": false,
          "required": ["1", "3", "5"],
          "properties": {
            "1": {"type": "string", "minLength": 10},
            "3": {"type": "string", "minLength": 10},
            "5": {"type": "string", "minLength": 10}
          }
        }
      }
    }
  }
}
```

- [ ] **Step 4: Write the hash tool**

`contracts/tools/instrument_hash.py`:

```python
"""Canonical content hash for instruments. Text changes must change the hash; status changes must not."""
from __future__ import annotations

import hashlib
import json

HASH_EXCLUDED = ("content_hash", "status")


def canonical_hash(instrument: dict) -> str:
    body = {key: value for key, value in instrument.items() if key not in HASH_EXCLUDED}
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def verify_hash(instrument: dict) -> bool:
    return instrument.get("content_hash") == canonical_hash(instrument)
```

- [ ] **Step 5: Write the first real instrument with a placeholder hash, then compute the hash**

`contracts/instruments/retail-associate.v1.json` (write `content_hash` as `sha256:` followed by 64 zeros first; Step 6 replaces it):

```json
{
  "instrument_id": "retail-associate",
  "role_family": "retail-associate",
  "version": 1,
  "status": "active",
  "rubric_scale": {"min": 1, "max": 5},
  "questions": [
    {
      "question_id": "q01",
      "text": "Tell me about a time a customer was unhappy. What did they want, and what did you do?",
      "competency": "customer-recovery",
      "follow_up_allowed": true,
      "anchors": {
        "1": "Cannot describe a specific situation, or blames the customer without describing any action they took.",
        "3": "Describes a real situation and a reasonable action, but the outcome or what they learned is unclear.",
        "5": "Describes a specific situation, the action they chose and why, the outcome, and what they would repeat or change."
      }
    },
    {
      "question_id": "q02",
      "text": "Walk me through how you would handle a line of five customers when a coworker has just called in sick.",
      "competency": "prioritization",
      "follow_up_allowed": true,
      "anchors": {
        "1": "No plan beyond working faster, or would leave customers unacknowledged.",
        "3": "Acknowledges the line and works through it in order, but does not mention asking for help or setting expectations.",
        "5": "Acknowledges everyone, sets expectations, handles quick requests first, and calls for backup or a manager."
      }
    },
    {
      "question_id": "q03",
      "text": "Describe a shift where you had to follow a procedure you disagreed with. What did you do?",
      "competency": "following-procedures",
      "follow_up_allowed": true,
      "anchors": {
        "1": "Ignored the procedure, or cannot give an example of following one they disliked.",
        "3": "Followed the procedure but did not raise the concern with anyone.",
        "5": "Followed the procedure, then raised the concern with the right person and explained why."
      }
    },
    {
      "question_id": "q04",
      "text": "What does reliable attendance look like to you, and how do you make sure you get to work on time?",
      "competency": "reliability",
      "follow_up_allowed": false,
      "anchors": {
        "1": "Gives no concrete habit or plan, or describes attendance as someone else's responsibility.",
        "3": "Names one habit, such as an alarm or a set route, without a backup for when it fails.",
        "5": "Names concrete habits and a backup plan, and says how they would tell a manager early if late."
      }
    },
    {
      "question_id": "q05",
      "text": "Tell me about a time you helped a teammate finish a task that was not yours.",
      "competency": "teamwork",
      "follow_up_allowed": true,
      "anchors": {
        "1": "Cannot give an example, or describes doing so only when told to.",
        "3": "Gives a real example but the reason for helping or the result is vague.",
        "5": "Gives a specific example, explains why they stepped in, and what it meant for the team or customer."
      }
    },
    {
      "question_id": "q06",
      "text": "A customer asks for a discount you are not allowed to give. What do you say to them?",
      "competency": "policy-under-pressure",
      "follow_up_allowed": true,
      "anchors": {
        "1": "Would give the discount anyway, or would refuse in a way that dismisses the customer.",
        "3": "Declines politely but offers no alternative and does not involve a manager.",
        "5": "Declines clearly and kindly, explains what they can offer, and escalates to a manager if the customer insists."
      }
    },
    {
      "question_id": "q07",
      "text": "Describe a time you noticed something wrong on the floor, like a spill or a wrong price. What did you do?",
      "competency": "ownership",
      "follow_up_allowed": true,
      "anchors": {
        "1": "Cannot give an example, or left it for someone else without telling anyone.",
        "3": "Fixed or reported it, but only after being asked or after some delay.",
        "5": "Acted immediately, made it safe or correct, and told the right person so it stayed fixed."
      }
    },
    {
      "question_id": "q08",
      "text": "Tell me about something you had to learn quickly in a past job or activity. How did you learn it?",
      "competency": "learning-speed",
      "follow_up_allowed": true,
      "anchors": {
        "1": "Cannot give an example, or waited to be trained without trying anything themselves.",
        "3": "Gives an example and a method, such as watching a coworker, but does not say how they checked their understanding.",
        "5": "Gives a specific example, a method, how they checked they had it right, and how fast they became independent."
      }
    }
  ],
  "content_hash": "sha256:0000000000000000000000000000000000000000000000000000000000000000"
}
```

- [ ] **Step 6: Compute and store the real hash**

Run:

```bash
.venv/bin/python -c "import json; from pathlib import Path; from contracts.tools.instrument_hash import canonical_hash; p=Path('contracts/instruments/retail-associate.v1.json'); d=json.loads(p.read_text(encoding='utf-8')); d['content_hash']=canonical_hash(d); p.write_text(json.dumps(d, indent=2, ensure_ascii=False)+'\n', encoding='utf-8'); print(d['content_hash'])"
```

Expected: one line starting with `sha256:` followed by 64 hex characters. Open the file and confirm the value replaced the zeros.

- [ ] **Step 7: Write the invalid fixture**

`contracts/fixtures/invalid/instrument/four-questions.json`: copy `retail-associate.v1.json`, delete questions `q05` through `q08` so only four remain, and keep everything else unchanged (the stale hash is irrelevant; the test asserts only on `is too short`).

- [ ] **Step 8: Run the tests to verify they pass**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_instrument.py -v`
Expected: `7 passed`

- [ ] **Step 9: Commit**

```bash
git add contracts/schemas/instrument.schema.json contracts/tools/instrument_hash.py contracts/instruments/retail-associate.v1.json contracts/fixtures/invalid/instrument/four-questions.json tests/test_instrument.py
git commit -m "feat(contracts): instrument schema, content hash, retail-associate v1"
```

---

### Task 3: Disclosure receipt schema

**Files:**
- Create: `contracts/schemas/disclosure_receipt.schema.json`
- Create: `contracts/fixtures/valid/disclosure_receipt/basic.json`
- Create: `contracts/fixtures/valid/disclosure_receipt/pooling-opt-in.json`
- Create: `contracts/fixtures/invalid/disclosure_receipt/pooling-without-text-version.json`
- Create: `contracts/fixtures/invalid/disclosure_receipt/record-consent-false.json`
- Create: `tests/test_disclosure_receipt.py`

**Interfaces:**
- Consumes: `errors_for`, `load_json`, `FIXTURES` from Task 1.
- Produces: the `receipt_id` (UUID) that `interview_session.disclosure_receipt_id` references in Task 4; the `consent_pooling` boolean that Task 7's pooling rules depend on.

- [ ] **Step 1: Write the failing tests**

`tests/test_disclosure_receipt.py`:

```python
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
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_disclosure_receipt.py -v`
Expected: FAIL with `FileNotFoundError` for `disclosure_receipt.schema.json`

- [ ] **Step 3: Write the schema**

`contracts/schemas/disclosure_receipt.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://tryashley.ai/contracts/disclosure_receipt.schema.json",
  "title": "DisclosureReceipt",
  "description": "Evidence that Ashley identified herself as an AI interviewer and the candidate acknowledged it. Consent to record is required for a receipt to exist; consent to pooled learning is separate and opt-in.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "receipt_id", "session_id", "disclosed_at", "disclosure_text_version", "candidate_ack",
    "candidate_ack_at", "consent_record", "consent_pooling", "locale", "jurisdiction_hints"
  ],
  "properties": {
    "receipt_id": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"},
    "session_id": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"},
    "disclosed_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"},
    "disclosure_text_version": {"type": "string", "pattern": "^disclosure-v[0-9]+$"},
    "candidate_ack": {"enum": ["spoken", "clicked", "typed"]},
    "candidate_ack_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"},
    "consent_record": {"const": true},
    "consent_pooling": {"type": "boolean"},
    "consent_pooling_text_version": {"type": "string", "pattern": "^pooling-v[0-9]+$"},
    "locale": {"type": "string", "pattern": "^[a-z]{2}(-[A-Z]{2})?$"},
    "jurisdiction_hints": {
      "type": "array",
      "uniqueItems": true,
      "items": {"enum": ["US-NYC", "US-IL", "US-MD", "US-CA", "US-CO", "US-TX", "EU", "UK", "OTHER"]}
    }
  },
  "if": {"properties": {"consent_pooling": {"const": true}}, "required": ["consent_pooling"]},
  "then": {"required": ["consent_pooling_text_version"]}
}
```

- [ ] **Step 4: Write the fixtures**

`contracts/fixtures/valid/disclosure_receipt/basic.json`:

```json
{
  "receipt_id": "11111111-1111-4111-8111-111111111111",
  "session_id": "22222222-2222-4222-8222-222222222222",
  "disclosed_at": "2026-10-06T14:02:11Z",
  "disclosure_text_version": "disclosure-v1",
  "candidate_ack": "clicked",
  "candidate_ack_at": "2026-10-06T14:02:19Z",
  "consent_record": true,
  "consent_pooling": false,
  "locale": "en-US",
  "jurisdiction_hints": ["US-IL"]
}
```

`contracts/fixtures/valid/disclosure_receipt/pooling-opt-in.json`: same as `basic.json` except `"receipt_id": "11111111-1111-4111-8111-111111111112"`, `"consent_pooling": true`, and an added `"consent_pooling_text_version": "pooling-v1"`.

`contracts/fixtures/invalid/disclosure_receipt/pooling-without-text-version.json`: same as `basic.json` except `"consent_pooling": true` (no `consent_pooling_text_version`).

`contracts/fixtures/invalid/disclosure_receipt/record-consent-false.json`: same as `basic.json` except `"consent_record": false`.

- [ ] **Step 5: Run the tests to verify they pass**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_disclosure_receipt.py -v`
Expected: `5 passed`

- [ ] **Step 6: Commit**

```bash
git add contracts/schemas/disclosure_receipt.schema.json contracts/fixtures/valid/disclosure_receipt contracts/fixtures/invalid/disclosure_receipt tests/test_disclosure_receipt.py
git commit -m "feat(contracts): disclosure receipt schema with separate pooling consent"
```

---

### Task 4: Interview session schema

**Files:**
- Create: `contracts/schemas/interview_session.schema.json`
- Create: `contracts/fixtures/valid/interview_session/completed.json`
- Create: `contracts/fixtures/valid/interview_session/abandoned.json`
- Create: `contracts/fixtures/invalid/interview_session/completed-without-result.json`
- Create: `contracts/fixtures/invalid/interview_session/abandoned-with-result.json`
- Create: `tests/test_interview_session.py`

**Interfaces:**
- Consumes: `errors_for`, `load_json`, `FIXTURES` from Task 1; `instrument_id` and `version` semantics from Task 2; `receipt_id` from Task 3.
- Produces: `session_id` (UUID) that score rows (Task 5), outcome events (Task 6), and deletion logs (Task 7) reference; the `ats.system` enum reused by `outcome_event.source.system` in Task 6.

- [ ] **Step 1: Write the failing tests**

`tests/test_interview_session.py`:

```python
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
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_interview_session.py -v`
Expected: FAIL with `FileNotFoundError` for `interview_session.schema.json`

- [ ] **Step 3: Write the schema**

`contracts/schemas/interview_session.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://tryashley.ai/contracts/interview_session.schema.json",
  "title": "InterviewSession",
  "description": "One candidate conversation with Ashley: which instrument version was used, when, under which disclosure receipt, how the recording is retained, and (when completed) the recommendation for a human to review. Candidate identity is pseudonymous here; the ATS holds the person.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "session_id", "org_id", "role_id", "instrument_id", "instrument_version", "candidate_ref",
    "language", "started_at", "status", "disclosure_receipt_id", "ats", "recording_retention"
  ],
  "properties": {
    "session_id": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"},
    "org_id": {"type": "string", "pattern": "^org_[A-Za-z0-9]{6,}$"},
    "role_id": {"type": "string", "pattern": "^role_[A-Za-z0-9]{6,}$"},
    "instrument_id": {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"},
    "instrument_version": {"type": "integer", "minimum": 1},
    "candidate_ref": {"type": "string", "pattern": "^cand_[A-Za-z0-9]{16,}$"},
    "language": {"type": "string", "pattern": "^[a-z]{2}$"},
    "started_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"},
    "ended_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"},
    "duration_seconds": {"type": "integer", "minimum": 0},
    "status": {"enum": ["in_progress", "completed", "abandoned"]},
    "disclosure_receipt_id": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"},
    "ats": {
      "type": "object",
      "additionalProperties": false,
      "required": ["system"],
      "properties": {
        "system": {"enum": ["ashby", "greenhouse", "icims", "bullhorn", "workstream", "fountain", "harri", "other", "none"]},
        "external_candidate_id": {"type": "string", "minLength": 1},
        "external_application_id": {"type": "string", "minLength": 1},
        "stage_at_trigger": {"type": "string", "minLength": 1}
      }
    },
    "recording_retention": {
      "type": "object",
      "additionalProperties": false,
      "required": ["policy", "deleted_at", "deletion_request_id"],
      "properties": {
        "policy": {"enum": ["customer-default", "aivia-30-day"]},
        "deleted_at": {"type": ["string", "null"], "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"},
        "deletion_request_id": {"type": ["string", "null"], "minLength": 1}
      }
    },
    "result": {
      "type": "object",
      "additionalProperties": false,
      "required": ["recommendation", "summary", "overall_score", "scoring_prompt_version", "generated_at"],
      "properties": {
        "recommendation": {"enum": ["advance", "review", "do-not-advance"]},
        "summary": {"type": "string", "minLength": 20},
        "overall_score": {"type": "number", "minimum": 1, "maximum": 5},
        "scoring_prompt_version": {"type": "string", "pattern": "^scoring-v[0-9]+$"},
        "generated_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"}
      }
    }
  },
  "allOf": [
    {
      "if": {"properties": {"status": {"const": "completed"}}, "required": ["status"]},
      "then": {"required": ["ended_at", "duration_seconds", "result"]}
    },
    {
      "if": {"properties": {"status": {"const": "abandoned"}}, "required": ["status"]},
      "then": {"not": {"required": ["result"]}}
    }
  ]
}
```

- [ ] **Step 4: Write the fixtures**

`contracts/fixtures/valid/interview_session/completed.json`:

```json
{
  "session_id": "22222222-2222-4222-8222-222222222222",
  "org_id": "org_acme001",
  "role_id": "role_retail01",
  "instrument_id": "retail-associate",
  "instrument_version": 1,
  "candidate_ref": "cand_9f8e7d6c5b4a3210",
  "language": "en",
  "started_at": "2026-10-06T14:02:30Z",
  "ended_at": "2026-10-06T14:21:05Z",
  "duration_seconds": 1115,
  "status": "completed",
  "disclosure_receipt_id": "11111111-1111-4111-8111-111111111111",
  "ats": {
    "system": "ashby",
    "external_candidate_id": "c_48213",
    "external_application_id": "a_90871",
    "stage_at_trigger": "Application Review"
  },
  "recording_retention": {"policy": "aivia-30-day", "deleted_at": null, "deletion_request_id": null},
  "result": {
    "recommendation": "advance",
    "summary": "Consistent, specific examples for customer recovery and ownership; weaker on prioritization under pressure.",
    "overall_score": 3.9,
    "scoring_prompt_version": "scoring-v1",
    "generated_at": "2026-10-06T14:21:40Z"
  }
}
```

`contracts/fixtures/valid/interview_session/abandoned.json`:

```json
{
  "session_id": "22222222-2222-4222-8222-222222222223",
  "org_id": "org_acme001",
  "role_id": "role_retail01",
  "instrument_id": "retail-associate",
  "instrument_version": 1,
  "candidate_ref": "cand_0a1b2c3d4e5f6a7b",
  "language": "es",
  "started_at": "2026-10-06T15:40:00Z",
  "ended_at": "2026-10-06T15:41:35Z",
  "duration_seconds": 95,
  "status": "abandoned",
  "disclosure_receipt_id": "11111111-1111-4111-8111-111111111113",
  "ats": {"system": "none"},
  "recording_retention": {"policy": "customer-default", "deleted_at": null, "deletion_request_id": null}
}
```

`contracts/fixtures/invalid/interview_session/completed-without-result.json`: copy of `completed.json` with the whole `result` object removed.

`contracts/fixtures/invalid/interview_session/abandoned-with-result.json`: copy of `abandoned.json` with the `result` object from `completed.json` added.

- [ ] **Step 5: Run the tests to verify they pass**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_interview_session.py -v`
Expected: `6 passed`

- [ ] **Step 6: Commit**

```bash
git add contracts/schemas/interview_session.schema.json contracts/fixtures/valid/interview_session contracts/fixtures/invalid/interview_session tests/test_interview_session.py
git commit -m "feat(contracts): interview session schema with retention and result rules"
```

---

### Task 5: Score row schema and panel aggregation

**Files:**
- Create: `contracts/schemas/score_row.schema.json`
- Create: `contracts/tools/panel.py`
- Create: `contracts/fixtures/valid/score_row/q01.json`
- Create: `contracts/fixtures/invalid/score_row/two-raters.json`
- Create: `tests/test_score_row.py`

**Interfaces:**
- Consumes: `errors_for`, `load_json`, `FIXTURES` from Task 1; `question_id` pattern from Task 2; `session_id` from Task 4.
- Produces: `contracts.tools.panel.aggregate(ratings: list[int]) -> tuple[float, int]` returning `(median_score, max_minus_min)` and raising `ValueError` for fewer than three ratings or ratings outside 1 to 5. `MIN_PANEL = 3`.

- [ ] **Step 1: Write the failing tests**

`tests/test_score_row.py`:

```python
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
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_score_row.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'contracts.tools.panel'`

- [ ] **Step 3: Write the panel tool**

`contracts/tools/panel.py`:

```python
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
```

- [ ] **Step 4: Write the schema**

`contracts/schemas/score_row.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://tryashley.ai/contracts/score_row.schema.json",
  "title": "ScoreRow",
  "description": "One scored answer: one row per (session, question). Stamps the instrument version, the scoring prompt version, and every model in the panel so the row can be reproduced and audited. Scores read the transcript only.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "score_row_id", "session_id", "question_id", "instrument_id", "instrument_version",
    "transcript_span", "panel", "aggregate", "disagreement", "scoring_prompt_version", "scored_at"
  ],
  "properties": {
    "score_row_id": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"},
    "session_id": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"},
    "question_id": {"type": "string", "pattern": "^q[0-9]{2}$"},
    "instrument_id": {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"},
    "instrument_version": {"type": "integer", "minimum": 1},
    "transcript_span": {
      "type": "object",
      "additionalProperties": false,
      "required": ["start_ms", "end_ms", "text_hash"],
      "properties": {
        "start_ms": {"type": "integer", "minimum": 0},
        "end_ms": {"type": "integer", "minimum": 0},
        "text_hash": {"type": "string", "pattern": "^sha256:[0-9a-f]{64}$"}
      }
    },
    "panel": {
      "type": "array",
      "minItems": 3,
      "maxItems": 7,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["rater_id", "rating", "rationale"],
        "properties": {
          "rater_id": {"type": "string", "pattern": "^[a-z0-9.-]+@[0-9]{4}-[0-9]{2}(-[0-9]{2})?$"},
          "rating": {"type": "integer", "minimum": 1, "maximum": 5},
          "rationale": {"type": "string", "minLength": 20}
        }
      }
    },
    "aggregate": {
      "type": "object",
      "additionalProperties": false,
      "required": ["method", "score"],
      "properties": {
        "method": {"const": "median"},
        "score": {"type": "number", "minimum": 1, "maximum": 5}
      }
    },
    "disagreement": {"type": "integer", "minimum": 0, "maximum": 4},
    "scoring_prompt_version": {"type": "string", "pattern": "^scoring-v[0-9]+$"},
    "scored_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"}
  }
}
```

- [ ] **Step 5: Write the fixtures**

`contracts/fixtures/valid/score_row/q01.json`:

```json
{
  "score_row_id": "33333333-3333-4333-8333-333333333301",
  "session_id": "22222222-2222-4222-8222-222222222222",
  "question_id": "q01",
  "instrument_id": "retail-associate",
  "instrument_version": 1,
  "transcript_span": {
    "start_ms": 41200,
    "end_ms": 118900,
    "text_hash": "sha256:9c1185a5c5e9fc54612808977ee8f548b2258d31f8d0d2f4a0f7c2f0f4a1b2c3"
  },
  "panel": [
    {"rater_id": "glm-5.3@2026-09", "rating": 4, "rationale": "Specific situation, action, and outcome; learning stated only briefly."},
    {"rater_id": "claude-sonnet-5@2026-09", "rating": 4, "rationale": "Clear example with action and result; what they would change is implied, not stated."},
    {"rater_id": "gpt-5@2026-09", "rating": 5, "rationale": "All four anchor elements present: situation, chosen action with reason, outcome, reflection."}
  ],
  "aggregate": {"method": "median", "score": 4.0},
  "disagreement": 1,
  "scoring_prompt_version": "scoring-v1",
  "scored_at": "2026-10-06T14:21:31Z"
}
```

`contracts/fixtures/invalid/score_row/two-raters.json`: copy of `q01.json` with the third panel entry (`gpt-5@2026-09`) removed, leaving two raters.

- [ ] **Step 6: Run the tests to verify they pass**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_score_row.py -v`
Expected: `9 passed`

- [ ] **Step 7: Commit**

```bash
git add contracts/schemas/score_row.schema.json contracts/tools/panel.py contracts/fixtures/valid/score_row contracts/fixtures/invalid/score_row tests/test_score_row.py
git commit -m "feat(contracts): score row schema and panel aggregation"
```

---

### Task 6: Outcome event schema, webhook signing, and the webhook contract document

**Files:**
- Create: `contracts/schemas/outcome_event.schema.json`
- Create: `contracts/tools/webhook_sign.py`
- Create: `contracts/WEBHOOKS.md`
- Create: `contracts/fixtures/valid/outcome_event/application_decision.json`
- Create: `contracts/fixtures/valid/outcome_event/hired.json`
- Create: `contracts/fixtures/valid/outcome_event/retained_90.json`
- Create: `contracts/fixtures/valid/outcome_event/separated.json`
- Create: `contracts/fixtures/valid/outcome_event/performance_rating.json`
- Create: `contracts/fixtures/invalid/outcome_event/bad-decision.json`
- Create: `contracts/fixtures/invalid/outcome_event/unknown-type.json`
- Create: `contracts/fixtures/invalid/outcome_event/hired-with-payload.json`
- Create: `tests/test_outcome_event.py`

**Interfaces:**
- Consumes: `errors_for`, `load_json`, `FIXTURES` from Task 1; `session_id` from Task 4.
- Produces: `contracts.tools.webhook_sign.sign(secret: bytes, message: bytes) -> str` returning `sha256=<hex>`, `verify(secret: bytes, message: bytes, header_value: str) -> bool`, `PREFIX = "sha256="`. The signed message is `f"{timestamp}.".encode() + body` as documented in `WEBHOOKS.md`. Outcome event types are consumed by Task 7's selection-rate rows (`application_decision.decision == "advanced"` is the selection).

- [ ] **Step 1: Write the failing tests**

`tests/test_outcome_event.py`:

```python
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
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_outcome_event.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'contracts.tools.webhook_sign'`

- [ ] **Step 3: Write the signing tool**

`contracts/tools/webhook_sign.py`:

```python
"""HMAC-SHA256 signing for outcome webhooks. Header: X-Ashley-Signature: sha256=<hex>.

The signed message is the timestamp header value, a dot, and the raw request body:
    message = f"{timestamp}.".encode() + body
"""
from __future__ import annotations

import hashlib
import hmac

PREFIX = "sha256="


def sign(secret: bytes, message: bytes) -> str:
    return PREFIX + hmac.new(secret, message, hashlib.sha256).hexdigest()


def verify(secret: bytes, message: bytes, header_value: str) -> bool:
    if not header_value.startswith(PREFIX):
        return False
    return hmac.compare_digest(sign(secret, message), header_value)
```

- [ ] **Step 4: Write the schema**

`contracts/schemas/outcome_event.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://tryashley.ai/contracts/outcome_event.schema.json",
  "title": "OutcomeEvent",
  "description": "An inbound fact about what happened after an interview, keyed to the session: application decision, hire, start, retention checkpoints, separation, manager rating. These are the only labels that compound.",
  "type": "object",
  "additionalProperties": false,
  "required": ["event_id", "session_id", "event_type", "occurred_at", "source", "payload"],
  "properties": {
    "event_id": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"},
    "session_id": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"},
    "event_type": {
      "enum": ["application_decision", "hired", "started", "retained_30", "retained_90", "retained_365", "separated", "performance_rating"]
    },
    "occurred_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"},
    "source": {
      "type": "object",
      "additionalProperties": false,
      "required": ["system", "external_ref"],
      "properties": {
        "system": {"enum": ["ashby", "greenhouse", "icims", "bullhorn", "workstream", "fountain", "harri", "hris", "manual", "other"]},
        "external_ref": {"type": "string", "minLength": 1}
      }
    },
    "payload": {"type": "object"}
  },
  "allOf": [
    {
      "if": {"properties": {"event_type": {"const": "application_decision"}}, "required": ["event_type"]},
      "then": {
        "properties": {
          "payload": {
            "type": "object",
            "additionalProperties": false,
            "required": ["decision"],
            "properties": {"decision": {"enum": ["advanced", "rejected", "withdrawn"]}}
          }
        }
      }
    },
    {
      "if": {"properties": {"event_type": {"const": "separated"}}, "required": ["event_type"]},
      "then": {
        "properties": {
          "payload": {
            "type": "object",
            "additionalProperties": false,
            "required": ["reason", "tenure_days"],
            "properties": {
              "reason": {"enum": ["voluntary", "involuntary", "unknown"]},
              "tenure_days": {"type": "integer", "minimum": 0}
            }
          }
        }
      }
    },
    {
      "if": {"properties": {"event_type": {"const": "performance_rating"}}, "required": ["event_type"]},
      "then": {
        "properties": {
          "payload": {
            "type": "object",
            "additionalProperties": false,
            "required": ["scale_min", "scale_max", "value", "rated_at"],
            "properties": {
              "scale_min": {"type": "number"},
              "scale_max": {"type": "number"},
              "value": {"type": "number"},
              "rated_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"}
            }
          }
        }
      }
    },
    {
      "if": {"properties": {"event_type": {"enum": ["hired", "started", "retained_30", "retained_90", "retained_365"]}}, "required": ["event_type"]},
      "then": {"properties": {"payload": {"type": "object", "additionalProperties": false}}}
    }
  ]
}
```

- [ ] **Step 5: Write the fixtures**

All valid fixtures share `"session_id": "22222222-2222-4222-8222-222222222222"` and `"source": {"system": "ashby", "external_ref": "a_90871"}`.

`contracts/fixtures/valid/outcome_event/application_decision.json`:

```json
{
  "event_id": "44444444-4444-4444-8444-444444444401",
  "session_id": "22222222-2222-4222-8222-222222222222",
  "event_type": "application_decision",
  "occurred_at": "2026-10-08T16:10:00Z",
  "source": {"system": "ashby", "external_ref": "a_90871"},
  "payload": {"decision": "advanced"}
}
```

`hired.json`: same shape with `"event_id": "44444444-4444-4444-8444-444444444402"`, `"event_type": "hired"`, `"occurred_at": "2026-10-15T09:00:00Z"`, `"payload": {}`.

`retained_90.json`: `"event_id": "44444444-4444-4444-8444-444444444403"`, `"event_type": "retained_90"`, `"occurred_at": "2027-01-14T09:00:00Z"`, `"source": {"system": "hris", "external_ref": "emp_1180"}`, `"payload": {}`.

`separated.json`: `"event_id": "44444444-4444-4444-8444-444444444404"`, `"event_type": "separated"`, `"occurred_at": "2027-03-06T18:00:00Z"`, `"source": {"system": "hris", "external_ref": "emp_1180"}`, `"payload": {"reason": "voluntary", "tenure_days": 143}`.

`performance_rating.json`: `"event_id": "44444444-4444-4444-8444-444444444405"`, `"event_type": "performance_rating"`, `"occurred_at": "2027-01-20T12:00:00Z"`, `"source": {"system": "manual", "external_ref": "review-2027-q1"}`, `"payload": {"scale_min": 1, "scale_max": 5, "value": 4, "rated_at": "2027-01-20T12:00:00Z"}`.

`contracts/fixtures/invalid/outcome_event/bad-decision.json`: copy of `application_decision.json` with `"payload": {"decision": "maybe"}`.

`contracts/fixtures/invalid/outcome_event/unknown-type.json`: copy of `hired.json` with `"event_type": "promoted"`.

`contracts/fixtures/invalid/outcome_event/hired-with-payload.json`: copy of `hired.json` with `"payload": {"note": "great"}`.

- [ ] **Step 6: Write the webhook contract document**

`contracts/WEBHOOKS.md`:

```markdown
# Outcome webhooks (inbound to Ashley)

This document fixes the payload and signing contract for outcome events that customers and
integrations send back to Ashley. The endpoint URL and per-organization secret are issued during
onboarding; they are not part of this contract.

## Request

- Method: `POST`, body: one JSON document valid against `schemas/outcome_event.schema.json`.
- Headers:
  - `Content-Type: application/json`
  - `X-Ashley-Timestamp`: Unix seconds when the request was signed.
  - `X-Ashley-Event-Id`: the body's `event_id`, repeated for log correlation.
  - `X-Ashley-Signature`: `sha256=<hex>` where hex is HMAC-SHA256 over the message
    `"{X-Ashley-Timestamp}." + raw body bytes`, keyed with the organization's secret.
    Reference implementation: `tools/webhook_sign.py`.

## Responses

| Status | Meaning |
|---|---|
| 202 | Accepted and stored. |
| 200 | Duplicate `event_id` already stored; body ignored (idempotent). |
| 400 | Body fails the schema; response lists validation messages. |
| 401 | Signature missing or invalid, or timestamp older than 300 seconds. |
| 404 | `session_id` unknown to this organization. |

## Delivery rules for senders

- Retry on 5xx and on network failure with backoff at 1 minute, 5 minutes, 30 minutes, 2 hours,
  and 12 hours (five attempts), then alert a human. Never retry a 400 without changing the body.
- Delivery order is not guaranteed; consumers key on `session_id` and `occurred_at`.
- `event_id` must be a new UUID per fact; re-sending the same fact re-uses the same `event_id`.

## Event types and payloads

| `event_type` | `payload` |
|---|---|
| `application_decision` | `{"decision": "advanced" \| "rejected" \| "withdrawn"}` |
| `hired`, `started`, `retained_30`, `retained_90`, `retained_365` | `{}` |
| `separated` | `{"reason": "voluntary" \| "involuntary" \| "unknown", "tenure_days": <int>}` |
| `performance_rating` | `{"scale_min", "scale_max", "value", "rated_at"}` |

`selected`, for selection-rate reporting (`tools/selection_rates.py`), means an
`application_decision` with `decision == "advanced"`.
```

- [ ] **Step 7: Run the tests to verify they pass**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_outcome_event.py -v`
Expected: `12 passed`

- [ ] **Step 8: Commit**

```bash
git add contracts/schemas/outcome_event.schema.json contracts/tools/webhook_sign.py contracts/WEBHOOKS.md contracts/fixtures/valid/outcome_event contracts/fixtures/invalid/outcome_event tests/test_outcome_event.py
git commit -m "feat(contracts): outcome event schema, webhook signing, delivery contract"
```

---

### Task 7: Selection-rate math and the audit export manifest

**Files:**
- Create: `contracts/tools/selection_rates.py`
- Create: `contracts/schemas/audit_export.schema.json`
- Create: `contracts/fixtures/valid/audit_export/nyc-ll144-q4.json`
- Create: `contracts/fixtures/invalid/audit_export/deletion-missing-completed.json`
- Create: `tests/test_selection_rates.py`
- Create: `tests/test_audit_export.py`

**Interfaces:**
- Consumes: `errors_for`, `load_json`, `load_schema`, `FIXTURES` from Task 1; instrument `content_hash` shape from Task 2; `session_id` from Task 4.
- Produces: `contracts.tools.selection_rates.impact_ratios(rows: list[dict]) -> list[dict]` where each input row is `{"category": str, "group": str, "selected": bool}` (one per candidate per category) and each output row is `{"category", "group", "applicants", "selected", "selection_rate", "impact_ratio", "flagged"}` sorted by category then group; `FOUR_FIFTHS = 0.8`. Output rows validate against `audit_export.schema.json#/properties/selection_rates/items`.

- [ ] **Step 1: Write the failing tests**

`tests/test_selection_rates.py`:

```python
from contracts.tools.selection_rates import FOUR_FIFTHS, impact_ratios


def _rows(category, group, applicants, selected):
    return [{"category": category, "group": group, "selected": index < selected} for index in range(applicants)]


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
```

`tests/test_audit_export.py`:

```python
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
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_selection_rates.py tests/test_audit_export.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'contracts.tools.selection_rates'`

- [ ] **Step 3: Write the selection-rate tool**

`contracts/tools/selection_rates.py`:

```python
"""Selection rates and impact ratios per group, in the four-fifths form used by adverse-impact reporting.

Input rows: one per candidate per category, {"category": str, "group": str, "selected": bool}.
"selected" means an application_decision event with decision == "advanced".
"""
from __future__ import annotations

FOUR_FIFTHS = 0.8


def impact_ratios(rows: list[dict]) -> list[dict]:
    counts: dict[tuple[str, str], list[int]] = {}
    for row in rows:
        key = (row["category"], row["group"])
        applicants_selected = counts.setdefault(key, [0, 0])
        applicants_selected[0] += 1
        applicants_selected[1] += 1 if row["selected"] else 0

    by_category: dict[str, dict[str, list[int]]] = {}
    for (category, group), applicants_selected in counts.items():
        by_category.setdefault(category, {})[group] = applicants_selected

    output: list[dict] = []
    for category in sorted(by_category):
        groups = by_category[category]
        rates = {group: (selected / applicants if applicants else 0.0) for group, (applicants, selected) in groups.items()}
        top = max(rates.values())
        for group in sorted(groups):
            applicants, selected = groups[group]
            ratio = rates[group] / top if top else 0.0
            output.append({
                "category": category,
                "group": group,
                "applicants": applicants,
                "selected": selected,
                "selection_rate": round(rates[group], 4),
                "impact_ratio": round(ratio, 4),
                "flagged": (ratio < FOUR_FIFTHS) if top else False,
            })
    return output
```

- [ ] **Step 4: Write the schema**

`contracts/schemas/audit_export.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://tryashley.ai/contracts/audit_export.schema.json",
  "title": "AuditExport",
  "description": "Manifest of an audit export pack for one organization, period, and jurisdiction: which instrument versions were in use, selection rates and impact ratios per group, the deletion log, and disclosure counts.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "export_id", "org_id", "generated_at", "period", "jurisdiction", "instruments",
    "selection_rates", "deletion_log", "disclosure_receipts_count", "notices_sent"
  ],
  "properties": {
    "export_id": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"},
    "org_id": {"type": "string", "pattern": "^org_[A-Za-z0-9]{6,}$"},
    "generated_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"},
    "period": {
      "type": "object",
      "additionalProperties": false,
      "required": ["from", "to"],
      "properties": {
        "from": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"},
        "to": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"}
      }
    },
    "jurisdiction": {"enum": ["US-NYC-LL144", "US-IL-AIVIA", "US-IL-HB3773", "US-CA-ADMT", "EU-AIA"]},
    "instruments": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["instrument_id", "version", "content_hash"],
        "properties": {
          "instrument_id": {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"},
          "version": {"type": "integer", "minimum": 1},
          "content_hash": {"type": "string", "pattern": "^sha256:[0-9a-f]{64}$"}
        }
      }
    },
    "selection_rates": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["category", "group", "applicants", "selected", "selection_rate", "impact_ratio", "flagged"],
        "properties": {
          "category": {"type": "string", "minLength": 1},
          "group": {"type": "string", "minLength": 1},
          "applicants": {"type": "integer", "minimum": 0},
          "selected": {"type": "integer", "minimum": 0},
          "selection_rate": {"type": "number", "minimum": 0, "maximum": 1},
          "impact_ratio": {"type": "number", "minimum": 0, "maximum": 1},
          "flagged": {"type": "boolean"}
        }
      }
    },
    "deletion_log": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["session_id", "requested_at", "completed_at", "scope"],
        "properties": {
          "session_id": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"},
          "requested_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"},
          "completed_at": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$"},
          "scope": {"enum": ["recording", "transcript", "derived-features", "all"]}
        }
      }
    },
    "disclosure_receipts_count": {"type": "integer", "minimum": 0},
    "notices_sent": {"type": "integer", "minimum": 0}
  }
}
```

- [ ] **Step 5: Write the fixtures**

`contracts/fixtures/valid/audit_export/nyc-ll144-q4.json` (the instrument hash here is illustrative; the export generator copies the real hash from the instrument file):

```json
{
  "export_id": "55555555-5555-4555-8555-555555555501",
  "org_id": "org_acme001",
  "generated_at": "2027-01-05T10:00:00Z",
  "period": {"from": "2026-10-01", "to": "2026-12-31"},
  "jurisdiction": "US-NYC-LL144",
  "instruments": [
    {"instrument_id": "retail-associate", "version": 1, "content_hash": "sha256:0000000000000000000000000000000000000000000000000000000000000000"}
  ],
  "selection_rates": [
    {"category": "sex", "group": "female", "applicants": 120, "selected": 50, "selection_rate": 0.4167, "impact_ratio": 0.9029, "flagged": false},
    {"category": "sex", "group": "male", "applicants": 130, "selected": 60, "selection_rate": 0.4615, "impact_ratio": 1.0, "flagged": false},
    {"category": "race_ethnicity", "group": "black", "applicants": 70, "selected": 24, "selection_rate": 0.3429, "impact_ratio": 0.7714, "flagged": true},
    {"category": "race_ethnicity", "group": "white", "applicants": 90, "selected": 40, "selection_rate": 0.4444, "impact_ratio": 1.0, "flagged": false}
  ],
  "deletion_log": [
    {"session_id": "22222222-2222-4222-8222-222222222223", "requested_at": "2026-11-02T09:15:00Z", "completed_at": "2026-11-02T09:15:42Z", "scope": "all"}
  ],
  "disclosure_receipts_count": 250,
  "notices_sent": 250
}
```

`contracts/fixtures/invalid/audit_export/deletion-missing-completed.json`: copy of `nyc-ll144-q4.json` with `completed_at` removed from the deletion log entry.

- [ ] **Step 6: Run the tests to verify they pass**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_selection_rates.py tests/test_audit_export.py -v`
Expected: `9 passed`

- [ ] **Step 7: Commit**

```bash
git add contracts/tools/selection_rates.py contracts/schemas/audit_export.schema.json contracts/fixtures/valid/audit_export contracts/fixtures/invalid/audit_export tests/test_selection_rates.py tests/test_audit_export.py
git commit -m "feat(contracts): four-fifths selection rates and audit export manifest"
```

---

### Task 8: Fixture sweep, words-only guard, and the contracts README

**Files:**
- Create: `tests/test_fixture_sweep.py`
- Create: `tests/test_words_only_guard.py`
- Create: `tests/test_contracts_readme.py`
- Create: `contracts/README.md`

**Interfaces:**
- Consumes: `errors_for`, `load_json`, `SCHEMAS`, `FIXTURES`, `INSTRUMENTS` from Task 1; every schema and fixture from Tasks 2 to 7.
- Produces: nothing new; this task locks the invariants every later change must keep.

- [ ] **Step 1: Write the failing tests**

`tests/test_fixture_sweep.py`:

```python
import pytest

from contracts.tools.validate import FIXTURES, INSTRUMENTS, SCHEMAS, errors_for, load_json


def _cases(kind: str) -> list[tuple[str, object]]:
    root = FIXTURES / kind
    return sorted(
        (schema_dir.name, path)
        for schema_dir in root.iterdir() if schema_dir.is_dir()
        for path in schema_dir.glob("*.json")
    )


VALID = _cases("valid")
INVALID = _cases("invalid")


@pytest.mark.parametrize("schema_name,path", VALID, ids=[f"{name}/{path.name}" for name, path in VALID])
def test_valid_fixture_validates(schema_name, path):
    assert errors_for(schema_name, load_json(path)) == []


@pytest.mark.parametrize("schema_name,path", INVALID, ids=[f"{name}/{path.name}" for name, path in INVALID])
def test_invalid_fixture_fails(schema_name, path):
    assert errors_for(schema_name, load_json(path)) != []


def test_every_instrument_file_validates():
    files = sorted(INSTRUMENTS.glob("*.json"))
    assert files, "no instruments found"
    for path in files:
        assert errors_for("instrument", load_json(path)) == [], path.name


def test_every_schema_has_valid_and_invalid_examples():
    for schema_path in sorted(SCHEMAS.glob("*.schema.json")):
        name = schema_path.name.removesuffix(".schema.json")
        has_valid = any((FIXTURES / "valid" / name).glob("*.json")) or (name == "instrument" and any(INSTRUMENTS.glob("*.json")))
        has_invalid = any((FIXTURES / "invalid" / name).glob("*.json"))
        assert has_valid, f"{name}: no valid example"
        assert has_invalid, f"{name}: no invalid example"
```

`tests/test_words_only_guard.py`:

```python
import re

from contracts.tools.validate import SCHEMAS, load_json

FORBIDDEN = re.compile(r"(expression|emotion|facial|\bface\b|appearance|accent|gaze|posture|smile|attractive)", re.IGNORECASE)


def _property_names(node, found: set[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "properties" and isinstance(value, dict):
                for prop_name, prop_schema in value.items():
                    found.add(prop_name)
                    _property_names(prop_schema, found)
            elif key in ("enum", "required", "const", "pattern", "description", "title"):
                continue
            else:
                _property_names(value, found)
    elif isinstance(node, list):
        for item in node:
            _property_names(item, found)


def test_no_schema_exposes_appearance_or_emotion_features():
    offenders = []
    for schema_path in sorted(SCHEMAS.glob("*.schema.json")):
        names: set[str] = set()
        _property_names(load_json(schema_path), names)
        offenders += [f"{schema_path.name}:{name}" for name in sorted(names) if FORBIDDEN.search(name)]
    assert offenders == []


def test_guard_catches_a_forbidden_name():
    names: set[str] = set()
    _property_names({"properties": {"facial_expression_score": {"type": "number"}}}, names)
    assert any(FORBIDDEN.search(name) for name in names)
```

`tests/test_contracts_readme.py`:

```python
from contracts.tools.validate import ROOT, SCHEMAS

README = ROOT / "contracts" / "README.md"


def test_readme_names_every_schema_and_the_webhook_doc():
    text = README.read_text(encoding="utf-8")
    for schema_path in SCHEMAS.glob("*.schema.json"):
        assert schema_path.name in text, schema_path.name
    assert "WEBHOOKS.md" in text
    assert "content_hash" in text
```

- [ ] **Step 2: Run the tests to verify the README test fails**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_fixture_sweep.py tests/test_words_only_guard.py tests/test_contracts_readme.py -v`
Expected: the sweep and guard tests PASS; `test_readme_names_every_schema_and_the_webhook_doc` FAILS with `FileNotFoundError` for `contracts/README.md`

- [ ] **Step 3: Write the README**

`contracts/README.md`:

```markdown
# Ashley contracts

Interface contracts for the moat design (`docs/superpowers/specs/2026-09-23-competitive-moat-design.md`).
The product implements against these; this repository only defines and tests them.

## Layout

| Path | Purpose |
|---|---|
| `schemas/instrument.schema.json` | Versioned, immutable interview instrument per hourly role family |
| `schemas/disclosure_receipt.schema.json` | Evidence of AI disclosure and consent; pooling consent is separate and opt-in |
| `schemas/interview_session.schema.json` | One conversation: instrument version, retention, result for human review |
| `schemas/score_row.schema.json` | One scored answer with a panel of model ratings and every version stamped |
| `schemas/outcome_event.schema.json` | Inbound facts after the interview: decision, hire, retention, separation, rating |
| `schemas/audit_export.schema.json` | Manifest of an audit export pack per organization, period, jurisdiction |
| `instruments/` | Real instruments in use (each must validate and carry a correct `content_hash`) |
| `fixtures/valid/<schema>/`, `fixtures/invalid/<schema>/` | Examples that must pass or must fail |
| `tools/` | Reference implementations: validation CLI, instrument hash, panel aggregation, webhook signing, selection rates |
| `WEBHOOKS.md` | Outcome webhook delivery and signing contract |

## Rules

- Instruments are immutable once `active`. Any change to question or anchor text is a new
  `version` with a new `content_hash` (computed by `tools/instrument_hash.py`, over every field
  except `content_hash` and `status`). `status` may change without a new version.
- Scores read the transcript only. No schema may carry a property about expression, emotion,
  face, appearance, accent, gaze, or posture; `tests/test_words_only_guard.py` enforces this.
- Consent to record is required for a session to exist. Consent to pooled learning is a separate
  boolean on the disclosure receipt; when true, the pooling text version shown must be named.
- Deletion propagates to derived features and every completed deletion appears in the export
  pack's `deletion_log`.
- Schemas evolve compatibly (new optional fields only). A breaking change is a new file with a
  new `$id` ending in `/v2/...`; the old file stays until no producer emits it.

## Validate a document

```bash
.venv/bin/python -m contracts.tools.validate interview_session path/to/session.json
```

Prints each validation message and `VALID` or `INVALID (n errors)`; exit code 0 or 1.

## Run the tests

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest
```
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -v`
Expected: all tests pass; the sweep reports one `test_valid_fixture_validates` and one `test_invalid_fixture_fails` case per fixture file (11 valid, 10 invalid at this point)

- [ ] **Step 5: Commit**

```bash
git add tests/test_fixture_sweep.py tests/test_words_only_guard.py tests/test_contracts_readme.py contracts/README.md
git commit -m "test(contracts): fixture sweep, words-only guard, README"
```

---

### Task 9: Company OS wiki page and index row

**Files:**
- Create: `blueprint/wiki/moat-decisions.md`
- Modify: `blueprint/INDEX.md` (add one row to the Wiki table, after the `wiki/onboarding.md` row)
- Create: `tests/test_company_os_docs.py`

**Interfaces:**
- Consumes: `ROOT` from Task 1.
- Produces: nothing; this records the decision where Claude sessions in this repo will find it.

- [ ] **Step 1: Write the failing test**

`tests/test_company_os_docs.py`:

```python
from contracts.tools.validate import ROOT

WIKI = ROOT / "blueprint" / "wiki" / "moat-decisions.md"
INDEX = ROOT / "blueprint" / "INDEX.md"
SPEC = "docs/superpowers/specs/2026-09-23-competitive-moat-design.md"


def test_wiki_page_links_spec_and_contracts():
    text = WIKI.read_text(encoding="utf-8")
    assert SPEC in text
    assert "contracts/schemas" in text
    assert "words only" in text.lower()


def test_index_lists_wiki_page():
    assert "wiki/moat-decisions.md" in INDEX.read_text(encoding="utf-8")
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_company_os_docs.py -v`
Expected: FAIL with `FileNotFoundError` for `blueprint/wiki/moat-decisions.md`

- [ ] **Step 3: Write the wiki page**

`blueprint/wiki/moat-decisions.md`:

```markdown
# Moat decisions

Decided 2026-09-23 after a five-worker research run. Full design and evidence:
`docs/superpowers/specs/2026-09-23-competitive-moat-design.md` (research reports beside it).

## The decision

- The in-house real-time face is a cost and latency advantage, not the moat. Real-time photoreal
  avatars rent from about $0.04 per minute and open-source lip-sync models run in real time on a
  single consumer GPU.
- The moat is an embedded, instrumented interview layer for hourly hiring: two-way ATS
  integration, outcome webhooks coming back in, a stable versioned instrument per role family,
  and per-customer outcome calibration. Switching costs now, a data moat later.
- Cheap compliance products are layered on: disclosure receipts, audit exports, a published
  bias audit when cash allows, and the ISO 42001 clock started without spend.
- Scoring reads words only, forever. No expression, emotion, appearance, or accent features.

## Where the contracts live

`contracts/schemas/` holds the JSON schemas for instruments, disclosure receipts, interview
sessions, score rows, outcome events, and audit exports; `contracts/tools/` holds the reference
calculations; `contracts/WEBHOOKS.md` fixes the inbound webhook contract.

## Rules for future sessions

- Never add a scored feature about a candidate's face, voice tone, or appearance.
- Never change an active instrument in place; publish a new version.
- Never pool interview data across employers without the pooling consent flag on the receipt.
- Prefer one integration and one proof point per quarter; the founders are two people.
```

- [ ] **Step 4: Add the index row**

In `blueprint/INDEX.md`, under `## Wiki`, add this row after the `wiki/onboarding.md` row:

```markdown
| wiki/moat-decisions.md | Moat strategy decision, contract locations, rules for future work | 2026-09-24 |
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_company_os_docs.py -v`
Expected: `2 passed`

- [ ] **Step 6: Commit**

```bash
git add blueprint/wiki/moat-decisions.md blueprint/INDEX.md tests/test_company_os_docs.py
git commit -m "docs(company-os): record moat decisions in the wiki and index"
```

---

### Task 10: Flagship criteria and the ATS check

**Files:**
- Create: `docs/moat/flagship-targets.md`
- Create: `docs/moat/ats-check.md`
- Create: `tests/test_q4_docs.py`

**Interfaces:**
- Consumes: `ROOT` from Task 1; the ATS enum from Task 4 (`ashby`, `greenhouse`, `icims`, `bullhorn`, `workstream`, `fountain`, `harri`).
- Produces: the two documents the founders fill in during Q4; Task 11 extends the same test file.

- [ ] **Step 1: Write the failing test**

`tests/test_q4_docs.py`:

```python
from contracts.tools.validate import ROOT

DOCS = ROOT / "docs" / "moat"
ATS_SYSTEMS = ["Workstream", "Fountain", "Harri", "Ashby", "Greenhouse", "iCIMS", "Bullhorn"]
FLAGSHIP_COLUMNS = ["Company", "Segment", "Locations", "Applicants/month", "ATS", "Contact path", "Why now", "Status", "Next step"]


def test_flagship_doc_has_criteria_and_tracking_columns():
    text = (DOCS / "flagship-targets.md").read_text(encoding="utf-8")
    assert "## Qualification criteria" in text
    assert "## Disqualifiers" in text
    assert "## Definition of done" in text
    for column in FLAGSHIP_COLUMNS:
        assert column in text, column


def test_ats_check_covers_every_candidate_system():
    text = (DOCS / "ats-check.md").read_text(encoding="utf-8")
    for system in ATS_SYSTEMS:
        assert f"## {system}" in text, system
    assert "Webhook on stage change" in text
    assert "Write back a score" in text
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_q4_docs.py -v`
Expected: FAIL with `FileNotFoundError` for `docs/moat/flagship-targets.md`

- [ ] **Step 3: Write the flagship document**

`docs/moat/flagship-targets.md`:

```markdown
# Flagship target: one multi-location hourly employer

The Q4 2026 proof point is one flagship signed on per-interview pricing with outcome webhooks
enabled. Everything in the moat design is built to make that customer expensive to leave.

## Qualification criteria

- Multi-location operator: at least 5 locations under one hiring owner (franchise group, retail
  chain, QSR operator, or a staffing agency on Bullhorn placing hourly workers).
- Volume: at least 200 applicants per month across locations for roles inside the ten hourly
  role families the instruments cover.
- Stack: uses one of Ashby, Greenhouse, iCIMS, Bullhorn, Workstream, Fountain, or Harri, or is
  willing to run interviews from a hosted link until the integration lands.
- Owner: one person who owns hiring operations and can sign a month-to-month plan without a
  procurement cycle.
- Outcomes: willing to send hire and 90-day retention events back under the data-processing
  agreement (customer owns its data; pooling stays opt-in).
- Jurisdiction: US locations where the audit exports apply (New York City, Illinois, California,
  Texas, or states with no extra AI-hiring rule).

## Disqualifiers

- Enterprise security review longer than 8 weeks or an RFP process.
- EU-only hiring before the EU AI Act high-risk date (2 December 2027).
- Roles outside the instrument set (skilled trades, licensed clinical, knowledge work).
- Refuses outcome data sharing entirely; without labels the account does not build the moat.

## Outreach outline

1. Lead with the coverage gap: they interview a fraction of applicants; Ashley interviews all of
   them in minutes, on the candidate's schedule.
2. Offer the free 10 interviews on one real role, scored on their rubric, within a week.
3. Close on per-interview pricing plus the outcome webhook, framed as "we show you which
   interview answers predict your own 90-day retention".

## Tracking table

| Company | Segment | Locations | Applicants/month (est.) | ATS | Contact path | Why now | Status | Next step |
|---|---|---|---|---|---|---|---|---|

Add one row per qualified target. Keep disqualified targets in the table with Status
`disqualified` and the reason in Next step, so the same company is not researched twice.

## Definition of done

One flagship signed on per-interview pricing, integrated with its ATS or running from a hosted
link, with `application_decision` and `hired` outcome events arriving for real candidates.
```

- [ ] **Step 4: Write the ATS check document**

`docs/moat/ats-check.md`:

```markdown
# ATS integration check

Answer every question for every system before choosing the first integration. The choice is
made by where the flagship's applicants live, not by marketplace prestige.

Questions to answer per system:

1. Public API documentation URL found?
2. Webhook on stage change (so an interview can be triggered when a candidate reaches a stage)?
3. Write back a score, transcript link, and recommendation to the candidate or application record?
4. Partner or marketplace program: requirements, review time, listing fee?
5. Sandbox or test account available without a customer?
6. Auth model (OAuth app, API key per customer, or partner credentials)?
7. Rate limits that matter at 400 interviews a month?
8. Estimated integration effort in engineer-days, assuming one founder.

Known starting points: Ashby (`developers.ashbyhq.com`, Assessments framework), Greenhouse
(`developers.greenhouse.io`, Harvest API and Assessment API), Bullhorn (`bullhorn.github.io`,
REST API). For Workstream, Fountain, Harri, and iCIMS, start from the vendor's own site and
its partner page; the research run did not verify these.

## Workstream

| # | Question | Answer | Source URL | Date |
|---|---|---|---|---|
| 1 | Public API documentation URL found? | | | |
| 2 | Webhook on stage change? | | | |
| 3 | Write back a score, transcript link, recommendation? | | | |
| 4 | Partner or marketplace program? | | | |
| 5 | Sandbox available? | | | |
| 6 | Auth model? | | | |
| 7 | Rate limits? | | | |
| 8 | Effort (engineer-days)? | | | |

## Fountain

| # | Question | Answer | Source URL | Date |
|---|---|---|---|---|
| 1 | Public API documentation URL found? | | | |
| 2 | Webhook on stage change? | | | |
| 3 | Write back a score, transcript link, recommendation? | | | |
| 4 | Partner or marketplace program? | | | |
| 5 | Sandbox available? | | | |
| 6 | Auth model? | | | |
| 7 | Rate limits? | | | |
| 8 | Effort (engineer-days)? | | | |

## Harri

| # | Question | Answer | Source URL | Date |
|---|---|---|---|---|
| 1 | Public API documentation URL found? | | | |
| 2 | Webhook on stage change? | | | |
| 3 | Write back a score, transcript link, recommendation? | | | |
| 4 | Partner or marketplace program? | | | |
| 5 | Sandbox available? | | | |
| 6 | Auth model? | | | |
| 7 | Rate limits? | | | |
| 8 | Effort (engineer-days)? | | | |

## Ashby

| # | Question | Answer | Source URL | Date |
|---|---|---|---|---|
| 1 | Public API documentation URL found? | | | |
| 2 | Webhook on stage change? | | | |
| 3 | Write back a score, transcript link, recommendation? | | | |
| 4 | Partner or marketplace program? | | | |
| 5 | Sandbox available? | | | |
| 6 | Auth model? | | | |
| 7 | Rate limits? | | | |
| 8 | Effort (engineer-days)? | | | |

## Greenhouse

| # | Question | Answer | Source URL | Date |
|---|---|---|---|---|
| 1 | Public API documentation URL found? | | | |
| 2 | Webhook on stage change? | | | |
| 3 | Write back a score, transcript link, recommendation? | | | |
| 4 | Partner or marketplace program? | | | |
| 5 | Sandbox available? | | | |
| 6 | Auth model? | | | |
| 7 | Rate limits? | | | |
| 8 | Effort (engineer-days)? | | | |

## iCIMS

| # | Question | Answer | Source URL | Date |
|---|---|---|---|---|
| 1 | Public API documentation URL found? | | | |
| 2 | Webhook on stage change? | | | |
| 3 | Write back a score, transcript link, recommendation? | | | |
| 4 | Partner or marketplace program? | | | |
| 5 | Sandbox available? | | | |
| 6 | Auth model? | | | |
| 7 | Rate limits? | | | |
| 8 | Effort (engineer-days)? | | | |

## Bullhorn

| # | Question | Answer | Source URL | Date |
|---|---|---|---|---|
| 1 | Public API documentation URL found? | | | |
| 2 | Webhook on stage change? | | | |
| 3 | Write back a score, transcript link, recommendation? | | | |
| 4 | Partner or marketplace program? | | | |
| 5 | Sandbox available? | | | |
| 6 | Auth model? | | | |
| 7 | Rate limits? | | | |
| 8 | Effort (engineer-days)? | | | |

## Decision

First integration: (system) because (flagship's stack). Second integration: (system) because
(reason). Record the date and who decided.
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_q4_docs.py -v`
Expected: `2 passed`

- [ ] **Step 6: Commit**

```bash
git add docs/moat/flagship-targets.md docs/moat/ats-check.md tests/test_q4_docs.py
git commit -m "docs(moat): flagship criteria and ATS integration check"
```

---

### Task 11: Audit vendor RFQ and the ISO 42001 skeleton

**Files:**
- Create: `docs/moat/audit-vendor-rfq.md`
- Create: `docs/moat/iso42001-skeleton.md`
- Modify: `tests/test_q4_docs.py` (append two tests)

**Interfaces:**
- Consumes: `ROOT` from Task 1; contract file names from Tasks 2 to 7 (referenced as evidence).
- Produces: nothing; these are the founders' working documents for the compliance layer.

- [ ] **Step 1: Append the failing tests**

Append to `tests/test_q4_docs.py`:

```python
AUDIT_VENDORS = ["BABL AI", "Warden AI", "Holistic AI"]
ISO_SECTIONS = ["## 4. Context", "## 5. Leadership", "## 6. Planning", "## 7. Support", "## 8. Operation", "## 9. Performance evaluation", "## 10. Improvement"]


def test_audit_rfq_names_vendors_and_questions():
    text = (DOCS / "audit-vendor-rfq.md").read_text(encoding="utf-8")
    for vendor in AUDIT_VENDORS:
        assert vendor in text, vendor
    assert "## Questions for every vendor" in text
    assert "impact ratio" in text
    assert "publication" in text.lower()


def test_iso42001_skeleton_maps_clauses_to_evidence():
    text = (DOCS / "iso42001-skeleton.md").read_text(encoding="utf-8")
    for section in ISO_SECTIONS:
        assert section in text, section
    for evidence in ["instrument.schema.json", "disclosure_receipt.schema.json", "audit_export.schema.json"]:
        assert evidence in text, evidence
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/test_q4_docs.py -v`
Expected: the two new tests FAIL with `FileNotFoundError`; the two Task 10 tests PASS

- [ ] **Step 3: Write the audit RFQ**

`docs/moat/audit-vendor-rfq.md`:

```markdown
# Independent bias audit: request for quotes

Purpose: a standing annual independent bias audit of Ashley's scoring, published with its
methodology. The first audit is bought when cash allows (research estimate $25k to $75k a year).
Vendors to approach: BABL AI, Warden AI, Holistic AI. Ribbon already advertises a 2025 NYC audit
and Eightfold publishes a BABL AI audit, so this closes a gap; publishing methodology and results
is the differentiating part.

## What to send each vendor

- `contracts/schemas/instrument.schema.json` and the active instruments.
- `contracts/schemas/score_row.schema.json` (panel scoring, versions stamped per row).
- `contracts/schemas/audit_export.schema.json` and the selection-rate calculation in
  `contracts/tools/selection_rates.py`.
- Expected volumes for the audit period and the demographic categories available.

## Questions for every vendor

1. Scope for a scored tool under NYC Local Law 144: impact ratio on selection rates, and the
   scoring-rate analysis for scored outputs. Which do you perform, and on what minimum sample?
2. Do you also cover Illinois HB 3773 and California FEHA automated-decision rules in the same
   engagement, or is that separate?
3. What data do you need, in what format, and can you consume our export pack as is?
4. Timeline from data handoff to signed audit, and the annual re-audit cadence and price.
5. Price for year one and for renewal; what changes the price (volume, categories, instruments).
6. Publication rights: can we publish the full audit and methodology, not only a summary?
7. Independence: confirm no employment or ownership relationship with Ashley or the customer.
8. Do you audit the reference calculation itself (`selection_rates.py`) or only its outputs?

## Comparison table

| Vendor | LL144 scope | Other laws covered | Data format | Timeline | Year-one price | Renewal | Publication rights | Notes |
|---|---|---|---|---|---|---|---|---|
| BABL AI | | | | | | | | |
| Warden AI | | | | | | | | |
| Holistic AI | | | | | | | | |

## Decision rule

Choose the vendor that allows full publication and audits the calculation itself; price is the
tiebreaker. Record the decision date and the audit period it will cover.
```

- [ ] **Step 4: Write the ISO 42001 skeleton**

`docs/moat/iso42001-skeleton.md`:

```markdown
# ISO/IEC 42001 skeleton: start the clock, defer the spend

Certification takes months and Sapia.ai already holds the first one in the category. This
document maps each clause of the standard to evidence Ashley produces anyway, so certification
becomes a paperwork exercise when a customer demands it. Fill each "Evidence" line with a file
path or a link; leave nothing as prose only.

## 4. Context

- Interested parties: employers, candidates, regulators (NYC DCWP, Illinois IDHR, California CRD,
  EU market surveillance), auditors.
- Scope statement: AI-conducted first-round interviews scored on words only.
- Evidence: this file; `docs/superpowers/specs/2026-09-23-competitive-moat-design.md`.

## 5. Leadership

- AI policy: disclosed AI, words-only scoring, human decides, no auto-rejection, opt-in pooling.
- Roles: one founder named as AI management system owner; one as data protection contact.
- Evidence: `blueprint/wiki/moat-decisions.md`; the public candidates page.

## 6. Planning

- Risk assessment per instrument version: adverse impact, prompt sensitivity, deletion failure,
  disclosure failure, expression-scoring drift.
- Objectives: impact ratio at or above 0.8 per category; zero un-receipted interviews; deletion
  completed within 30 days of request.
- Evidence: `contracts/schemas/instrument.schema.json` (versioning), `contracts/schemas/audit_export.schema.json` (impact ratios, deletion log).

## 7. Support

- Competence: who may publish an instrument version or a scoring prompt version.
- Documentation control: schemas and instruments are version-controlled in this repository.
- Evidence: `contracts/README.md`; git history.

## 8. Operation

- AI system lifecycle: instrument creation, panel scoring, human review, outcome ingestion.
- Data management: consent and disclosure receipts, retention policies, deletion propagation,
  pooling only on opted-in rows.
- Evidence: `contracts/schemas/disclosure_receipt.schema.json`, `contracts/schemas/interview_session.schema.json`, `contracts/schemas/score_row.schema.json`, `contracts/WEBHOOKS.md`.

## 9. Performance evaluation

- Monitoring: per-instrument impact ratios each quarter; benchmark results before every scoring
  change; candidate completion and complaint rates.
- Internal audit: annual review of exports against the schema; independent bias audit.
- Evidence: audit export packs; `docs/moat/audit-vendor-rfq.md`.

## 10. Improvement

- Nonconformity handling: a flagged impact ratio triggers instrument review before the next
  version; a disclosure or deletion failure is logged and root-caused.
- Evidence: issue log (to be created when the first nonconformity occurs); new instrument versions.
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -v`
Expected: all tests pass, including `4 passed` in `tests/test_q4_docs.py`

- [ ] **Step 6: Commit**

```bash
git add docs/moat/audit-vendor-rfq.md docs/moat/iso42001-skeleton.md tests/test_q4_docs.py
git commit -m "docs(moat): audit vendor RFQ and ISO 42001 skeleton"
```

---

## Deferred to the product code-level plan

These spec items need Ashley's product codebase and get their own plan once it is available. Each maps to a contract above so the two plans meet at a tested boundary.

| Spec item | Contract here | Product work deferred |
|---|---|---|
| Append-only event log (4.3) | `score_row`, `interview_session`, `outcome_event` schemas | Persistence, retention jobs, feature-store deletion |
| Two-way ATS integration (4.2) | `interview_session.ats`, outcome `source.system` | Stage-change triggers, write-back per system |
| Outcome webhooks in (4.2) | `outcome_event.schema.json`, `WEBHOOKS.md`, `webhook_sign.py` | Endpoint, secret issuance, idempotent store, retries |
| Stable instrument per role family (4.2) | `instrument.schema.json`, `instrument_hash.py`, `instruments/` | Instrument registry, activation workflow, the other five to nine instruments |
| Panel scoring (4.3) | `score_row.schema.json`, `panel.py` | Scoring service calling several models, prompt versioning |
| Disclosure receipts (4.4) | `disclosure_receipt.schema.json` | Interview UI, receipt storage |
| Audit exports (4.4) | `audit_export.schema.json`, `selection_rates.py` | Export generator, demographic data handling |
| Per-customer calibration (4.2) | `outcome_event` labels joined on `session_id` | Reporting per customer |
| Frozen benchmark per role family (4.3) | `score_row` rows plus outcome labels | Dataset curation, evaluation harness |
