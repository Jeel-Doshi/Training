# Write a code to load a .json file and print JSON data. Display error if a file is empty or data is not in a json format

import json

try:
    with open("JSON/File.json",'r') as file :
        data = json.load(file)
        print(data)

except Exception :
    print("Error occurred ")