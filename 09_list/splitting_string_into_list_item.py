#!/usr/bin/env python

import re
cars = "toyota, honda, bmw, audi"
print("string: " + cars)
car_list = re.split(',', cars)
print("list: " + str(car_list))
