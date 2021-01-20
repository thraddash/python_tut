#!/usr/bin/env python
a="""
############################################
# Reading line by line and make uppercase
# remove newline with rstrip 
# Enumerate() methods adds a counter to an iterable and return it in a form of an obj
# can be used in a for loop or converted into a list of tuples using list() method

l1 = ["eat","sleep","repeat"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:",type(obj1))
print (list(enumerate(l1)))
 
# changing start index to 2 from 0
print (list(enumerate(s1,2)))

with open('data.txt') as fobj:
    for num, line in enumerate(fobj):
        print(num+1, line.upper())
"""
print(a)
print("############ Classic way:  strip() #########")
with open('data.txt') as fobj:
    for num, line in enumerate(fobj):
        print(num+1, line.upper().strip())

print("############ rstrip() ######################")
print("print(num+1, line.upper().rstrip('\\n'))")
with open('data.txt') as fobj:
    for num, line in enumerate(fobj):
        print(num+1, line.upper().strip('\n'))

print("############ replace('\\r', '').replace('\\n', '') ######################")
with open('data.txt') as fobj:
    for num, line in enumerate(fobj):
        print(num+1, line.upper().replace("\r", "").replace("\n", ""))
       
