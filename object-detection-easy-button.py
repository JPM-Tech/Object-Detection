import os
import sys
import pathlib

# This script will be the one stop shop for training an object detection model

# USE os.path.isfile(file_path) to check if a file exists
# USE os.path.isdir(folder_path) to check if a folder exists

# Question 1
print("\n[ 1 ] I already have data and it is labeled.")
print("[ 2 ] I know the name(s) of the class(es) that I want to download from the Open Images Dataset.")
print("[ 3 ] I want to resume training the model I was working on.")
print("[ 4 ] I want to create models from my own custom weight files.")
print("[ 5 ] How do I label images for object detection?")
print("[ 6 ] What is the Open Images Dataset?")
print("[ 7 ] I want run my object detector on a test image.")
question_one = input("Enter one of the numbers above and press enter (CRTL + C to quit): ")

i_want_to_train_a_model = question_one == '1' or question_one == '2'

if i_want_to_train_a_model:
  print("\n[ 1 ] I want to train the model on my local computer.")
  print("[ 2 ] I want to train the model using Google CoLab.")
  question_two = input("Enter one of the numbers above and press enter (CRTL + C to quit): ")

  print("\n[ 3 ] I want to train with Yolo v3.")
  print("[ 4 ] I want to train with Yolo v4.")
  yolo_version = input("Enter one of the numbers above and press enter (CRTL + C to quit): ")

  if question_one == '1':
    data_location = "local"
  if question_one == '2':
    data_location = "cloud"
  if question_two == '1':
    training_location = "local"
  if question_two == '2':
    training_location = "cloud"

  os.chdir("./Scripts")
  os.system("python3 train-a-model.py " + data_location + " " + training_location + " " + yolo_version)

if question_one == '3':
  # run the code to resume training the model
  print("\n[ 3 ] I want to train with Yolo v3 (the version that you began training with).")
  print("[ 4 ] I want to train with Yolo v4 (the version that you began training with).")
  yolo_version = input("Enter one of the numbers above and press enter (q to quit): ")
  if yolo_version == '3' or yolo_version == '4':
    # may need ./darknet.exe for windows
    os.system("./darknet detector train data/obj.data cfg/yolov" + yolo_version + "-custom.cfg yolov" + yolo_version + "-obj_last.weights")

elif question_one == '4':
  os.chdir("./Scripts")
  os.system("python3 generate-tf-model.py")
  os.system("python3 generate-core-ml-model.py")


elif question_one == '5':
  print("Send to LabelImg Repo")


elif question_one == '6':
  print("Send to Open Images Dataset")


elif question_one == '7':
  path_to_image = input("Enter the file path to the image: ")
  print("\n[ 3 ] I want to train with Yolo v3 (the version that you began training with).")
  print("[ 4 ] I want to train with Yolo v4 (the version that you began training with).")
  yolo_version = input("Enter one of the numbers above and press enter: ")
  os.chdir("./Scripts/Functions-For-TensorFlow-and-TensorFlow-Lite-Model")
  # run the code to test the image

  # make sure the checkpoints/custom-416 file is there
  os.system("python3 detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov" + yolo_version + " --images " + path_to_image.rstrip())

# Question 3 - (Answered 1 & 1)
# start running the code to train a model locally from data I already have
# (Answered 1 & 2)
# start running the code to train a model on Google CoLab
# (Answered 2 & 1)
# start running the code to download images from open images dataset and train a model locally
# (Answered 2 & 2)
# start running code to download images from open images dataset and train on Google CoLab
