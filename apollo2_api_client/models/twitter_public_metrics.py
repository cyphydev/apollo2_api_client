# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt

class TwitterPublicMetrics(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    like_count: Optional[StrictInt] = None
    quote_count: Optional[StrictInt] = None
    reply_count: Optional[StrictInt] = None
    retweet_count: Optional[StrictInt] = None
    followers_count: Optional[StrictInt] = None
    following_count: Optional[StrictInt] = None
    listed_count: Optional[StrictInt] = None
    tweet_count: Optional[StrictInt] = None
    __properties = ["like_count", "quote_count", "reply_count", "retweet_count", "followers_count", "following_count", "listed_count", "tweet_count"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TwitterPublicMetrics:
        """Create an instance of TwitterPublicMetrics from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TwitterPublicMetrics:
        """Create an instance of TwitterPublicMetrics from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TwitterPublicMetrics.parse_obj(obj)

        _obj = TwitterPublicMetrics.parse_obj({
            "like_count": obj.get("like_count"),
            "quote_count": obj.get("quote_count"),
            "reply_count": obj.get("reply_count"),
            "retweet_count": obj.get("retweet_count"),
            "followers_count": obj.get("followers_count"),
            "following_count": obj.get("following_count"),
            "listed_count": obj.get("listed_count"),
            "tweet_count": obj.get("tweet_count")
        })
        return _obj

