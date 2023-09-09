#!/usr/bin/env python3
"""test_utils module"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''Test cases for testing access_nested_map method'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, a, b, e):
        '''Checks if the access_nested_map returns the correct output'''
        self.assertEqual(access_nested_map(a, b), e)


if __name__ == '__main__':
    unittest.main()
