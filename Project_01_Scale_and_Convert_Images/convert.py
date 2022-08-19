"""This script will rotate the images CCW 90 degrees and change the image resolution"""

import os
from PIL import Image

directory_path = os.path.abspath(os.getcwd())
sample_images = "SampleImages"
processed_images = "ProcessedImages"

def get_image_size():
    print("Please input the width and the height desired for the image. Please note that if the values are not positive integers you will be prompted to input them again")
    image_size = ()                                  # This is a tuple due to the fact that the .resize method accepts tuples as inputs.
    while True:
        print("Please input the desired width:")
        image_width = int(input())
        print("Please input the desired height:")
        image_height = int(input())
        if (image_width > 0) & (image_height > 0):   # This is an workaround to create a do-while sequence.
            break
    image_size = (image_width,image_height)
    return image_size


def rotate_and_change_resolution():
    change_image_size = input("Would you also like to change the image sizes(yes or no)?")
    if change_image_size == "yes":
        image_size = get_image_size()
    for root, dirs, files in os.walk(sample_images):
        root_destination = root.replace(sample_images, processed_images)                    # root_destination is used to copy the folder structure of the source folder
        for filename in files:
            full_location = os.path.join(directory_path, root, filename)
            full_destination = os.path.join(directory_path, root_destination, filename)
            folder_full_destination = os.path.join(directory_path, root_destination)
            is_exist = os.path.exists(folder_full_destination)                              # This checks if the folder structure is already present in the destination folder
            
            im = Image.open(full_location)
            new_im = im.rotate(90, expand=True)
            if change_image_size == "yes":                                                  # If the user does not want to also resize the pictures this prevents it
                new_im = im.resize(image_size)
            if not is_exist:
                os.makedirs(folder_full_destination)                                        # If the folder is not already present it will create it
            
            new_im.save(full_destination)

rotate_and_change_resolution()
