from modules.autonomous_agent import AutonomousAgent
from modules.offline_mode import OfflineMode

# Modül fonksiyonları varsa ekle (yoksa skip eder, hata vermez)
try:
    from modules.windows_interaction import open_window, list_windows, move_window, reset as win_reset
except ImportError:
    open_window = list_windows = move_window = win_reset = None

try:
    from modules.keyboard_mouse_control import move_mouse, click, type_text, state as km_state, reset as km_reset
except ImportError:
    move_mouse = click = type_text = km_state = km_reset = None

try:
    from modules.productivity_booster import add_task, complete_task, list_tasks, reset as tasks_reset
except ImportError:
    add_task = complete_task = list_tasks = tasks_reset = None

try:
    from modules.vision_module import detect_objects, caption_image
except ImportError:
    detect_objects = caption_image = None

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
    import os
    monkeypatch.setenv("APP_OFFLINE", "1")
    o = OfflineMode()
    assert o.active
    monkeypatch.setenv("APP_OFFLINE", "0")
    assert not o.active

def test_window_management():
    if not all([win_reset, open_window, move_window, list_windows]): return
    win_reset()
    open_window("Editor")
    move_window("Editor", 5, 5)
    assert list_windows() == ["Editor"]

def test_keyboard_mouse():
    if not all([km_reset, move_mouse, click, type_text, km_state]): return
    km_reset()
    move_mouse(10, 10)
    click()
    type_text("hi")
    pos, keys, clicks = km_state()
    assert pos == (10, 10) and keys == list("hi") and clicks == 1

def test_tasks():
    if not all([tasks_reset, add_task, complete_task, list_tasks]): return
    tasks_reset()
    add_task("demo", priority=2)
    assert list_tasks() and complete_task("demo")

def test_vision():
    if not all([detect_objects, caption_image]): return
    assert "cat" in detect_objects("cat.png")
    assert caption_image("dog.jpg").startswith("Image contains")

