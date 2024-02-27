#!/usr/bin/python3
"""
Test module for the models package.

This module contains unit tests for the classes and functionalities
defined in the models package, including the Base, Rectangle, and
Square classes.

The tests cover initialization, attribute manipulation, serialization,
deserialization, file saving/loading, and other functionalities
provided by the classes.

Author: Zubby Peculiar
"""

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """
    def test_init(self):
        """
        Test initialization of Base class with id.
        """
        base1 = Base()
        self.assertEqual(base1.id, 1)

    def test_init_with_id(self):
        """
        Test initialization of Base class with id.
        """
        base12 = Base(12)
        self.assertEqual(base12.id, 12)

    def test_init_with_two_args(self):
        """
        Test initialization of Base class with 2 arguments
        """
        with self.assertRaises(TypeError):
            base2_3 = Base(2, 3)

    def test_to_json_string(self):
        """
        Test Base class method to_json_string valid.
        """
        dictionary = {'id': 1, 'size': 5, 'x': 2, 'y': 8}
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(json_dict,
                         '[{"id": 1, "size": 5, "x": 2, "y": 8}]')
        self.assertTrue(type(json_dict) is str)

    def test_to_json_string_none(self):
        """
        Test Base class method to_json_string with None input.
        """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """
        Test Base class method to_json_string with an empty list.
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        """
        Test Base class method save_to_file with a valid input.
        """
        s1 = Square(5)
        Base.save_to_file([s1])
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", 'r') as file:
            self.assertEqual(file.read(),
                             '[{"id": 2, "x": 0, "size": 5, "y": 0}]')

    def test_save_to_file_none(self):
        """
        Test Base class method save_to_file with None input
        """
        Base.save_to_file(None)
        self.assertTrue(os.path.exists)
        with open("Base.json", 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_from_json_string_none(self):
        """
        Test Base class method from_json_string with None input.
        """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list(self):
        """
        Test Base class method from_json_string with an empty list.
        """
        self.assertEqual(Base.from_json_string([]), [])

    def from_json_string(self):
        """
        Test Base class method from_json_string with a valid string.
        """
        json_dict = '[{"id": 1, "size": 5, "x": 2, "y": 8}]'
        dictionary = Base.from_json_string(json_dict)
        self.assertEqual(dictionary,
                         [{'id': 1, 'size': 5, 'x': 2, 'y': 8}])
        self.assertTrue(type(dictionary) is list)


class TestBase_load_json(unittest.TestCase):
    """
    Unittes for load from Json file
    """
    def test_load_from_file_nonexistent(self):
        """
        Test Base class method load_from_file with a nonexistent file.
        """
        try:
            os.remove("Square.json")
        except IOError:
            pass
        empty_output = Square.load_from_file()
        self.assertEqual(empty_output, [])

    def test_load_from_file_valid(self):
        """
        Test Base class method load_from_file with a valid file.
        """
        sqr = [Square(5)]
        Square.save_to_file(sqr)
        sqr_str = Square.load_from_file()
        self.assertEqual(str(sqr_str[0]), "[Square] (5) 0/0 - 5")


class TestBase_create(unittest.TestCase):
    """
    Unittest for the create method
    """

    def test_create_rectangle(self):
        """
        Test Base class method create for creating a rectangle instance.
        """
        rect_dict = {'width': 3, 'height': 5, 'x': 1, 'y': 0, 'id': '17'}
        rect_inst = Rectangle.create(**rect_dict)
        self.assertEqual(str(rect_inst), "[Rectangle] (17) 1/0 - 3/5")

    def test_create_square(self):
        """
        Test Base class method create for creating a square instance.
        """
        sqr_dict = {'size': 5, 'x': 2, 'y': 1, 'id': '18'}
        sqr_inst = Square.create(**sqr_dict)
        self.assertEqual(str(sqr_inst), "[Square] (18) 2/1 - 5")


class Testbase_save_to_csv(unittest.TestCase):
    """
    Test cases for the save_to_file_csv methods.
    """
    def test_save_to_csv_rectangle(self):
        """
        Test saving rectangle instances to CSV file.
        """
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass

        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(2, 4)
        list_rectangles_input = [rect1, rect2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        with open("Rectangle.csv", 'r') as file:
            self.assertEqual('9,10,7,2,8\n10,2,4,0,0\n', file.read())

    def test_save_to_csv_square(self):
        """
        Test saving square instances to CSV file.
        """
        try:
            os.remove("Square.csv")
        except IOError:
            pass

        sqr1 = Square(5)
        sqr2 = Square(7, 9, 1)
        list_squares_input = [sqr1, sqr2]
        Square.save_to_file_csv(list_squares_input)
        with open("Square.csv", 'r') as file:
            self.assertEqual('11,5,0,0\n12,7,9,1\n', file.read())


if __name__ == '__main__':
    unittest.main()
