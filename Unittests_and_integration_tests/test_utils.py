#!/usr/bin/env python3
"""
Unittesting for Utils
Modules:
access_nested_map,
get_json,
memoize
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize
)




class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for access_nested_map function.

    Tests that access_nested_map correctly accesses nested elemenets
    and raises a KeyError when a key is missing.

    Methods:
    - test_access_nested_map: Tests that access_nested_map correctly accesses
    nested elements and returns the correct result.
    - test_access_nested_map_exception: Tests that access_nested_map raises a
    KeyError with the correct message when a key is missing.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        uses the parameterized decorator to test with different inputs.

        Args:
        - nested_map: The nested map to access.
        - path: The path to the element to access.
        - expected: The expected result.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, missing_key):
        """
        uses parameterized...

        Args:
        ditto...
        ditto...
        - missing_key: The key that is missing from the nested map.
        """
        with self.assertRaises(KeyError) as conman:
            access_nested_map(nested_map, path)
        self.assertEqual(str(conman.exception), repr(missing_key))


class TestGetJson(unittest.TestCase):
    """
    Test cases for get_json function.

    This class contains unit tests for the get_json function.
    It tests that get_json makes the correct HTTP requests
    and returns the correct results.

    Methods:
    -test_get_json: Tests that get_json makes a request to the correct URL
    and returns the correct result.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        uses parameterized and patch decorators to test get_json with
        different inputs and without making actual HTTP requests.
        It checks that get_json makes a request to the correct URL
        and that it returns the correct result.

        Args:
        - test_url: The URL that get_json should make a request to.
        - test_payload: The result that get_json should return.
        - mock_get: A mock of the requests.get function.
        """
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        mock_get.return_value = mock_resp

        response = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases for memoize decorator.

    tests that a method decorated with @memoize is called multiple times,
    the method it decorates is only called once.

    Methods:
    - test_memoize: Tests that when a_property (decorated with @memoize) is
    called multiple times, a_method is only called once.
    """
    def test_memoize(self):
        """
        ditto...

        This test uses the patch.object decorator to replace a_method with a
        mock method. It checks that when a_property is called multiple times,
        a_method is only called once.
        """
        class TestClass:
            """
            A class created to test the memoize decorator.

            This class contains a method (a_method) and a property (a_property)
            that is decorated with @memoize and calls a_method.

            Methods:
            - a_method: A method that returns 42.
            - a_property: A property that is decorated with @memoize and calls
            a_method.
            """
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
