import os
import sys

path_to_weights_file = input("Enter the directory path to the .weights file: ")

print("\n[ 3 ] I want to train with Yolo v3 (the version that you began training with).")
print("[ 4 ] I want to train with Yolo v4 (the version that you began training with).")
yolo_version = input("Enter one of the numbers above and press enter (q to quit): ")

os.chdir("Functions-For-TensorFlow-and-TensorFlow-Lite-Model/")

print("Creating TensorFlow Model")
os.system("python3 save_model.py --weights " + path_to_weights_file.rstrip() + " --output ./checkpoints/custom-416 --input_size 416 --model yolov" + yolo_version)

print("Creating TensorFlow Light Model")
os.system("python3 save_model.py --weights " + path_to_weights_file.rstrip() + " --output ./checkpoints/custom-416-tf-lite --input_size 416 --model yolov" + yolo_version + " --framework tflite")

print("TensorFlow model created successfully")
print("Path to created model...")
open("Functions-For-TensorFlow-and-TensorFlow-Lite-Model/checkpoints/custom-416")
