from .. import cylma

# Search IP for test
cylma.ip_analysis('8.8.8.8', shodan=True, ip_api=True)


def test_ip_api():
    assert cylma.ip_data['status'] == 'success'

def test_shodan_api():
    assert cylma.shodan_data['isp'] == 'Google'
