# Move idempotency replay storage to Redis

## Status

Rejected

## Proposal

Store idempotency keys and serialized order results in Redis with a 24-hour
expiration. This would make replay state independent of the order database.

## Decision

Do not adopt this proposal for the fixture. Splitting an accepted order from its
replay record creates a consistency boundary that is harder to reason about than
the current persistence-aligned design. It also adds an external dependency
without improving the OpenSteward test scenarios.

## Reconsider when

Revisit Redis only if measured order volume requires independent replay
retention or if multiple service instances cannot share the primary order
store.
