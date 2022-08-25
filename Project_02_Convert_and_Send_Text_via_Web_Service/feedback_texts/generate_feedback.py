import os
import sys

def generate_file():
    input_file = ""
    try:
        input_file = sys.argv[1]
        print(input_file)
        print(type(input_file))

    except:
        print("There is no CSV as input for the script.")
        if len(os.listdir()) < 10:
            filename = "00" + str(len(os.listdir())-1) + ".txt"
        elif len(os.listdir()) < 100 and len(os.listdir()) >= 10:
           filename = "0" + str(len(os.listdir())-1) +".txt"
        else:
           filename = str(len(os.listdir())-1) + ".txt"
        print("Please enter manual values:")
        print(filename)


generate_file()
