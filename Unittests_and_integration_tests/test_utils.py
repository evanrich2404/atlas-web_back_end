#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize
)

"""
Unittesting for Utils
Modules:
access_nested_map,
get_json,
memoize
"""


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for access_nested_map function:
    "test_access_nested_map" method checks to see if it returns
    what it is supposed to,
    "test_access_nested_map_exception" method is checking for
    errors or more specifically if it checks for errors properly
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, missing_key):
        with self.assertRaises(KeyError) as conman:
            access_nested_map(nested_map, path)
        self.assertEqual(str(conman.exception), repr(missing_key))


class TestGetJson(unittest.TestCase):
    """
    Test cases for get_json function:
    "test_get_json" method tests that it returns the expected result
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        mock_get.return_value = mock_resp

        response = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases for memoize function:
    "test_memoize" method that makes sure when calling a_property twice,
    the correct result is returned but a_method is only called once
    """
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_a_method:
            test_class = TestClass()
            result1 = test_class.a_property
            result2 = test_class.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
