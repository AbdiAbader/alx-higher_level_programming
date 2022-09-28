#!/usr/bin/python3
""" 0 Read file """


def read_file(filename=""):
    """ read file """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
