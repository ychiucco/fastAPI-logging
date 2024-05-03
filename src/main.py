import uvicorn

from fastapi import BackgroundTasks
from fastapi import FastAPI
from time import sleep


app = FastAPI()


def sleep_and_log(wait: int):
    print(f"Wait {wait} seconds...\t", end="")
    sleep(wait)
    print("done!")


@app.post("/wait/{wait}/")
async def send_notification(wait: int, background_tasks: BackgroundTasks):
    print(f"Let's add a Task[{wait}]")
    background_tasks.add_task(sleep_and_log, wait)
    print(f"Task[{wait}] added")
    return {"message": f"Task[{wait}]"}



if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )