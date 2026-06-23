# SuperStore ETL Project

## Overview
This repository contains a Python-based ETL pipeline for processing SuperStore sales data. The pipeline:
- extracts and cleans raw CSV data
- transforms it into dimension and fact tables
- loads the transformed data into PostgreSQL staging tables
- merges the staging data into warehouse tables
- performs basic data quality checks

## Project Structure

- `data/raw/`
  - `Sample - Superstore.csv` — raw source dataset
- `data/processed/`
  - generated CSV files: `dim_customer.csv`, `dim_product.csv`, `dim_location.csv`, `dim_ship_mode.csv`, `dim_date.csv`, `fact_sales.csv`
- `etl/`
  - `01_extract_transform.py` — extract raw CSV and build dimension/fact CSV outputs
  - `02_load_staging.py` — load processed CSV files into PostgreSQL staging tables
  - `03_merge_warehouse.py` — merge staging tables into warehouse tables with conflict handling
  - `04_data_quality.py` — run simple count checks on warehouse tables
  - `logging_config.py` — logging helper for ETL scripts
  - `run_pipeline.py` — execute the full ETL pipeline sequentially
- `sql/`
  - `create_staging_tables.sql` — DDL for staging tables
  - `create_tables.sql` — DDL for warehouse tables
  - `load_fact.sql` — additional load SQL resources
- `insights/`
  - `business_insights.md` — analysis and project insights
- `images/`
  - supporting visuals for the project

## Requirements

- Python 3.x
- PostgreSQL
- Python packages:
  - `pandas`
  - `sqlalchemy`
  - `psycopg2`

> Note: There is no `requirements.txt` included in the repository. Install packages manually or generate one from your environment.

## Setup

1. Create a PostgreSQL database called `superstore`.
2. Update the connection details in ETL scripts if your PostgreSQL credentials or host differ.
   - default connection string: `postgresql://postgres:password@localhost:5432/superstore`
3. Create staging and warehouse tables:
   - `sql/create_staging_tables.sql`
   - `sql/create_tables.sql`

## Usage

### Run the full ETL pipeline

From the project root:

```powershell
python etl\run_pipeline.py
```

### Run individual ETL steps

```powershell
python etl\01_extract_transform.py
python etl\02_load_staging.py
python etl\03_merge_warehouse.py
python etl\04_data_quality.py
```

## Data Flow

1. `01_extract_transform.py`
   - reads raw SuperStore CSV
   - cleans and normalizes column names and text fields
   - fills missing postal codes with `UNKNOWN`
   - generates dimension tables: `dim_customer`, `dim_product`, `dim_location`, `dim_ship_mode`, `dim_date`
   - generates fact table: `fact_sales`
   - writes processed CSV files to `data/processed/`
2. `02_load_staging.py`
   - reads processed CSV files
   - truncates PostgreSQL staging tables
   - loads data into staging tables using SQLAlchemy
3. `03_merge_warehouse.py`
   - inserts or updates warehouse tables from staging tables
   - uses `ON CONFLICT` logic for idempotent merges
4. `04_data_quality.py`
   - validates table row counts for basic quality assurance

## Notes

- The ETL scripts currently depend on hard-coded file paths for input and output locations.
- The PostgreSQL connection string is also hard-coded in `etl/02_load_staging.py`, `etl/03_merge_warehouse.py`, and `etl/04_data_quality.py`.
- If you deploy this pipeline to another environment, update the connection string and paths accordingly.

## Recommended Improvements

- add a `requirements.txt` or `pyproject.toml`
- parameterize database credentials and file paths
- add more data quality checks and logging for failures
- add documentation for expected source schema and output metrics
