#!/usr/bin/python3
""" Class Student """


class Student:
    """ class student """
    def __init__(self, first_name, last_name, age):
        """ consturctor for class student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrive dic represatation of class student """
        if attrs is None:
            return self.__dict__
        d = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                d[key] = value
        return d
