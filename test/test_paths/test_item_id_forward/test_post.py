# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import apollo2_api_client
from apollo2_api_client.paths.item_id_forward import post  # noqa: E501
from apollo2_api_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestItemIdForward(ApiTestMixin, unittest.TestCase):
    """
    ItemIdForward unit test stubs
        Item Id Forward Batch Translate  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
