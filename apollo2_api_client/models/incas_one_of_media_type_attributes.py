# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel
from apollo2_api_client.models.incas_twitter_data import IncasTwitterData

class IncasOneOfMediaTypeAttributes(BaseModel):
    """
    IncasOneOfMediaTypeAttributes
    """
    reddit_data: Optional[Dict[str, Any]] = None
    twitter_data: Optional[IncasTwitterData] = None
    __properties = ["reddit_data", "twitter_data"]

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
    def from_json(cls, json_str: str) -> IncasOneOfMediaTypeAttributes:
        """Create an instance of IncasOneOfMediaTypeAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of twitter_data
        if self.twitter_data:
            _dict['twitter_data'] = self.twitter_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IncasOneOfMediaTypeAttributes:
        """Create an instance of IncasOneOfMediaTypeAttributes from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IncasOneOfMediaTypeAttributes.parse_obj(obj)

        _obj = IncasOneOfMediaTypeAttributes.parse_obj({
            "reddit_data": obj.get("reddit_data"),
            "twitter_data": IncasTwitterData.from_dict(obj.get("twitter_data")) if obj.get("twitter_data") is not None else None
        })
        return _obj

