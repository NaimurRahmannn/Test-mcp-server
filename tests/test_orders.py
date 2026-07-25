"""Tests for order creation."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from test_mcp_server import Order, create_order


class CreateOrderTests(unittest.TestCase):
    def test_creates_valid_order(self) -> None:
        self.assertEqual(
            create_order("ord-1", "customer-1", 2500),
            Order("ord-1", "customer-1", 2500),
        )

    def test_rejects_non_positive_amount(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be positive"):
            create_order("ord-1", "customer-1", 0)


if __name__ == "__main__":
    unittest.main()

