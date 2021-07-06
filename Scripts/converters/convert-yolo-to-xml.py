import os
import re
from PIL import Image

folder_holding_yolo_files = input("Enter the path to the yolo files: ").replace("'", "").strip()
# TODO: Make a func that compaires the number in the yolo file to the corresponding name from the obj.names file
object_name = 'license_plate'

def is_number(n):
  try:
    float(n)
    return True
  except ValueError:
    return False

os.mkdir('XML')

for each_yolo_file in os.listdir(folder_holding_yolo_files):
  if each_yolo_file.endswith("txt"):
    the_file = open(each_yolo_file, 'r')
    all_lines = the_file.readlines()

    # Check to see if there is an image that matches the txt file
    image_name = each_yolo_file.replace('txt', 'jpeg')
    if os.path.exists(image_name):
      orig_img = Image.open(image_name) # open the image
      image_width = orig_img.width
      image_height = orig_img.height

      # Start the XML file
      with open('XML' + os.sep + each_yolo_file.replace('txt', 'xml'), 'w') as f:
        f.write('<annotation verified="yes">\n')
        f.write('\t<folder>XML</folder>\n')
        f.write('\t<filename>' + image_name + '</filename>\n')
        f.write('\t<path>' + os.getcwd() + os.sep + image_name + '</path>\n')
        f.write('\t<source>\n')
        f.write('\t\t<database>Unknown</database>\n')
        f.write('\t</source>\n')
        f.write('\t<size>\n')
        f.write('\t\t<width>' + image_width + '</width>\n')
        f.write('\t\t<height>' + image_height + '</height>\n')
        f.write('\t\t<depth>3</depth>\n') # assuming a 3 channel color image (RGB)
        f.write('\t</size>\n')
        f.write('\t<segmented>0</segmented>\n')
      
      for each_line in all_lines:
        # regex to find the numbers in each line of the text file
        yolo_array = re.split("\s", each_line)

        # initalize the variables
        class_number = 0.0
        x_yolo = 0.0
        y_yolo = 0.0
        yolo_width = 0.0
        yolo_height = 0.0
        yolo_array_contains_only_digits = True

        # make sure the array has the correct number of items
        if len(yolo_array) == 5:
          for each_value in yolo_array:
            # If a value is not a number, then the format is not correct, return false
            if not is_number(each_value):
              yolo_array_contains_only_digits = False
          
          if yolo_array_contains_only_digits:
            # assign the variables
            class_number = int(yolo_array[0])
            x_yolo = float(yolo_array[1])
            y_yolo = float(yolo_array[2])
            yolo_width = float(yolo_array[3])
            yolo_height = float(yolo_array[4])

            # Description of Yolo Format values
            # 15 0.448743 0.529142 0.051587 0.021081
            # class_number x_yolo y_yolo yolo_width yolo_height

            # Convert Yolo Format to Pascal VOC format
            box_width = yolo_width * image_width
            box_height = yolo_height * image_height
            x_min = int(x_yolo * image_width - (box_width / 2))
            y_min = int(y_yolo * image_height - (box_height / 2))
            x_max = int(x_yolo * image_width + (box_width / 2))
            y_max = int(y_yolo * image_height + (box_height / 2))

            # write each object to the file
            f.write('\t<object>\n')
            f.write('\t\t<name>' + object_name + '</name>\n')
            f.write('\t\t<pose>Unspecified</pose>\n')
            f.write('\t\t<truncated>1</truncated>\n')
            f.write('\t\t<difficult>1</difficult>\n')
            f.write('\t\t<bndbox>\n')
            f.write('\t\t\t<xmin>' + x_min + '</xmin>\n')
            f.write('\t\t\t<ymin>' + y_min + '</ymin>\n')
            f.write('\t\t\t<xmax>' + x_max + '</xmax>\n')
            f.write('\t\t\t<ymax>' + y_max + '</ymax>\n')
            f.write('\t\t</bndbox>\n')
            f.write('\t</object>\n')

      # Close the annotation tag once all the objects have been written to the file
      f.write('</annotation>\n')
      f.close() # Close the file
