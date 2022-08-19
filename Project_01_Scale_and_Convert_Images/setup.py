"""This script will turn the files 90 degrees in case you want to use a different sample set"""
import os
from PIL import Image

def get_files():
    #Get the absolute path of the working directory as PIL seems to need it
    directory_path = os.path.abspath(os.getcwd())
    directory = 'SampleImages'
    #Pass through all the files in the SampleImages folder
    for root, dirs, files in os.walk(directory):
        for filename in files:
            full_location = os.path.join(directory_path, root, filename)
            im = Image.open(full_location)
            #Rotate the image with -90 degrees so that when the main script is applied the images are correctly shown
            new_im = im.rotate(-90, expand=True)
            new_im.save(full_location)

get_files()
