import os
import sys
import shutil

combined_file_name = ""
upload_to_google_folder_path = "upload_these_files_to_google_drive"

class_list_length = sys.argv[1]
training_folder_path = sys.argv[2]
validation_folder_path = sys.argv[3]
yolo_version = sys.argv[4]

# moving back into repo root folder
# so that the zip files end up in the upload_to_google_folder_path
os.chdir("..")
print("Creating zip files")
# Zip the image folders
# to_location, filetype, from_location
shutil.make_archive(upload_to_google_folder_path + "/obj", "zip", training_folder_path)
shutil.make_archive(upload_to_google_folder_path + "/test", "zip", validation_folder_path)

# moving back into scripts folder so that the custom files can continue to be written
os.chdir("Scripts")
os.system("python3 create-custom-training-files.py " + class_list_length + " " + yolo_version)
