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
from apollo2_api_client.models.raw_data_post_request import RawDataPostRequest  # noqa: E501
from apollo2_api_client.rest import ApiException

class TestRawDataPostRequest(unittest.TestCase):
    """RawDataPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RawDataPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RawDataPostRequest`
        """
        model = apollo2_api_client.models.raw_data_post_request.RawDataPostRequest()  # noqa: E501
        if include_optional :
            return RawDataPostRequest(
                override = True, 
                data = [
                    apollo2_api_client.models.raw_data_post_entry.RawDataPostEntry(
                        source = apollo2_api_client.models.source.Source(
                            id = '', 
                            type = '', 
                            platform = 'News', 
                            sid = 56, 
                            enrichments = [
                                null
                                ], 
                            clusters = [
                                apollo2_api_client.models.cluster_member.ClusterMember(
                                    id = 56, 
                                    cluster_id = 56, 
                                    node_id = 56, 
                                    data = apollo2_api_client.models.data.Data(), )
                                ], 
                            name = '', 
                            data = null, ), 
                        items = [
                            apollo2_api_client.models.item.Item(
                                id = '', 
                                author = '', 
                                platform = 'News', 
                                time_published = 56, 
                                sid = 56, 
                                source_id = 56, 
                                enrichments = [
                                    null
                                    ], 
                                clusters = [
                                    apollo2_api_client.models.cluster_member.ClusterMember(
                                        id = 56, 
                                        cluster_id = 56, 
                                        node_id = 56, )
                                    ], 
                                media_items = [
                                    apollo2_api_client.models.media_item.MediaItem(
                                        id = 56, 
                                        type = 'Link', 
                                        content = '', )
                                    ], 
                                text = '', 
                                data = null, )
                            ], )
                    ]
            )
        else :
            return RawDataPostRequest(
                data = [
                    apollo2_api_client.models.raw_data_post_entry.RawDataPostEntry(
                        source = apollo2_api_client.models.source.Source(
                            id = '', 
                            type = '', 
                            platform = 'News', 
                            sid = 56, 
                            enrichments = [
                                null
                                ], 
                            clusters = [
                                apollo2_api_client.models.cluster_member.ClusterMember(
                                    id = 56, 
                                    cluster_id = 56, 
                                    node_id = 56, 
                                    data = apollo2_api_client.models.data.Data(), )
                                ], 
                            name = '', 
                            data = null, ), 
                        items = [
                            apollo2_api_client.models.item.Item(
                                id = '', 
                                author = '', 
                                platform = 'News', 
                                time_published = 56, 
                                sid = 56, 
                                source_id = 56, 
                                enrichments = [
                                    null
                                    ], 
                                clusters = [
                                    apollo2_api_client.models.cluster_member.ClusterMember(
                                        id = 56, 
                                        cluster_id = 56, 
                                        node_id = 56, )
                                    ], 
                                media_items = [
                                    apollo2_api_client.models.media_item.MediaItem(
                                        id = 56, 
                                        type = 'Link', 
                                        content = '', )
                                    ], 
                                text = '', 
                                data = null, )
                            ], )
                    ],
        )
        """

    def testRawDataPostRequest(self):
        """Test RawDataPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
