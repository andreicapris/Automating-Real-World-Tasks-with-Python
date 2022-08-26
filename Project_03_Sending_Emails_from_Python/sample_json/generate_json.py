"""This script modifies car_sales.json either by adding elements or rewriting the file as per the users desire"""
import os
import json


car_sales_key = ["id", "car", "price", "total_sales"]
car_key = ["car_make", "car_model", "car_year"]
car_sales_l = []

def add_or_restart_json():                                 #when adding it actually reads the current json and loads it as a dictionary, updates it and the rewrites the whole file
    global car_sales_l
    print("Would you like to add to the existing file or rewrite it?(add/new)")
    answer = str(input())
    if answer.lower() == "add":
        with open('car_sales.json', 'r') as car_json:
            car_sales_l = json.load(car_json)
            print("Current status of the dictionary:")
            print(car_sales_l)
            input_element()
    elif answer.lower() == "new":
        with open('car_sales.json', 'w') as car_json:
            input_element()
    else:
        print("No appropriate answer ending script")
        exit()

def create_dictionary():                                    #based on the 2 global lists it prompts the user to input every value for that particular key in order to create the appropriate dictionary
    car_sales_d = {}
    car_properties_d = {}
    for k in car_sales_key:
        if k == "car":
            print("Please input car properties:")
            for v in car_key:
                print( "{} = ".format(v))
                car_properties_d[v] = input()
                if car_properties_d[v].isdigit() and v == "car_year":
                    car_properties_d[v] = int(car_properties_d[v])
            car_sales_d['car'] = car_properties_d
        else:
            print("{} = ".format(k))
            car_sales_d[k] = input()
            if car_sales_d[k].isdigit() and (k == "id" or k == "total_sales"):
                car_sales_d[k] = int(car_sales_d[k])
    return car_sales_d

def input_element():                                        #user can add individual elements to the list of dictionaries no will end the script
    global car_sales_l
    print("Would you like to add a new element?(yes/no)")
    answer = str(input())
    if answer.lower() == "yes":
        car_sales_l.append(create_dictionary())
        print(car_sales_l)
        input_element()
    else:
        apply_changes()
        print(car_sales_l)
        exit()

def apply_changes():                                         #rewrites the json with either a new dictionary or with the updated one
    with open('car_sales.json', 'w') as car_json:
        json.dump(car_sales_l, car_json)

add_or_restart_json()
