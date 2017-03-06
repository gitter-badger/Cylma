from .. import cylma


cylma.ua_analysis("Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F56.0.2924.87%20Safari%2F537.36")

def test_ua():
    assert cylma.ua_data == {
        "data": {
            "ua_type": "Desktop",
            "os_name": "Windows",
            "os_version": "10",
            "browser_name": "Chrome",
            "browser_version": "56.0.2924.87",
            "engine_name": "WebKit",
            "engine_version": "537.36"
        }
    }
