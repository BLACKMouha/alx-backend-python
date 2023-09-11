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
        (
            'google',
            {'repos_url': 'https://api.github.com/orgs/google/repos'},
            ['episodes.dart', 'cpp-netlib']
        ),
        (
            'abc',
            {'message': 'Not found!'},
            []
        )
    ])
    @patch('client.get_json', new_callable=Mock)
    def test_public_repos_url(self, org_name, response, repos, mock_get_json):
        '''Test cases for GithubOrgClient._public_repos_url and
        GihubOrgClient.public_repos_url'''
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pru:
            goc = GithubOrgClient(org_name=org_name)
            url = goc.ORG_URL.format(org=org_name)
            if 'repos_url' in response:
                mock_pru.return_value = response['repos_url']
                mock_get_json(response['repos_url']).return_value = repos
                self.assertEqual(response['repos_url'], goc._public_repos_url)
            else:
                self.assertRaises(KeyError,
                                  msg=response['message'])
        return
