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
            return "done"

        s.schedule(1, noop, name="test_job")
        await asyncio.sleep(0.1)
        # tasks() ile kontrol et, yoksa _tasks ile
        task_names = s.tasks() if hasattr(s, "tasks") else list(s._tasks)
        assert "test_job" in task_names
        s.cancel("test_job")
        task_names = s.tasks() if hasattr(s, "tasks") else list(s._tasks)
        assert "test_job" not in task_names

    asyncio.run(runner())

def test_scheduler_manual_trigger():
    async def runner():
        results = []
        s = Scheduler()

        async def inc():
            results.append(1)

        s.schedule(1, inc, name="trig")
        s.trigger("trig")
        await asyncio.sleep(0.2)
        assert results, "Manual trigger should append at least once"

        s.cancel_all()
    asyncio.run(runner())
