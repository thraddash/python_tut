#!/usr/bin/env python

import logging
import employee

# test.log was not created because import employee module logging was created first
# test.py module is sharing the same root logger that have already been configured
# configuring another root logger doesn't override previous settings
# no logging was capture in this test.py module because employee.py logger is set to INFO
# test.py current logging is set to DEBUG 

# modify logging from debug to info will output data to employee.log file
# CONS: logfile is not generated, log level is not captured, formatting is not captured

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

num_1 = 10
num_2 = 2 

add_result = add(num_1, num_2)
# update logging.debug to logging.info
logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
# update logging.debug to logging.info
logging.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))
