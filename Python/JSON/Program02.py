# Write a code to load a .json file and print JSON data. Display error if a file is empty or data is not in a json format

import json
import os

try:
    split_tup = os.path.splitext('JSON/File.json')
    file_extension = split_tup[1]
    if file_extension != '.json':
        raise FileNotFoundError
    elif os.stat('JSON/File.json').st_size == 0:
        raise FileNotFoundError
    else:
        with open("JSON/File.json",'r') as file :
            data = json.load(file)
            print(data)
except FileNotFoundError:
    print("Error occurred ")