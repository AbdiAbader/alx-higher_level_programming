#!/usr/bin/python3
""" form json to object """


import json


def load_from_json_file(filename):
    """ creates object from JSON file """
    with open(filename) as f:
        return json.load(f)
