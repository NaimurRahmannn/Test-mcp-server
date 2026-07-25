# Store idempotency results with order persistence

## Status

Accepted

## Context

Order clients retry requests after network failures. Reprocessing the same
command can duplicate downstream work even when the order identifier is stable.

## Decision

Associate each caller-provided idempotency key with the first accepted order.
Repeated requests return that original result. The fixture uses an in-memory
store, while a deployed service would keep this mapping beside SQLite order
persistence.

## Consequences

Idempotency keys become part of the order-creation contract. Storage cleanup,
retention, and replay behavior require explicit review when they change.
