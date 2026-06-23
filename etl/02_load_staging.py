import pandas as pd
from sqlalchemy import create_engine, text
from logging_config import log_message
import psycopg2
engine = create_engine(
    "postgresql://postgres:password@localhost:5432/superstore"
)

base_path = r"C:\Users\anike\OneDrive\Documents\SuperStore\data\processed"

files = {
    "stg_customer": "dim_customer.csv",
    "stg_product": "dim_product.csv",
    "stg_location": "dim_location.csv",
    "stg_ship_mode": "dim_ship_mode.csv",
    "stg_date": "dim_date.csv",
    "stg_sales": "fact_sales.csv"
}

for table, file in files.items():

    df = pd.read_csv(f"{base_path}\\{file}")

    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {table}"))

        try:
            df.to_sql(
                table,
                conn,
                if_exists="append",
                index=False,
                method="multi"
            )
        except Exception as e:
            print(f"\nERROR LOADING TABLE: {table}")
            print(f"CSV Columns: {list(df.columns)}")
            print(str(e))
            raise
        log_message(f"{table} loaded")

