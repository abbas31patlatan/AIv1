"""Gelişmiş asyncio tabanlı görev zamanlayıcı (Scheduler)."""

from __future__ import annotations
import asyncio
import time
from collections.abc import Awaitable, Callable
from typing import Any, Optional

class ScheduledTask:
    def __init__(self, name: str, interval: int, coro_func: Callable[[], Awaitable[Any]]):
        self.name = name
        self.interval = interval
        self.coro_func = coro_func
        self._task: Optional[asyncio.Task] = None
        self.last_run: float = 0.0
        self.cancelled: bool = False
        self.last_exception: Optional[Exception] = None

    async def _run(self):
        while not self.cancelled:
            try:
                await self.coro_func()
                self.last_run = time.time()
            except Exception as e:
                self.last_exception = e
            await asyncio.sleep(self.interval)

    def start(self):
        self._task = asyncio.create_task(self._run())

    def cancel(self):
        self.cancelled = True
        if self._task:
            self._task.cancel()

class Scheduler:
    """Asenkron görev zamanlayıcı: periyodik ve yönetilebilir."""

    def __init__(self):
        self._tasks: dict[str, ScheduledTask] = {}
        self._is_running = True

    def schedule(
        self,
        interval: int,
        coro_func: Callable[[], Awaitable[Any]],
        *,
        name: str | None = None,
    ) -> ScheduledTask:
        """Her interval saniyede bir *coro_func*’u çalıştır."""
        name = name or f"task-{len(self._tasks)}"
        task = ScheduledTask(name, interval, coro_func)
        self._tasks[name] = task
        task.start()
        return task

    def cancel(self, name: str):
        """Belirli bir görevi iptal et."""
        if name in self._tasks:
            self._tasks[name].cancel()
            del self._tasks[name]

    def cancel_all(self):
        """Tüm görevleri iptal et."""
        for name in list(self._tasks):
            self.cancel(name)

    def tasks(self) -> list[str]:
        """Planlanmış tüm görev isimleri."""
        return list(self._tasks)

    def task_status(self, name: str) -> Optional[dict]:
        """Belirli bir görevin son çalıştırma zamanı ve hatası."""
        t = self._tasks.get(name)
        if not t: return None
        return {
            "last_run": t.last_run,
            "cancelled": t.cancelled,
            "exception": t.last_exception,
            "interval": t.interval,
        }

    def trigger(self, name: str):
        """Bir görevi manuel (hemen) tetikle."""
        t = self._tasks.get(name)
        if t:
            asyncio.create_task(t.coro_func())

    def stop(self):
        """Scheduler’ı tamamen durdur."""
        self._is_running = False
        self.cancel_all()

    async def run_forever(self):
        """Görevler arasında asenkron bekleme. (Hızlı test için override edilebilir)"""
        while self._is_running and self._tasks:
            await asyncio.sleep(1)

# Kısa test
if __name__ == "__main__":
    async def hello():
        print("Hello", time.time())
    sch = Scheduler()
    sch.schedule(2, hello, name="hello")
    try:
        asyncio.run(sch.run_forever())
    except KeyboardInterrupt:
        sch.stop()
        print("Scheduler stopped.")
