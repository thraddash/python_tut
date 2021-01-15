#!/usr/bin/env python

## else block

def div(x, y):
    try:
        result = x / y
    except:
        print("Division by zero not possible")
    else:
        print("Div result is: " + str(result))

(div(8, 0))
(div(8, 2))

####

def div2(x, y):
    try:
        result = x / y
    except:
        return "Division by zero not possible"
    else:
        return "Div result is: " + str(result)

print(div2(8, 0))
print(div2(8, 2))



# raise allows you to throw an exception at any time.
# assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
# try clause, all statements are executed until an exception is encountered.
# except is used to catch and handle the exception(s) that are encountered in the try clause.
# else lets you code sections that should run only when no exceptions are encountered in the try clause.
# finally enables you to execute sections of code that should always run, with or without any previously encountered exceptions.


