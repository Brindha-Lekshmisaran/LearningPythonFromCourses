#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

import ast
def readTupleFromFile(filename):
    newList = []
    inputfile = open(filename, "r")
    for line in inputfile:
        lineAsTuple = ast.literal_eval(line)
        newList.append(lineAsTuple)
    return newList

#Testing
readTupleFromFile("Movies.txt")