#!/usr/bin/python3
def magic_string(s=[0]):
    s[0] += 1
    return ', '.join("BestSchool" for i in range(s[0]))
