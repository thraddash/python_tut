#!/usr/bin/env python

import numpy as np

pets = np.array(["dog", "cat", "rabbit"])

for pet in np.nditer(pets):
    print(pet)
