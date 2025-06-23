"""Tiny asyncio scheduler for periodic tasks.

The :class:`Scheduler` class is intentionally lightweight but supports starting
and cancelling named periodic jobs.  It utilises :mod:`asyncio` so that tasks
can run concurrently with the rest of the application.
"""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import Any


class Scheduler:
    """Schedule asynchronous tasks to run periodically."""

    def __init__(self) -> None:
        self._tasks: dict[str, asyncio.Task[Any]] = {}

    def schedule(
        self,
        interval: int,
        coro_func: Callable[[], Awaitable[Any]],
        *,
        name: str | None = None,
    ) -> asyncio.Task[Any]:
        """Schedule *coro_func* every *interval* seconds."""

        async def wrapper() -> None:
            while True:
                await coro_func()
                await asyncio.sleep(interval)

        task = asyncio.create_task(wrapper())
        self._tasks[name or f"task-{len(self._tasks)}"] = task
        return task

    def cancel(self, name: str) -> None:
        """Cancel a previously scheduled task."""
        task = self._tasks.pop(name, None)
        if task:
            task.cancel()

    def tasks(self) -> list[str]:
        """Return a list of scheduled task names."""
        return list(self._tasks)

    async def run_forever(self) -> None:
        if not self._tasks:
            return
        try:
            await asyncio.gather(*self._tasks.values())
        except asyncio.CancelledError:
            pass
