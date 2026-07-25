"""Bearer-token validation for protected-path testing."""

import hmac


def validate_bearer_token(provided: str, expected: str) -> bool:
    """Compare non-empty bearer tokens without leaking timing information."""

    if not provided or not expected:
        return False
    return hmac.compare_digest(provided, expected)

