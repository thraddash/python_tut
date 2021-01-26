#!/usr/bin/env python
import logging

# create a new logger, when __name__ is executed the variable will be equal to the module name
# Note: if employee logger does not have anything set, it will fall back to the root logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) #set log Level

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s') # Create formatter

file_handler = logging.FileHandler('employee.log') # Create new fileHandler
file_handler.setFormatter(formatter) # Set formatter

logger.addHandler(file_handler)

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'A')
emp_2 = Employee('John', 'B')
emp_2 = Employee('Jane', 'C')
