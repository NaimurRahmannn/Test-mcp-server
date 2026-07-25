"""Tests for idempotent order creation."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from test_mcp_server import IdempotentOrderStore, Order


class IdempotentOrderStoreTests(unittest.TestCase):
    def test_replays_first_order_for_repeated_key(self) -> None:
        store = IdempotentOrderStore()

        first = store.create(
            idempotency_key="request-1",
            order_id="ord-1",
            customer_id="customer-1",
            amount_cents=2500,
        )
        replay = store.create(
            idempotency_key="request-1",
            order_id="ord-2",
            customer_id="customer-2",
            amount_cents=9000,
        )

        self.assertEqual(first, Order("ord-1", "customer-1", 2500))
        self.assertIs(replay, first)

    def test_rejects_empty_idempotency_key(self) -> None:
        store = IdempotentOrderStore()

        with self.assertRaisesRegex(ValueError, "idempotency_key is required"):
            store.create(
                idempotency_key=" ",
                order_id="ord-1",
                customer_id="customer-1",
                amount_cents=2500,
            )


if __name__ == "__main__":
    unittest.main()

