#!/usr/bin/env python
###https://regex101.com/
import re

text = "13/Feb/2019 blah blah 01/Nov/2020 blah"
phone = "2004-959-559 # This is Phone Number"

a="""
https://regex101.com/

text = "13/Feb/2019 blah blah 01/Nov/2020 blah"
phone = "2004-959-559 # This is Phone Number"
#########################################
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
#########################################
# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
#### re.match ###########################
if re.match(r'\d+/[a-zA-Z]+/\d{4}', text):
    print("Found")
else:
    print("Not Found")
#### re.findall #########################
found = re.findall(r'(\d+/[a-zA-Z]+/\d{4})', text)
"""
print(a)
print("OUTPUT:\n")
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)
print()
print("############ re.findall ##############")
found = re.findall(r'(\d+/[a-zA-Z]+/\d{4})', text)
print(found)
print("############ re.match ################")
if re.match(r'\d+/[a-zA-Z]+/\d{4}', text):
    print("Found")
else:
    print("Not Found")

