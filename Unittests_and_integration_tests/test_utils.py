#!/usr/bin/env python3
import unittest
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
    errors or more specifically if it checks for errors properly,
    ""
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
