"""Bearer-token validation for protected-path testing."""

import hmac


def validate_bearer_token(authorization: str, expected: str) -> bool:
    """Parse and compare a bearer credential without leaking timing information."""

    scheme, separator, provided = authorization.partition(" ")
    if (
        not separator
        or scheme.casefold() != "bearer"
        or not provided
        or not expected
    ):
        return False
    return hmac.compare_digest(provided, expected)

