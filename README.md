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
The different calls can be interfaced with `GET` methods. All images must be located in the `static/images` folder, or otherwise specify the relative path, from that folder, in `filename` parameter. If the request is correct, the modified image will be returned. The syntaxes and an example for each function are described herein.

### Flip
```
GET /flip/<mode>/<filename>
```
where `mode` can either be `vertical` or `horizontal` and `filename` is the image file name, including extension and relative to the images folder. Browser input example:
```
http://127.0.0.1:5000/flip/vertical/minimalistic-coca-cola_00411260.jpg
```

### Rotate
```
GET /rotate/<angle>/<filename>
```
where `angle` can take any value between 0 and 359 degrees. A positive value indicates clockwise rotation, whereas a negative one indicates counter-clockwise rotation. `filename` is the image file name, including extension and relative to the images folder. Browser input example:
```
http://127.0.0.1:5000/rotate/30/Star-War-l.jpg
```

### Crop
```
GET /crop/<x1>/<y1>/<x2>/<y2>/<filename>
```
with the start and stop point coordinates, (`x1, y1`) and (`x2, y2`), respectively. `filename` is the image file name, including extension and relative to the images folder. Browser input example:
```
http://127.0.0.1:5000/crop/150/250/350/500/The_Scream.jpg
```

### Blend
```
GET /blend/<alpha>/<filename1>/<filename2>
```
where `alpha`, in % (between 0 and 100), is the weight of the first image in the blend. `filename1` and `filename2` specify the images to blend. If one of them is in gray scale, the other one will be converted automatically. Antialias resizing is also done behind the curtains. Browser input example:
```
http://127.0.0.1:5000/blend/50/3x1gKAL.png/blend.jpg
```

## Web application
Run `app.py` and navigate to `localhost:5000`. Use the `SELECT FILE` button to upload the desired file. If successful, the browser will redirect to the processing page.

Input the desired parameters to apply the corresponding transformation. The modified image will be opened with your default image viewing program. The parameters are now sent through the form data with a post method, instead of being passed as arguments in the GET request. So, this app showcases a different approach to API functionality. The different transformations are:

* Flip: simply click either the `Vertical` or the `Horizontal` buttons.
* Rotate: input the degrees between 0 and 359 (html field validation). Use a positive number for clockwise rotation or a negative one for a counter-clockwise one. Click `GO` to proceed.
* Crop: input the start and stop point coordinates, (`x1, y1`) and (`x2, y2`), respectively. Click `GO` to proceed. Will be validated by the API.
* Blend: input alpha (%) between 0 and 100, html validated. The image will be blend with the stock photo `blend.jpg`. The higher the alpha parameter, the more weight will be assigned to the stock photo (i.e. for alpha equals 0 the image will remain unchanged). Click `GO` to proceed.


