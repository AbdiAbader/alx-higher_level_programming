#!/usr/bin/python3
""" Class Student """


class Student:
    """ class student """
    def __init__(self, first_name, last_name, age):
        """ consturctor for class student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrive dic represatation of class student """
        return self.__dict__
