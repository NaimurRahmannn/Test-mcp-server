"""In-memory idempotency behavior for order commands."""

from dataclasses import dataclass, field

from test_mcp_server.orders import Order, create_order


@dataclass
class IdempotentOrderStore:
    """Return the first order associated with each idempotency key."""

    _orders_by_key: dict[str, Order] = field(default_factory=dict)

    def create(
        self,
        *,
        idempotency_key: str,
        order_id: str,
        customer_id: str,
        amount_cents: int,
    ) -> Order:
        """Create once, then replay the original result for the same key."""

        if not idempotency_key.strip():
            raise ValueError("idempotency_key is required")

        existing = self._orders_by_key.get(idempotency_key)
        if existing is not None:
            return existing

        order = create_order(order_id, customer_id, amount_cents)
        self._orders_by_key[idempotency_key] = order
        return order

