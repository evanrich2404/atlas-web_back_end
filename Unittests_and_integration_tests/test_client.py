#!/usr/bin/env python3
"""
Tests for client.py
"""
import unittest
import requests
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from utils import (
    access_nested_map,
    get_json,
    memoize
)
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD

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

    @patch('client.get_json', return_value=[{"name": "mock_repo"}])
    def test_public_repos(self, mock_get_json):
        """
        Tests that public_repos returns the correct value.

        Uses the patch function as a decorator to mock the get_json function,
        and as a context manager to mock the _public_repos_url property.

        Arg:
        - mock_get_json: A mock of the get_json function
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'mock_url'
            test_client = GithubOrgClient('org_name')
            response = test_client.public_repos()

            self.assertEqual(response, ["mock_repo"])
            mock_get_json.assert_called_once_with('mock_url')
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Tests that GithubOrgClient.has_license returns the correct value.

        This test uses parameterized.expand decorator to test multiple inputs
        for the has_license method.

        Args:
        - repo: The repo dictionary to test.
        - license_key: The license key to test.
        - expected: The expected return value from the has_license method.
        """
        test_client = GithubOrgClient("org_name")
        response = test_client.has_license(repo, license_key)

        self.assertEqual(response, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up the class by starting
        a patcher that mocks requests.get to return example payloads.
        """
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            cls.org_payload,
            cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class by stopping the patcher.
        """
        cls.get_patcher.stop()
