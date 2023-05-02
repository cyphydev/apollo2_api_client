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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from apollo2_api_client.models.enrichment_type import EnrichmentType

class ArrayEnrichmentMeta(BaseModel):
    """
    ArrayEnrichmentMeta
    """
    description: StrictStr = Field(..., description="Description of the enrichment algorithm.")
    name: StrictStr = Field(..., description="The enrichment name for the enrichment.")
    provider: StrictStr = Field(..., description="The team who provides the enrichment.")
    tag: StrictStr = Field(..., description="The tag within the same (provider, name).")
    version: StrictStr = Field(..., description="The version within the same (provider, name).")
    data: Optional[Dict[str, Any]] = None
    type: Optional[EnrichmentType] = None
    label_map: Dict[str, StrictInt] = Field(..., description="The mapping from label to index.")
    __properties = ["description", "name", "provider", "tag", "version", "data", "type", "label_map"]

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
    def from_json(cls, json_str: str) -> ArrayEnrichmentMeta:
        """Create an instance of ArrayEnrichmentMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ArrayEnrichmentMeta:
        """Create an instance of ArrayEnrichmentMeta from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ArrayEnrichmentMeta.parse_obj(obj)

        _obj = ArrayEnrichmentMeta.parse_obj({
            "description": obj.get("description"),
            "name": obj.get("name"),
            "provider": obj.get("provider"),
            "tag": obj.get("tag"),
            "version": obj.get("version"),
            "data": obj.get("data"),
            "type": obj.get("type"),
            "label_map": obj.get("label_map")
        })
        return _obj

