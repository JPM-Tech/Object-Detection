import argparse
import fileinput
import os
import sys
import pathlib

parser = argparse.ArgumentParser()
# parser.add_argument("--optional_value_one_from_cmd", help="text for when someone runs --help")
# parser.add_argument("required_value_one_from_cmd", help="text for when someone runs --help")
parser.add_argument("data_located_at", help="text for when someone runs --help")
parser.add_argument("training_to_be_done", help="text for when someone runs --help")
parser.add_argument("using_yolo_v", help="text for when someone runs --help")

args = parser.parse_args()
# print(args.required_value_one_from_cmd)

if args.data_located_at == 'local':
  # Create files from my own data
  print("\nEnter a name of an object from your classes.txt (that should be in the same folder as the labeled images), then")
  while True:
    entry = input("\nObject Name (q to quit): ")
    if entry.lower() == 'q' or entry.lower == '':
      break
    class_list.append(entry)

  print("\nEnter the file path to the folder that holds the images and labels used for training")
  training_folder = input("Training Path: ").rstrip()

  print("\nEnter the file path to the folder that holds the images and labels used for validation")
  validation_folder = input("Validation Path: ").rstrip()

  print("Looking for Dakrnet model...")
  darknet_folder_path = Path("./Scripts/darknet")
  if darknet_folder_path.exists():
    print("Found Darknet yolo model")
  else:
    print("Downloading Darknet yolo model...")
    os.system("python3 build-darknet.py")
  
  os.system("python3 create-files-from-my-own-data.py class_list_length " + str(len(class_list)) + " training_folder_path " + training_folder + " validation_folder_path " + validation_folder)
