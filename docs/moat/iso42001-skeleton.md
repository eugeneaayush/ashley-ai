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
