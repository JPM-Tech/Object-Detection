# Training a Model with CoLab
## Step 1: Setup your google drive to be ready to train your model
Open Google Drive
Once in your main google drive folder, create a new folder named
```
yolov4
```

Inside the "yolov4" folder, create another folder named
```
backup
```

Then drag and Drop the files from your local folder 
```
upload_these_files_to_google_drive
```
into the folder on Google Drive named
```
yolov4
```

## Step 2. Add the CoLab Notebook into your CoLab Session
You can use the Notebook linked [here](https://colab.research.google.com/github/JPM-Tech/Object-Detection/blob/main/Training/Train-a-model-with-CoLab/Notebook-to-be-used-in-Google-CoLab.ipynb) that has been setup to train an object detection model.

## Step 3: Enable GPU Training
In the CoLab Menu:
Click "Edit"
Then "Notebook Settings" 
Under "Hardware" select "GPU", Then click "Save"

## Step 4: Run All
In the CoLab Menu:
Click "Runtime"
Then "Run All"
The following steps will automatically take place in the notebook

## Google CoLab Code
In case you want to view the code before using the notebook, the following is a copy of the code used in the CoLab Notebook. The Notebook can be found [here](https://colab.research.google.com/github/JPM-Tech/Object-Detection/blob/main/Training/Train-a-model-with-CoLab/Notebook-to-be-used-in-Google-CoLab.ipynb).

```py
#clone darknet repo
!git clone https://github.com/AlexeyAB/darknet

#change makefile to have GPU and OPENCV enabled
%cd darknet
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile
!sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

#verify CUDA
!/usr/local/cuda/bin/nvcc --version

#make darknet (builds darknet so that you can then use the darknet executable file to run or train object detectors)
!make

#get pretrained weights for darknet for Yolov4
!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights

#define helper functions
def imShow(path):
  import cv2
  import matplotlib.pyplot as plt
  %matplotlib inline

  image = cv2.imread(path)
  height, width = image.shape[:2]
  resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  plt.axis("off")
  plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
  plt.show()

#use this to upload files
def upload():
  from google.colab import files
  uploaded = files.upload() 
  for name, data in uploaded.items():
    with open(name, 'wb') as f:
      f.write(data)
      print ('saved file', name)

#use this to download a file  
def download(path):
  from google.colab import files
  files.download(path)

#run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights data/person.jpg

#show image using our helper function
imShow('predictions.jpg')

#mount Your Google Drive into the CoLab Virtual Machine and Prepare Google Drive Environment
%cd ..
from google.colab import drive
drive.mount('/content/gdrive')

#this creates a symbolic link so that now the path /content/gdrive/My\ Drive/ is equal to /mydrive
!ln -s /content/gdrive/My\ Drive/ /mydrive
!ls /mydrive

#cd back into the darknet folder to run detections
%cd darknet

#copy over the data from google drive into the directory of the Colab VM
!cp /mydrive/yolov4/obj.zip ../
!cp /mydrive/yolov4/test.zip ../
!cp /mydrive/yolov4/yolov4-obj.cfg ./cfg
!cp /mydrive/yolov4/obj.names ./data
!cp /mydrive/yolov4/obj.data  ./data
!cp /mydrive/yolov4/generate_train.py ./
!cp /mydrive/yolov4/generate_test.py ./

#unzip the datasets and their contents so that they are now in /darknet/data/ folder
!unzip ../obj.zip -d data/
!unzip ../test.zip -d data/

#create the path names to the training and testing images
!python generate_train.py
!python generate_test.py

# verify that the newly generated files train.txt and test.txt are listed below
!ls data/

#Download pretrained weights for the convolutional layers of darknet
COPY THIS FILE TO MY REPO
!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137

# train your custom detector! (uncomment %%capture below if you run into memory issues or your Colab is crashing)
# %%capture
!./darknet detector train data/obj.data cfg/yolov4-obj.cfg yolov4.conv.137 -dont_show -map
```
