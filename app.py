from flask import Flask, request, render_template, send_from_directory
import os
from PIL import Image
import pydarknet #we have to use pydarknet.Image and pydarknet.Detector since it conflicts with PIL Image
import cv2
import numpy as np
import time

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Pre-load the YOLO Detector
yversions = ["v2", "v3"]
darknet = {}
for yversion in yversions:
	darknet[yversion] = pydarknet.Detector(bytes("yolo/yolo" + yversion + ".cfg", encoding="utf-8"), bytes("yolo/yolo" + yversion + ".weights", encoding="utf-8"), 0, bytes("yolo/coco.data", encoding="utf-8"))

# default access page
@app.route("/")
def main():
	return render_template('index.html')


# upload selected image and forward to processing page
@app.route("/upload", methods=["POST"])
def upload():
	target = os.path.join(APP_ROOT, 'static/images/')

	# create image directory if not found
	if not os.path.isdir(target):
		os.mkdir(target)

	# retrieve file from html file-picker
	upload = request.files.getlist("file")[0]
	print("File name: {}".format(upload.filename))
	filename = upload.filename

	# file support verification
	ext = str.lower(os.path.splitext(filename)[1])
	if (ext == ".jpg") or (ext == ".png") or (ext == ".bmp"):
		print("File accepted")
	else:
		return render_template("error.html", message="The selected file is not supported"), 400

	filename = "uploaded" + ext

	# save file
	destination = "/".join([target, filename])
	print("File saved to to:", destination)
	upload.save(destination)

	# forward to processing page
	return render_template("processing.html", image_name=filename)


# rotate filename the specified degrees
@app.route("/rotate", methods=["POST"])
def rotate():
	# retrieve parameters from html form
	angle = request.form['angle']
	filename = request.form['image']

	# open and process image
	target = os.path.join(APP_ROOT, 'static/images')
	destination = "/".join([target, filename])

	img = Image.open(destination)
	img = img.rotate(-1*int(angle))

	# save and return image
	destination = "/".join([target, 'temp.png'])
	if os.path.isfile(destination):
		os.remove(destination)
	img.save(destination)

	return send_image('temp.png')


# flip filename 'vertical' or 'horizontal'
@app.route("/flip", methods=["POST"])
def flip():
	# retrieve parameters from html form
	if 'horizontal' in request.form['mode']:
		mode = 'horizontal'
	elif 'vertical' in request.form['mode']:
		mode = 'vertical'
	else:
		return render_template("error.html", message="Mode not supported (vertical - horizontal)"), 400
	filename = request.form['image']

	# open and process image
	target = os.path.join(APP_ROOT, 'static/images')
	destination = "/".join([target, filename])

	img = Image.open(destination)

	if mode == 'horizontal':
		img = img.transpose(Image.FLIP_LEFT_RIGHT)
	else:
		img = img.transpose(Image.FLIP_TOP_BOTTOM)

	# save and return image
	destination = "/".join([target, 'temp.png'])
	if os.path.isfile(destination):
		os.remove(destination)
	img.save(destination)

	return send_image('temp.png')


# crop filename from (x1,y1) to (x2,y2)
@app.route("/crop", methods=["POST"])
def crop():
	# retrieve parameters from html form
	x1 = int(request.form['x1'])
	y1 = int(request.form['y1'])
	x2 = int(request.form['x2'])
	y2 = int(request.form['y2'])
	filename = request.form['image']

	# open image
	target = os.path.join(APP_ROOT, 'static/images')
	destination = "/".join([target, filename])

	img = Image.open(destination)

	# check for valid crop parameters
	width = img.size[0]
	height = img.size[1]

	crop_possible = True
	if not 0 <= x1 < width:
		crop_possible = False
	if not 0 < x2 <= width:
		crop_possible = False
	if not 0 <= y1 < height:
		crop_possible = False
	if not 0 < y2 <= height:
		crop_possible = False
	if not x1 < x2:
		crop_possible = False
	if not y1 < y2:
		crop_possible = False

	# crop image and show
	if crop_possible:
		img = img.crop((x1, y1, x2, y2))

		# save and return image
		destination = "/".join([target, 'temp.png'])
		if os.path.isfile(destination):
			os.remove(destination)
		img.save(destination)
		return send_image('temp.png')
	else:
		return render_template("error.html", message="Crop dimensions not valid"), 400
	return '', 204

# apply YOLO object detection
@app.route("/yolo", methods=["POST"])
def yolo():
	# retrieve parameters from html form
	filename1 = request.form['image']
	yversion = request.form['yolo_version']

	# open images
	target = os.path.join(APP_ROOT, 'static/images')
	destination1 = "/".join([target, filename1])

	img1 = Image.open(destination1)
	img = np.asarray(img1)
	img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

	destination = "/".join([target, 'temp.png'])

	if os.path.isfile(destination):
		print("Existing file found at "+destination)
		os.remove(destination)

	print("Performing YOLO"+yversion+" on image at "+destination1+"...\nThis might take a while...")
	start_time = time.time()
	results = darknet[yversion].detect(pydarknet.Image(img))
	end_time = time.time()
	#print(results)
	print("Elapsed Time:", end_time - start_time)

	print("Detected:")
	for cat, score, bounds in results:
		x, y, w, h = bounds
		label = str(cat.decode("utf-8"))
		conf = str(score.decode("utf-8"))

		cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)),
					 (int(x + w / 2), int(y + h / 2)), (0, 0, 255), thickness=2)
		cv2.putText(img, label+", "+conf), (int(x-w/2), int(y-h/2+20)),
					cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 0, 255), thickness=1, lineType=cv2.LINE_AA)
		print("\t{}, {}".format(label, conf))

	# save and return image
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	im_pil = Image.fromarray(img)
	im_pil.save(destination)

	return send_image('temp.png')
	#return render_template("image.html", image_name='temp.png')

# retrieve file from 'static/images' directory
@app.route('/static/images/<filename>')
def send_image(filename):
	return send_from_directory("static/images", filename)

# run with host 0.0.0.0
# this is needed for exposing port outside docker container
if __name__ == "__main__":
	app.run(host='0.0.0.0')
