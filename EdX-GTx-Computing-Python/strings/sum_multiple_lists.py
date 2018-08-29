#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#Write a function called sum_lists. sum_lists should take
#one parameter, which will be a list of lists of integers.
#sum_lists should return the sum of adding every number from
#every list.
#
#For example:
#
# list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# sum_list(list_of_lists) -> 67


#Add your code here!
def sum_lists(mulList):
     sum = 0
     #Iterate through the outer list
     #In each iteration, the subList will contain the each sub list of the main list
     for subList in mulList:
          #Iterate through the sub lists
          for item in subList:
               #Add the items in the subList
               sum += item
     #return total sum after all the sublists in the main lists are been iterated through
     return sum


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 78
list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sum_lists(list_of_lists))



