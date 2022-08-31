#!/usr/bin/python3
def roman_to_int(roman_string):
    sum1 = 0
    j = 0
    rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is str and not None:
        r = list(reversed(list(roman_string)))
        for i in r:
            for keys, values in rome.items():
                if i == keys:
                    if values >= j:
                        sum1 += values
                        j = values
                    else:
                        sum1 -= values
        return sum1
    else:
        return sum1
