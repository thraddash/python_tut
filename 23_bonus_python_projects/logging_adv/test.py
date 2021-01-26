#!/usr/bin/env python

import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) #set log Level

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s') # Create formatter

file_handler = logging.FileHandler('test.log') # Create new fileHandler
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter) # Set formatter

stream_handler = logging.StreamHandler() #create a StreamHandler to display on console
stream_handler.setFormatter(formatter) # Set StreamHandler to same format as above formatter

logger.addHandler(file_handler)
logger.addHandler(stream_handler) # add stream_handler

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        #logger.error('Tried to divide by zero')
        logger.exception('Tried to divide by zero') #Use traceback
    else:
        return result

num_1 = 10
num_2 = 0 

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
