#!/usr/bin/env python
#Sorting list

fruit = ['apple', 'pear', 'orange', 'cherry']
print(fruit,"\n")
print("#fruit.sort()")
fruit.sort()
print(fruit, "\n")
print("#fruit.sort(reverse=True)")
fruit.sort(reverse=True)
print(fruit, "\n")

print("#keep original list sorted(fruit)")
fruit = ['apple', 'orange', 'pineapple', 'cherry']
print(sorted(fruit), "\n")

print("#Reverse list")
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers, "\n")

print("#List length")
numbers = [1, 2, 3, 4]
print(len(numbers))

