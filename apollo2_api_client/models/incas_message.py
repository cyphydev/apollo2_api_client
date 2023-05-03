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


from typing import Any, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, conlist
from apollo2_api_client.models.geo_location import GeoLocation
from apollo2_api_client.models.incas_annotation import IncasAnnotation
from apollo2_api_client.models.incas_extra_attribute import IncasExtraAttribute
from apollo2_api_client.models.incas_one_of_media_type_attributes import IncasOneOfMediaTypeAttributes
from apollo2_api_client.models.incas_segment import IncasSegment
from apollo2_api_client.models.platform_type import PlatformType

class IncasMessage(BaseModel):
    """
    IncasMessage
    """
    data_type: Optional[StrictStr] = 'Incas'
    annotations: Optional[conlist(IncasAnnotation)] = None
    data_tags: Optional[conlist(StrictStr)] = None
    embedded_urls: Optional[conlist(StrictStr)] = None
    extra_attributes: Optional[conlist(IncasExtraAttribute)] = None
    image_urls: Optional[conlist(StrictStr)] = None
    segments: Optional[conlist(IncasSegment)] = None
    author: Optional[StrictStr] = None
    content_text: Optional[StrictStr] = None
    geolocation: Optional[GeoLocation] = None
    id: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    media_type: Optional[PlatformType] = None
    media_type_attributes: Optional[IncasOneOfMediaTypeAttributes] = None
    mentioned_users: Optional[conlist(Any)] = None
    name: Optional[StrictStr] = None
    time_published: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    translated_content_text: Optional[StrictStr] = None
    translated_title: Optional[StrictStr] = None
    __properties = ["data_type", "annotations", "data_tags", "embedded_urls", "extra_attributes", "image_urls", "segments", "author", "content_text", "geolocation", "id", "language", "media_type", "media_type_attributes", "mentioned_users", "name", "time_published", "title", "url", "translated_content_text", "translated_title"]

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
    def from_json(cls, json_str: str) -> IncasMessage:
        """Create an instance of IncasMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in annotations (list)
        _items = []
        if self.annotations:
            for _item in self.annotations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['annotations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in extra_attributes (list)
        _items = []
        if self.extra_attributes:
            for _item in self.extra_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['extra_attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in segments (list)
        _items = []
        if self.segments:
            for _item in self.segments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['segments'] = _items
        # override the default output from pydantic by calling `to_dict()` of geolocation
        if self.geolocation:
            _dict['geolocation'] = self.geolocation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of media_type_attributes
        if self.media_type_attributes:
            _dict['media_type_attributes'] = self.media_type_attributes.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IncasMessage:
        """Create an instance of IncasMessage from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IncasMessage.parse_obj(obj)

        _obj = IncasMessage.parse_obj({
            "data_type": obj.get("data_type") if obj.get("data_type") is not None else 'Incas',
            "annotations": [IncasAnnotation.from_dict(_item) for _item in obj.get("annotations")] if obj.get("annotations") is not None else None,
            "data_tags": obj.get("data_tags"),
            "embedded_urls": obj.get("embedded_urls"),
            "extra_attributes": [IncasExtraAttribute.from_dict(_item) for _item in obj.get("extra_attributes")] if obj.get("extra_attributes") is not None else None,
            "image_urls": obj.get("image_urls"),
            "segments": [IncasSegment.from_dict(_item) for _item in obj.get("segments")] if obj.get("segments") is not None else None,
            "author": obj.get("author"),
            "content_text": obj.get("content_text"),
            "geolocation": GeoLocation.from_dict(obj.get("geolocation")) if obj.get("geolocation") is not None else None,
            "id": obj.get("id"),
            "language": obj.get("language"),
            "media_type": obj.get("media_type"),
            "media_type_attributes": IncasOneOfMediaTypeAttributes.from_dict(obj.get("media_type_attributes")) if obj.get("media_type_attributes") is not None else None,
            "mentioned_users": obj.get("mentioned_users"),
            "name": obj.get("name"),
            "time_published": obj.get("time_published"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "translated_content_text": obj.get("translated_content_text"),
            "translated_title": obj.get("translated_title")
        })
        return _obj

