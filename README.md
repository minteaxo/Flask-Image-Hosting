# Flask Image Hosting
A Restful service to host and share image.

## Customize your own Cloudinary account
Currently I am using a free account that has a limitation of 100MB storage.
You may customize the configuration settings in config.py.

## Run the app
The main app is located at app.py.
Additionally you could try it on cloud, deployed to Heroku:
https://tranquil-ravine-80792.herokuapp.com/

## Release notes
There are quite a lot of things to learn, so far I managed to complete Story 1 and Story 2.2 only.

**Story 1**
I want to attach a picture to the Service,
And I want to have a permanent link to this picture,
Otherwise, I want to be rejected and informed if the file is not a picture.

**Story 2.2**
I want to have thumbnails returned for any uploaded images which sizes are
equal to or larger than 128px by 128px