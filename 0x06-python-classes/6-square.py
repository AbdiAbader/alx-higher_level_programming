#!/usr/bin/python3
""" Create Class for square and add Exeception to size """


class Square:
    """ Class with Init method and Exeception try / execpt """

    def __init__(self, size=0, position=(0, 0)):
        """initialization"""
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """ getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """Prints"""
        if self.__size == 0:
            print("")
            return
        for o in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end='')
            for j in range(0, self.__size):
                print("#", end='')
            print("")
