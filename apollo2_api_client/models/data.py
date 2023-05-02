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

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from apollo2_api_client.models.incas_message import IncasMessage
from apollo2_api_client.models.twitter_data import TwitterData
from typing import Any, List
from pydantic import StrictStr, Field

DATA_ANY_OF_SCHEMAS = ["IncasMessage", "TwitterData", "object"]

class Data(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: TwitterData
    __anyof_schema_1: Optional[TwitterData] = None
    # data type: object
    __anyof_schema_2: Optional[Dict[str, Any]] = None
    # data type: IncasMessage
    __anyof_schema_3: Optional[IncasMessage] = None
    actual_instance: Any
    any_of_schemas: List[str] = Field(DATA_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        error_messages = []
        # validate data type: TwitterData
        if type(v) is not TwitterData:
            error_messages.append(f"Error! Input type `{type(v)}` is not `TwitterData`")
        else:
            return v

        # validate data type: object
        if type(v) is not object:
            error_messages.append(f"Error! Input type `{type(v)}` is not `object`")
        else:
            return v

        # validate data type: IncasMessage
        if type(v) is not IncasMessage:
            error_messages.append(f"Error! Input type `{type(v)}` is not `IncasMessage`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Data with anyOf schemas: IncasMessage, TwitterData, object. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_json(cls, json_str: str) -> Data:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        # __anyof_schema_1: Optional[TwitterData] = None
        try:
            instance.actual_instance = TwitterData.from_json(json_str)
            return instance
        except ValidationError as e:
             error_messages.append(str(e))
        # __anyof_schema_3: Optional[IncasMessage] = None
        try:
            instance.actual_instance = IncasMessage.from_json(json_str)
            return instance
        except ValidationError as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Data with anyOf schemas: IncasMessage, TwitterData, object. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())
