#!/usr/bin/env python

import numpy as np

nums = np.array([10, 8, 5, 4, 2, 3, 1])
print("####### 10, 8, 5, 4, 2, 3, 1 #######")
# returns the postion of the even numbers
even = np.where(nums % 2 == 0)

# returns the position of odd numbers
odd = np.where(nums % 2 ==1)

print("Even:")
for x in even:
    print(nums[x])

print("Odd:")
for y in odd:
    print(nums[y])

