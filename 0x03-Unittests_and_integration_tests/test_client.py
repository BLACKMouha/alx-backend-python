#!/usr/bin/env python3
'''test_client module'''
import unittest
from unittest.mock import patch, Mock
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
