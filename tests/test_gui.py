from gui.gui_main import AppGUI
from gui.themes import THEMES
from config.gui_preferences import prefs


def test_app_theme():
    gui = AppGUI()
    try:
        assert gui.root.cget("bg") == THEMES[prefs.theme]["bg"]
    finally:
        gui.root.destroy()

