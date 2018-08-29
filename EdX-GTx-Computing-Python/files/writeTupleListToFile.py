#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

def writeTupleListToFile(filename, mytuple):
    outputfile = open(filename, "w")
    for item in mytuple:
        print(item, file=outputfile)
    outputfile.close()
    
#Testing
movieList = [('Rogue One', 530, 2017), ('Finding Dory', 486, 2017), ('Captain America: Civil War', 408, 2017)] 
writeTupleListToFile("Movies.txt", movieList)