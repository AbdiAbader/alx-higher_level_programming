#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    '''return a list of integers of pascal triangle '''
    newlist = []
    for i in range(n):
        newlist.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                newlist[i].append(1)
            else:
                newlist[i].append(newlist[i - 1][j - 1] + newlist[i - 1][j])
    return newlist
