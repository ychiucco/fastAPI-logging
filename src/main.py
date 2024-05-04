import uvicorn
import logging
import json

from fastapi import BackgroundTasks
from fastapi import FastAPI
from pathlib import Path
from time import sleep
from logging import getLogger


def setup_logging(path: Path):
    with open(path) as f:
        config = json.load(f)
    logging.config.dictConfig(config)


app = FastAPI()

logger = getLogger(__name__)
config_file = Path("src/loggerConfig.json")
setup_logging(config_file)

async def sleep_and_log(wait: int):
    logger.info(f"Wait {wait} seconds...\t")
    sleep(wait)
    logger.info("done!")


@app.post("/wait/{wait}/")
async def wait(wait: int, background_tasks: BackgroundTasks):
    
    logger.debug(f"Debug from Task[{wait}]")
    logger.info(f"Info from Task[{wait}]")
    logger.warning(f"Warning from Task[{wait}]")
    logger.error(f"Error from Task[{wait}]")
    logger.critical(f"Critical from Task[{wait}]")

    background_tasks.add_task(sleep_and_log, wait)

    logger.info(f"Task[{wait}] added")

    return {"message": f"Task[{wait}]"}



if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )