# Use SQLite for order persistence

## Status

Accepted

## Context

The fixture needs deterministic local persistence without an external service.
Historical pull requests should be able to discuss order storage and database
migrations using the same vocabulary as future changes.

## Decision

Use SQLite for order persistence and keep schema changes as numbered SQL files
under `migrations/`.

## Consequences

Database changes require migration review. A future production deployment would
need a different availability and backup strategy.

