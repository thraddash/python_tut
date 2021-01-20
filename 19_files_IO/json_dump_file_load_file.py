#!/usr/bin/env python

a="""
#####################################################
# Dumping data in file and load from file
# write dictionary as json format to json_data.json
#####################################################
import json

data = {
    'name' : 'Rob',
    'age'  : 25,
    'country' : 'US',
    'is_retired' : False
}

with open('json_data.json', 'w') as fobj:
	json.dump(data, fobj)
"""
print(a)

import json

data = {
    'name' : 'Rob',
    'age'  : 25,
    'country' : 'US',
    'is_retired' : False
}

with open('json_data.json', 'w') as fobj:
	json.dump(data, fobj)

b="""
############################################
Read json_data.json file

with open('json_data.json', 'r') as fobj:
    json_data = json.load(fobj)
    print(json_data)
############################################
"""
print(b)

with open('json_data.json', 'r') as fobj:
    json_data = json.load(fobj)
    print(json_data)
