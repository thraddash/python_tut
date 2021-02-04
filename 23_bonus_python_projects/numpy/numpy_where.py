#!/usr/bin/env python

print("###### numpy search() method #######")

import numpy as np

pets = np.array(["dog", "cat", "dog"])
print("dog, cat, dog ")
dogs = np.where(pets == "dog")
print(dogs)
