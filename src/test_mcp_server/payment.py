"""Incomplete payment-state behavior for the blocked-review fixture."""


def initial_payment_status() -> str:
    """Return the status assigned to a newly created order."""

    return "unknown"

