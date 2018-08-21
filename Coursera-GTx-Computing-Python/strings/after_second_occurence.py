#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#Write a function called after_second that accepts two 
#arguments: a target string to search, and string to search
#for. The  function should return everything in the first
#string *after* the *second* occurrence of the search term.
#You can assume  there will always be at least two
#occurrences of the search term in the first string. 
#
#For example:
#  after_second("11223344554321", "3") -> 44554321
#
#The search term "3" appears at indices 4 and 5. So, this
#returns everything from the index 6 to the end.
#
#  after_second("heyyoheyhi!", "hey") -> hi!
#
#The search term "hey" appears at indices 0 and 5. The
#search term itself is three characters. So, this returns
#everything from the index 8 to the end.
#
#Hint: This may be more complicated than it looks! You'll
#have to look at the length of the search string and
#either modify the target string or take advantage of the
#extra arguments you can pass to find().


#Write your function here!
def after_second(target_str, search_str):
     #search for index of searchstr in target
     first = target_str.find(search_str)
#     print(first)
     #Now add the length of the search string to get the index of the last char of search string
     first += len(search_str)
#     print(first)
     #This time do the search after the length of the search string.
     second = target_str.find(search_str, first)
#     print(second)
     #Now add the length of the search string to get the index of the last char of search string
     second += len(search_str)
#     print(second)
     #Grab the remaining target string after the index of the last char of the search string
     outStr = target_str[second:]
     return outStr


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 44554321 and hi!, each on their own line.
print(after_second("11223344554321", "3"))
print(after_second("heyyoheyhi!", "hey"))
print(after_second("She sells seashells by the seashore", "se"))

'''
#Answers from the course

def after_second(target, search):
    
    #We can do this in two ways. First, let's do it with
    #arguments to the find() method. First, we want to find
    #the first place that search appears:
    
    first_loc = target.find(search)
    
    #Next, we want to find the second location where search
    #appears:
    
    second_loc = target.find(search, first_loc + 1)
    
    #Now, second_loc stores the second place that search
    #appears. We want to return everything from after that
    #instance of search -- so, we add the length of search
    #to move past it, and return that substring:
    
    return target[second_loc + len(search):]

#Another method

def after_second(target, search):
    
    #This time, let's instead modify the target string and
    #use that. We'll basically delete the portions of the
    #string we don't want to return.
    #
    #First, we want to delete the string until and including
    #the first instance of search:
    
    target = target[target.find(search) + len(search):]
    
    #That line finds the first instance of search, adds the
    #length of the search string, and creates a new string
    #starting from the next character. So, we've deleted up
    #until the first instance of search.
    #
    #Next, we just do the exact same thing again!
    
    target = target[target.find(search) + len(search):]
    
    #Now we've deleted up to and including the second
    #instance of search. Because we're storing these results
    #back to target, we can now just return target:
    
    return target
    
#And here's a solution in a single line:

def after_second(target, search):
	return target[target.find(search, target.find(search) + len(search)) + len(search):]

#Don't fret if that's hard to follow! Try parsing it from the outside in. At
#the top level, we're returning a substring of search. At the end, we see a
#colon, then a bracket, so almost the entire line is calculating where to
#start the substring.
#
#Within that, we're adding two things: the result of a call to target.find(),
#and the result of a call to len(). The complexity is in the call to
#target.find().
#
#Within target.find(), we're searching for the search term, starting at
#the index given by target.find(search) + len(search). That itself gives
#the first location of search, so this is giving the second location of
#search.
#
#Sure enough, this method is what you get if you just copy/paste the
#different parts of sample_answer_1.py into the variables into which
#they were assigned.
'''

