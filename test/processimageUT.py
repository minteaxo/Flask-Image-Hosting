import sys
sys.path.append('../')
import processimage
import config

def test_checkExtension():
    for ext in config.ALLOWED_EXTENSIONS:
        assert processimage.checkExtension(ext) == True, "Expected file extension " + ext + " support."
    assert processimage.checkExtension('xlsx') == False, "Expected file extension xlsx does not support."

def test_getExtensions():
    actual = processimage.getExtensions()
    expected = ".GIF, .JPEG, .JPG, .PNG, .WEBP"
    assert actual == expected, "Expected: " + expected + ", Actual: " + actual + " | Extension string not match."

if __name__ == "__main__":
    test_checkExtension()
    test_getExtensions()
    print("Everything passed.")