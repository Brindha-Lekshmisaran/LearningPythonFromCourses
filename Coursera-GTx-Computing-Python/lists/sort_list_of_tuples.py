#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#We've learned a lot in this chapter. Let's try to use a lot
#of it for one final exercise.
#
#Write a function called sort_artists. sort_artists will
#take as input a list of tuples. Each tuple will have two
#items: the first item will be a string holding an artist's
#name, and the second will be an integer representing their
#total album sales (in millions).
#
#Return a tuple of two lists. The first list in the
#resulting tuple should be all the artists sorted
#alphabetically. The second list should be all the revenues
#sorted in descending numerical order.
#
#For example:
# artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
# sort_artists(artists) -> (["Elvis Presley", "Michael Jackson", "The Beatles"], [270.8, 211.5, 183.9])
#
#Notice that artists is a list of tuples (brackets first,
#then parentheses), but sort_artists outputs a tuple of
#lists (parentheses first, then brackets).


#Write your function here!
def sort_list_of_tuples(list_of_tuples):
     '''
     To return a tuple of two lists
     '''
     #Steps:
     #To build the first list; the list of artists
     #Sort it alphabetically
     #Build the second list; the list of album sales
     #sort is descending order
     
     #Pseudo code
     #Iterate through the outer list to grab each list item (which is a tuple)
          #unpack each tuple into two variables
          #Add first element to a new list of artists
          #Add second element to new list of album sales
     #Sort that new list of artists
     #Sort that new list of sales
     #Create a new 2D tuple of these two lists
     
     artists = []
     sales = []
     for tuple in list_of_tuples:
          print(tuple)
          artist, sale = tuple
          artists.append(artist)
          sales.append(sale)
     
     artists.sort()
     sales.sort(reverse=True) #Also u can use #sort.reverse()
     newTup = (artists, sales)
     return newTup
     
     
     


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#(['Elvis Presley', 'Michael Jackson', 'The Beatles'], [270.8, 211.5, 183.9])  
artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_list_of_tuples(artists))



