from core.ai_core import AICore


def test_ai_core_interact():
    core = AICore()
    assert "Hello" in core.interact("hi")

