#!/usr/bin/python3
def magic_calculation(a, b):
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("To far")
            else:
                result = a ** b
                result /= i
        except:
            result = a + b
            break
    return result
