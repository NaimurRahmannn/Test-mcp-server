"""Tests exposing the intentionally incomplete payment implementation."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from test_mcp_server.payment import initial_payment_status


class InitialPaymentStatusTests(unittest.TestCase):
    def test_new_orders_start_pending(self) -> None:
        self.assertEqual(initial_payment_status(), "pending")


if __name__ == "__main__":
    unittest.main()
