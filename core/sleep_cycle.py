"""Manage sleep and wake cycles."""
from __future__ import annotations

import asyncio


class SleepCycle:
    """Provide async sleep functionality."""

    async def nap(self, seconds: int) -> None:
        await asyncio.sleep(seconds)
