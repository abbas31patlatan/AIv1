"""Central logging utilities.

This module exposes :func:`get_logger` which configures Python's built-in
``logging`` module for use across the project. Logs are written to both the
console and an optional file if provided.
"""
from __future__ import annotations

import logging
from logging import Logger
from typing import Optional


def get_logger(name: str = "AIv1", log_file: Optional[str] = None) -> Logger:
    """Return a configured :class:`logging.Logger` instance."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    stream = logging.StreamHandler()
    stream.setFormatter(formatter)
    logger.addHandler(stream)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
