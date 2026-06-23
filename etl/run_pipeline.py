import subprocess
from logging_config import log_message
import psycopg2
log_message("Pipeline Started")
import sys

subprocess.run(
    [sys.executable, "01_extract_transform.py"],
    check=True
)

subprocess.run(
    [sys.executable, "02_load_staging.py"],
    check=True
)

subprocess.run(
    [sys.executable, "03_merge_warehouse.py"],
    check=True
)

subprocess.run(
    [sys.executable, "04_data_quality.py"],
    check=True
)

log_message("Pipeline Completed")