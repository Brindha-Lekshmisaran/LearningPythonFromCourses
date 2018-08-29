#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#Write a function called grade_scantron. grade_scantron should
#take as input two lists: answers and key. Each list contain
#strings. Each string will be only one letter, a character
#from A to E. grade_scantron should return how many questions
#the student got "right", where a student gets a question
#right if their answer for a problem matches the answer key.
#
#In other words, if value of the first item in answers matches
#the value of the first item in key, the student gets a point.
#If it does not, the student does not get a point.
#
#If the lists do not have the same number of items, return
#-1 to indicate that the answer key did not belong to the
#same test as the student's answers.\
#
#Hint: in the past, lots of people have tried to do this using
#the index() method. That won't work! You'll need to track the
#index yourself.


#Write your function here!

def grade_scantron(answers, key):
     '''
     True if answers match with keys
     '''
     
     #If the two lists do not have the same number of items, return -1
     #Match first element of answers lst with key list, and so on.
     #Create a counter to tally the number of matches
     
     if len(answers) != len(key):
          return -1
     
     counter = 0
     for idx in range(0, len(answers)):
         if answers[idx] == key[idx]:
                    counter += 1
     return counter

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 7
test_answers = ["A", "B", "B", "A", "D", "A", "B", "A", "E"]
test_key = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
print(grade_scantron(test_answers, test_key))

test_answers = ["A", "B", "B", "A", "D", "A", "B"]
test_key = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
print(grade_scantron(test_answers, test_key))

test_answers = ["A", "B", "B", "A", "D", "A", "B", "A", "E"]
test_key = ["A", "B", "B", "A", "D", "E"]
print(grade_scantron(test_answers, test_key))

test_answers = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
test_key = ["A", "B", "B", "A", "D", "E", "B", "A", "D", "B", "A", "D"]
print(grade_scantron(test_answers, test_key))

test_key = ["B", "C", "D", "A", "D", "B", "E", "B", "C"]
test_answers = ["B", "C", "D", "A", "E", "B", "A", "B", "C"]
print(grade_scantron(test_answers, test_key))