from modules.api_connector import APIConnector

def test_fetch_valid_url():
    c = APIConnector()
    result = c.fetch('http://example.com')
    assert 'url' in result
    assert result['url'] == 'http://example.com'

def test_fetch_invalid_url():
    c = APIConnector()
    # Hatalı bir URL verdiğimizde fallback düzgün çalışıyor mu?
    result = c.fetch('http://not.a.real.url.this.should.fail')
    assert 'url' in result
    assert result['url'].startswith('http')

def test_fetch_localhost():
    c = APIConnector()
    result = c.fetch('http://localhost')
    assert 'url' in result
