# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from apollo2_api_client.paths.media_item_get.post import MediaItemBatchGet
from apollo2_api_client.paths.media_item_count.get import MediaItemCountGet
from apollo2_api_client.paths.media_item.get import MediaItemGet
from apollo2_api_client.paths.media_item_id.delete import MediaItemIdDelete
from apollo2_api_client.paths.media_item_id.get import MediaItemIdGet
from apollo2_api_client.paths.media_item_id_identifer.get import MediaItemIdIdentiferGet
from apollo2_api_client.paths.media_item_identifer_delete.post import MediaItemIdentiferDelete
from apollo2_api_client.paths.media_item_identifer_post.post import MediaItemIdentiferPost
from apollo2_api_client.paths.media_item_max_id.get import MediaItemMaxIdGet


class MediaItemApi(
    MediaItemBatchGet,
    MediaItemCountGet,
    MediaItemGet,
    MediaItemIdDelete,
    MediaItemIdGet,
    MediaItemIdIdentiferGet,
    MediaItemIdentiferDelete,
    MediaItemIdentiferPost,
    MediaItemMaxIdGet,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
