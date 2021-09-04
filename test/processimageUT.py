import sys
sys.path.append('../')
import processimage

def test_checkExtension_Positive():
    assert processimage.checkExtension('png') == True, "Expected file extension support."

def test_checkExtension_Negative():
    assert processimage.checkExtension('xlsx') == False, "Expected file extension does not support."

def test_getExtensions():
    actual = processimage.getExtensions()
    expected = ".GIF, .JPEG, .JPG, .PNG, .WEBP"
    assert actual == expected, "Expected: " + expected + ", Actual: " + actual + " | Extension string not match."

if __name__ == "__main__":
    test_checkExtension_Positive()
    test_checkExtension_Negative()
    test_getExtensions()
    print("Everything passed.")