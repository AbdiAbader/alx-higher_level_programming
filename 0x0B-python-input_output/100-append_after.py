#!/usr/bin/python3
""" Search and update """


def append_after(filename="", search_string="", new_string=""):
    """ append after specific string """
    with open(filename, mode="r+", encoding="utf-8") as f:
        t = ""
        for i in f:
            t += i
            if search_string in i:
                t += new_string
        f.seek(0)
        f.write(t)
