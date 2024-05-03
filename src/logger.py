import logging
import sys

logger = logging.getLogger()

formatter = logging.Formatter(
    fmt=(
        "%(asctime)s\t"
        "%(levelname)s\t"
        "%(filename)s::%(funcName)s::%(lineno)d\t"
        "%(message)s"
    )
)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]

logger.setLevel(logging.DEBUG)