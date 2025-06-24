"""Simple cross platform keyboard and mouse automation stubs.

These helpers mimic high level user interaction with the desktop.  They record
state internally for testability but can be swapped out for `pyautogui` or other
platform libraries when real automation is required.

Example
-------
>>> move_mouse(10, 20)
(10, 20)
>>> click()
1
>>> type_text('hello')
5
"""
from __future__ import annotations

from typing import List, Tuple

_MOUSE_POS: Tuple[int, int] = (0, 0)
_TYPED_KEYS: List[str] = []
_CLICK_COUNT: int = 0


def move_mouse(x: int, y: int) -> Tuple[int, int]:
    """Move the mouse to *(x, y)* and return the new position."""
    global _MOUSE_POS
    _MOUSE_POS = (x, y)
    return _MOUSE_POS


def click(button: str = "left") -> int:
    """Register a mouse click and return the total number of clicks."""
    global _CLICK_COUNT
    _CLICK_COUNT += 1
    return _CLICK_COUNT


def key_press(key: str) -> str:
    """Record a key press and return the key."""
    _TYPED_KEYS.append(key)
    return key


def type_text(text: str) -> int:
    """Type a string character by character and return number of chars."""
    for char in text:
        key_press(char)
    return len(text)


def state() -> tuple[Tuple[int, int], List[str], int]:
    """Return the current internal state for testing."""
    return _MOUSE_POS, list(_TYPED_KEYS), _CLICK_COUNT


def reset() -> None:
    """Reset internal counters."""
    global _MOUSE_POS, _TYPED_KEYS, _CLICK_COUNT
    _MOUSE_POS = (0, 0)
    _TYPED_KEYS = []
    _CLICK_COUNT = 0
