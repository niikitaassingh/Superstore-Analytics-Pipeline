import pandas as pd
from pathlib import Path
from logging_config import log_message

# ==================================================
# STEP 1: READ DATA
# ==================================================

df = pd.read_csv(
    r"C:\Users\anike\OneDrive\Documents\SuperStore\data\raw\Sample - Superstore.csv",
    encoding="latin1"
)

project_root = Path(__file__).resolve().parent.parent
processed_folder = project_root / "data" / "processed"
processed_folder.mkdir(parents=True, exist_ok=True)

# ==================================================
# STEP 2: CLEAN COLUMNS
# ==================================================

df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# ==================================================
# STEP 3: CLEAN DATA
# ==================================================

df.drop_duplicates(inplace=True)

df["postal_code"] = df["postal_code"].fillna("UNKNOWN")

df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

log_message("Data Cleaning Completed")

# ==================================================
# STEP 4: DIM CUSTOMER
# ==================================================

dim_customer = df[["customer_id", "customer_name", "segment"]].drop_duplicates()

dim_customer.insert(0, "customer_key", range(1, len(dim_customer) + 1))

# ==================================================
# STEP 5: DIM PRODUCT
# ==================================================

dim_product = df[["product_id", "product_name", "category"]].drop_duplicates()
dim_product.insert(0, "product_key", range(1, len(dim_product) + 1))

# ==================================================
# STEP 6: DIM LOCATION
# ==================================================

dim_location = df[["country", "region", "state", "city", "postal_code"]].drop_duplicates()
dim_location.insert(0, "location_key", range(1, len(dim_location) + 1))

# ==================================================
# STEP 7: DIM SHIP MODE
# ==================================================

dim_ship_mode = df[["ship_mode"]].drop_duplicates()
dim_ship_mode.insert(0, "ship_mode_key", range(1, len(dim_ship_mode) + 1))

# ==================================================
# STEP 8: DIM DATE
# ==================================================

date_range = pd.date_range(df["order_date"].min(), df["ship_date"].max())

dim_date = pd.DataFrame({"full_date": date_range})

dim_date["date_key"] = dim_date["full_date"].dt.strftime("%Y%m%d").astype(int)
dim_date["day"] = dim_date["full_date"].dt.day
dim_date["month"] = dim_date["full_date"].dt.month
dim_date["month_name"] = dim_date["full_date"].dt.month_name()
dim_date["quarter"] = dim_date["full_date"].dt.quarter
dim_date["year"] = dim_date["full_date"].dt.year
dim_date["week"] = dim_date["full_date"].dt.isocalendar().week

# ==================================================
# STEP 9: FACT TABLE
# ==================================================

fact = df.copy()

fact["order_date_key"] = fact["order_date"].dt.strftime("%Y%m%d").astype(int)
fact["ship_date_key"] = fact["ship_date"].dt.strftime("%Y%m%d").astype(int)

fact_sales = fact[[
    "order_id",
    "customer_id",
    "product_id",
    "country",
    "region",
    "state",
    "city",
    "postal_code",
    "ship_mode",
    "order_date_key",
    "ship_date_key",
    "sales",
    "quantity",
    "discount",
    "profit"
]]

# fact_sales.insert(0, "sales_key", range(1, len(fact_sales) + 1))
fact_sales.insert(
    0,
    "sales_key",
    fact["order_id"].astype(str)
    + "_"
    + fact["product_id"].astype(str)
)
log_message(f"Fact rows: {len(fact_sales)}")

# ==================================================
# STEP 10: EXPORT
# ==================================================

dim_customer.to_csv(processed_folder / "dim_customer.csv", index=False)
dim_product.to_csv(processed_folder / "dim_product.csv", index=False)
dim_location.to_csv(processed_folder / "dim_location.csv", index=False)
dim_ship_mode.to_csv(processed_folder / "dim_ship_mode.csv", index=False)
dim_date.to_csv(processed_folder / "dim_date.csv", index=False)
fact_sales.to_csv(processed_folder / "fact_sales.csv", index=False)
log_message("ETL pipeline completed")
