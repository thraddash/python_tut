#!/usr/bin/env python

import datetime

now = datetime.datetime.now()
x = dir(datetime)
datetime_obj = datetime.datetime.today()

print(now)
print("###### dir() - list module var, func, classs ########")
print(x)
print("######################################")
print(datetime_obj)
print("###### datetime constructor #################")
print("year, month, day , hour, min, sec, microsecond")
datetime_obj2 = datetime.datetime(2000, 6, 4, 22, 21, 30, 546842)
print("Datetime: ", datetime_obj2)
print("###### format datetime string - strftime() #################")
a = """
d = datetime.datetime.today()
print(d.strftime("%B %d %Y"))
"""
print(a)
d = datetime.datetime.today()
print(d.strftime("%B %d %Y"))

