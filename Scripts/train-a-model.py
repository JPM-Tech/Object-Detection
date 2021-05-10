import fileinput
import os
import sys

data_located_at = sys.argv[1]
training_to_be_done = sys.argv[2]
yolo_version = sys.argv[3]
class_list = []
final_class_name = []
combined_file_name = ""

if data_located_at == 'local':
  # Create files from my own data
  print("\nEnter a name of an object from your classes.txt (that should be in the same folder as the labeled images)")
  while True:
    entry = input("Object Name (d for done): ")
    if entry.lower() == 'd' or entry.lower == '':
      break
    class_list.append(entry)

  print("\nEnter the file path to the folder that holds the images and labels used for training")
  training_folder = input("Training Path: ").rstrip()

  print("\nEnter the file path to the folder that holds the images and labels used for validation")
  validation_folder = input("Validation Path: ").rstrip()

# ************
# We need to check all the images and make sure that they are *.jpg since that is the only file that CoLab can use to create a model
# ************


  print("Installing required dependencies")
  os.system("pip install -r requirements.txt")

  if training_to_be_done == 'local':
    print("Checking for Dakrnet yolo weights file...")
    if os.path.exists("darknet/yolov3.weights") || os.path.exists("darknet/yolov4.weights"):
      print("Found Darknet yolo model")
    else:
      print("Downloading Darknet yolo weights...")
      os.system("python3 download-and-build-darknet.py")

  # create obj.names file
  os.chdir("../upload_these_files_to_google_drive")
  print("Creating obj.names file")
  with open('obj.names', 'w') as f:
    for each_key in class_list:
      f.write(each_key + "\n")

  os.chdir("../Scripts")
  os.system("python3 create-files-from-my-own-data.py " + str(len(class_list)) + " " + training_folder + " " + validation_folder + " " + yolo_version)

# ************
# GET DATA FROM CLOUD
# ************
if data_located_at == 'cloud':
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

  if training_to_be_done == 'local':
    print("Checking for Dakrnet yolo weights file...")
    if os.path.exists("darknet/yolov3.weights") || os.path.exists("darknet/yolov4.weights"):
      print("Found Darknet yolo model")
    else:
      print("Downloading Darknet yolo weights...")
      os.system("python3 download-and-build-darknet.py")

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

  os.chdir("../Scripts")
  os.system("python3 collect-data-from-Googles-Open-Images-Dataset.py " + str(len(class_list)) + " " + str(max_number_of_training_files) + " " + str(max_number_of_validation_files) + " " + combined_file_name + " " + yolo_version)


print("\n\nPre-Processing Script Complete\n\n")


if training_to_be_done == 'local':
  print("insert local training script here")
  # os.system("python3 generate-tf-model.py")
  # os.system("python3 generate-core-ml-model.py")

if training_to_be_done == 'cloud':
  if data_located_at == 'local':
    print("use the following link to open the Notebook in Google CoLab")
    print("") # add link here to colab notebook for use with locally gathered data
    print("Remember before running a new CoLab notebook, go to Edit, then Notebook Settings, then Hardware Accelleration, and select GPU, then click Save.")
  if data_located_at == 'cloud':
    print("use the following link to open the Notebook in Google CoLab")
    print("") # add link here to colab notebook for use with data gathered from Open Images Dataset