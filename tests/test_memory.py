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

# Gelişmiş memory fonksiyonları (varsa, yoksa skip eder)
def test_save_and_load(tmp_path):
    m = Memory()
    idx = m.add("persistent")
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
