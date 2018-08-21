#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#Write a function called attendance_check. attendance_check
#should have two parameters: roster and present. Both roster
#and present will be lists of strings. Return a list (sorted
#alphabetically) of all strings in the list roster that are
#not in the list present. In other words, if roster is a
#list of students enrolled in a class and present is a list
#of students in class today, return a list of students that
#are absent.
#
#You may assume that every item in each list will be a
#string. You may also assume that every name in the list
#present will be in the list roster. If no students are
#absent, return an empty list.


#Write your function here!
def attendance_check(roster, today):
     '''
     Return list of elements available in roster but not part of today list
     '''
     absentees = []
     #Iterate through the roster, and check which names are absent today. Add those names to a new list
     for name in roster:
          if name not in today:
               absentees.append(name)
     absentees.sort()
     return absentees


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#['Ferguson', 'Winston']
test_roster = ['Jessica', 'Nick', 'Winston', 'Schmidt', 'Cece', 'Ferguson']
test_present = ['Nick', 'Cece', 'Schmidt', 'Jessica']
print(attendance_check(test_roster, test_present))



