#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#Write a function, called lucky_sevens, that takes in one
#parameter, a list of integers, and returns True if the list
#has three '7's  in a row and False if the list doesn't.
#
#For example:
#
#  lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]) -> True
#  lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]) -> False
#
#Hint: As soon as you find one instance of three sevens, you
#could go ahead and return True -- you only have to find it
#once for it to be True! Then, if you get to the end of the
#function and haven't returned True yet, then you might
#want to return False.


#Write your function here!
def lucky_sevens(mylst):
     '''
     True if three 7s in a row
     '''
     #Find the first 7.
     #Iterate through the indices and check the values of the next items.
     for i in range(0, len(mylst)-1):
          if (mylst[i] == 7) and (mylst[i+1] == 7) and (mylst[i+2] == 7):
               return True
     return False



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False
print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))

'''
#Method from tutorial

def lucky_sevens(a_list):
    
    #The challenge with using a for-each loop is that we have
    #no way to look up the next character in the string because
    #we don't have the index of the character we're looking at.
    #We could track it manually, but then we're basically just
    #doing a for loop.
    #
    #Instead, let's keep a counter of how many consecutive 7s
    #we have found so far:
    
    consecutive_7s = 0
    
    #Now, we loop through the items in the list:
        
    for num in a_list:
        
        #If this is a 7, we want to increment the number of
        #consecutive 7s we've found:
        
        if num == 7:
            consecutive_7s += 1
        
        #If it isn't, then we need to reset our counter of
        #consecutive 7s to 0 -- otherwise we're counting the
        #total number of 7s, not the consecutive ones:
        
        else:
            consecutive_7s = 0
        
        #Now, that means that if we find three 7s in a row,
        #but then find something else, consecutive_7s will
        #be reset to 0. So, we need to check if we've found
        #three straight inside the loop:
        
        if consecutive_7s == 3:
            return True
        
        #Note that this could have been placed inside the
        #conditional on line 23 as well: it can't be true
        #unless the current item is 7.
        
                
    #Then, same as before, the only way we reach the line below
    #is if we never returned True above. So, if we reach the end
    #of that loop and haven't exited the function, then we didn't
    #find three straight 7s:
    
    return False


# Another method from tutorial
def lucky_sevens(a_list):
    
    #map() takes two arguments: a function and a list. It returns
    #a new list created by applying that function to each item in
    #that list:
    
    a_list_as_strings = map(str, a_list)
    
    #So, this effectively duplicates the code in the comment above,
    #but without changing a_list. It applies the function str() to
    #each item in a_list, and returns a list of the results.
    #
    #Then, we can check if "777" is in the result of joining that
    #list of strings:
    
    a_list_as_one_string = "".join(a_list_as_strings)
    return "777" in a_list_as_one_string

    #All of which could becompressed down to one line:
    #return "777" in "".join(map(str, a_list))
'''
