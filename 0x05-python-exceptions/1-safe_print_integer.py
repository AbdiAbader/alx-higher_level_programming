#!/usr/bin/python3
def safe_print_integer(value):
    """ Returns True if value has been correctly printed
(it means the value is an integer)"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
