#!/usr/bin/python3
""" module Base """


import json
import csv
import os
import turtle


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ construcator function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json represantation """
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ json representation to a file """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(cls.to_json_string([o.to_dictionary()
                        for o in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                dummy = cls(1)
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                i = cls.from_json_string(f.read())
                return [cls.create(**key) for key in i]
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes and deserializes in CSV """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            for i in list_objs:
                if cls.__name__ == "Rectangle":
                    wr.writerow([i.id, i.width, i.height, i.x, i.y])
                if cls.__name__ == "Square":
                    wr.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """ load csv file """
        obj = []
        filename = cls.__name__ + ".csv"
        if os.path.isfile(filename):
            with open(filename, 'r', newline='') as f:
                c_read = csv.reader(f)
                for row in c_read:
                    if cls.__name__ == "Rectangle":
                        names = {"id": int(row[0]), "width": int(row[1]),
                                 "height": int(row[2]), "x": int(row[3]),
                                 "y": int(row[4])}
                    if cls.__name__ == "Square":
                        names = {"id": int(row[0]), "size": int(row[1]),
                                 "x": int(row[2]), "y": int(row[3])}
                    link = cls.create(**names)
                    obj.append(link)
        return obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draws using turtle """
        t = turtle.Turtle()
        turtle.title("The Turtle")
        t.pen(pencolor="green", fillcolor="orange", pensize=4, speed=1)
        t.pensize(4)
        for i in list_rectangles:
            t.up()
            t.goto(i.x, i.y)
            t.down()
            for j in range(2):
                t.begin_fill()
                t.fd(i.width)
                t.lt(90)
                t.fd(i.height)
                t.lt(90)
                t.end_fill()
        for i in list_squares:
            t.up()
            t.goto(i.x, i.y)
            t.down()
            for j in range(2):
                t.fd(i.size)
                t.lt(90)
                t.fd(i.size)
                t.lt(90)
