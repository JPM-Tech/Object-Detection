# Creating An Object Detection Model Using Images That I Collected And Labeled Myself

First things first, make sure the labels are in the correct Yolo format.
The label file should look similar the following example for our example image:
IMG_1234.txt
```
0 0.222470 0.349206 0.059524 0.039683
```

Next move the files that you will use for training into a folder named
```
obj
```
(this should include the images and corresponding label files)

Then move 20% to 30% of the images from the training folder into another folder named
```
train
```
(this should include the images and corresponding label files)

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
python3 create-files-from-my-own-data.py
```

It will ask you for the class name that are in your data set (Object Name).

**IMPORTANT!**
The Object Name cannot have spaces or special characters in it!
(I Assume you know that if you are labeling your own data)
**IMPORTANT!**

After the classes have been entered, it will ask you for the path to the folders holding the training images and labels.
This should look something like
```
C:/users/yourusername/otherfolders/training
```

Then it will ask you to enter the path to the images and labels that will be used for validation

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
