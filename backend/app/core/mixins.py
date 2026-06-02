from typing import Any

from app.core.logger import log


class LogMixin:
    def log(self, msg: Any, force: bool = False) -> None:
        log(f"{self.__class__.__name__} {msg}", force=force)
