#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ rectangle """
    def __init__(self, width=0, height=0):
        """ constructor """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ parameter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ This method returns the string representation of the object """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            t = "\n".join(["#" * self.__width for i in range(self.__height)])
            return t
