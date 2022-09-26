#!/usr/bin/python3
""" int Rebels inverts == and != """


class MyInt(int):
    """ class MYint """
    def __init_(self, num):
        self.num = num

    def __eq__(self, num):
        return num != num

    def __ne__(self, num):
        return num == num
