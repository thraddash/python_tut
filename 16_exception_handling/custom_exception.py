#!/usr/bin/env python

# Creating custom exception
# any vowel inputs are not accepted

class VowelNotAccepted(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status

def check_chars(word):
    for char in word:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            raise VowelNotAccepted("Vowel is not accepted", 101) # raising exception, defining random 101 random value as an error
    return word

try: 
    print(check_chars("love"))
    #print(check_chars("my"))
except Exception as e:
    print("Error reason: ", e.message)
