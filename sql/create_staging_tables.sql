CREATE TABLE IF NOT EXISTS stg_customer (
    customer_id TEXT,
    customer_name TEXT,
    segment TEXT
);

CREATE TABLE IF NOT EXISTS stg_product (
    product_id TEXT,
    product_name TEXT,
    category TEXT
);

CREATE TABLE IF NOT EXISTS stg_location (
    country TEXT,
    region TEXT,
    state TEXT,
    city TEXT,
    postal_code TEXT
);

CREATE TABLE IF NOT EXISTS stg_ship_mode (
    ship_mode TEXT
);

CREATE TABLE IF NOT EXISTS stg_date (
    date_key TEXT,
    full_date DATE,
    day INT,
    month INT,
    month_name TEXT,
    quarter INT,
    year INT,
    week INT
);

CREATE TABLE IF NOT EXISTS stg_sales (
    sales_key TEXT,
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