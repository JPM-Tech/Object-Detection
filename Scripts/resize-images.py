import os
from PIL import Image
import sys

print("Enter the path to the folder containing the images you want to re-size")
folder_holding_orig_images = input("Path: ").replace("'", "").strip()
max_size = int(input("Enter the max pixel size of the image (ex: 1024): "))

folder_for_resized_images = "new_" + str(max_size) + "_images"
os.chdir(folder_holding_orig_images)
os.mkdir(folder_for_resized_images)

print("Updating image sizes, this may take a while, enjoy some quiet time while you wait...")
for each_image_file in os.listdir(folder_holding_orig_images):
  if each_image_file.endswith("jpg") or each_image_file.endswith("jpeg") or each_image_file.endswith("png"):
    orig_img = Image.open(each_image_file)
    new_file_path = os.path.join(folder_for_resized_images, each_image_file)
    aspect_ratio = orig_img.width / orig_img.height

    if orig_img.width > orig_img.height:
      new_width = max_size
      new_height = int(new_width / aspect_ratio)
    if orig_img.height > orig_img.width:
      new_height = max_size
      new_width = int(new_height * aspect_ratio)

    new_image = orig_img.resize((new_width, new_height))

    new_image.save(new_file_path)

print("Image size update complete")