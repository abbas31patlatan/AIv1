"""Simple asyncio scheduler for periodic tasks."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import Any


class Scheduler:
    """Schedule asynchronous tasks to run periodically."""

    def __init__(self) -> None:
        self._tasks: list[asyncio.Task[Any]] = []

    def schedule(self, interval: int, coro_func: Callable[[], Awaitable[Any]]) -> None:
        async def wrapper() -> None:
            while True:
                await coro_func()
                await asyncio.sleep(interval)

        self._tasks.append(asyncio.create_task(wrapper()))

    async def run_forever(self) -> None:
        await asyncio.gather(*self._tasks)
