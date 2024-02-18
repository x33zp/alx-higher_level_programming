#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_no_args(self):
        """Test for no argument passed"""
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        """Test for empty list"""
        self.assertIsNone(max_integer([]), None)

    def test_ordered_list(self):
        """Test for ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test for unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test for list with negative integers"""
        self.assertEqual(max_integer([-4, -8, -1, -6]), -1)

    def test_mixed_integers(self):
        """Test for list with mixed integers"""
        self.assertEqual(max_integer([-3, 2, 6.2, 0]), 6.2)

    def test_one_integers(self):
        """Test for one number in the list"""
        self.assertEqual(max_integer([9]), 9)

    def test_string_list(self):
        """Test for strings in list"""
        self.assertEqual(max_integer(["hello", "hi", "there"]), 'there', "it returns the string with the max ASCII value")

    def test_string_int(self):
        """Test for string and integers in list"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "hello", 4])

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()
