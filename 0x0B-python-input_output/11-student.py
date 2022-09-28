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
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """ change attribute name """
        for key, value in json.items():
            setattr(self, key, value)
