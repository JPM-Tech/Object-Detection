import os
import sys
import coremltools

path_to_tf_model = input("Enter the directory path to the TensorFlow Model (a .pb file): ")

print("Installing required dependencies")
os.system("pip install coremltools")

print("Creating TensorFlow Model")
# from example converting a TensorFlow v2 model:
# import tensorflow
# tf_model = tf.keras.applications.MobileNet()
# mlmodel = coremltools.convert(tf_model)

# from example converting a TensorFlow v1 model:
# import tensorflow
# mlmodel = coremltools.convert("mobilenet_frozen_graph.pb")

# Adding Model Info
# mlmodel.short_description = "short description of model"
# mlmodel.license = "Apache 2.0"
# mlmodel.author = "Name of the author"
# mlmodel.save("mobilenet.mlmodel")

mlmodel = coremltools.convert(path_to_tf_model.rstrip())

filename_name, f_ext = os.path.splitext(os.path.basename(path_to_tf_model.rstrip()))

mlmodel.save(os.getcwd() + os.path.sep + filename_name + ".mlmodel")

print("CoreML model created successfully")
print("Opening folder to stored model...")
