import sys

sys.path.append('../')
import config
import requests

def test_connection():
    url = "https://{}:{}@api.cloudinary.com/v1_1/{}/ping".format(config.api_key, config.api_secret, config.cloud_name)
    r = requests.get(url)
    assert r.status_code == 200, "Fail to connect to Cloudinary."
    assert b'{"status":"ok"}' in r.content, "Cloudinary status not ok."

if __name__ == "__main__":
    test_connection()
    print("Everything passed.")