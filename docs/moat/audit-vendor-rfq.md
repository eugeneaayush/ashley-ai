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
