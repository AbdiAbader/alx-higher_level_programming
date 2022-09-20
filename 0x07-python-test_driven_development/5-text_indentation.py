#!/usr/bin/python3
"""
module
prints a text with 2 new lines after each of these characters: ., ? and :

"""


def text_indentation(text):
    """ tesxt indentation """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
