# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import apollo2_api_client
from apollo2_api_client.api.default_api import DefaultApi  # noqa: E501
from apollo2_api_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ping_get(self):
        """Test case for ping_get

        Ping Get  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
