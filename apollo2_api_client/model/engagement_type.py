# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from apollo2_api_client import schemas  # noqa: F401


class EngagementType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enumeration.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ENGAGEMENT_UNSPECIFIED": "ENGAGEMENT_UNSPECIFIED",
            "mention": "MENTION",
            "quote": "QUOTE",
            "reply": "REPLY",
            "retweet": "RETWEET",
            "tweet": "TWEET",
            "page_post": "PAGE_POST",
        }
    
    @schemas.classproperty
    def ENGAGEMENT_UNSPECIFIED(cls):
        return cls("ENGAGEMENT_UNSPECIFIED")
    
    @schemas.classproperty
    def MENTION(cls):
        return cls("mention")
    
    @schemas.classproperty
    def QUOTE(cls):
        return cls("quote")
    
    @schemas.classproperty
    def REPLY(cls):
        return cls("reply")
    
    @schemas.classproperty
    def RETWEET(cls):
        return cls("retweet")
    
    @schemas.classproperty
    def TWEET(cls):
        return cls("tweet")
    
    @schemas.classproperty
    def PAGE_POST(cls):
        return cls("page_post")
