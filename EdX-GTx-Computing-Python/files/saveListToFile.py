#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

def saveList(filename, mylist):
    outputfile = open(filename, "w")
    for item in mylist:
        outputfile.write(item + "\n")
    outputfile.close()
    
#Testing
saveList("OutputList.txt", ["first", "second", "third"])