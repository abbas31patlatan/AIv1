from modules.api_connector import APIConnector


def test_fetch():
    c = APIConnector()
    result = c.fetch('http://example.com')
    assert 'url' in result

