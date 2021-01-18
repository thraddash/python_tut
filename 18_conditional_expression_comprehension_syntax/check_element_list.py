#!/usr/bin/env python
a="""
# check if all elements in list follow a condition
##################################################
# Method 1: 
# Using all()
test_list = [4, 5, 8, 9, 10] 
res = all(ele > 3 for ele in test_list) 
"""
print(a)
test_list = [4, 5, 8, 9, 10] 
res = all(ele > 3 for ele in test_list)

print("The original list : " + str(test_list)) 
print("Are all elements greater than 3? : " + str(res))

b="""
##################################################
# Method 2: 
# itertolls.takewhile()
import itertools

# initializing list 
test_list = [4, 5, 8, 9, 10] 

# Check if all elements in list follow a condition 
# Using itertools.takewhile() 
count = 0
for ele in itertools.takewhile(lambda x: x > 3, test_list): 
    count = count + 1
res = count == len(test_list)
"""
print(b)
import itertools

test_list = [4, 5, 8, 9, 10] 
count = 0
for ele in itertools.takewhile(lambda x: x > 3, test_list): 
    count = count + 1
res = count == len(test_list)
print("The original list : " + str(test_list)) 
print("Are all elements greater than 3 ? : " + str(res)) 
