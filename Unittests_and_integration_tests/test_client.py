#!/usr/bin/env python3
"""testing testing 321"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """CLASS - tests 'GithubOrgClient'
    """

    # below are inputs to be tested in 'test_org'
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """tests GithubOrgClient.org is returning correctly
        """
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """tests '_public_repos_url' is returning correctly
        """
        test_payload = {"repos_url":
                        "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = test_payload
        test_client = GithubOrgClient("google")
        result = test_client._public_repos_url
        self.assertEqual(result, test_payload["repos_url"])

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """tests that the list of repos is correct
        """
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        mock_public_repos_url.return_value = \
            "https://api.github.com/orgs/google/repos"

        test_client = GithubOrgClient("google")
        result = test_client.public_repos()
        self.assertEqual(result, ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    # below are inputs to be tested in 'test_has_license'
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Tests the has_license function from the GithubOrgClient class"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


# integration test - only mock code that sends external requests
@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0][0], "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2], "apache2_repos": TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """CLASS - tests 'public_repos' in the 'GithubOrgClient'
    """

    @classmethod
    def setUpClass(cls):
        """METHOD - sets up the class for integration testing
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            if url == "https://api.github.com/orgs/google/repos":
                return cls.repos_payload
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """METHOD - "tears down" the used class from integration testing
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """tests public repos without a license
        """
        test_client = GithubOrgClient("google")
        result = test_client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """tests public repos with a license
        """
        test_client = GithubOrgClient("google")
        result = test_client.public_repos("apache-2.0")
        self.assertEqual(result, self.apache2_repos)
