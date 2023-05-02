# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import apollo2_api_client
from apollo2_api_client.api.media_item_api import MediaItemApi  # noqa: E501
from apollo2_api_client.rest import ApiException


class TestMediaItemApi(unittest.TestCase):
    """MediaItemApi unit test stubs"""

    def setUp(self):
        self.api = apollo2_api_client.api.media_item_api.MediaItemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_media_item_batch_get(self):
        """Test case for media_item_batch_get

        Media Item Batch Get  # noqa: E501
        """
        pass

    def test_media_item_count_get(self):
        """Test case for media_item_count_get

        Media Item Count Get  # noqa: E501
        """
        pass

    def test_media_item_get(self):
        """Test case for media_item_get

        Media Item Get  # noqa: E501
        """
        pass

    def test_media_item_id_delete(self):
        """Test case for media_item_id_delete

        Media Item Id Delete  # noqa: E501
        """
        pass

    def test_media_item_id_get(self):
        """Test case for media_item_id_get

        Media Item Id Get  # noqa: E501
        """
        pass

    def test_media_item_id_identifer_get(self):
        """Test case for media_item_id_identifer_get

        Media Item Id Identifer Get  # noqa: E501
        """
        pass

    def test_media_item_identifer_delete(self):
        """Test case for media_item_identifer_delete

        Media Item Identifer Delete  # noqa: E501
        """
        pass

    def test_media_item_identifer_post(self):
        """Test case for media_item_identifer_post

        Media Item Identifer Post  # noqa: E501
        """
        pass

    def test_media_item_max_id_get(self):
        """Test case for media_item_max_id_get

        Media Item Max Id Get  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
