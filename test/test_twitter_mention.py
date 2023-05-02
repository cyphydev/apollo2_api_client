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
from apollo2_api_client.models.twitter_mention import TwitterMention  # noqa: E501
from apollo2_api_client.rest import ApiException

class TestTwitterMention(unittest.TestCase):
    """TwitterMention unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TwitterMention
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TwitterMention`
        """
        model = apollo2_api_client.models.twitter_mention.TwitterMention()  # noqa: E501
        if include_optional :
            return TwitterMention(
                end = 56, 
                id = '', 
                start = 56, 
                username = ''
            )
        else :
            return TwitterMention(
        )
        """

    def testTwitterMention(self):
        """Test TwitterMention"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
