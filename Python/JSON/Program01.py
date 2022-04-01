# Create a class Vehicle with properties name, engine, and price. Create a vehicle object and convert it into JSON and vice-versa.
import json

class Vehicle:

    def __init__(self,name,engine,price):
        self.name = name
        self.engine = engine
        self.price = price

object = Vehicle("Car","Diesel engine","200000")

# JSON 
json_obj = json.dumps(object.__dict__)
print(json_obj)
print(type(json_obj))
print()

# DICTIONARY
dict_obj = json.loads(json_obj)
print(dict_obj)
print(type(dict_obj))