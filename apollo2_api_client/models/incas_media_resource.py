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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from apollo2_api_client.models.account_type import AccountType

class IncasMediaResource(BaseModel):
    """
    IncasMediaResource
    """
    account_bio: Optional[StrictStr] = None
    account_id: Optional[StrictStr] = None
    account_status: Optional[StrictStr] = None
    account_type: Optional[AccountType] = None
    display_names: Optional[conlist(StrictStr)] = None
    follower_count: Optional[StrictInt] = None
    friends_count: Optional[StrictInt] = None
    hashed_user_names: Optional[conlist(StrictStr)] = Field(None, alias="hashedUser_names")
    language: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    user_names: Optional[conlist(StrictStr)] = None
    verified: Optional[StrictBool] = None
    __properties = ["account_bio", "account_id", "account_status", "account_type", "display_names", "follower_count", "friends_count", "hashedUser_names", "language", "url", "user_names", "verified"]

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
    def from_json(cls, json_str: str) -> IncasMediaResource:
        """Create an instance of IncasMediaResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IncasMediaResource:
        """Create an instance of IncasMediaResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IncasMediaResource.parse_obj(obj)

        _obj = IncasMediaResource.parse_obj({
            "account_bio": obj.get("account_bio"),
            "account_id": obj.get("account_id"),
            "account_status": obj.get("account_status"),
            "account_type": obj.get("account_type"),
            "display_names": obj.get("display_names"),
            "follower_count": obj.get("follower_count"),
            "friends_count": obj.get("friends_count"),
            "hashed_user_names": obj.get("hashedUser_names"),
            "language": obj.get("language"),
            "url": obj.get("url"),
            "user_names": obj.get("user_names"),
            "verified": obj.get("verified")
        })
        return _obj

