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
from pydantic import BaseModel, Field, StrictStr

class IncasLinks(BaseModel):
    """
    IncasLinks
    """
    messages: Optional[StrictStr] = None
    var_self: Optional[StrictStr] = Field(None, alias="self")
    __properties = ["messages", "self"]

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
    def from_json(cls, json_str: str) -> IncasLinks:
        """Create an instance of IncasLinks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IncasLinks:
        """Create an instance of IncasLinks from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IncasLinks.parse_obj(obj)

        _obj = IncasLinks.parse_obj({
            "messages": obj.get("messages"),
            "var_self": obj.get("self")
        })
        return _obj

