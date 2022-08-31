#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if isinstance(roman_string, str):
        for i in roman_string:
            for keys, values in rome.items():
                if i == keys:
                    sum += values
        return sum
    else:
        return None
