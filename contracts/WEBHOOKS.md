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
