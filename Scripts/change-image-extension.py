import os
from PIL import Image
import sys

# 
# This will take in a folder of images and resize all the images in that folder to where
# the largest side of the image is the max size that the user entered
# 
# This script is seperate from the other object detect scripts, however, it could be useful when trying to shrink image
# size to reduce memory usage
# 

print("Enter the path to the folder containing the images you want to update")
folder_holding_orig_images = input("Path: ").replace("'", "").strip()
new_extension = input("Enter the new extension type for the image (ex: jpg): ")

folder_for_resized_images = "new_" + new_extension + "_images"
os.chdir(folder_holding_orig_images)
os.mkdir(folder_for_resized_images)

print("Updating image extensions, this may take a while, enjoy some quiet time while you wait...")
for each_image_file in os.listdir(folder_holding_orig_images):
  if each_image_file.endswith("jpg") or each_image_file.endswith("jpeg") or each_image_file.endswith("png"):
    orig_img = Image.open(each_image_file)
    img_filename, img_fileext = os.path.splitext(each_image_file)
    new_file_path = os.path.join(folder_for_resized_images, each_image_file)

    orig_img.save(folder_for_resized_images + os.path.sep + img_filename + "." + new_extension)

print("Image update complete")