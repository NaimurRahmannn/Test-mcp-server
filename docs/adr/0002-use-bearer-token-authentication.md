# Use bearer-token authentication

## Status

Accepted

## Context

Order creation needs a narrow authentication boundary that is easy to exercise
in security-sensitive pull requests.

## Decision

Validate a bearer token before accepting an order command. Keep token handling
inside `src/test_mcp_server/security/`.

## Consequences

Token validation is a protected path and requires security-specialist review.
Secrets must never be logged or returned in error details.

