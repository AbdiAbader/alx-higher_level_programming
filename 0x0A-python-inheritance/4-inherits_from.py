#!/usr/bin/python3
""" Subclass """


def inherits_from(obj, a_class):
    """ check for subclass """
    return issubclass(type(obj), a_class) and type(obj) != a_class
