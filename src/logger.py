import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
    
LOG_FILE = os.path.join(LOGS_DIR,f"log_{datetime.now().strftime("%Y_%m_%d")}.log")

logging.basicConfig(
    filename = LOG_FILE,
    level = logging.INFO,
    format = '[%(asctime)s]%(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
    