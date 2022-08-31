#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s1 = set(set_1)
    s2 = set(set_2)
    return s1 ^ s2
