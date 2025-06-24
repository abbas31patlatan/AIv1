from data.data_cleaner import clean
from core.data_manager import DataManager
import os


def test_clean():
    assert clean('Hi!!') == 'hi'


def test_data_manager(tmp_path):
    dm = DataManager(tmp_path / 'd.json')
    dm.save({'a': 1})
    assert dm.load() == {'a': 1}

