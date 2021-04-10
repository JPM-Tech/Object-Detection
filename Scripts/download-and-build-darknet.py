import os
import sys

#clone darknet repo
os.system("git clone https://github.com/AlexeyAB/darknet")

os.system("cd darknet")

#change makefile to have GPU and OPENCV enabled
os.system("sed -i 's/OPENCV=0/OPENCV=1/' Makefile")
# os.system("sed -i 's/GPU=0/GPU=1/' Makefile")
# os.system("sed -i 's/CUDNN=0/CUDNN=1/' Makefile")
# os.system("sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile")

#make darknet (builds darknet so that you can then use the darknet executable file to run or train object detectors)
os.system("make")

# get pretrained weights for darknet for Yolov3
os.system("wget https://pjreddie.com/media/files/yolov3.weights")
# get pretrained weights for darknet for Yolov4
os.system("wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights")
