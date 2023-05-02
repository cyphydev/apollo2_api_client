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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

class TwitterAnnotation(BaseModel):
    """
    TwitterAnnotation
    """
    end: Optional[StrictInt] = None
    normalized_text: Optional[StrictStr] = None
    probability: Optional[StrictFloat] = None
    start: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
    __properties = ["end", "normalized_text", "probability", "start", "type"]

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
    def from_json(cls, json_str: str) -> TwitterAnnotation:
        """Create an instance of TwitterAnnotation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TwitterAnnotation:
        """Create an instance of TwitterAnnotation from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TwitterAnnotation.parse_obj(obj)

        _obj = TwitterAnnotation.parse_obj({
            "end": obj.get("end"),
            "normalized_text": obj.get("normalized_text"),
            "probability": obj.get("probability"),
            "start": obj.get("start"),
            "type": obj.get("type")
        })
        return _obj

