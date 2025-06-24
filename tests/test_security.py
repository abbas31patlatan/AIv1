from security_scan import scan


def test_scan():
    assert scan('clean file')
    assert not scan('contains malware code')

