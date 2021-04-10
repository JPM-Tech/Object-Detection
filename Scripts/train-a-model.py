import fileinput
import os
import sys
import pathlib

data_located_at = sys.argv[1]
training_to_be_done = sys.argv[2]
yolo_version = sys.argv[3]

if data_located_at == 'local':
  # Create files from my own data
  print("\nEnter a name of an object from your classes.txt (that should be in the same folder as the labeled images), then")
  while True:
    entry = input("\nObject Name (d for done): ")
    if entry.lower() == 'd' or entry.lower == '':
      break
    class_list.append(entry)

  print("\nEnter the file path to the folder that holds the images and labels used for training")
  training_folder = input("Training Path: ").rstrip()

  print("\nEnter the file path to the folder that holds the images and labels used for validation")
  validation_folder = input("Validation Path: ").rstrip()

  if training_to_be_done == 'local':
    print("Looking for Dakrnet model...")
    darknet_folder_path = Path("./Scripts/darknet")
    if darknet_folder_path.exists():
      print("Found Darknet yolo model")
    else:
      print("Downloading Darknet yolo model...")
      os.system("python3 download-and-build-darknet.py")

  # create obj.names file
  os.chdir("../upload_these_files_to_google_drive")
  print("Creating obj.names file")
  with open('obj.names', 'w') as f:
    for each_key in class_list:
      f.write(each_key + "\n")
  os.chdir("../Scripts")
  
  os.system("python3 create-files-from-my-own-data.py " + str(len(class_list)) + " " + training_folder + " " + validation_folder)

# ************
# GET DATA FROM CLOUD
# ************
if data_located_at == 'cloud':
  class_list = []
  final_class_name = []
  combined_file_name = ""

  print("\nEnter a name of an object from the Open Images Dataset that you want to download, then")
  print("enter a name that will be used to display results (NO SPACES), then press Enter to continue")
  while True:
    entry = input("\nObject Name (q to quit): ")
    if entry.lower() == 'q' or entry.lower == '':
      break
    temp = input("Display Name (q to quit): ")
    if temp.lower() == 'q' or temp.lower == '':
      break
    final_class_name.append(temp)
    class_list.append(entry)

  print("\nThis will automatically download a validation set of images that is 20 percent of the number of training files")
  max_number_of_training_files = input("How many training files would you like to download: ")
  max_number_of_validation_files = int(int(max_number_of_training_files) * .2)

  #move into OIDv4_ToolKit
  os.chdir("OIDv4_ToolKit")

  # Create a classes.txt file
  with open('classes.txt', 'w') as f:
    for each_key in class_list:
      f.write(each_key + "\n")
  
  #move into the folder where we will store all the files that will be uploaded to google drive
  os.chdir("../../upload_these_files_to_google_drive")

  print("Creating obj.names file")
  with open('obj.names', 'w') as f:
    for each_key in final_class_name:
      f.write(each_key + "\n")

  combined_file_name = "_".join(class_list)
