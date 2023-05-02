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


from typing import Dict
from pydantic import BaseModel, StrictInt

class RawDataPostResponse(BaseModel):
    """
    RawDataPostResponse
    """
    source_id_map: Dict[str, StrictInt] = ...
    item_id_map: Dict[str, StrictInt] = ...
    media_item_id_map: Dict[str, StrictInt] = ...
    __properties = ["source_id_map", "item_id_map", "media_item_id_map"]

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
    def from_json(cls, json_str: str) -> RawDataPostResponse:
        """Create an instance of RawDataPostResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RawDataPostResponse:
        """Create an instance of RawDataPostResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RawDataPostResponse.parse_obj(obj)

        _obj = RawDataPostResponse.parse_obj({
            "source_id_map": obj.get("source_id_map"),
            "item_id_map": obj.get("item_id_map"),
            "media_item_id_map": obj.get("media_item_id_map")
        })
        return _obj

