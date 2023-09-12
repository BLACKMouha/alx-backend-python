#!/usr/bin/env python3
'''test_client module'''
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Test cases for testing GithubOrgClient class'''

    @parameterized.expand([
        ('google', {'response': 'GOOD :D'}),
        ('abc', {'response': 'BAD :('})
    ])
    @patch('client.get_json', new_callable=Mock)
    def test_org(self, org_name, response, mock):
        '''Test cases for GithubOrgClient.org method'''
        goc = GithubOrgClient(org_name=org_name)
        url = goc.ORG_URL.format(org=org_name)
        mock(url).return_value = response
        mock.assert_called_once_with(url)
        self.assertEqual(response, goc.org())
        return

    @parameterized.expand([
        ('google', {'repos_url': 'https://api.github.com/orgs/google/repos'}),
        ('abc', {'message': 'Not found!'})
    ])
    def test_public_repos_url(self, org_name, response):
        '''Test cases for GithubOrgClient._public_repos_url'''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            goc = GithubOrgClient(org_name=org_name)
            url = goc.ORG_URL.format(org=org_name)
            mock.return_value = response
            if 'repos_url' in response:
                self.assertEqual(response['repos_url'], goc._public_repos_url)
            else:
                self.assertRaises(KeyError,
                                  msg=response['message'])
        return

    @patch("client.get_json", new_callable=Mock)
    def test_public_repos(self, mock_get_json):
        '''Test cases for GithubOrgClient.public_repos and
        GihubOrgClient.public_repos'''
        response = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                },
                {
                    "id": 7776515,
                    "name": "cpp-netlib",
                },
            ],
            'repos_name': ['episodes.dart', 'cpp-netlib']
        }
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pru:
            mock_get_json.return_value = response["repos"]
            mock_pru.return_value = response["repos_url"]
            goc = GithubOrgClient('google')
            self.assertEqual(
                goc.public_repos(), response['repos_name'])
        mock_get_json.assert_called_once()
        mock_pru.assert_called_once()
