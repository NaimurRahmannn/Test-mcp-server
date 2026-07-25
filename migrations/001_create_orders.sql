CREATE TABLE orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    amount_cents INTEGER NOT NULL CHECK (amount_cents > 0)
);

