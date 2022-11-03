#!/usr/bin/env python3

import os
from PIL import Image
import re

directory_path = os.path.abspath(os.getcwd())
destination_path = "supplier-data/images"
full_destination = os.path.join(directory_path, destination_path)
pattern = r"(\w*).tiff"

#print(full_destination)
#print(type(full_destination))

def process_images():
    for root, dirs, files in os.walk(destination_path):
        for filename in files: 
            found_pattern = re.match(pattern, filename)
            full_path = os.path.join(destination_path, filename)
            if found_pattern:
                im = Image.open(full_path)
                new_im = im.resize((600,400)).convert("RGB")
                new_filename = found_pattern[1]+".jpeg"
                full_destination =  os.path.join(destination_path, new_filename)
                new_im.save(full_destination)

process_images()
