# Idempotency retry guarantees

Clients should send a stable idempotency key for every logical order-creation
attempt. A retry with the same key returns the first accepted order, even when
the retry contains different order fields.

An empty idempotency key is rejected before order validation. Callers should
generate a new key only when they intend to create a distinct order.

The storage decision and its tradeoffs are recorded in
`docs/adr/0003-store-idempotency-results.md`.
