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
        dictionary = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(json_dict, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')
        self.assertTrue(type(json_dict) is str)

    def test_to_json_string_none(self):
