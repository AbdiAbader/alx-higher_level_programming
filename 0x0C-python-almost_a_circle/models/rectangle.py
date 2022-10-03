#!/usr/bin/python3
"""
   Rectangle Module
"""


from models.base import Base


class Rectangle(Base):
    """ class rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor method """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def x(self):
        """ getter of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def width(self):
        """ getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle calc method """
        return self.__width * self.__height

    def display(self):
        """ Display rectangle in # symbol"""
        print("\n" * self.__y +
              "\n".join([" " * self.__x + "#" * self.__width
                         for rows in range(self.__height)]))

    def __str__(self):
        """ str method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ update each attribute """
        if args:
            for j, i in enumerate(args):
                if j == 0:
                    self.id = i
                elif j == 1:
                    self.width = i
                elif j == 2:
                    self.height = i
                elif j == 3:
                    self.x = i
                elif j == 4:
                    self.y = i
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ print in dic mode """
        return {'x': self.x, 'id': self.id,
                'height': self.height, 'width': self.width}
