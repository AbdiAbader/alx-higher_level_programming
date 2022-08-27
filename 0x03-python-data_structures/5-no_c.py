#!/usr/bin/python3
def no_c(my_string):
    if 'c' or 'C' in my_string:
        new_string = ""
        for i in range(len(my_string)):
            if 'C' != my_string[i] and 'c' != my_string[i]:
                new_string += my_string[i]
    return new_string
