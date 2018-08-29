#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""
#Write a function called average_file. average_file should
#have one parameter: a filename.
#
#The file should have an integer on each line. average_file
#should return the average of these integers. However, if
#any of the lines of the file are _not_ integers,
#average_file should return the string "Error reading file!"
#
#Remember, by default, every time you read a line from a
#file, it's interpreted as a string.


#Add your function here!

def average_file(filename):
     '''
     To average the numbers in a file
     '''
     #Iterate through the contents
     #As even numbers are string, use the following method to check for type.
     #Inside if block use isdigit() to check if integer. If exception, have a try block to convert into float, and if further expection, deem it to be string.
     # Add each number to a running total. Also have a running count variable.
     #Calc average
     
     inputfile = open(filename, "r")
     total = 0
     count = 0
     for line in inputfile:
          line =  line.strip() #remove newline characters.
#          print(line)
          if line.isdigit():
              total+=int(line)
              count+=1
              
          else:
               try:
                    float(line)
                    total+= int(line)
                    count+=1
                    
               except:
                    return "Error reading file!"
          
     inputfile.close()
     average = total/count
     return average

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5.0, then Error reading file!
#
#You can select valid_file.txt and invalid_file.txt from
#the dropdown in the top left to preview their contents.
print(average_file("data/valid_file.txt"))
print(average_file("data/invalid_file.txt"))

'''
Suggestion from the tutorial

    
    #Recall that if _any_ line of the file is not an integer,
    #then we return an error. So, we would wrap the entire
    #logic of calculating the average into the try block:
    try:
        
        #Then, we want to go through each line in the file...
        for line in file:
            
            #Convert the line to an integer... this is the line
            #that will cause an error if the line doesn't
            #contain an integer!
            value = int(line)
            
            #And then we add the value to our running total...
            total += value
            
            #And increment the count:
            count += 1
    
    #The only error that could occur on the lines above is a
    #ValueError on line 28. So, we catch ValueErrors:
    except ValueError:
        file.close()
        return "Error reading file!"
    
    #If no errors occurred, then we return the average:
    else:
        file.close()
        return total / count
    
    #Notice that we close the file in both the except and
    #the else block: only one of these blocks will run,
    #but we also must close before we return, so we need
    #to close in both.
    #
    #If we wanted to instead skip lines that didn't
    #contain integers, we would put the try/except block
    #inside the loop instead.
    #
    #Note that if the file was empty, there would be an
    #uncaught ZeroDivisionError here because we would be
    #trying to return 0 / 0. We aren't checking your code
    #for that case, but if we wanted to, we would include
    #the average calculation in the try block, and add an
    #extra except block to catch ZeroDivisionErrors.
'''

