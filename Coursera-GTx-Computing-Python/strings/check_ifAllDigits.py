#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

import string

def check_ifAllDigits(myString):
    '''
    To check if the string is made up of digits.
    Function returns true if all the characters are digits. 
    '''
    for character in myString:
        #Check if character is a digit.
        if not character in string.digits:
            #Return false even if one character is not a digit.
            #Function is thus forced to exit here.
            return False
        #Return True if we reached here
        return True
    
    s = "abc12"
    print(check_ifAllDigits(s))
    
    #This function is similar to string isdigit method
    print(s.isdigit())
