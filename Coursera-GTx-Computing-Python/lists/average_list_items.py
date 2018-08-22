#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

#Imagine you're writing some code for an exercise tracker.
#The tracker measures heart rate, and should display the
#average heart rate from an exercise session.
#
#However, the tracker doesn't automatically know when the
#exercise session began. It assumes the session starts the
#first time it sees a heart rate of 100 or more, and ends
#the first time it sees one under 100.
#
#Write a function called average_heart_rate.
#average_heart_rate should have one parameter, a list of
#integers. These integers represent heart rate measurements
#taken 30 seconds apart. average_heart_rate should return
#the average of all heart rates between the first 100+
#heart rate and the last one. Return this as an integer
#(use floor division when calculating the average).
#
#You may assume that the list will only cross the 100 beats
#per minute threshold once: once it goes above 100 and below
#again, it will not go back above.


#Add your function here!
def average_heart_rate(intLst):
     '''
     To find average of items whose values are within a range
     '''
     #Pseudocode
     #Find the index of item when value is more than 100 for first time
     #Subsequently, find the index of item where value of item falls less than 100.
     #Grab the items between these two indcies
     #Take an average
     
     upIdx = 0
     downIdx = 0
     for idx, item in enumerate(intLst):
          if item > 100:
               upIdx = idx
               break 

     for i in range(upIdx, len(intLst)):
          if intLst[i] < 100:
               downIdx = i
               break
   
     actualLst = intLst[upIdx:downIdx] #You don't want to include the item at index downIdx

     total = 0
     for n in actualLst:
          total += n

     average = total//len(actualLst)
     return average
     
     


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 114 (because there are 14 measurements from 102 to
#101, their sum is 1609, and 1609 // 14 is 114).
beats = [72, 77, 79, 95, 102, 105, 112, 115, 120, 121, 121,
         125, 125, 123, 119, 115, 105, 101, 96, 92, 90, 85]
print(average_heart_rate(beats))

beats = [80, 88, 93, 94, 94, 95, 100, 104, 104, 106, 113, 114, 114, 116, 124, 124, 124, 120, 120, 120, 119, 118, 112, 104, 101, 98, 92, 85] 
print(average_heart_rate(beats))

beats = [71, 76, 83, 88, 90, 94, 100, 102, 110, 115, 121, 120, 118, 117, 113, 111, 110, 105, 100, 94, 94, 90]
print(average_heart_rate(beats))

