"""High level utilities for interacting with windows on the desktop.

This module provides a tiny abstraction over window management functionality.
It keeps an in-memory registry of opened windows so that behaviour can be
simulated in environments where access to the real OS APIs is unavailable.  The
functions are written to be easily replaceable with platform specific
implementations should the project need to control real windows.

Example
-------
>>> open_window('Editor')
'Editor'
>>> move_window('Editor', 10, 20)
(10, 20)
>>> close_window('Editor')
True
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

# ---------------------------------------------------------------------------
# Internal registry used only for demonstration purposes
# ---------------------------------------------------------------------------

@dataclass
class Window:
    title: str
    position: Tuple[int, int] = (0, 0)


_OPEN_WINDOWS: Dict[str, Window] = {}


def open_window(title: str) -> str:
    """Register a new window and return its title."""
    _OPEN_WINDOWS[title] = Window(title)
    return title


def close_window(title: str) -> bool:
    """Remove *title* from the registry and return ``True`` if it existed."""
    return _OPEN_WINDOWS.pop(title, None) is not None


def move_window(title: str, x: int, y: int) -> Tuple[int, int]:
    """Move *title* to the given coordinates and return them."""
    win = _OPEN_WINDOWS.setdefault(title, Window(title))
    win.position = (x, y)
    return win.position


def list_windows() -> List[str]:
    """Return the titles of all currently opened windows."""
    return list(_OPEN_WINDOWS)


def reset() -> None:
    """Clear internal state.  Useful for tests."""
    _OPEN_WINDOWS.clear()
