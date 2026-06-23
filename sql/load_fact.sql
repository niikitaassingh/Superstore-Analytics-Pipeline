CREATE TABLE fact_sales (
    sales_key TEXT PRIMARY KEY,
    order_id TEXT,
    customer_id TEXT,
    product_id TEXT,

    country TEXT,
    region TEXT,
    state TEXT,
    city TEXT,
    postal_code TEXT,

    ship_mode TEXT,
    order_date_key TEXT,
    ship_date_key TEXT,

    sales NUMERIC,
    quantity INT,
    discount NUMERIC,
    profit NUMERIC
);