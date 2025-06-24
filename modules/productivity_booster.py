"""Toy task tracking utilities with priority support."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(order=True)
class Task:
    priority: int
    title: str = field(compare=False)
    done: bool = field(default=False, compare=False)


_TASKS: Dict[str, Task] = {}


def add_task(title: str, priority: int = 1) -> None:
    """Add a new task with the given priority."""
    _TASKS[title] = Task(priority, title)


def complete_task(title: str) -> bool:
    """Mark ``title`` as complete, returning ``True`` if it existed."""
    task = _TASKS.get(title)
    if not task:
        return False
    task.done = True
    return True


def list_tasks(active_only: bool = True) -> List[Task]:
    """Return tasks optionally filtering out completed ones."""
    tasks = _TASKS.values()
    if active_only:
        tasks = [t for t in tasks if not t.done]
    return sorted(tasks)


def summary() -> str:
    """Return a short human readable summary."""
    remaining = len([t for t in _TASKS.values() if not t.done])
    return f"{remaining} incomplete task(s)"


def reset() -> None:
    _TASKS.clear()
