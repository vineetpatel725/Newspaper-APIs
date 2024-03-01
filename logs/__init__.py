import os
import logging
from logging.handlers import RotatingFileHandler

file_name = "logs/newspaper_backend.log"
maximum_size = 100
logging_handler = RotatingFileHandler(file_name, maxBytes=maximum_size * 1024 * 1024)
logging_handler.setLevel(logging.INFO)

logging_formatter = logging.Formatter("%(process)d - %(levelname)s - %(asctime)s - %(message)s")

logging_handler.setFormatter(logging_formatter)
logging_handler.setFormatter(logging_formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging_handler],
    datefmt='%d-%b-%y %H:%M:%S'
)

logger = logging.getLogger()
