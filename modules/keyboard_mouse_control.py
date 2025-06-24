"""Ultra gelişmiş cross platform keyboard and mouse automation module.

- Gerçek mouse/klavye kontrolü (pyautogui ile, otomatik fallback)
- Tuş/mouse makro kaydı & oynatma
- Tuş kombinasyonları, kısa yol, mouse wheel, clipboard desteği
- State & log fonksiyonları, test-friendly
- Delay, hızlı otomasyon, otomatik tuşla
- Ekran görüntüsü alma, ekran koordinatına göre tıklama vs.

Not: Gerçek otomasyon için pyautogui kurulu olmalı.
"""

from __future__ import annotations
from typing import List, Tuple, Optional, Callable, Dict
import time

try:
    import pyautogui
except ImportError:
    pyautogui = None

try:
    import pyperclip
except ImportError:
    pyperclip = None

_MOUSE_POS: Tuple[int, int] = (0, 0)
_TYPED_KEYS: List[str] = []
_CLICK_COUNT: int = 0
_LOGS: List[str] = []
_MACRO: List[Tuple[float, str, tuple, dict]] = []

def move_mouse(x: int, y: int, real: bool = False, duration: float = 0) -> Tuple[int, int]:
    """Move the mouse to (x, y). real=True ile pyautogui ile hareket ettir."""
    global _MOUSE_POS
    _MOUSE_POS = (x, y)
    _LOGS.append(f"mouse_move:{x},{y}")
    if real and pyautogui:
        pyautogui.moveTo(x, y, duration=duration)
    return _MOUSE_POS

def click(x: Optional[int] = None, y: Optional[int] = None, button: str = "left", real: bool = False, clicks: int = 1, interval: float = 0.0) -> int:
    """Mouse click at (x, y) or current pos. real=True ile gerçek tıklama."""
    global _CLICK_COUNT, _MOUSE_POS
    if x is not None and y is not None:
        _MOUSE_POS = (x, y)
    _CLICK_COUNT += clicks
    _LOGS.append(f"click:{_MOUSE_POS}, btn={button}")
    if real and pyautogui:
        pyautogui.click(x=_MOUSE_POS[0], y=_MOUSE_POS[1], clicks=clicks, interval=interval, button=button)
    return _CLICK_COUNT

def key_press(key: str, real: bool = False) -> str:
    """Basit tuş basımı, pyautogui ile gerçek tuş basabilir."""
    _TYPED_KEYS.append(key)
    _LOGS.append(f"key:{key}")
    if real and pyautogui:
        pyautogui.press(key)
    return key

def type_text(text: str, real: bool = False, interval: float = 0.0) -> int:
    """Text'i harf harf yazar (gerçek veya simüle)."""
    for char in text:
        key_press(char, real=real)
        if real and interval > 0:
            time.sleep(interval)
    if real and pyautogui:
        pyautogui.typewrite(text, interval=interval)
    return len(text)

def hotkey(*keys: str, real: bool = False):
    """Kombinasyonlu tuş (örn: Ctrl+S)."""
    _LOGS.append(f"hotkey:{'+'.join(keys)}")
    if real and pyautogui:
        pyautogui.hotkey(*keys)

def mouse_wheel(amount: int = 1, real: bool = False):
    """Mouse wheel up/down."""
    _LOGS.append(f"mouse_wheel:{amount}")
    if real and pyautogui:
        pyautogui.scroll(amount)

def get_clipboard() -> str:
    if pyperclip:
        return pyperclip.paste()
    return ""

def set_clipboard(text: str):
    if pyperclip:
        pyperclip.copy(text)

def screenshot(filename: str = "ss.png"):
    if pyautogui:
        pyautogui.screenshot(filename)
        _LOGS.append(f"screenshot:{filename}")

def record_macro(action: str, *args, **kwargs):
    _MACRO.append((time.time(), action, args, kwargs))
    _LOGS.append(f"macro_record:{action}")

def play_macro(real: bool = False):
    """Tüm kaydedilmiş macro'yu sırayla oynat."""
    start_time = _MACRO[0][0] if _MACRO else 0
    for t, action, args, kwargs in _MACRO:
        delay = t - start_time
        time.sleep(delay)
        if action == "click":
            click(*args, **kwargs, real=real)
        elif action == "move_mouse":
            move_mouse(*args, **kwargs, real=real)
        elif action == "key_press":
            key_press(*args, **kwargs, real=real)
        elif action == "type_text":
            type_text(*args, **kwargs, real=real)

def state() -> dict:
    """Tüm iç state ve loglar."""
    return {
        "mouse_pos": _MOUSE_POS,
        "typed_keys": list(_TYPED_KEYS),
        "click_count": _CLICK_COUNT,
        "logs": list(_LOGS),
        "macro": list(_MACRO),
    }

def reset() -> None:
    """Reset all states."""
    global _MOUSE_POS, _TYPED_KEYS, _CLICK_COUNT, _LOGS, _MACRO
    _MOUSE_POS = (0, 0)
    _TYPED_KEYS = []
    _CLICK_COUNT = 0
    _LOGS = []
    _MACRO = []

# Test ve örnek kullanım
if __name__ == "__main__":
    move_mouse(200, 150)
    click()
    type_text("hello world")
    key_press("enter")
    mouse_wheel(-5)
    set_clipboard("test")
    print("Clipboard:", get_clipboard())
    screenshot("test.png")
    print("STATE:", state())
