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
