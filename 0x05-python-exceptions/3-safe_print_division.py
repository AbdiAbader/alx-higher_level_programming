#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the value of the division, otherwise: None"""
    try:
        result = a / b
        print("Inside result: {}".format(result), end='')
    except ZeroDivisionError:
        print("Inside result: None", end='')
        return None
    finally:
        print("")
    return result
