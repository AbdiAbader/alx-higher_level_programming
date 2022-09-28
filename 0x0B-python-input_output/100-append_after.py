#!/usr/bin/python3
""" Search and update """


def append_after(filename="", search_string="", new_string=""):
    """ append after specific string """
    with open(filename, 'r+') as f:
        t = ""
        for i in f:
            t += i
            if i ==  search_string:
                t += new_string
        f.seek(0, 0)
        f.write(t)
