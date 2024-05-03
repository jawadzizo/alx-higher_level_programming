#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def setUp(self):
        """sets up some variables for the test"""

        self.full_list = [0, 3, 5, 1, 4]
        self.empty_list = []
        self.string = "hello world"

    def test_max(self):
        """tests the max_integer function"""
        self.assertEqual(max_integer(self.full_list), 5)
        self.assertIsInstance(max_integer(self.full_list), int)

        self.assertEqual(max_integer(self.empty_list), None)

        self.assertEqual(max_integer(self.string), 'w')


if __name__ == "__main__":
    unittest.main()
