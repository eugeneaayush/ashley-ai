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
