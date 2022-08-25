"""This script sends a HTTP POST request with the contents of dictionary as a JSON as payload"""
#The lab itself had a script that  would post the feedbacks on a separate webpage after POST request was made to http://(lab_url)/feedback
#It could be completed by just doing the request during the convert_to_dictionary function as it would iteratively send the request as each file is opened.

import os
import requests
import re

input_folder = "feedback_texts"
dictionary_keys =["title", "name", "date", "feedback"]
regex_pattern = r'[0-9]*.txt'                                     #Done to exclude any files that do not have the appropriate naming convention.
default_url = "https://httpbin.org/post"

def convert_to_dictionary():
    for path in os.listdir(input_folder):
        file_location = os.path.join(input_folder, path)
        if os.path.isfile(file_location) and re.match(regex_pattern, path) is not None:
            dictionary = {}
            i = 0
            f = open(file_location, "r")
            content = f.readlines()
            for element in dictionary_keys:
                dictionary[element] = content[i].strip()
                i+=1
            print(dictionary)
            return dictionary

def send_post(dictionary):
    response = requests.post(default_url, json = dictionary)      #Sends the post request with the input dictionary as a JSON
    print(response.status_code)
    print(response.request.url)
    print(response.request.body)

def change_default_folder_settings():
    print("Would you like to change the input folder?(yes/no):")  #Can be improved as it currently does not check if the file path is valid. 
    answer = str(input())
    if answer.lower() == "yes":
        print("Please input the full folder path:")
        folder_path = str(input())
    elif answer.lower() == "no":
        folder_path = input_folder
    else:
        change_default_folder_settings()
    return folder_path

def change_default_url_settings():
    print("Would you like to change the default URL?(yes/no):")
    answer = str(input())
    if answer.lower() == "yes":
        print("Please input the URL: ")
        url_path = str(input())
    elif answer.lower() == "no":
        url_path = default_url
    else:
        change_default_url_settings()
    return url_path

print("Would you like to change any of the script settings?(yes/no)")
answer = str(input())
if answer.lower() == "yes":
    input_folder = change_default_folder_settings()
    default_url = change_default_url_settings()
    send_post(convert_to_dictionary())
elif answer.lower() == "no":
    send_post(convert_to_dictionary())
else: 
    print("No appropriate answer!")
    exit()




