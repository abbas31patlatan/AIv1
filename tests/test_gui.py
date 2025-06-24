from gui.gui_main import AppGUI, run
from config.gui_preferences import prefs
from gui.themes import THEMES

def test_app_theme():
    gui = AppGUI()
    try:
        if hasattr(gui.root, "cget"):
            # Tkinter ile başlatıldıysa arka plan rengi temaya uygun olmalı
            assert gui.root.cget("bg") == THEMES[prefs.theme]["bg"]
    finally:
        if hasattr(gui.root, "destroy"):
            gui.root.destroy()

def test_run_gui_button():
    # Headless veya test modunda "run" fonksiyonu bir buton stringi döndürmeli
    screen = run()
    assert isinstance(screen, str)
    assert screen.startswith("[button]")

def test_prefs_toggle_voice():
    orig = prefs.voice_enabled
    prefs.toggle_voice()
    assert prefs.voice_enabled != orig
    prefs.toggle_voice()  # reset to original

def test_set_theme():
    orig = prefs.theme
    prefs.set_theme("dark")
    assert prefs.theme == "dark"
    prefs.set_theme(orig)  # revert

def test_appgui_toggle_voice():
    gui = AppGUI()
    prev = prefs.voice_enabled
    gui.toggle_voice()
    assert prefs.voice_enabled != prev
    gui.toggle_voice()
    if hasattr(gui.root, "destroy"):
        gui.root.destroy()


