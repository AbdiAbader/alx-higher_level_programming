#!/usr/bin/python3
""" Base Geometry """


class BaseGeometry:
    """ base geomotery Area checker """

    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ intger validator """
        if type(value) is not int:
            raise TypeError(f"{name:s} must be an integer")
        if value <= 0:
            raise ValueError(f"{name:s} must be greater than 0")
