#!/usr/bin/env python3
"""test_utils module"""
from parameterized import parameterized
import unittest
from utils import (access_nested_map, get_json, memoize)
from unittest.mock import Mock, patch


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

    @parameterized.expand([
        ({}, ('a', )),
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, a, b):
        '''Checks if a KeyError is raised in the following cases'''
        self.assertRaises(KeyError, access_nested_map, a, b)


class TestGetJson(unittest.TestCase):
    '''Test cases for get_json method'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get', new_callable=Mock)
    def test_get_json(self, a, b, mock):
        mock(a).json.return_value = b
        mock.assert_called_with(a)
        self.assertEqual(get_json(a), b)


class TestMemoize(unittest.TestCase):
    '''Test cases for memoize method from utils module'''
    def test_memoize(self):
        class TestClass:
            '''TestClass for testing memoize method'''
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', new_callable=Mock) as mock:
            t = TestClass()
            mock.return_value = 42
            t.a_property
            r = t.a_property
            mock.assert_called_once()
            self.assertEqual(42, r)


if __name__ == '__main__':
    unittest.main()
