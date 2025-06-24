"""Application settings and configuration options.

This module defines the :class:`Settings` dataclass which stores runtime
configuration for the AI system. Settings can be loaded from environment
variables or defaults may be used. Only a very small subset of options are
implemented as an example.

Example
-------
>>> from config.settings import Settings
>>> settings = Settings()
>>> settings.backup_interval
60
"""
from dataclasses import dataclass
import os


@dataclass
class Settings:
    """Container for user configurable settings."""

    data_path: str = os.getenv("AIV1_DATA", "./data")
    backup_interval: int = int(os.getenv("AIV1_BACKUP_INTERVAL", "60"))
    language: str = os.getenv("AIV1_LANG", "en")


settings = Settings()
"""Default application settings used throughout the system."""
