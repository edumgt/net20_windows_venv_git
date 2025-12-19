from urllib.parse import urlparse

def test_urlparse_basic():
    u = urlparse("https://example.com:443/a?x=1")
    assert u.scheme == "https"
    assert u.hostname == "example.com"
    assert u.port == 443
