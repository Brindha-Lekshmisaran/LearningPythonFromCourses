#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

def loadList(filename):
    newList = []
    inputfile = open(filename, "r")
    for line in inputfile:
        newList.append(line.strip())
    return newList

#Testing
saveList("OutputList.txt", ["first", "second", "third"])
outList = loadList("OutputList.txt")
outList