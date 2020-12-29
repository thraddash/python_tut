#!/usr/bin/env python
import subprocess
import sys

try:
        import colorama
except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
finally:
        from colorama import Fore
        from colorama import Style

title = "Pythong Course"
print(f"{Fore.RED}# Accessing string character{Style.RESET_ALL}")
print (title[0], title[1], title[-1], title[-2])
# String operation
print ('')
name = 'jonathon swift'
print ("# String operation")
print (name.title())
print (name.upper())
print (name.lower())

print('')
print(f"{Fore.RED}# String Concatenation{Style.RESET_ALL}")
first_name = "Steve"
last_name = "Jobs"
# string conctenation in variable
name = first_name + ' ' + last_name
print(name)
# string concatenation in string function
print(first_name + ' ' + last_name) 
print('')
print(f"{Fore.RED}# whitespace{Style.RESET_ALL}")
name = "     Mr. X      "
print('_' + name + '_')
print('# lstrip')
print('_' + name.lstrip() + '_')
print('# rstrip')
print('_' + name.rstrip() + '_')
print('# strip')
print('_' + name.strip() + '_')
print('# method chaining lstrip and rstrip')
print('_' + name.lstrip().rstrip() + '_')

print('')
print(f"{Fore.RED}# Printing Single and Double Quotes{Style.RESET_ALL}")
print("double quotes")
shop_name = "Rahim's Shop"
print(shop_name)

print("double single quote")
shop_name = 'Rahim"s Shop'
print(shop_name)

print("backslash to escape apostrophe")
shop_name = 'Rahim\'s Shop'
print(shop_name)
