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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, conlist

class ModifyMediaAttachmentRequest(BaseModel):
    """
    ModifyMediaAttachmentRequest
    """
    item_ids: conlist(StrictInt) = ...
    media_ids: conlist(StrictInt) = ...
    data: Optional[conlist(Dict[str, Any])] = None
    ignore_missing_when_deleting: Optional[StrictBool] = True
    __properties = ["item_ids", "media_ids", "data", "ignore_missing_when_deleting"]

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
    def from_json(cls, json_str: str) -> ModifyMediaAttachmentRequest:
        """Create an instance of ModifyMediaAttachmentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModifyMediaAttachmentRequest:
        """Create an instance of ModifyMediaAttachmentRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ModifyMediaAttachmentRequest.parse_obj(obj)

        _obj = ModifyMediaAttachmentRequest.parse_obj({
            "item_ids": obj.get("item_ids"),
            "media_ids": obj.get("media_ids"),
            "data": obj.get("data"),
            "ignore_missing_when_deleting": obj.get("ignore_missing_when_deleting") if obj.get("ignore_missing_when_deleting") is not None else True
        })
        return _obj

