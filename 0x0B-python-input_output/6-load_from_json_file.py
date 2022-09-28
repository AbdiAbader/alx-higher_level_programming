#!/usr/bin/python3
import json
""" form json to object """


def load_from_json_file(filename):
    """ creates object from JSON file """
    with open(filename, encoding='utf-8') as f:
        json.loads(f.read())
