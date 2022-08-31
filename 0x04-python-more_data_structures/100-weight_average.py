#!/usr/bin/python3
def weight_average(my_list=[]):
    s = 0
    m = 1
    t = 0
    if len(my_list) == 0:
        return 0
    else:
        for x in my_list:
            m = 1
            for i in x:
                m *= i
            t += i
            s += m
        return s / t
