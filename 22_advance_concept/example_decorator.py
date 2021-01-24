#!/usr/bin/env python
a="""
#####################################################################
A decorator is a function that takes another function as an argument, 
does some actions, and then returns the argument based on the actions 
performed. Since functions are first-class object in Python, they can 
be passed as arguments to another functions.
"""
print(a)
def reverse_decorator(function): 
  
    def reverse_wrapper(): 
        make_reverse = "".join(reversed(function())) 
        return make_reverse 
  
    return reverse_wrapper 
  
@reverse_decorator
def say_hi(): 
    return 'Hi George'
  
def main(): 
    print(say_hi()) 
  
if __name__ == "__main__": 
    main()
