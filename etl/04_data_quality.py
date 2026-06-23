from sqlalchemy import create_engine, text
from logging_config import log_message

engine = create_engine(
    "postgresql://postgres:password@localhost:5432/superstore"
)

checks = {
    "dim_customer":
        "SELECT COUNT(*) FROM dim_customer",

    "dim_product":
        "SELECT COUNT(*) FROM dim_product",

    "fact_sales":
        "SELECT COUNT(*) FROM fact_sales"
}

with engine.begin() as conn:

    for table, sql in checks.items():

        count = conn.execute(text(sql)).scalar()

        log_message(f"{table}: {count}")