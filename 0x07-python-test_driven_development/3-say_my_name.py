#!/usr/bin/python3
"""
prints
First name and Last name
"""


def say_my_name(first_name, last_name=""):
    """ prints last and first if they are string """
    if type(first_name) is not str or first_name == "":
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
