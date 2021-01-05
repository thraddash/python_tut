#!/usr/bin/env python

#function without a name, anonymous or Inline function (only in one line)
print("#lambda")
print("1.) function without a name")
print("2.) auto return")
print("3.) Inline function, one line exp")
print("4.) can have many arguments: only 1 expresssion")
print("5.) cannot use any if logic in lambda exp")

print("#lambda function addition 2,3")
add_numbers = lambda x, y: x + y 
print(add_numbers(2,3))

def cube(y):
    return y*y*y
print("#normal define function return y*y*y")
print(cube(5))

lambda_cube = lambda y : y*y*y
print("#lambda function lambda y : y*y*y")
print(lambda_cube(5))

print("# ages>18 adults")
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age>18, ages))
print(f"ages: {ages}")
print(adults)

