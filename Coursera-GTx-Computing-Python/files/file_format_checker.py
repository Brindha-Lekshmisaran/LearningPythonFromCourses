#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

#Let’s define a new filetype called ".cs1301". 
#In this file, every line should be structured like so:
#
#number assignment_name grade total weight
#
#In this file, each component will meet the following
#description:
#
# - number: an integer-like value of the assignment number 
#
# - assignment_name: a string value of the assignment name
#
# - grade: an integer-like value of a student’s grade
#
# - total: an integer-like value of the total possible
#   number of points
#
# - weight: a float-like value ranging from 0 to 1 
#   representing the percent of the student’s grade this 
#   assignment is worth. All the weights should add up to 1.
#
#Each component should be separated with exactly one space. 
#A good sample file is available to view as 
#"sample.cs1301".
#
#Write a function called format_checker that accepts a 
#filename and returns True if the file contents accurately 
#conform to the described format. Otherwise the function 
#should return False. In other words, it should return True
#if:
#
# - Each line has five elements separated by spaces, AND
# - The first, third, and fourth elements are integers, AND
# - The fifth element is a decimal number, AND
# - All the fifth elements add to 1.
#
#You can make changes to test.cs1301 to test your function,
#or test it with sample.cs1301. Right now, running it on
#sample.cs1301 should return True, and on test.cs1301
#should return False.
#
#Hint 1: .split() will likely help separate each line into 
#its components.
#Hint 2: .split() returns a list. So, if you were to do
#something like say split_line = line.split(), then
#split_line[0] would give the first item, split_line[1] would
#give the second item, etc.
#Hint 3: If you're having trouble, try breaking it down by
#parts. First check the file to see if it has the right
#number of items per line, then whether the items are of
#the correct type, then whether the fifth elements add to
#1. Remember, you know how to do each individual check
#(checking types, adding numbers, finding list lengths) --
#the hard part is knitting this all together into one bigger
#solution.


#Write your function here!
import decimal #for floating point arithmetic

def format_checker(filename):
     '''
     it should return True if: 
      - Each line has five elements separated by spaces, AND
      - The first, third, and fourth elements are integers, AND
      - The fifth element is a decimal number, AND
      - All the fifth elements add to 1.
     '''
     inputfile = open(filename, "r")
     #Initialize variables to be used inside the loop
     words = []
     total = 0
     #iterate through the lines
     for line in inputfile:
          #Does it have five elements seperated by spaces?
          if line.count(" ") == 4:
               print("first test pass")
               #Are the 1st, 3rd and 4th element integers? 
               #split line by spaces to get the elements
               words = line.split(" ")
               if (words[0].isdigit()) and (words[2].isdigit()) and (words[3].isdigit()):
                    print("second test pass")
                    #Is 5th element decimal?
                    try:
                         float(words[4])
                         #Now to check if all fifth elements add to one, create a running total of 5th elements.
                         total += decimal.Decimal(words[4])
                         print("third test pass")
                    except ValueError:
                         #If 5th element not decimal, return false
                         inputfile.close()
                         return False
               else:
                    #If 1st, 3nd & 4th elements not integers, return false
                    inputfile.close()
                    return False
          else:
               #If five elements not sep by spaces, return false
               inputfile.close()
               return False
          
     inputfile.close()
     #Return true if the last condition is true, i.e., the total of all 5th elements is 1
     if total == 1:
          print("fourth test pass")
          return True
     else:
          return False
     
#Test your function below. With the original values of these
#files, these should print True, then False:
#print(format_checker("data/sample_1.cs1301.txt"))
#print(format_checker("data/sample_2.cs1301.txt"))
print(format_checker("data/sample.cs1301.2.txt"))
'''
#Method from the tutorial

for line in file_reader:
        
        #First, let's split it up into its parts. We know
        #that spaces mark different pieces.
        
		parts = line.split(" ")
        
        #The first requirement in our file format is that
        #there by 5 parts on each line. If this line does
        #not have exactly 5 parts, we're done! This isn't
        #a valid line, and only one invalid line makes the
        #entire file invalid.
        
        if len(parts) != 5:
            
            file_writer.close()
			return False
        
        #Next, let's check to make sure each individual
        #part is of the right type. The first, third, and
        #fourth parts should be integers, and the 5th part
        #should be a float. If any of those conversions
        #cause an error, we're done!
        
		try:
			int(parts[0])
			int(parts[2])
			int(parts[3])
			float(parts[4])
            
            #Assuming all those conversions work, we now
            #want to add the fourth part to our running
            #total_weight variable.
            
			total_weight += float(parts[4])
		except:
            
            #If any of those conversions caused an error,
            #we're done. One error means this line is
            #invalid, and if this line is invalid, the
            #entire file is invalid.
            
            file_writer.close()
			return False
            
#If we reach this part of the function, it means that
    #none of the previous 'return False' lines ran. So,
    #that means we know that each line has 5 parts, and each
    #part of each line is the right type. The only thing we
    #have left to check is whether or not all those total
    #weights added to 1. If they don't, we return False.
    
    if total_weight != 1:
		return False
	
    #The only way this next line is reached is if all previous
    #checks were valid: five items per line, correct data
    #types, and weights that add to 1. If any of those were
    #not true, then a 'return False' line would have run. So,
    #we can safely return True.
    
	return True
'''