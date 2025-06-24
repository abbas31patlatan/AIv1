"""Dev tool for structured logging."""
from __future__ import annotations

from utils.logger import get_logger


logger = get_logger("devtools")


def log_debug(message: str) -> None:
    logger.debug(message)
