# Image API
Image Processing API written in Python, using the Pillow library for image manipulation and exposing the functions with the Flask framework. The API has been tested with jpg, png and bmp formats and is able to flip, rotate and crop an image, as well as blending two images, either RGB or gray scale.

## Getting started
The API includes three Python files:
* `core.py`: includes the basic calls of the API. Run the file and use `GET` requests on `localhost:5000`. For more details please refer to the documentation section in this file.
* `app.py`: a web application to test the functionality that serves as a proof of concept. Run it, navigate to `localhost:5000` and follow the instructions. For more details please refer to the documentation section in this file.
* `test.py`: a file to test API requests by checking the received http status codes. `core.py` needs to be running.

## Dependencies
Python installation needs the `PIL` library (image processing), `flask` with its dependencies (`werkzeug`, `jinja2`, `markupsafe`, `itsdangerous`) and testing libraries (`unittest` and `requests`).

## Documentation

## Web application
Run `app.py` and navigate to `localhost:5000`. Use the `SELECT FILE` button to upload the desired file. If successful, the browser will redirect to the processing page.

Input the desired parameters to apply the corresponding transformation. The modified image will be opened with your default image viewing program. The parameters are now sent through the form data with a post method, instead of being passed as arguments in the GET request. So, this app showcases a different approach to API functionality. The different transformations are:

* Flip: simply click either the `Vertical` or the `Horizontal` buttons.
* Rotate: input the degrees between 0 and 359 (html field validation). Use a positive number for clockwise rotation or a negative one for a counter-clockwise one. Click `GO` to proceed.
* Crop: input the start and stop point coordinates, (`x1, y1`) and (`x2, y2`), respectively. Click `GO` to proceed. Will be validated by the API.
* Blend: input alpha (%) between 0 and 100, html validated. The image will be blend with the stock photo `blend.jpg`. The higher the alpha parameter, the more weight will be assigned to the stock photo (i.e. for alpha equals 0 the image will be unchanged).


