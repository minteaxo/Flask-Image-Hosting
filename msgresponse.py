import processimage

def fileNotSupported(extension):
    return "Invalid image. File extension ." + extension.upper() + " is not supported. Supported file format includes " + processimage.getExtensions() + "."

noImgUploaded = "Please select an image to upload."
uploadEmptyPost = "POST an image to view the result."