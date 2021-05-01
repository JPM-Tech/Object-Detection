import fileinput
import os
import re
import sys
import shutil

class_list_length = sys.argv[1]
max_number_of_training_files = sys.argv[2]
max_number_of_validation_files = sys.argv[3]
combined_file_name = sys.argv[4]
yolo_version = sys.argv[5]
upload_to_google_folder_path = "upload_these_files_to_google_drive"

# #move into OIDv4_ToolKit
os.chdir("OIDv4_ToolKit")

print("Downloading Training images from Open Images Dataset. This may take a while, just be patient.")
os.system("python3 main.py downloader --classes classes.txt --type_csv train --limit " + max_number_of_training_files + " --multiclasses 1")
print("Downloading Validation images from Open Images Dataset. This may take a while, just be patient.")
os.system("python3 main.py downloader --classes classes.txt --type_csv validation --limit " + max_number_of_validation_files + " --multiclasses 1")

print("Converting labels to the correct yolo format")
os.system("python3 convert_annotations.py")

# move back up into the main folder
os.chdir('../../')

print("Creating zip files")
# Zip the image folders
# to_location, filetype, from_location
shutil.make_archive(upload_to_google_folder_path + "/obj", "zip", "./Scripts/OIDv4_ToolKit/OID/Dataset/train/" + combined_file_name)
shutil.make_archive(upload_to_google_folder_path + "/test", "zip", "./Scripts/OIDv4_ToolKit/OID/Dataset/validation/" + combined_file_name)

# moving back into scripts folder so that the custom files can continue to be written
os.chdir("Scripts")
os.system("python3 create-custom-training-files.py " + class_list_length + " " + yolo_version)
