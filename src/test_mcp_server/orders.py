"""Order creation domain logic."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    """An accepted customer order."""

    order_id: str
    customer_id: str
    amount_cents: int


def create_order(order_id: str, customer_id: str, amount_cents: int) -> Order:
    """Validate and create an order."""

    if not order_id.strip():
        raise ValueError("order_id is required")
    if not customer_id.strip():
        raise ValueError("customer_id is required")
    if amount_cents <= 0:
        raise ValueError("amount_cents must be positive")

    return Order(
        order_id=order_id,
        customer_id=customer_id,
        amount_cents=amount_cents,
    )


def order_total(order: Order) -> int:
    """Return the order total in minor currency units."""

    return order.amount_cents

