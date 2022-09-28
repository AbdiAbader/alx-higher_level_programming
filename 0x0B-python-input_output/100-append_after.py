#!/usr/bin/python3
""" Search and update """


def append_after(filename="", search_string="", new_string=""):
    """ append after specific string """
    with open(filename) as f:
        t = ""
        for i in f:
            t += i
            if i in search_string:
                t += new_string
    with open(filename, 'w') as f:
        f.write(t)
