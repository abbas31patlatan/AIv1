from gui.gui_main import run
from config.gui_preferences import prefs


def test_run_gui():
    assert run().startswith('[button]')


def test_prefs_toggle_voice():
    start = prefs.voice_enabled
    prefs.toggle_voice()
    assert prefs.voice_enabled != start
    prefs.toggle_voice()  # reset


def test_set_theme():
    old = prefs.theme
    prefs.set_theme('dark')
    assert prefs.theme == 'dark'
    prefs.set_theme(old)

