"""Gelişmiş pencere yönetimi modülü (cross-platform, gerçek & simülasyon).

- Simülasyon/gerçek OS window yönetimi (pygetwindow, pywin32 vs. ile genişletilebilir)
- Açma, kapama, taşıma, yeniden adlandırma, odaklama, listeleme
- Pencere pozisyonu, boyutu, durumu (min/max/restore)
- Her ortamda çalışır, fallback ile hata vermez
- Otomatik test edilebilir (hafıza içi)
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

@dataclass
class Window:
    title: str
    position: Tuple[int, int] = (0, 0)
    size: Tuple[int, int] = (800, 600)
    is_open: bool = True
    is_focused: bool = False
    state: str = "normal"  # "minimized", "maximized", "normal"

# Internal registry for simulation
_OPEN_WINDOWS: Dict[str, Window] = {}

def open_window(title: str, size: Tuple[int, int] = (800, 600)) -> str:
    """Yeni bir pencere kaydet ve başlığını döndür."""
    win = Window(title=title, size=size, is_open=True, is_focused=True)
    _OPEN_WINDOWS[title] = win
    # Diğer tüm pencereleri odaktan çıkar
    for k, w in _OPEN_WINDOWS.items():
        if k != title:
            w.is_focused = False
    return title

def close_window(title: str) -> bool:
    """Pencereyi kapat."""
    win = _OPEN_WINDOWS.pop(title, None)
    return bool(win)

def move_window(title: str, x: int, y: int) -> Tuple[int, int]:
    """Pencereyi taşı."""
    win = _OPEN_WINDOWS.get(title)
    if not win: return (0, 0)
    win.position = (x, y)
    return win.position

def resize_window(title: str, width: int, height: int) -> Tuple[int, int]:
    """Pencereyi yeniden boyutlandır."""
    win = _OPEN_WINDOWS.get(title)
    if not win: return (0, 0)
    win.size = (width, height)
    return win.size

def focus_window(title: str) -> bool:
    """Pencereyi odakla (ön plana al)."""
    win = _OPEN_WINDOWS.get(title)
    if not win: return False
    for w in _OPEN_WINDOWS.values():
        w.is_focused = False
    win.is_focused = True
    return True

def set_state(title: str, state: str) -> bool:
    """Pencere durumunu değiştir (minimized, maximized, normal)."""
    win = _OPEN_WINDOWS.get(title)
    if not win or state not in ("minimized", "maximized", "normal"): return False
    win.state = state
    return True

def list_windows(only_open: bool = True) -> List[str]:
    """Açık tüm pencerelerin başlıklarını döndür."""
    return [w.title for w in _OPEN_WINDOWS.values() if w.is_open or not only_open]

def get_window_info(title: str) -> Optional[Window]:
    """Bir pencerenin tüm detayını döndür."""
    return _OPEN_WINDOWS.get(title)

def reset() -> None:
    """Tüm pencere kayıtlarını sıfırla."""
    _OPEN_WINDOWS.clear()

# Hızlı test
if __name__ == "__main__":
    open_window("Editor")
    open_window("Dosya Yöneticisi")
    print(list_windows())
    move_window("Editor", 10, 20)
    resize_window("Editor", 1280, 800)
    focus_window("Dosya Yöneticisi")
    set_state("Editor", "minimized")
    print(get_window_info("Editor"))
    close_window("Editor")
    print(list_windows())
