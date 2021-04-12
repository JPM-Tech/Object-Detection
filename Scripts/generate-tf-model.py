import os
import sys

print("Now that you have downloaded the best .weights file from your 'Google Drive/yolov4/backup' folder")
path_to_weights_file = input("Enter the directory path to the .weights file: ")

os.chdir("Functions-For-TensorFlow-and-TensorFlow-Lite-Model/")

print("Creating TensorFlow Model")
os.system("python3 save_model.py --weights " + path_to_weights_file.rstrip() + " --output ./checkpoints/custom-416 --input_size 416 --model yolov4 ")

print("Creating TensorFlow Light Model")
os.system("python3 save_model.py --weights " + path_to_weights_file.rstrip() + " --output ./checkpoints/custom-416 --input_size 416 --model yolov4 --framework tflite")

print("TensorFlow model created successfully")
print("Path to created model...")
open("Functions-For-TensorFlow-and-TensorFlow-Lite-Model/checkpoints/custom-416")
