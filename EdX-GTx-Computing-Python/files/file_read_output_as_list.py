#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

#Write a function called "reader" that reads in a ".cs1301" 
#file described in the previous problem. The function should 
#return a list of tuples representing the lines in the file like so:
#
#[(line_1_number, line_1_assignment_name, line_1_grade, line_1_total, line_1_weight), 
#(line_2_number, line_2_assignment_name, line_2_grade, line_2_total, line_2_weight)]
#
#All items should be of type int except for the name (string) 
#and the weight (float). You can assume the file will be in the 
#proper format -- in a real program, you would use your code
#from the previous problem to check for formatting before
#trying to call the function below.
#
#Hint: Although you could use readlines() to read in all
#the lines at once, they would all be strings, not a list.
#You still need to go line-by-line and convert each string
#to a list.


#Write your function here!
import decimal
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
#               print("first test pass")
               #Are the 1st, 3rd and 4th element integers? 
               #split line by spaces to get the elements
               words = line.split(" ")
               if (words[0].isdigit()) and (words[2].isdigit()) and (words[3].isdigit()):
#                    print("second test pass")
                    #Is 5th element decimal?
                    try:
                         float(words[4])
                         #Now to check if all fifth elements add to one, create a running total of 5th elements.
                         total += decimal.Decimal(words[4])
#                         print("third test pass")
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
#          print("fourth test pass")
          return True
     else:
          return False

def reader(filename):
     '''
     Assuming correct file format, The function should return a list of tuples representing the lines in the file. 
     #[(line_1_number, line_1_assignment_name, line_1_grade, line_1_total, line_1_weight)(line_2_number, line_2_assignment_name, line_2_grade, line_2_total, line_2_weight)]
     #All items should be of type int except for the name (string) 
#and the weight (float).
     '''
     #Make sure that the file is in the expected format
     if (format_checker(filename) == True):
          words = []
          outputlist = []
          mytuple = ()
          inputfile = open(filename, "r")
          for line in inputfile:
               words = line.split(" ")
               #create tuple with the words
               mytuple = (int(words[0]), words[1], int(words[2]), int(words[3]), float(words[4]))
               #add this tuple to the outputlist
               outputlist.append(mytuple)
          inputfile.close()
          return outputlist
     else:
          return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#[(1, 'assignment_1', 85, 100, 0.25), (2, 'test_1', 90, 100, 0.25), (3, 'exam_1', 95, 100, 0.5)]
#print(reader("data/sample.cs1301.txt"))
#print(reader("data/sample_1.cs1301.txt"))
#print(reader("data/sample_2.cs1301.txt"))
print(reader("data/sample.cs1301.2.txt"))




