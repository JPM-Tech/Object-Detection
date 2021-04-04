import os
import sys

print("Now that you have downloaded the best .weights file from your 'Google Drive/yolov4/backup' folder")
path_to_weights_file = input("Enter the directory path to the .weights file: ")

#move into Functions-For-TensorFlow-and-TensorFlow-Lite-Model
os.chdir("Functions-For-TensorFlow-and-TensorFlow-Lite-Model")

print("Installing required dependencies")
os.system("pip install -r requirements.txt")

print("Creating TensorFlow Model")
os.system("python3 save_model.py --weights " + path_to_weights_file.rstrip() + " --output ./checkpoints/custom-416 --input_size 416 --model yolov4 ")

print("TensorFlow model created successfully")
print("Opening folder to stored model...")
open(os.path.abspath(os.getcwd()) + "/checkpoints/custom-416")
