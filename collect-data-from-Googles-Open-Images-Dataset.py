import fileinput
import os
import re
import sys
import shutil

class_list = []
final_class_name = []
combined_file_name = ""
upload_to_google_folder_path = "upload_these_files_to_google_drive"
new_filter_number = 0
new_class_number = 0

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

combined_file_name = "_".join(class_list)

print("Installing required dependencies")
os.system("pip install -r requirements.txt")

print("Downloading Training images from Open Images Dataset. This may take a while, just be patient.")
os.system("python3 main.py downloader --classes classes.txt --type_csv train --limit " + max_number_of_training_files + " --multiclasses 1")
print("Downloading Validation images from Open Images Dataset. This may take a while, just be patient.")
os.system("python3 main.py downloader --classes classes.txt --type_csv validation --limit " + str(max_number_of_validation_files) + " --multiclasses 1")

print("Converting labels to the correct yolo format")
os.system("python3 convert_annotations.py")

# move back up into the main folder
os.chdir('..')

print("Creating zip files")
# Zip the image folders
# to_location, filetype, from_location
shutil.make_archive(upload_to_google_folder_path + "/obj", "zip", "OIDv4_ToolKit/OID/Dataset/train/" + combined_file_name)
shutil.make_archive(upload_to_google_folder_path + "/test", "zip", "OIDv4_ToolKit/OID/Dataset/validation/" + combined_file_name)

#move into the folder where we will store all the files that will be uploaded to google drive
os.chdir(upload_to_google_folder_path)

print("Creating obj.names file")
with open('obj.names', 'w') as f:
  for each_key in final_class_name:
    f.write(each_key + "\n")

print("Creating obj.data file")
with open('obj.data', 'w') as f:
  f.write("classes = " + str(len(class_list)) + "\n")
  f.write("train = data/train.txt\n")
  f.write("valid = data/test.txt\n")
  f.write("names = data/obj.names\n")
  f.write("backup = /mydrive/yolov4/backup\n")

new_class_number = len(class_list)
new_filter_number = (new_class_number + 5) * 3
max_batches = len(class_list) * 2000
if len(class_list) <= 3:
  max_batches = 6000

min_steps = int(max_batches * 0.8)
max_steps = int(max_batches * 0.9)
number_of_steps = str(min_steps) + "," + str(max_steps)

print("Creating config file ")
with open('yolov4-obj.cfg', 'w') as f:
  f.write("[net]\nbatch=64\nsubdivisions=16\nwidth=416\nheight=416\nchannels=3\nmomentum=0.949\ndecay=0.0005\nangle=0\nsaturation = 1.5\nexposure = 1.5\nhue=.1\nlearning_rate=0.001\nburn_in=1000\n")
  f.write("max_batches = " + max_batches + "\n")
  f.write("policy=steps\n")
  f.write("steps=" + number_of_steps + "\n")
  f.write("scales=.1,.1\n\nmosaic=1\n[convolutional]\nbatch_normalize=1\nfilters=32\nsize=3\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=3\nstride=2\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\nstride=1\npad=1\nactivation=mish\n[route]\nlayers = -2\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=32\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\nstride=1\n")
  f.write("pad=1\nactivation=mish\n[route]\nlayers = -1,-7\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=2\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\nstride=1\npad=1\nactivation=mish\n[route]\nlayers = -2\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=64\nsize=1\n")
  f.write("stride=1\npad=1\nactivation=mish\n[route]\nlayers = -1,-10\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=2\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n[route]\nlayers = -2\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\n")
  f.write("filters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\n")
  f.write("activation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=mish\n[route]\nlayers = -1,-28\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=2\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n[route]\nlayers = -2\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=256\n")
  f.write("size=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n")
  f.write("[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=mish\n[route]\nlayers = -1,-28\n[convolutional]\n")
  f.write("batch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=1024\nsize=3\nstride=2\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=mish\n[route]\nlayers = -2\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\n")
  f.write("batch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=mish\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=mish\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=3\nstride=1\npad=1\nactivation=mish\n\n[shortcut]\nfrom=-3\nactivation=linear\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=mish\n[route]\nlayers = -1,-16\n[convolutional]\nbatch_normalize=1\nfilters=1024\nsize=1\nstride=1\npad=1\nactivation=mish\nstopbackward=800\n\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=1024\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n\n[maxpool]\nstride=1\nsize=5\n[route]\nlayers=-2\n[maxpool]\nstride=1\nsize=9\n[route]\n")
  f.write("layers=-4\n[maxpool]\nstride=1\nsize=13\n[route]\nlayers=-1,-3,-5,-6\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=1024\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[upsample]\nstride=2\n[route]\nlayers = 85\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[route]\nlayers = -1, -3\n\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=512\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\n")
  f.write("pad=1\nfilters=512\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[upsample]\nstride=2\n[route]\nlayers = 54\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[route]\nlayers = -1, -3\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=256\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=256\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=128\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=256\nactivation=leaky\n[convolutional]\nsize=1\nstride=1\npad=1")
  f.write("filters=" + str(new_filter_number) + "\n")
  f.write("activation=linear\n[yolo]\nmask = 0,1,2\nanchors = 12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401\n")
  f.write("classes=" + str(new_class_number) + "\n")
  f.write("num=9\njitter=.3\nignore_thresh = .7\ntruth_thresh = 1\nscale_x_y = 1.2\niou_thresh=0.213\ncls_normalizer=1.0\niou_normalizer=0.07\niou_loss=ciou\nnms_kind=greedynms\nbeta_nms=0.6\nmax_delta=5\n[route]\nlayers = -4\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=2\npad=1\nfilters=256\nactivation=leaky\n[route]\nlayers = -1, -16\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=512\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=512\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=256\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=512\nactivation=leaky\n[convolutional]\nsize=1\nstride=1\npad=1\n")
  f.write("filters=" + str(new_filter_number) + "\n")
  f.write("activation=linear\n[yolo]\nmask = 3,4,5\nanchors = 12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401\n")
  f.write("classes=" + str(new_class_number) + "\n")
  f.write("num=9\njitter=.3\nignore_thresh = .7\ntruth_thresh = 1\nscale_x_y = 1.1\niou_thresh=0.213\ncls_normalizer=1.0\niou_normalizer=0.07\niou_loss=ciou\nnms_kind=greedynms\nbeta_nms=0.6\nmax_delta=5\n[route]\nlayers = -4\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=2\npad=1\nfilters=512\nactivation=leaky\n[route]\nlayers = -1, -37\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=1024\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=1024\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nfilters=512\nsize=1\nstride=1\npad=1\nactivation=leaky\n[convolutional]\nbatch_normalize=1\nsize=3\nstride=1\npad=1\nfilters=1024\nactivation=leaky\n\n[convolutional]\nsize=1\nstride=1\npad=1\n")
  f.write("filters=" + str(new_filter_number) + "\n")
  f.write("\nactivation=linear\n\n\n[yolo]\nmask = 6,7,8\nanchors = 12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401\n")
  f.write("classes=" + str(new_class_number) + "\n")
  f.write("num=9\njitter=.3\nignore_thresh = .7\ntruth_thresh = 1\nrandom=0\nscale_x_y = 1.05\niou_thresh=0.213\ncls_normalizer=1.0\niou_normalizer=0.07\niou_loss=ciou\nnms_kind=greedynms\nbeta_nms=0.6\nmax_delta=5\n")

print("\n\nPre-Processing Script Complete\n\n")
