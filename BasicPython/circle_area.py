# Calculating the area of a circle
import math as m
def new_func():
    radius = float(input('Radius: '))
    new_var = m.pow(radius, 2)
    area = m.pi * (new_var)
    return area

area = new_func()
print(area)
