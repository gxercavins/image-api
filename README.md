# Image API
Image Processing API written in Python, using the Pillow library for image manipulation and exposing the functions with the Flask framework. The API has been tested with jpg, png and bmp formats and is able to flip, rotate and crop an image, as well as blending two images, either RGB or gray scale.

For a live demo, please visit this [link](https://image-demo-dot-gxt-proj1.appspot.com/). The App has been deployed to the Google Cloud Platform using App Engine.

## Getting started
The API includes three Python files:
* `core.py`: includes the basic calls of the API. Run the file and use `GET` requests on `localhost:5000`. For more details please refer to the documentation section in this file.
* `app.py`: a web application to test the functionality that serves as a proof of concept. Run it, navigate to `localhost:5000` and follow the instructions. For more details please refer to the documentation section in this file.
* `test.py`: a file to test API requests by checking the received http status codes. `core.py` needs to be running.

Other files have been included for GCP deployment: `app.yaml`, `appengine_config.py` and `requirements.txt`.

## Dependencies
Python installation needs the `PIL` library (image processing), `flask` with its dependencies (`werkzeug`, `jinja2`, `markupsafe`, `itsdangerous`), testing libraries (`unittest` and `requests`) and `gunicorn` to provide an entrypoint for the live deployment. It is recommended to use the provided `requirements.txt` file:
```
sudo pip install -r requirements.txt
```

## Documentation
The different calls can be interfaced with `GET` methods. All images must be located in the `static/images` folder, or otherwise specify the relative path, from that folder, in `filename` parameter. If the request is correct, the modified image will be returned. The syntaxes and an example for each function are described herein.

### Flip
``` http
GET /flip/<mode>/<filename>
```
where `mode` can either be `vertical` or `horizontal` and `filename` is the image file name, including extension and relative to the images folder. Browser input example:
```
http://127.0.0.1:5000/flip/vertical/minimalistic-coca-cola_00411260.jpg
```
![flip](https://user-images.githubusercontent.com/29493411/27295171-3b04a502-551c-11e7-82b1-9283f49a050d.PNG)

### Rotate
``` http
GET /rotate/<angle>/<filename>
```
where `angle` can take any value between 0 and 359 degrees. A positive value indicates clockwise rotation, whereas a negative one indicates counter-clockwise rotation. `filename` is the image file name, including extension and relative to the images folder. Browser input example:
```
http://127.0.0.1:5000/rotate/30/Star-War-l.jpg
```
![rotate](https://user-images.githubusercontent.com/29493411/27295173-3b07127e-551c-11e7-89e6-d76a4fee731e.PNG)

### Crop
``` http
GET /crop/<x1>/<y1>/<x2>/<y2>/<filename>
```
with the start and stop point coordinates, (`x1, y1`) and (`x2, y2`), respectively. `filename` is the image file name, including extension and relative to the images folder. Browser input example:
```
http://127.0.0.1:5000/crop/150/250/350/500/The_Scream.jpg
```
![crop](https://user-images.githubusercontent.com/29493411/27295172-3b06dade-551c-11e7-9b92-0ae0c20d5981.PNG)

### Blend
``` http
GET /blend/<alpha>/<filename1>/<filename2>
```
where `alpha`, in % (between 0 and 100), is the weight of the first image in the blend. `filename1` and `filename2` specify the images to blend. If one of them is in gray scale, the other one will be converted automatically. Antialias resizing is also done behind the curtains. Browser input example:
```
http://127.0.0.1:5000/blend/50/3x1gKAL.png/blend.jpg
```
![blend](https://user-images.githubusercontent.com/29493411/27295174-3b09945e-551c-11e7-94d9-7eecd4fae415.PNG)

## Web application
To test the app localy, run `app.py` and navigate to `localhost:5000`. Otherwise, navigate to the live demo.

Use the `SELECT FILE` button to upload the desired file. 

![web1](https://user-images.githubusercontent.com/29493411/27295175-3b0a1af0-551c-11e7-94fd-7b4106330537.PNG)

If successful, the browser will redirect to the processing page.

![web2](https://user-images.githubusercontent.com/29493411/27295176-3b0d56de-551c-11e7-9cc8-0628eecd22d0.PNG)

Input the desired parameters to apply the corresponding transformation. The modified image will be opened with your default image viewing program. The parameters are now sent through the form data with a post method, instead of being passed as arguments in the GET request. So, this app showcases a different approach to API functionality. The different transformations are:

* Flip: simply click either the `Vertical` or the `Horizontal` buttons.
* Rotate: input the degrees between 0 and 359 (html field validation). Use a positive number for clockwise rotation or a negative one for a counter-clockwise one. Click `GO` to proceed.
* Crop: input the start and stop point coordinates, (`x1, y1`) and (`x2, y2`), respectively. Click `GO` to proceed. Will be validated by the API.
* Blend: input alpha (%) between 0 and 100, html validated. The image will be blend with the stock photo `blend.jpg`. The higher the alpha parameter, the more weight will be assigned to the stock photo (i.e. for alpha equals 0 the image will remain unchanged). Click `GO` to proceed.

## License
This API is provided under the MIT license.

## Issues
Report any issue to the GitHub issue tracker.
