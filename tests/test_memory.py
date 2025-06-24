from memory_ import Memory

def test_add_and_search():
    m = Memory()
    idx1 = m.add("hello world")
    idx2 = m.add("goodbye world")
    results = m.search("hello")
    assert results[0][0] == idx1
    assert any("hello" in m.get(i) for i, _ in results)

def test_update_and_remove():
    m = Memory()
    idx = m.add("foo")
    m.update(idx, "bar")
    assert m.get(idx) == "bar"
    m.remove(idx)
    assert len(m) == 0

def test_clear_and_len():
    m = Memory()
    m.add("a")
    m.add("b")
    m.clear()
    assert len(m) == 0

def test_save_and_load(tmp_path):
    m = Memory()
    idx = m.add("persistent")
    # Eğer Memory gelişmiş ise (save/load methodları varsa)
    if hasattr(m, "save") and hasattr(m, "load"):
        path = tmp_path / "mem.json"
        m.save(path)
        m2 = Memory()
        m2.load(path)
        assert "persistent" in list(m2)

def test_regex_and_autosave(tmp_path):
    from pathlib import Path
    m = Memory()
    if hasattr(m, "enable_autosave") and hasattr(m, "search_regex"):
        path = tmp_path / "auto.json"
        m.enable_autosave(path)
        idx = m.add("foo bar")
        assert m.search_regex("foo") == [idx]
        assert Path(path).exists()

def test_synonyms_and_similarity():
    m = Memory()
    if hasattr(m, "search_synonyms") and hasattr(m, "find_similar"):
        id1 = m.add("hello friend")
        id2 = m.add("farewell companion")
        # search_synonyms should match based on 'hi' expanding to 'hello'
        assert m.search_synonyms("hi")[0][0] == id1
        # find_similar should match similar wording
        assert id2 in m.find_similar("bye companion")

def test_remove_and_summary():
    m = Memory()
    if hasattr(m, "remove_matching") and hasattr(m, "summarise"):
        m.add("first entry to keep")
        m.add("remove me please")
        removed = m.remove_matching("remove")
        assert removed == 1 and len(m) == 1
        summary = m.summarise()
        assert "first entry" in summary
