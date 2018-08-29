#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

#Recall in the previous problem you counted the number of
#instances of a certain first name in a list of full names.
#You returned a dictionary with the name as the key, and the
#number of times it appeared as the value.
#
#Modify that code such that instead of having a count as the
#value, you instead have a list of the full names that had
#that first name. So, each key in the dictionary would still
#be a first name, but the values would be lists of names.
#Make sure to sort the list of names, too.
#
#Name this new function name_lists.


#Add your function here!

def name_lists(lst):
     '''
     collate names which has same first name into seperate groups, and return as dictionary
     '''
     #Initialize variables
     outputdict = {}
     #Iterate through the list
     for item in lst:
          #Get first and last name
          first, last = item.split()
          #If the firstname is not present as a key already in dictionary, create the key with empty list as value.
          if not first in outputdict:
               outputdict[first] = []
          #Now create values for the key. The values are a list of the fullnames which contain the key which is the firstname. Each time you encounter a first name which is already a key, add the fullname to its value (which is a list itself)
          outputdict[first].append(item)
     
     #sort list items that is in the values of the dictionary
     for keys, vals in outputdict.items():
         vals.sort()
     return outputdict

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Odle', 'Shelba Fry'],
#'David': ['David Joyner', 'David Zuber'], 'Brenton': ['Brenton Joyner', 'Brenton Zuber'],
#'Maren': ['Maren Fry'], 'Nicol': ['Nicol Barthel']}

name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
print(name_lists(name_list))



