#!/usr/bin/env python3
"""
Tests for client.py
"""
import unittest
from unittest.mock import patch, PropertyMock
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
    def test_org(self, org_name, mock_get_json):
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
        self.assertEqual(response, {"fake_key": "fake_value"})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Tests that _public_repos_url returns the correct value.

        Uses the patch function as context manager to mock the org property.

        Arg:
        - mock_org: A mock of the org property.
        """
        mock_org.return_value = {"repos_url": "mock_url"}
        test_client = GithubOrgClient("org_name")
        response = test_client._public_repos_url

        self.assertEqual(response, "mock_url")
