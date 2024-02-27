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
        self.assertEqual(base1.id, 2)

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

    def test_save_to_file_none(self):
        """
        Test Base class method save_to_file with None input
        """
        Base.save_to_file(None)
        self.assertTrue(os.path.exists)
        with open("Base.json", 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file(self):
        """
        Test Base class method save_to_file with a valid input.
        """
        s1 = Square(5)
        Base.save_to_file([s1])
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", 'r') as file:
            self.assertEqual(file.read(),
                             '[{"id": 3, "x": 0, "size": 5, "y": 0}]')

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

    def test_create_rectangle(self):
        """
        Test Base class method create for creating a rectangle instance.
        """
        rect_dict = {'width': 3, 'height': 5, 'x': 1, 'y': 0, 'id': '1'}
        rect_inst = Rectangle.create(**rect_dict)
        self.assertEqual(str(rect_inst), "[Rectangle] (1) 1/0 - 3/5")
        


if __name__ == '__main__':
    unittest.main()