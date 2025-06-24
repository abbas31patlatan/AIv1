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


def test_synonyms_and_similarity():
    m = Memory()
    id1 = m.add("hello friend")
    id2 = m.add("farewell companion")
    # search_synonyms should match based on 'hi' expanding to 'hello'
    assert m.search_synonyms("hi")[0][0] == id1
    # find_similar should match similar wording
    assert id2 in m.find_similar("bye companion")


def test_remove_and_summary():
    m = Memory()
    m.add("first entry to keep")
    m.add("remove me please")
    removed = m.remove_matching("remove")
    assert removed == 1 and len(m) == 1
    summary = m.summarise()
    assert "first entry" in summary
