#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = [0, 0]
    if len(tuple_a) >= 2:
        x[0] += tuple_a[0]
        x[1] += tuple_a[1]
    elif tuple_a:
        x[0] += tuple_a[0]
    if len(tuple_b) >= 2:
        x[0] += tuple_b[0]
        x[1] += tuple_b[1]
    elif tuple_b:
        x[0] += tuple_b[0]
    new = (x[0], x[1])
    return new
