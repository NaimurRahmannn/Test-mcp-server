"""Tests for bearer-token validation."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from test_mcp_server.security import validate_bearer_token


class ValidateBearerTokenTests(unittest.TestCase):
    def test_accepts_matching_token(self) -> None:
        self.assertTrue(validate_bearer_token("Bearer secret", "secret"))
        self.assertTrue(validate_bearer_token("bearer secret", "secret"))

    def test_rejects_missing_scheme_or_different_token(self) -> None:
        self.assertFalse(validate_bearer_token("", "secret"))
        self.assertFalse(validate_bearer_token("secret", "secret"))
        self.assertFalse(validate_bearer_token("Basic secret", "secret"))
        self.assertFalse(validate_bearer_token("Bearer wrong", "secret"))


if __name__ == "__main__":
    unittest.main()
