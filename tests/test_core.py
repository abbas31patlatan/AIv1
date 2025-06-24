from core.ai_core import AICore
from scheduler import Scheduler
import asyncio


def test_ai_core_interact():
    core = AICore()
    assert "Hello" in core.interact("hi")


def test_scheduler_cancel():
    async def runner():
        s = Scheduler()

        async def noop():
            pass

        s.schedule(1, noop, name="t")
        assert "t" in s.tasks()
        s.cancel("t")
        assert "t" not in s.tasks()

    asyncio.run(runner())

