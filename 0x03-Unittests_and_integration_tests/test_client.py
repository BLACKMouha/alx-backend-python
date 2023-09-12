#!/usr/bin/env python3
'''test_client module'''
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
import requests
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        return

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, boolean):
        '''Test case for GithubOrgClient.test_has_license method'''
        goc = GithubOrgClient('google')
        r = goc.has_license(repo, license_key)
        with patch.object(GithubOrgClient,
                          'has_license',
                          return_value=boolean,
                          new_callable=Mock) as mock_has_license:
            self.assertEqual(r, boolean)
        return


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration test cases for testing GithubOrgClient class'''

    @classmethod
    def setUpClass(cls):
        urls = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in urls:
                return Mock(**{'json.return_value': urls[url]})
            return Mock(**{'json.side_effect': KeyError('repos_url')})
        cls.get_patcher = patch('requests.get', get_payload)
        cls.mock_get = cls.get_patcher.start()
        cls.addClassCleanup(cls.get_patcher.stop)

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(cls):
        '''Integration test cases for GithubOrgClient.public_repos method'''
        goc = GithubOrgClient('google')
        cls.assertEqual(goc.public_repos(), cls.expected_repos)
        return

    def test_public_repos_with_license(cls):
        '''Integration test cases for public repos with license'''
        goc = GithubOrgClient('google')
        cls.assertEqual(
            goc.public_repos(license='apache-2.0'),
            cls.apache2_repos
        )
