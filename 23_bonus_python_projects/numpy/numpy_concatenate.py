#!/usr/bin/env python

import numpy as np

x = np.array(["bannana", "apple", "orange"])
y = np.array(["grape", "cherry", "mango"])

fruits = np.concatenate((x, y))
print("##### numpy concatenate() method ######")
print(fruits)
