import uvicorn

from fastapi import FastAPI
from logger import get_logger
from logger import config
from api import router

logger = get_logger(__name__)

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_config=config)