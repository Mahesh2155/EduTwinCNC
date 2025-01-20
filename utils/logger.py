# logger.py
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
