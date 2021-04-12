import os
import sys
import coremltools
# import tensorflow

path_to_tf_model = input("Enter the directory path to the TensorFlow Model (the folder containing the .pb file): ")

print("Creating TensorFlow Model")
mlmodel = coremltools.convert(path_to_tf_model.rstrip())

mlmodel.save(path_to_tf_model.rstrip() + ".mlmodel")

print("CoreML model created successfully")
