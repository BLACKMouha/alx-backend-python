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

    @parameterized.expand([
        (
            'google',
            {
                'repos_url': 'https://api.github.com/orgs/google/repos',
                'repos': [
                    {
                        "id": 7697149,
                        "name": "episodes.dart",
                    },
                    {
                        "id": 7776515,
                        "name": "cpp-netlib",
                    }
                ]
            },
            ['episodes.dart', 'cpp-netlib']
        ),
        (
            'abc',
            {'message': 'Not Found'},
            [KeyError, 'repos_url']
        )
    ])
    @patch('client.get_json', new_callable=Mock)
    def test_public_repos(self, org_name, response, public_repos, mock_get_json):
        '''Test cases for GithubOrgClient.public_repos and
        GihubOrgClient.public_repos_url'''
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pru:
            goc = GithubOrgClient(org_name)
            if 'repos_url' in response:
                mock_pru.return_value = response['repos_url']
                mock_get_json.return_value = response['repos']
                self.assertEqual(goc._public_repos_url, response['repos_url'])
                self.assertEqual(goc.public_repos(),
                                 public_repos)
                mock_get_json.assert_called_once_with(response['repos_url'])
            else:
                self.assertRaises(KeyError, msg='repos_url')
            
