#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""
#Check if students have answered their questions correctly and assign grades based on the answer key.
#There are two dictionaries here:
#One is answerkey which provides the right answer to each question
#The second dictionary has student as key and a answers dictionary as value. This dictionary holds the answers provided by that student.
#The aim of this program is to check the answers provided each student against the answerkey and grade them.

ANSWER_KEY = {"1" : "A", "2" : "B", "3" : "C", "4" : "D", "5" : "A"}

students={}
students["David"] = {"1" : "A", "2" : "B", "3" : "A", "4" : "B", "5" : "C"}
students["Terra"] = {"1" : "A", "2" : "B", "3" : "C", "4" : "D", "5" : "A"}
students["Lugos"] = {"1" : "A", "2" : "C", "3" : "C", "4" : "D", "5" : "A"}

#View the students dictionary
print(students)

#Using nested for loop to access the main dictionary and the inner dictionary. Once you have reached the innner dictionary to grab content, match it with the ANSWERKEY dictionary. 
#If tehre is a match, then increment the grade. 
#After the inner dictionary is exhausted, add a new key called grade to the inner dictionary.

#For each student and their answers
for (student, answers) in students.items(): 
    grade = 0   #Start grade at 0
    #For each question and answer
    for (question, answer) in answers.items():  
        #If the answer matches ANSWER_KEY's answer...
        if answer == ANSWER_KEY[question]:  
            grade +=1   #Increment their grade
    #Create a new key "grade" and assign it their grade
    students[student]["grade"] = grade  
    
#Print out the grades for each student
#For each student and their answers
for (student, answers) in students.items(): 
    #Print the name and grade
    print(student, ": ", answers["grade"], sep = "", end = "; ")

#View the students dictionary now
print(students) #You can see the new entry called grade within the value.