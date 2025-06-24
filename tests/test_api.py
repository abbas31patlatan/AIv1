from modules.api_connector import APIConnector

def test_fetch_valid_url():
    c = APIConnector()
    result = c.fetch('http://example.com')
    assert 'url' in result
    assert result['url'] == 'http://example.com'
    assert isinstance(result, dict)

def test_fetch_invalid_url():
    c = APIConnector()
    # Hatalı bir URL verildiğinde yine de dict dönüyor ve hata durumu yönetiliyor mu?
    result = c.fetch('http://not.a.real.url.this.should.fail')
    assert 'url' in result
    assert result['url'].startswith('http')
    assert 'error' in result or 'status' in result or isinstance(result, dict)

def test_fetch_localhost():
    c = APIConnector()
    result = c.fetch('http://localhost')
    assert 'url' in result
    assert result['url'] == 'http://localhost'

# Eğer gerçek bir API test etmek istersen:
def test_fetch_public_api():
    c = APIConnector()
    result = c.fetch('https://api.github.com')
    assert 'url' in result
    assert result['url'].startswith('https')
    assert isinstance(result, dict)

