import json
from logging import getLogger
from logging.config import dictConfig
from pathlib import Path


logger = getLogger(__name__)

config_file = Path("src/loggerConfig.json")
with open(config_file) as f:
    config = json.load(f)
dictConfig(config)

def get_logger(logger_name: str):
    logger.debug(f"Returning logger with name '{logger_name}'")
    return getLogger(logger_name)