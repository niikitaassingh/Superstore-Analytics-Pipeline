from sqlalchemy import create_engine, text
from logging_config import log_message

engine = create_engine(
    "postgresql://postgres:password@localhost:5432/superstore"
)

def run(sql):
    with engine.begin() as conn:
        conn.execute(text(sql))


# -----------------------
# CUSTOMER DIMENSION
# -----------------------
run("""
INSERT INTO dim_customer
(
    customer_key,
    customer_id,
    customer_name,
    segment
)
SELECT
    customer_key,
    customer_id,
    customer_name,
    segment
FROM stg_customer
ON CONFLICT (customer_id)
DO UPDATE SET
    customer_key = EXCLUDED.customer_key,
    customer_name = EXCLUDED.customer_name,
    segment = EXCLUDED.segment;
""")


# -----------------------
# PRODUCT DIMENSION
# -----------------------
run("""
INSERT INTO dim_product
SELECT *
FROM stg_product
ON CONFLICT (product_id)
DO UPDATE SET
    product_name = EXCLUDED.product_name,
    category = EXCLUDED.category;
""")


# -----------------------
# LOCATION DIMENSION
# -----------------------
run("""
INSERT INTO dim_location
SELECT *
FROM stg_location
ON CONFLICT (country, region, state, city, postal_code)
DO NOTHING;
""")


# -----------------------
# SHIP MODE DIMENSION
# -----------------------
run("""
INSERT INTO dim_ship_mode
SELECT *
FROM stg_ship_mode
ON CONFLICT (ship_mode)
DO NOTHING;
""")


# -----------------------
# DATE DIMENSION
# -----------------------
run("""
INSERT INTO dim_date
SELECT *
FROM stg_date
ON CONFLICT (date_key)
DO UPDATE SET
    full_date = EXCLUDED.full_date,
    day = EXCLUDED.day,
    month = EXCLUDED.month,
    month_name = EXCLUDED.month_name,
    quarter = EXCLUDED.quarter,
    year = EXCLUDED.year,
    week = EXCLUDED.week;
""")


# -----------------------
# FACT SALES
# -----------------------
run("""
INSERT INTO fact_sales
SELECT *
FROM stg_sales
ON CONFLICT (sales_key)
DO UPDATE SET
    order_id = EXCLUDED.order_id,
    customer_id = EXCLUDED.customer_id,
    product_id = EXCLUDED.product_id,
    country = EXCLUDED.country,
    region = EXCLUDED.region,
    state = EXCLUDED.state,
    city = EXCLUDED.city,
    postal_code = EXCLUDED.postal_code,
    ship_mode = EXCLUDED.ship_mode,
    order_date_key = EXCLUDED.order_date_key,
    ship_date_key = EXCLUDED.ship_date_key,
    sales = EXCLUDED.sales,
    quantity = EXCLUDED.quantity,
    discount = EXCLUDED.discount,
    profit = EXCLUDED.profit;
""")

log_message("Warehouse merge completed")
print("Warehouse merge completed")