"""High level task scheduler built atop :mod:`scheduler`."""
from __future__ import annotations

from scheduler import Scheduler
from typing import Awaitable, Callable, Any


class ActionScheduler(Scheduler):
    """Convenience wrapper for scheduling named actions."""

    def schedule_action(
        self, name: str, interval: int, coro_func: Callable[[], Awaitable[Any]]
    ) -> None:
        super().schedule(interval, coro_func, name=name)

    def cancel_action(self, name: str) -> None:
        """Cancel a scheduled action."""
        self.cancel(name)
