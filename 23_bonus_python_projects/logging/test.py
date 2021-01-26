#!/usr/bin/env python

import logging
a="""
$$$$$$$$$####################################################################################
DEBUG: Detailed information, typically of interest only when diagnosing problems.

INFO: Confirmation that things are working as expected.

WARNING: An indication that something unexpected happened, or indicative 
of some problem in the near future (e.g. ‘disk space low’). The software is 
still working as expected.

ERROR: Due to a more serious problem, the software has not been able to p
erform some function.

CRITICAL: A serious error, indicating that the program itself may be unable 
to continue running.
#############################################################################################
"""

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

b="""
#######################################################################
args
asctime %(asctime)s
created %(created)f
exc_info
filename %(filename)s
funcName %(funcName)s
levelname %(levelname)s
levelno %(levelno)s
lineno %(lineno)d
message %(message)s
module %(module)s
msecs %(msecs)d
msg
name %(name)s
pathname %(pathname)s
process %(process)d
processName %(processName)s
relativeCreated %(relativeCreated)d
stack_info
thread %(thread)d
threadName %(threadName)s
"""