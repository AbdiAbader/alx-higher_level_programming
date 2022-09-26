#!/usr/bin/python3
""" changes attributes  if possible """


def add_attribute(objects, attribute, value):
    """ add new attributes usaing setatrr() function
        abnd check possible using hasatr functiom
    """
    if not hasattr(objects, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objects, attribute, value)
