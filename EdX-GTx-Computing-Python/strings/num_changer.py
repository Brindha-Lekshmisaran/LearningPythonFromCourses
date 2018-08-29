#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#Write a function called "num_changer" that accepts a string 
#of digits (0-9). You should make an integer from the digits 
#of the even indices and another number from the digits in 
#the odd indices. Return the sum of these two numbers. You 
#can assume the given string will have a length of at least 
#2 digits.
#
#For example, if the string was "123456", you would split
#this into two integers, 135 and 246. Adding them would give
#381. Or if the string was "13579", you would split this into
#159 and 37, then add them to get 196.
#

#Write your function here!

def num_changer(myNum):
    first = last = " "
    for idx, item in enumerate(myNum):
        if idx % 2: #if odd indices
              first+=item
        else:
              last+=item
    sum = int(first) + int(last)
    return sum
    
'''
A more pythonic method

def num_changer(digits):
   even_digits = digits[0::2]
   odd_digits = digits[1::2]
   return int(even_digits) + int(odd_digits)

'''

#TESTING the function
#
#If your function works correctly, this will originally
#print: 123456 -> 381
string_int = "123456"
result = num_changer(string_int)
print(string_int + " -> " + str(result))




