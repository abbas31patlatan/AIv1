from modules.autonomous_agent import AutonomousAgent
from modules.offline_mode import OfflineMode
from modules.windows_interaction import open_window, list_windows, move_window, reset as win_reset
from modules.keyboard_mouse_control import move_mouse, click, type_text, state as km_state, reset as km_reset
from modules.productivity_booster import add_task, complete_task, list_tasks, reset as tasks_reset
from modules.vision_module import detect_objects, caption_image


def test_autonomous_agent():
    agent = AutonomousAgent()
    assert agent.act('I am happy') == 'encourage'


def test_offline_toggle():
    o = OfflineMode()
    o.force(True)
    assert o.active
    o.force(False)
    assert isinstance(o.active, bool)


def test_offline_env(monkeypatch):
    monkeypatch.setenv("APP_OFFLINE", "1")
    o = OfflineMode()
    assert o.active
    monkeypatch.setenv("APP_OFFLINE", "0")
    assert not o.active


def test_window_management():
    win_reset()
    open_window("Editor")
    move_window("Editor", 5, 5)
    assert list_windows() == ["Editor"]


def test_keyboard_mouse():
    km_reset()
    move_mouse(10, 10)
    click()
    type_text("hi")
    pos, keys, clicks = km_state()
    assert pos == (10, 10) and keys == list("hi") and clicks == 1


def test_tasks():
    tasks_reset()
    add_task("demo", priority=2)
    assert list_tasks() and complete_task("demo")


def test_vision():
    assert "cat" in detect_objects("cat.png")
    assert caption_image("dog.jpg").startswith("Image contains")

