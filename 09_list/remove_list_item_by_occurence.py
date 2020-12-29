#!/usr/bin/env python

# Remove all occurence of 2 with while loop
numbers = [1, 2, 3, 4, 5, 6, 5]
while 5 in numbers:
    numbers.remove(5)
print(numbers)
