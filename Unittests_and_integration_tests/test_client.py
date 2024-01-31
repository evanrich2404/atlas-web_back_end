#!/usr/bin/env python3
"""
Tests for client.py
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize
)
from client import GithubOrgClient



class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for client.py and it's class GithubOrgClient
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """
        Tests that GithubOrgClient returns the correct value.

        This test uses parameterized.expand decorator to test multiple inputs
        for the org method, and the patch decorator to mock get_json.

        Args:
        - org_name: The name of the Github organization to test.
        - expected_payload: The expected return value from the get_json func.
        - mock_get_json: A mock of the get_json function.
        """
        test_client = GithubOrgClient(org_name)
        mock_get_json.return_value = {"fake_key": "fake_value"}
        response = test_client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(response, expected_payload)
