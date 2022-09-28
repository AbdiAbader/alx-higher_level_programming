#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """ pascal triangle """
    l = []
    a = 1
    for row in range(1, n + 1):
        for r in range(1, row + 1):
            l.append((row - r)/ r)
    return l
