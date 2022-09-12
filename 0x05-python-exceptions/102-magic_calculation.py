#!/usr/bin/python3
def magic_calculation(a, b):
    for i in range(1, 3):
        i += 1
    if i > a:
       raise("To far")
    else:
        result = a ** b
    result /= i
    result += a+b
    return result
