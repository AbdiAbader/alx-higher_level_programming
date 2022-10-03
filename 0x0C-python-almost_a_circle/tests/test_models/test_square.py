#!/usr/bin/python3
"""Tests for Square"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square(unittest.TestCase):
    """testing Square"""

    def test_empty(self):
        self.assertRaises(TypeError, Square, ())

    def test_size(self):
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -2)
        self.assertRaises(TypeError, Square, (1, 2))
        self.assertRaises(TypeError, Square, 'a')
        self.assertRaises(TypeError, Square, [1, 2, 3, 4])
        self.assertRaises(TypeError, Square, {'a': 'hola', 'b': 1})
        self.assertRaises(TypeError, Square, 1.5)
        self.assertRaises(TypeError, Square, 'nan')
        self.assertRaises(TypeError, Square, 'inf')
        Base._Base__nb_objects = 0
        s1 = Square(2)
        self.assertEqual(s1.size, 2)

    def test_x(self):
        self.assertRaises(ValueError, Square, 2, -5)
        for x in ['a', 'hola', (1, 2)]:
            with self.subTest(x=x):
                self.assertRaises(TypeError, Square, 2, x)

    def test_y(self):
        self.assertRaises(ValueError, Square, 2, 5, -2)
        for y in ['a', 'hola', (1, 2)]:
            with self.subTest(y=y):
                self.assertRaises(TypeError, Square, 2, 2, y)

    def test_area(self):
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)

    def test_update(self):
        s1 = Square(2, 4, 1)
        s1.update(89)
        self.assertEqual(s1.__str__(), '[Square] (89) 4/1 - 2')

if __name__ == '__main__':
    unittest.main()
