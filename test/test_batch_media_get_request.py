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
from apollo2_api_client.models.batch_media_get_request import BatchMediaGetRequest  # noqa: E501
from apollo2_api_client.rest import ApiException

class TestBatchMediaGetRequest(unittest.TestCase):
    """BatchMediaGetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BatchMediaGetRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchMediaGetRequest`
        """
        model = apollo2_api_client.models.batch_media_get_request.BatchMediaGetRequest()  # noqa: E501
        if include_optional :
            return BatchMediaGetRequest(
                ids = [
                    56
                    ]
            )
        else :
            return BatchMediaGetRequest(
                ids = [
                    56
                    ],
        )
        """

    def testBatchMediaGetRequest(self):
        """Test BatchMediaGetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
