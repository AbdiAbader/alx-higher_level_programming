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


class Rectangle(BaseGeometry):
    """ Rectangle Class"""
    def __init__(self, width, height):
        """validates and construct """
        super(). integer_validator("width", width)
        self.__width = width
        super(). integer_validator("height", height)
        self.height = height
