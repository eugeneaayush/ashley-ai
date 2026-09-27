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
- Scores read the transcript only. No schema may carry a name about expression, emotion, face,
  appearance, accent, gaze, posture, smile, tone, prosody, pitch, eyes, or affect;
  `tests/test_words_only_guard.py` enforces this by tokenizing: every property name and every
  string value inside `enum` and `const` in every schema is split into lowercase word tokens
  (on `_`, `-`, `.`, whitespace, and camelCase boundaries) and flagged when any token is
  forbidden, so `face_score` and `faceScore` are caught while `interface_id` and
  `pitchfork_count` pass.
- Consent to record is required for a session to exist. Consent to pooled learning is a separate
  boolean on the disclosure receipt; when true, the pooling text version shown must be named.
- A receipt with `consent_pooling` false may still record the pooling text version it showed, as
  evidence of what was declined; only the true direction is enforced by the schema.
- The optional `pooling_opted_in_receipts` count on audit exports is how the export evidences
  that pooled learning used only opted-in rows.
- Deletion propagates to derived features and every completed deletion appears in the export
  pack's `deletion_log`.
- Schemas evolve compatibly (new optional fields only). A breaking change is a new file with a
  new `$id` ending in `/v2/...`; the old file stays until no producer emits it.

## Rules JSON Schema cannot express

- A score row's `aggregate.score` and `disagreement` equal the panel median and the panel max
  minus min, and `transcript_span.end_ms >= start_ms` (`tools/panel.py` `consistency_errors`).
- A panel has 3 to 7 ratings (schema and `tools/panel.py`).
- Question ids are unique within an instrument (instrument authors).
- The canonical instrument form for hashing uses integers for integer values and NFC-normalized
  text (instrument authors).
- A performance rating has `scale_min < scale_max` and `value` within the scale (senders of
  outcome events).
- `selected <= applicants`, `period.from <= period.to`, and deletion `completed_at >=
  requested_at` (the export generator).
- The export generator copies each instrument's live `content_hash` into the export (the
  fixture's all-zero hash is illustrative).
- `flagged` uses the unrounded impact ratio (`tools/selection_rates.py`).

## Validate a document

```bash
.venv/bin/python -m contracts.tools.validate interview_session path/to/session.json
```

Prints each validation message and `VALID` or `INVALID (n errors)`; exit code 0 or 1.

## Run the tests

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest
```
