#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = 1
if (number < 0):
    s = -1
last = number * s % 10
if ((number * s) % 10 > 5):
    print(f'Last digit of {number} is {last} and is greater than 5')
elif ((number * s) % 10 == 0):
    print(f'Last digit of {number} is {last} is zero')
else:
    print(f'Last digit of {number} is {last} and is less than 6 and not 0')
