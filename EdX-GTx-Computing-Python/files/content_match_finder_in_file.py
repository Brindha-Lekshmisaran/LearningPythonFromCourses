#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

#Write a function called "angry_file_finder" that accepts a
#filename as a parameter. The function should open the file,
#read it, and return True if the file contains "!" on every
#line. Otherwise the function should return False. 
#
#Hint: there are lots of ways to do this. We'd suggest using
#either the readline() or readlines() methods. readline()
#returns the next line in the file; readlines() returns a
#list of all the lines in the file.


#Write your function here!

def angry_file_finder(filename):
     inputfile = open(filename, "r")
     for line in inputfile:
          if "!" not in line:
#               print(line)
               #Even if one line has no "!", then return false and abort the rest of the loop
               return False
     inputfile.close()
     return True

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True
print(angry_file_finder("AngryFileFinderInput.txt"))
print(angry_file_finder("AngryFileFinderInput2.txt"))
print(angry_file_finder("AngryFileFinderInput3.txt"))
print(angry_file_finder("AngryFileFinderInput4.txt"))

'''
Comments from tutorial:

 #We could either get all the lines using
    #file_reader.readlines() and iterate over that list,
    #or we can use our loop syntax, which does the same
    #thing.
    

'''
