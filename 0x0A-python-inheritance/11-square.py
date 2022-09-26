#!/usr/bin/python3
""" Square functions """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size):
        """ """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area of square """
        return self.__size ** 2

    def __str__(self):
        """ string reprsatation """
        return f"[Square] {self.__size:d}/{self.__size:d}"
