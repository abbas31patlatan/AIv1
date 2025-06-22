from gui.gui_main import run


def test_run_gui():
    assert run().startswith('[button]')

