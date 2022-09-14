from email_sales import *
import os
import json


json_folder="sample_json"
json_file="car_sales.json"
json_path=os.path.join(json_folder, json_file)

#Opens the json and creates a list of dictionaries based on it.
def json_to_dict(in_path):
    with open(in_path, 'r') as in_json:
        json_dict = json.load(in_json)
    return json_dict

#Computes the car that generated the most revenue. 
def max_revenue(in_dict):
    max = 0
    for element in in_dict:
        convert_price = float(element['price'].replace('$', '')) #Converts the price from string to float and removes $ sign.
        revenue = element['total_sales']*convert_price
        if revenue > max:
            most_revenue = element
            max = revenue
    return most_revenue, max           #Returns a tuple first element is a dictionary and the second is a float containing most revenue value.

#For debugging purposes
#print(max_revenue(json_to_dict(json_path)))  

#Computes which car had the most number of sales.
def most_sales_units(in_dict):
    max = 0
    for element in in_dict:
        if element['total_sales'] > max:
            max = element['total_sales']
            max_element = element
    return max_element                 #Returns a dictionary

#For debugging purposes
#print(most_sales_units(json_to_dict(json_path)))

#Computes the year with the most car sales.
def most_popular_year(in_dict):
    popularity_dict = {}               #This dictionary is used to contain the year as key and units sold as value.
    max = 0
    
    for element in in_dict:            #Iterates through the list of cars
        if element['car']['car_year'] not in popularity_dict:                       #If the key is not present add a new element to the dictionary.
            popularity_dict[element['car']['car_year']] = element['total_sales']
        else:                                                                       #Else add the new unit number to the one already present.
            popularity_dict[element['car']['car_year']] += element['total_sales']

    for element in popularity_dict:    #Check which year had the most sales.
        if popularity_dict[element] > max:
            max = popularity_dict[element]
            best_year = element
    return best_year, max              #Returns a tuple

#For debugging purposes
#print(most_popular_year(json_to_dict(json_path)))

def to_summary():
    most_revenue = max_revenue(json_to_dict(json_path))
    print(type(most_revenue[0]))
    print(type(json_to_dict(json_path)))
    first_string = "The {} {} generated the most revenue: {}".format(most_revenue[0]['car']['car_make'], most_revenue[0]['car']['car_model'], most_revenue[1])
    print(first_string)

    most_sales = most_sales_units(json_to_dict(json_path))
    second_string = "The {} {} ({}) had the most sales: {}".format(most_sales['car']['car_make'], most_sales['car']['car_model'], most_sales['car']['car_year'], most_sales['total_sales'])
    print(second_string)

    best_year_units = most_popular_year(json_to_dict(json_path))
    third_string = "The most popular year was {} with {} sales.".format(best_year_units[0], best_year_units[1])
    print(third_string)
to_summary()
