from memory_ import Memory


def test_add_and_search():
    m = Memory()
    m.add("hello world")
    m.add("goodbye world")
    results = m.search("hello")
    assert results[0][0] == 0
