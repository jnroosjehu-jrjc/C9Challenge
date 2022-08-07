#coding : UTF-8
"""
Yo ba w antre ak sòti sa yo:

a = 5                 2
b = 2         

a = 3                 3
b = 4

a = 1                 1
b = 1
Kreye kòd pou input ak output sa yo.
"""

def min(a, b):
    min = a
    if b<a:
        min = b
    elif b==a:
        min=a
    else:
        min = a
    return min


print(min(1,1))