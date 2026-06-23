CREATE TABLE dim_customer (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT,
    segment TEXT
);
CREATE TABLE dim_product (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT
);
CREATE TABLE dim_location (
    country TEXT,
    region TEXT,
    state TEXT,
    city TEXT,
    postal_code TEXT,
    PRIMARY KEY (country, region, state, city, postal_code)
);
CREATE TABLE dim_ship_mode (
    ship_mode TEXT PRIMARY KEY
);
CREATE TABLE dim_date (
    date_key TEXT PRIMARY KEY,
    full_date DATE,
    day INT,
    month INT,
    month_name TEXT,
    quarter INT,
    year INT,
    week INT
);

CREATE TABLE etl_control (
    id INT PRIMARY KEY,
    last_loaded_date TEXT
);