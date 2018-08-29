#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

#Write a function called phonebook that takes two lists as
#input:
#
# - names, a list of names as strings
# - numbers, a list of phone numbers as strings
#
#phonebook() should take these two lists and create a
#dictionary that maps each name to its phone number. For
#example, the first name in names should become a key in
#the dictionary, and the first number in numbers should
#become the value corresponding to the first name. Then, it
#should return the dictionary that results.
#
#Hint: Because you're mapping the first name with the first
#number, the second name with the second number, etc., you do
#not need two loops. For a similar exercise, check back on
#Coding Problem 4.3.3, the Scantron grading problem.
#
#You may assume that the two lists have the same number of
#items: there will be no names without numbers or numbers
#without names.


#Write your function here!

def phonebook(namelst, numlst):
     '''
     create dictionary from two lists
     '''
     outputdict = {}
     #Create keys from first list, and assign values from second list
     #The length of both lists is same in this example
     for i in range(0, len(namelst)):
          #dict[key] = value
          outputdict[namelst[i]] = numlst[i]
     return outputdict


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Jackie': '404-555-1234', 'Joshua': '678-555-5678', 'Marguerite': '770-555-9012'

name_list = ['Jackie', 'Joshua', 'Marguerite']
number_list = ['404-555-1234', '678-555-5678', '770-555-9012']
print(phonebook(name_list, number_list))


