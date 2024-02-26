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

from models.base import Base
import unittest
import json
import os


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
        with self.assertRaises(TypeError):
            base2_3 = Base(2, 3)
        """

    def test_to_json_string(self):
        """
        Test Base class method to_json_string with an empty list.
        """
        dictionary = {'id': 1, 'size': 10, 'x': 2, 'y': 8}
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

        """
        self.assertEqual(Base.to_json_string(None), "[]")


if __name__ == '__main__':
    unittest.main()
