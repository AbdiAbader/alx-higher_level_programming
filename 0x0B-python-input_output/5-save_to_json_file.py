#!/usr/bin/python3
import json
""" sfunction save to json file """


def save_to_json_file(my_obj, filename):
    """ saves to json file """
    with open(filename, 'w') as f:
        json.dumps(my_obj, f)
