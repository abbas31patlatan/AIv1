from modules_builder import build


def test_build():
    mods = build(['modules.api_connector'])
    assert mods[0].__name__ == 'modules.api_connector'

