#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Returns True if value has been correctly printed
     (it means the value is an integer)
     Otherwise, returns False and prints in stderr the error precede by
     Exception:"""
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as a:
        sys.stderr.write("Exception: {}\n".format(a))
        return False
    return True
