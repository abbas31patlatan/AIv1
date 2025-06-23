from memory_ import Memory


def test_add_and_search():
    m = Memory()
    m.add("hello world")
    m.add("goodbye world")
    results = m.search("hello")
    assert results[0][0] == 0


def test_update_and_remove():
    m = Memory()
    idx = m.add("foo")
    m.update(idx, "bar")
    assert m.get(idx) == "bar"
    m.remove(idx)
    assert len(m) == 0


def test_save_and_load(tmp_path):
    m1 = Memory()
    m1.add("persistent")
    path = tmp_path / "mem.json"
    m1.save(path)

    m2 = Memory()
    m2.load(path)
    assert "persistent" in list(m2)


def test_regex_and_autosave(tmp_path):
    path = tmp_path / "auto.json"
    m = Memory(autosave_path=path)
    idx = m.add("foo bar")
    assert m.search_regex("foo") == [idx]
    assert path.exists()
