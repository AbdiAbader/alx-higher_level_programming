#!/usr/bin/python3
""" Base Geometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class"""
    def __init__(self, width, height):
        """validates and construct """
        self. integer_validator("width", width)
        self.__width = width
        self. integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Area Return """
        return self.__width * self.__height

    def __str__(self):
        """string represtation """
        return f"[Rectangle] {self.__width:d}/{self.__height:d}"
