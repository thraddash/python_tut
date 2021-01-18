#!/usr/bin/env python
print("# Removing duplicates from a list")

list_data = [1, 3, 5, 6, 3, 5, 6, 1]
a="""
# Removing duplicates from a list 5 Methods
############################################################################################
# Method 1: 
# traverse and append first occurence to new list, ignore all other occurence
list = [1, 3, 5, 6, 3, 5, 6, 1]
res = []
for i in list:
    if i not in res:
        res.append(i)
"""
print(a)

res = []
for i in list_data:
    if i not in res:
        res.append(i)
print("New List after removing duplicates: " + str(res))
b="""
####################################################
# Method 2: 
# Using List comprehension
res =[]
[res.append(i) for i in list if i not in res] 
"""
print(b)
res =[]
[res.append(i) for i in list_data if i not in res] 
print("List comprehension after removing duplicates: " + str(res))

c="""
#################################################################
# Method 3: 
# Using Set, however ordering of the element is lost 
list_data = [1, 3, 5, 6, 3, 5, 6, 1]
list_data = list(set(list_data))
"""
print(c)
list_data = list(set(list_data)) 
print ("The list after removing duplicates : " + str(list_data)) 

d="""
###################################################################################
# Method 4: 
# Using list comprehension + enumerate()
# looks for already occured elments and skips adding them, preserves list ordering
list_data = [1, 3, 5, 6, 3, 5, 6, 1]
res = [i for n, i in enumerate(list_data) if i not in list_data[:n]]
print(res)
"""
print(d)
res = [i for n, i in enumerate(list_data) if i not in list_data[:n]]
print(res)

e="""
####################################################################################
# Method 5:
# collection.OrderedDict.fromkeys()
# OrderedDict is a dictionary subclass that remembers the order the keys were first inserted
pip3 install collection OrderedDict

from collections import OrderedDict
list_data = [1, 3, 5, 6, 3, 5, 6, 1]
res = list(OrderedDict.fromkeys(list_data))
"""
print(e)
from collections import OrderedDict

list_data = [1, 3, 5, 6, 3, 5, 6, 1]
res = list(OrderedDict.fromkeys(list_data))
print(res)

