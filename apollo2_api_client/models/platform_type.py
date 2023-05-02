# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PlatformType(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    NEWS = 'News'
    REDDIT = 'Reddit'
    TWITTER = 'Twitter'
    YOUTUBE = 'Youtube'
    MEDIA_UNSPECIFIED = 'MEDIA_UNSPECIFIED'
    WEBPAGE = 'Webpage'
    BLOG = 'Blog'
    COMMENT = 'Comment'
    FACEBOOK = 'Facebook'
    FORUM = 'Forum'
    GOOGLE_PLUS = 'Google Plus'
    LINE = 'LINE'
    SEARCH_RESULT = 'Search Result'
    VK = 'VK'
    BING = 'Bing'
    WIKIPEDIA = 'Wikipedia'
    OTHER = 'Other'
