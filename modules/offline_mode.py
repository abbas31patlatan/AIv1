"""Determine whether the application should operate in offline mode."""
from __future__ import annotations

from utils.internet_checker import connected


class OfflineMode:
    """Simple helper that exposes the current offline status."""

    def __init__(self) -> None:
        self._forced = False

    @property
    def active(self) -> bool:
        """Return ``True`` when the system is offline."""
        return self._forced or not connected()

    def force(self, value: bool) -> None:
        """Manually toggle offline mode."""
        self._forced = value


_INSTANCE = OfflineMode()


def available() -> bool:
    """Backward compatible check for offline availability."""
    return _INSTANCE.active
