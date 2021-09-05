from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import config

# To make sure the extension is allowed in the ALLOWED_EXTENSIONS set.
def checkExtension(extension):
    return extension in config.ALLOWED_EXTENSIONS

# Returns the string of supported file extensions.
def getExtensions():
    string = ''
    for extension in sorted(config.ALLOWED_EXTENSIONS):
        string = string + '.' + extension.upper() + ', '
    # Magical number -2 to remove the last two characters of comma and space.
    string = string[:-2]
    return string

# Returns the thumbnail url.
def getThumbnail(upload_result):
    thumbnail32width = None
    thumbnail64width = None
    if upload_result['width'] >= 128 and upload_result['height'] >= 128:
        thumbnail32width, options = cloudinary_url(upload_result['public_id'], width = 32, crop = "scale")
        thumbnail64width, options = cloudinary_url(upload_result['public_id'], width = 64, crop = "scale")
    return thumbnail32width, thumbnail64width