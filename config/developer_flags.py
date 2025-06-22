"""Developer flags affecting runtime behaviour."""
from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass
class DeveloperFlags:
    """Toggle experimental or debug features."""

    debug: bool = bool(int(os.getenv("AIV1_DEBUG", "0")))
    verbose: bool = bool(int(os.getenv("AIV1_VERBOSE", "0")))
    safe_mode: bool = bool(int(os.getenv("AIV1_SAFE_MODE", "1")))


flags = DeveloperFlags()
"""Active developer flags."""
