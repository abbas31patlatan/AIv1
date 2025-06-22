from modules.api_connector import APIConnector


def test_fetch():
    c = APIConnector()
    assert c.fetch('http://example.com')['url'] == 'http://example.com'

