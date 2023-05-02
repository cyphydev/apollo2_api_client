# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import apollo2_api_client
from apollo2_api_client.models.cluster import Cluster  # noqa: E501
from apollo2_api_client.rest import ApiException

class TestCluster(unittest.TestCase):
    """Cluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Cluster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Cluster`
        """
        model = apollo2_api_client.models.cluster.Cluster()  # noqa: E501
        if include_optional :
            return Cluster(
                id = 56, 
                description = '', 
                name = '', 
                provider = '', 
                tag = '', 
                version = '', 
                data = apollo2_api_client.models.data.Data(), 
                type = None
            )
        else :
            return Cluster(
                name = '',
                provider = '',
                tag = '',
                version = '',
        )
        """

    def testCluster(self):
        """Test Cluster"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
