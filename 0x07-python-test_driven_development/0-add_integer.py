#!/usr/bin/python3
"""
Adds Two intgers a and b
return a + b

"""


def add_integer(a, b=98):
    """ Returns sum of a and b
    float number cast to int
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
