"""Gelişmiş görev (task) takip ve productivity helper modülü.

- Görev ekleme, tamamlama, düzenleme, silme
- Öncelik, açıklama, son tarih, etiket
- Tamamlanan/tamamlanmayan filtreleme, özet, ilerleme yüzdesi
- Export/import desteği (JSON)
- Eski API ile tamamen uyumlu
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime
import json

@dataclass(order=True)
class Task:
    priority: int
    title: str = field(compare=False)
    done: bool = field(default=False, compare=False)
    description: str = field(default="", compare=False)
    due: Optional[datetime] = field(default=None, compare=False)
    tags: List[str] = field(default_factory=list, compare=False)

    def to_dict(self):
        return {
            "priority": self.priority,
            "title": self.title,
            "done": self.done,
            "description": self.description,
            "due": self.due.isoformat() if self.due else None,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, d):
        d = dict(d)
        if d.get("due"):
            d["due"] = datetime.fromisoformat(d["due"])
        return cls(**d)

_TASKS: Dict[str, Task] = {}

def add_task(title: str, priority: int = 1, description: str = "", due: str = "", tags: Optional[List[str]] = None):
    """Görev ekle."""
    tags = tags or []
    due_date = datetime.fromisoformat(due) if due else None
    _TASKS[title] = Task(priority, title, False, description, due_date, tags)

def edit_task(title: str, **kwargs):
    """Bir görevin çeşitli alanlarını düzenle."""
    t = _TASKS.get(title)
    if not t: return False
    for k, v in kwargs.items():
        if hasattr(t, k): setattr(t, k, v)
    return True

def complete_task(title: str) -> bool:
    """Mark ``title`` as complete, returning ``True`` if it existed."""
    task = _TASKS.get(title)
    if not task:
        return False
    task.done = True
    return True

def remove_task(title: str) -> bool:
    """Görevi sil."""
    return bool(_TASKS.pop(title, None))

def list_tasks(active_only: bool = True, tag: Optional[str] = None) -> List[Task]:
    """Görevleri döndür (aktif veya tüm)."""
    tasks = _TASKS.values()
    if active_only:
        tasks = [t for t in tasks if not t.done]
    if tag:
        tasks = [t for t in tasks if tag in t.tags]
    return sorted(tasks)

def summary() -> str:
    """Return a short human readable summary."""
    total = len(_TASKS)
    remaining = len([t for t in _TASKS.values() if not t.done])
    return f"{remaining}/{total} incomplete task(s) ({progress():.1f}%)"

def progress() -> float:
    """Tamamlanma yüzdesi döndürür."""
    total = len(_TASKS)
    if not total: return 0.0
    done = len([t for t in _TASKS.values() if t.done])
    return done / total * 100

def export_tasks(filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in _TASKS.values()], f, ensure_ascii=False, indent=2)

def import_tasks(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for d in data:
            t = Task.from_dict(d)
            _TASKS[t.title] = t

def reset() -> None:
    _TASKS.clear()

# Eski API ile uyumlu fonksiyonlar:
todo_summary = summary

# Hızlı test:
if __name__ == "__main__":
    add_task("Kod yaz", priority=2, description="Projenin modülünü geliştir.", due="2025-07-01", tags=["AI","dev"])
    add_task("Belge güncelle", priority=1, tags=["doc"])
    complete_task("Kod yaz")
    print(summary())
    print(list_tasks())
    export_tasks("tasks.json")
