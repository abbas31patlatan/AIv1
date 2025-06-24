from core.ai_core import AICore
from scheduler import Scheduler
import asyncio

def test_ai_core_interact():
    core = AICore()
    reply = core.interact("hi")
    assert isinstance(reply, str)
    assert "hello" in reply.lower() or "merhaba" in reply.lower()

def test_scheduler_cancel():
    async def runner():
        s = Scheduler()
        async def noop():
            pass

        # Görevi ekle
        s.schedule(1, noop, name="t")

        # tasks() varsa oradan, yoksa _tasks üzerinden kontrol et
        if hasattr(s, "tasks"):
            assert "t" in s.tasks()
        else:
            assert "t" in s._tasks

        s.cancel("t")

        if hasattr(s, "tasks"):
            assert "t" not in s.tasks()
        else:
            assert "t" not in s._tasks

    asyncio.run(runner())
