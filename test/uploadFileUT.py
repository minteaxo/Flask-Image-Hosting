import io
import sys
from flask.helpers import url_for
sys.path.append('../')
import msgresponse
import app

client = app.app.test_client()

def test_fileUpload():
    with app.app.app_context(), app.app.test_request_context(), open('test_image.png', 'rb') as img:
        response = client.post(url_for('uploadFile'),
                            content_type='multipart/form-data',
                            follow_redirects=True,
                            data={'file' : (io.BytesIO(img.read()), 'test_image.png')})
        assert b'Upload Success!' in response.data, "Failed to upload image, result: " + str(response.data)
        assert b'thumbnail' in response.data, "Expected to see thumbnails, result: " + str(response.data)
        
def test_fileUpload_small():
    with app.app.app_context(), app.app.test_request_context(), open('test_thumbnail.png', 'rb') as img:
        response = client.post(url_for('uploadFile'),
                            content_type='multipart/form-data',
                            follow_redirects=True,
                            data={'file' : (io.BytesIO(img.read()), 'test_thumbnail.png')})
        assert b'Upload Success!' in response.data, "Failed to upload image, result: " + str(response.data)
        assert not (b'thumbnail' in response.data), "Expected not to see thumbnails, result: " + str(response.data)

def test_fileUpload_GET():
    with app.app.app_context(), app.app.test_request_context():
        response = client.get(url_for('uploadFile'),
                            follow_redirects=True)
        assert msgresponse.uploadEmptyPost in str(response.data), "Different message received, result: " + str(response.data)

if __name__ == "__main__":
    test_fileUpload()
    test_fileUpload_small()
    test_fileUpload_GET()
    print("Everything passed.")