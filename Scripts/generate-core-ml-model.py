import os
import sys
import coremltools

path_to_tf_model = input("Enter the directory path to the TensorFlow Model (the folder containing the .pb file): ").rstrip()
# path_to_tf_model = "Functions-For-TensorFlow-and-TensorFlow-Lite-Model/checkpoints/custom-416"

print("Creating CoreML Model")
mlmodel = coremltools.convert(path_to_tf_model, source="tensorflow")

print("Saving CoreML Model")
mlmodel.save(path_to_tf_model + ".mlmodel")

print("CoreML model created successfully")
