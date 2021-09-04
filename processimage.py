import config

# Returns image ratio.
def getRatio(width, height):
    return width / height

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