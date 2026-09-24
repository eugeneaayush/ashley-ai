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
