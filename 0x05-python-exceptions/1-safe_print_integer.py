def safe_print_integer(value):
    """ Returns True if value has been correctly printed
(it means the value is an integer)"""
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    else:
        return True
