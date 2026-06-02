import logging
from sys import stdout
from time import gmtime

from app.core.config import settings


def get_logger() -> logging.Logger:
    logger = logging.getLogger("app")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    formatter.converter = gmtime

    handler = logging.StreamHandler(stdout)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    logger.addHandler(handler)

    return logger


def log(msg: str, force: bool = False) -> None:
    if settings.FULL_LOGS or force:
        get_logger().info(msg)
