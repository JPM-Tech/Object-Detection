
import os
import shutil


folder_holding_images = input("Enter the path to the folder holding both the training and test image folders: ").replace("'", "").strip()
folder_holding_training_images = folder_holding_images + os.sep + 'train'
folder_holding_testing_images = folder_holding_images + os.sep + 'test'

# Create zip for training
shutil.make_archive(folder_holding_images + os.sep + 'train', "zip", folder_holding_training_images)

# Create zip for testing
shutil.make_archive(folder_holding_images + os.sep + 'test', "zip", folder_holding_testing_images)
