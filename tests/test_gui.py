from gui.gui_main import AppGUI, run
from config.gui_preferences import prefs
from gui.themes import THEMES

def test_app_theme():
    gui = AppGUI()
    try:
        if hasattr(gui.root, "cget"):
            assert gui.root.cget("bg") == THEMES[prefs.theme]["bg"]
    finally:
        if hasattr(gui.root, "destroy"):
            gui.root.destroy()

def test_run_gui_button():
    # Headless (test) modda çalışıyor ve geri dönüşü kontrol ediyoruz
    screen = run()
    assert isinstance(screen, str)
    assert screen.startswith("[button]")

def test_prefs_toggle_voice():
    orig = prefs.voice_enabled
    prefs.toggle_voice()
    assert prefs.voice_enabled != orig
    prefs.toggle_voice()  # eskiye döndür

def test_set_theme():
    orig = prefs.theme
    prefs.set_theme("dark")
    assert prefs.theme == "dark"
    prefs.set_theme(orig)  # eskiye döndür


