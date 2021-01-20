#!/usr/bin/env python
a="""
########################################
## JSON Data Encode and Decode
########################################
"""
print(a)
import json

data = {
    'name' : 'Bill',
    'age'  : 55,
    'country' : 'US',
    'is_retired' : True
}

json_encoded_str = json.dumps(data)
print("### true lower case after encode into json ###")
print(json_encoded_str)
print()

json_decode = json.loads(json_encoded_str)
print("### True is uppercase after decoding back into python format ###")
print(json_decode)
