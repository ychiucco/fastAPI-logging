from time import sleep

from logger import get_logger


logger = get_logger(__name__)

async def sleep_and_log(wait: int):
    logger.info(f"Wait {wait} seconds...\t")
    sleep(wait)
    logger.info("done!")