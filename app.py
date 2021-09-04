from flask import Flask, render_template, request, jsonify, abort
from flask_cors import CORS, cross_origin
import cloudinary
import cloudinary.uploader
import cloudinary.api
import config
import processimage
import msgresponse

app = Flask(__name__)
# Make all APIs allow cross-origin access.
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/upload", methods=['POST', 'GET'])
@cross_origin()
def uploadFile():
    cloudinary.config( 
        cloud_name = config.cloud_name, 
        api_key = config.api_key, 
        api_secret = config.api_secret
    )
    upload_result = None
    if request.method == 'POST':
        file_to_upload = request.files['file']
        extension = file_to_upload.filename.rsplit('.', 1)[1].lower()
        if file_to_upload and processimage.checkExtension(extension):
            upload_result = cloudinary.uploader.upload(file_to_upload)
            return upload_result['secure_url']
        else:
            abort(400, description = msgresponse.fileNotSupported(extension))

if __name__ == '__main__':
    app.run()