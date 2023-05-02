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


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictStr
from apollo2_api_client.models.twitter_public_metrics import TwitterPublicMetrics

class TwitterUserData(BaseModel):
    """
    TwitterUserData
    """
    description: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    pinned_tweet_id: Optional[StrictStr] = None
    profile_image_url: Optional[StrictStr] = None
    protected: Optional[StrictBool] = None
    public_metrics: Optional[TwitterPublicMetrics] = None
    username: Optional[StrictStr] = None
    verified: Optional[StrictBool] = None
    __properties = ["description", "location", "pinned_tweet_id", "profile_image_url", "protected", "public_metrics", "username", "verified"]

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
    def from_json(cls, json_str: str) -> TwitterUserData:
        """Create an instance of TwitterUserData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of public_metrics
        if self.public_metrics:
            _dict['public_metrics'] = self.public_metrics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TwitterUserData:
        """Create an instance of TwitterUserData from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TwitterUserData.parse_obj(obj)

        _obj = TwitterUserData.parse_obj({
            "description": obj.get("description"),
            "location": obj.get("location"),
            "pinned_tweet_id": obj.get("pinned_tweet_id"),
            "profile_image_url": obj.get("profile_image_url"),
            "protected": obj.get("protected"),
            "public_metrics": TwitterPublicMetrics.from_dict(obj.get("public_metrics")) if obj.get("public_metrics") is not None else None,
            "username": obj.get("username"),
            "verified": obj.get("verified")
        })
        return _obj

