#!/usr/bin/env python

# finally block for clean up action

def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error Division by Zero")
    else:
        print("Result is: ", result)
    finally:
        print("Execute finally clause")

div(100, 10)
div(2, 0)
