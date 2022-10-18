#!/usr/bin/env python3

import requests
import os
import re

url = "http://localhost/upload/"
directory_path = os.path.abspath(os.getcwd())
folder_path = "supplier-data/images"
full_location = os.path.join(directory_path, folder_path)
pattern = r"(\w)*.jpeg"

for root, dirs, files in os.walk(full_location):
    for filename in files:
        if re.match(pattern, filename):
            #print(filename)
            full_filename = os.path.join(full_location, filename)
            with open(full_filename, 'rb') as opened:
                r = requests.post(url, files = {'file' : opened})
