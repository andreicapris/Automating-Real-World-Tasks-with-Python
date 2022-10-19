#!/usr/bin/env python3

import os
import requests
import re
import json #requests might not work without this

directory_path = os.path.abspath(os.getcwd())
image_path = "supplier-data/images"
text_path = "supplier-data/descriptions"
im_fp = os.path.join(directory_path, image_path)
txt_fp = os.path.join(directory_path, text_path)

default_url = "http://[replace_with_lab_ip_address]/fruits/"

dictionary_keys = ["name", "weight", "description", "image_name"]

im_pattern = r"(\w)*.jpeg"
txt_pattern = r"(\w)*.txt"

def get_image_name():
    im_list = []
    for root, dirs, files in os.walk(im_fp):
        for filename in files:
            if re.match(im_pattern, filename):
                im_list.append(filename)
    return im_list

def get_text_inf(path):
    txt_list = []
    with open(path) as file:
    for line in file.readlines():
        if line.strip() != '' #two of the descriptions have a newline at the end of the file that causes the list to not be properly generated
            txt_list.append(line.strip())
    return txt_list

def add_im_to_txt_list(im_list, txt_list, filename):
    for element in im_list:
        if int(re.match(im_pattern, element)[1] == int(re.match(txt_pattern, filename)[1]):
            txt_list.append(element)
    return txt_list

def convert_to_dict(filename):
    result_dict = {}
    i = 0
    pattern = r"[0-9]"
    im_list = get_image_name()
    tmp_fp = os.path.join(txt_fp, filename)
    tmp_list = get_text_inf(tmp_fp)
    txt_list = add_im_to_txt_list(im_list, tmp_list, filename)
    for element in dictionary_keys:
        result_dict[element] = txt_list[i]
        if element == "weight":
            result_dict[element] = int(re.match(pattern, txt_list[i])
        i+=1
    return result_dict

def send_post():
    for root, dirs, files in os.walk(txt_fp):
        for filename in files:
            dict = convert_to_dict(filename)
            response = requests.post(default_url, json = dict)
            response.raise_for_status()
            print(response.request.url)
            print(response.status_code)

send_post()
