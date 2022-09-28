#!/usr/bin/python3
""" function returns JSON representation of an object """


import json


def to_json_string(my_obj):
    """ returns json representation """
    return json.dumps(my_obj)
