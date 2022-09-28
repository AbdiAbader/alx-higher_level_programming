#!/usr/bin/python3
""" creates a list of json """


import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
a = []
if len(sys.argv) != 1:
    for i in range(1, len(sys.argv)):
        a.append(sys.argv[i])
save_to_json_file(a, filename)
p = load_from_json_file(filename)
print(p)
