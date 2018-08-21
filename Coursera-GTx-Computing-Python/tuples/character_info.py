#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#Remember asciitable.com from an earlier exercise? We're
#going to use it again. Remember, ordinal values for
#characters are given in the 'Dec' column of asciitable.com.
#
#Write a function called character_info. character_info will
#take as input a string with only one character. It should
#return a 3-tuple with three pieces of information:
#
# - In the first spot, the character itself.
# - In the second spot, the ordinal value of the character,
#   obtained using the ord() function (e.g. ord("a") -> 97).
# - In the third spot, what type of character it is: either
#   "letter", "number", or "punctuation".
#
#You may assume that anything that is not a letter (either
#upper or lower case) or a number is punctuation. You may
#also assume the ordinal will be between 32 (" ") and 126
#("~").


#Write your function here!
def character_info(myChar):
     #find type of character
     if myChar.isdigit():
          tp = "number"
     elif myChar.isalpha():
          tp = "letter"
     else:
          tp = "punctuation"
        
     return (myChar, ord(myChar), tp)
    
        
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#('q', 113, 'letter')
#('7', 55, 'number')
#('`', 96, 'punctuation')
print(character_info("q"))
print(character_info("7"))
print(character_info("`"))


'''
#Method in course

def character_info(a_char):
    
    #To start, let's go ahead and get and save the ordinal
    #of the character. We could do this inside each
    #conditional, but it's better to do it once since it
    #means we're not recomputing it several times.
    
    ordinal = ord(a_char)
    
    #Next we want to test the ordinal against several
    #ranges. The numbers are the easiest because they're
    #one continuous group, so let's start there:
    
    if ordinal >= 48 and ordinal <= 57:
        char_type = "number"
    
    #We could return our resultant tuple right there, but
    #it's better to wait until the end: otherwise we're
    #duplicating a lot of code.
    #
    #Next, we need to look at either letters or
    #punctuation. These are a little tougher because 
    #they're both non-continuous ranges. Punctuation
    #falls into four ranges while letters only fall
    #into two, though, so let's use letters.
    #
    #The range of capital letters is 65 to 90, and the
    #range of lower case letters is 97 to 122. So, if
    #it falls into either (or) of those ranges, it's
    #a letter:
    
    elif (ordinal >= 65 and ordinal <= 90) or (ordinal >=97 and ordinal <= 122):
        char_type = "letter"
    
    #Finally, if it's not a letter and it's not a
    #number, we said you can assume it's punctuation:
    
    else:
        char_type = "punctuation"
    
    #Now we want to return our 3-tuple. The first item
    #is the original character, the second is its
    #ordinal, and the third is the type we just saved
    #for it:
    
    return (a_char, ordinal, char_type)
'''

