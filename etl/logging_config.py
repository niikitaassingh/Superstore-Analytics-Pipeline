import logging
from pathlib import Path

log_folder = Path("logs")
log_folder.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_folder / "etl_pipeline.log",
    filemode="a",
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)

def log_message(message):
    logging.info(message)
    print(message)