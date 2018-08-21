#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

def find_all_indices_subString(myString, findString):
    '''
    To find all the instances of a substring within a string, and get their indices
    This will give all the locations of that substring within a string.
    '''
    currentLocation = myString.find(findString)
    while currentLocation >= 0:
        print(findString, "found at", currentLocation)
        currentLocation = myString.find(findString, currentLocation + 1)
    
myString = "ABCDBCDEABCBCABDABCDECDEABC"
findString = "ABC"
find_all_indices_subString(myString, findString)