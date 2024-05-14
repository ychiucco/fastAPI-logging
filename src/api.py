from fastapi import BackgroundTasks
from fastapi import APIRouter

from logger import get_logger
from task import sleep_and_log


logger = get_logger(__name__)

router = APIRouter()

@router.post("/wait/{wait}/")
async def wait(wait: int, background_tasks: BackgroundTasks):
    
    logger.debug(f"Debug from Task[{wait}]")
    background_tasks.add_task(sleep_and_log, wait)
    return {"message": f"Task[{wait}]"}