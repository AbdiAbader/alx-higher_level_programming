#!/usr/bin/python3
""" Create Class for square and add Exeception to size """


class Square:
    """ Class with Init method and Exeception try / execpt """

    def __init__(self, size=0):
        """initialization"""
        self.__size = size

    @property
    def size(self):
        """ getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    def area(self):
        """Area calculation"""
        return self.__size ** 2
