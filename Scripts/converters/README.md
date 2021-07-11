# Converters

## Convert Yolo to XML
In order to install and run this script you will only need two dependencies: Python version 3 or higher, and PIL.

PIL is a python based library that makes working with images much easier. PIL can be installed by running the following two commands:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

### Running the Yolo to XML Script
Once the dependencies are installed, change into the directory that holds the script.

The script will ask you for the path to the folder that holds both the images and .txt yolo format (these are expected to exist in the same folder).

It will also ask for the path to the class names. This file is usally named something like "classes.txt" or "obj.names"

On a mac, the easiest way of getting the file path is by dragging and droping the folder and file onto the terminal window when prompted for each.

Once the script has run, it will create a new folder in the same directory that holds the images that is called "XML". A new folder is created to prevent any issues where a program like "LabelImg" may have trouble firguring out what format to save any newly labeled images in.

Running the following command will run the script and from there, start converting your files:
```
python3 convert-yolo-to-xml.py
```


## Resize Images
In order to install and run this script you will only need two dependencies: Python version 3 or higher, and PIL.

PIL is a python based library that makes working with images much easier. PIL can be installed by running the following two commands:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

If you want to resize your images to save on storage space or speed up load times while using online GPU solutions like CoLab. You can use this script to shrink the size of the image, all while keeping the correct aspect ratios so that images aren't distorted. It will also automatically convert all the files that are run through this script to a ".jpeg" format.

This will ask you for the folder containing the images you want to resize (it is best if they are first copied into a new folder from the original images, incase you decide you still want to use the full scale images at some point down the road).

The next thing it will ask you for is the maximum size (in pixels) that you want to images to be. Note, the aspect ratio will be kept so that the images don't look distorted.

Running the following command will run the script and from there, start converting your files:
```
python3 resize-images.py
```
