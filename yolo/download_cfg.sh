#!/bin/sh

echo "Downloading config files..."

wget -O ./coco.data https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/coco.data
wget -O ./yolov2.cfg https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov2.cfg
wget -O ./yolov3.cfg https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg

echo "Modify config parameters to enable Testing mode"
sed -i '/batch=64/c\# batch=64' ./yolov2.cfg
sed -i '/subdivisions=16/c\# subdivisions=16' ./yolov2.cfg
sed -i '/# batch=1/c\batch=1' ./yolov2.cfg
sed -i '/# subdivisions=1/c\subdivisions=1' ./yolov2.cfg

sed -i '/batch=64/c\# batch=64' ./yolov3.cfg
sed -i '/subdivisions=16/c\# subdivisions=16' ./yolov3.cfg
sed -i '/# batch=1/c\batch=1' ./yolov3.cfg
sed -i '/# subdivisions=1/c\subdivisions=1' ./yolov3.cfg

sed -i 's/data\///g' ./coco.data
sed -i 's/coco.names/yolo\/coco.names/g' ./coco.data
sed -i 's/\/home\/pjreddie\///g' ./coco.data

wget -O ./coco.names https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names

echo "Downloading yolo v2 and v3 weights"
wget -O ./yolov2.weights https://pjreddie.com/media/files/yolov2.weights
wget -O ./yolov3.weights https://pjreddie.com/media/files/yolov3.weights
