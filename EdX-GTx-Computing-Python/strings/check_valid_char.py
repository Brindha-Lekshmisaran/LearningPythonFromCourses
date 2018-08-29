#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#Write a function called "valid_char" that determines
#if a single character (a string of length one) has an
#ordinal value corresponding to a valid character for a
#password. Valid characters are any character on the
#keyboard except spaces. Return True if it's a valid
#character, False if it is not.
#
#Hint: you can find the ordinal value of a character using 
#the built-in Python function ord(): ord("a") -> 97
#
#Hint 2: the range of legal characters will be one
#continuous range (e.g. characters 55 through 65, not
#separate ranges like 55 through 65 and 69 through 79).
#You can use asciitable.com to look up what range you
#should use.


#Write your function here!
def valid_char(myChar):
    if 33 <= ord(myChar) <= 126:
        return True
    return False

'''
A more pythonic way will be

def valid_char(character):
    return 33 <= ord(character) <= 126
'''

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False

print(valid_char("a"))
print(valid_char(" "))
print(valid_char("!"))
print(valid_char("☺"))
