import uvicorn

from fastapi import BackgroundTasks
from fastapi import FastAPI
from time import sleep

from logger import logger

logger.info("Creating app...")
app = FastAPI()
logger.info("App created!")


def sleep_and_log(wait: int):
    print(f"Wait {wait} seconds...\t", end="")
    sleep(wait)
    print("done!")


@app.post("/wait/{wait}/")
async def wait(wait: int, background_tasks: BackgroundTasks):
    logger.info(f"Let's add Task[{wait}]")
    background_tasks.add_task(sleep_and_log, wait)
    logger.info(f"Task[{wait}] added")
    return {"message": f"Task[{wait}]"}



if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )