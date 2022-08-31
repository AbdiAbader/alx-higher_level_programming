#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    s = sum([i for i in my_list])
    return s
