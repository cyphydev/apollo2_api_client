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
from pydantic import BaseModel, StrictInt, StrictStr, conlist
from apollo2_api_client.models.cluster_member import ClusterMember
from apollo2_api_client.models.item_data import ItemData
from apollo2_api_client.models.enrichment import Enrichment
from apollo2_api_client.models.media_item import MediaItem
from apollo2_api_client.models.platform_type import PlatformType

class Item(BaseModel):
    """
    Item
    """
    id: StrictStr = ...
    author: StrictStr = ...
    platform: PlatformType = ...
    time_published: StrictInt = ...
    sid: Optional[StrictInt] = None
    source_id: Optional[StrictInt] = None
    enrichments: Optional[conlist(Enrichment)] = None
    clusters: Optional[conlist(ClusterMember)] = None
    media_items: Optional[conlist(MediaItem)] = None
    text: Optional[StrictStr] = None
    data: ItemData = ...
    __properties = ["id", "author", "platform", "time_published", "sid", "source_id", "enrichments", "clusters", "media_items", "text", "data"]

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
    def from_json(cls, json_str: str) -> Item:
        """Create an instance of Item from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in enrichments (list)
        _items = []
        if self.enrichments:
            for _item in self.enrichments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['enrichments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in clusters (list)
        _items = []
        if self.clusters:
            for _item in self.clusters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['clusters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in media_items (list)
        _items = []
        if self.media_items:
            for _item in self.media_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['media_items'] = _items
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Item:
        """Create an instance of Item from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Item.parse_obj(obj)

        _obj = Item.parse_obj({
            "id": obj.get("id"),
            "author": obj.get("author"),
            "platform": obj.get("platform"),
            "time_published": obj.get("time_published"),
            "sid": obj.get("sid"),
            "source_id": obj.get("source_id"),
            "enrichments": [Enrichment.from_dict(_item) for _item in obj.get("enrichments")] if obj.get("enrichments") is not None else None,
            "clusters": [ClusterMember.from_dict(_item) for _item in obj.get("clusters")] if obj.get("clusters") is not None else None,
            "media_items": [MediaItem.from_dict(_item) for _item in obj.get("media_items")] if obj.get("media_items") is not None else None,
            "text": obj.get("text"),
            "data": ItemData.from_dict(obj.get("data")) if obj.get("data") is not None else None
        })
        return _obj

