#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#Write a function called "in_parentheses" that accepts a 
#single argument, a string representing a sentence that
#contains some words in parentheses. Your function should
#return the contents of the parentheses.
#
#For example:
#
# in_parentheses("This is a sentence (words!)") -> "words!"
#
#If no text appears in parentheses, return an empty string.
#Note that there are several edge cases introduced by this:
#all of the following function calls would return an empty
#string:
#
# in_parentheses("No parentheses")
# in_parentheses("Open ( only")
# in_parentheses("Closed ) only")
# in_parentheses("Closed ) before ( open")
#
#You may assume, however, that there will not be multiple
#open or closed parentheses.


#Write your function here!

'''
Pseudo code:
    #find the index of the open paranthesis
    #find the index of the closed paranthesis
    #Proceed to substring only if start and close are found. 
    #grab the string within those indexes
'''

def in_parentheses(myStr):
    start = myStr.find("(")
    close = myStr.find(")")

    #Proceed to substring only if start and close are found. 
    if start != -1 and close != -1:
        result = myStr[start+1 : close]
    else:
        result = "No parantheses found"
    return result


#Testing
print(in_parentheses("This is a sentence (words!)."))
print(in_parentheses("No parentheses here!"))
print(in_parentheses("David tends to use parentheses a lot (as he is doing right now). It tends to be quite annoying."))
print(in_parentheses("Open ( only"))
print(in_parentheses("Closed ) only"))
print(in_parentheses("Closed ) before ( open"))
print(in_parentheses("That's a lot of test cases(!)"))


