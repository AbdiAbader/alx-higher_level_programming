#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list):
        rev = reversed(my_list)
        for i in rev:
            print("{:d}".format(i))
