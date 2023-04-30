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


class AccountType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enumeration.
    """
    
    @schemas.classproperty
    def MEDIA_UNSPECIFIED(cls):
        return cls("MEDIA_UNSPECIFIED")
    
    @schemas.classproperty
    def NEWS(cls):
        return cls("News")
    
    @schemas.classproperty
    def REDDIT(cls):
        return cls("Reddit")
    
    @schemas.classproperty
    def TWITTER(cls):
        return cls("Twitter")
    
    @schemas.classproperty
    def WEBPAGE(cls):
        return cls("Webpage")
    
    @schemas.classproperty
    def BLOG(cls):
        return cls("Blog")
    
    @schemas.classproperty
    def COMMENT(cls):
        return cls("Comment")
    
    @schemas.classproperty
    def FACEBOOK(cls):
        return cls("Facebook")
    
    @schemas.classproperty
    def FORUM(cls):
        return cls("Forum")
    
    @schemas.classproperty
    def GOOGLE_PLUS(cls):
        return cls("Google Plus")
    
    @schemas.classproperty
    def LINE(cls):
        return cls("LINE")
    
    @schemas.classproperty
    def SEARCH_RESULT(cls):
        return cls("Search Result")
    
    @schemas.classproperty
    def VK(cls):
        return cls("VK")
    
    @schemas.classproperty
    def BING(cls):
        return cls("Bing")
    
    @schemas.classproperty
    def WIKIPEDIA(cls):
        return cls("Wikipedia")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("Other")
