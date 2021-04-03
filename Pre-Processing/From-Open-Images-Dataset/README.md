# Creating An Object Detection Model Using Images From Googles Open Images Dataset

If you want to view what is available from the Open Images Dataset, you can view their images from the following link:
```
https://storage.googleapis.com/openimages/web/visualizer/index.html?set=train&type=detection
```

Once you know the specific tags/classes that you want to use to train an object detection model on, then we are ready to start.

## Step 1. Download this repo
Once the repo is downloaded to your local machine, use your terminal to "cd" into the repos location on your computer.
**Hint**
If you use a Mac, type
```
cd
```
into the terminal, then drag and drop the folder for the repo onto the terminal
**Hint**

## Step 2. Run the script
In your terminal, run the following command
```
python3 collect-data-from-Googles-Open-Images-Dataset.py
```

It will ask you for the class name from the Open Images Dataset (Object Name), followed by the name that will be displayed in your model once the detector has been trained (Display Name).

**IMPORTANT!**
The Display Name cannot have spaces or special characters in it!
**IMPORTANT!**

Once you have entered all the name of the objects you want to detect in your model, the script will ask how many images you want to using for training. It will automatically download the images needed to validate how the training is running.

This process can take a while, so please be patient while the images are downloading.

Once the pre-processing steps are complete, a message will appear in the terminal that says
```
Pre-Processing Script Complete
```

The following files will be created that you will need to train your model using Googles CoLab
```
generate_train.py
generate_test.py
obj.data
obj.names
obj.zip
test.zip
yolov4-obj.cfg
```

They will be available in a folder under the root directory for this repo named
```
upload_these_files_to_google_drive
```

We are now ready to move to the next section:
[Training a model with CoLab](https://github.com/JPM-Tech/Object-Detection/tree/master/Training/Train-a-model-with-CoLab)
