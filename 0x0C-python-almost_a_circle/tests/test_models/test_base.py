#!/usr/bin/python3
"""
    tests for 0x0C. Python - Almost a circle:
        task 1
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import path


class Test_Base(unittest.TestCase):
    """test Base id"""

    def test_a_no_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_int_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_a_no_id_2(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_str_id(self):
        b1 = Base('hola')
        self.assertEqual(b1.id, 'hola')

    def test_a_none_id(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 3)

    def test_neg_id(self):
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_zero_id(self):
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_documentation(self):
        self.assertTrue(len(Base.__doc__) > 0)
        self.assertTrue(len(Base.__doc__) > 0)
        self.assertTrue(len(Base.to_json_string.__doc__) > 0)
        self.assertTrue(len(Base.create.__doc__) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

    def test_z_create_r(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertDictEqual(r1_dictionary, r2.to_dictionary())

    def test_z_create_s(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertDictEqual(s1_dictionary, s2.to_dictionary())


# Tests for json

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)


    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        self.assertTrue(path.isfile('Rectangle.json'))

        s2 = Square(2)
        Square.save_to_file([s2])
        with open("Square.json", "r") as my_file:
            read = my_file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(s2.to_dictionary(), my_list[0])

    def test_from_json_string_r(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(json_list_input) is str)
        self.assertTrue(type(list_output) is list)

    def test_from_json_string_s(self):
        list_input = [
            {'id': 89, 'width': 10}, 
            {'id': 7, 'width': 1}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertTrue(type(json_list_input) is str)
        self.assertTrue(type(list_output) is list)

    def test_load_from_file_r(self):
        r1 = Rectangle(10, 7, 2, 8, 89)
        r2 = Rectangle(2, 4, 0, 0, 90)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        
        self.assertEqual(list_rectangles_input[1].__str__(),
                                    "[Rectangle] (90) 0/0 - 2/4")
        self.assertEqual(list_rectangles_output[1].__str__(),
                                    "[Rectangle] (90) 0/0 - 2/4")

    def test_load_from_file_s(self):
        s1 = Square(10, 7, 2, 89)
        s2 = Square(2, 4, 0, 90)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
       

if __name__ == '__main__':
    unittest.main()
