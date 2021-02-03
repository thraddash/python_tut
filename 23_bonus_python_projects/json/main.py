#!/usr/bin/env python

import json

x = '{"first_name": "John", "last_name": "Doe", "age": "30"}'

my_json = json.loads(x) # json.loads() convert JSON to dictionary

a = my_json["first_name"]
b = my_json["last_name"]
c = my_json["age"]
print("############## json.loads convert JSON to dictionary #################")
print(a, b, c)
print("############## json.dumps convert dictionary to JSON #################")
r = {'first_name': 'John', 'last_name': 'Wick'}
json_data = json.dumps(r) # json.dumps convert dictionary to JSON 
print(json_data)
print("############## json.dumps(x, indent = 4) indents using 4 spaces ######")

json_data = json.dumps(r, indent = 4)
print(json_data)
