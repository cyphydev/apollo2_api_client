# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from apollo2_api_client import schemas  # noqa: F401


class Edge(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "src_id",
            "dst_id",
            "graph_id",
            "type",
        }
        
        class properties:
            graph_id = schemas.IntSchema
            src_id = schemas.IntSchema
            dst_id = schemas.IntSchema
            type = schemas.StrSchema
            id = schemas.IntSchema
            timestamp = schemas.IntSchema
            data = schemas.DictSchema
            __annotations__ = {
                "graph_id": graph_id,
                "src_id": src_id,
                "dst_id": dst_id,
                "type": type,
                "id": id,
                "timestamp": timestamp,
                "data": data,
            }
    
    src_id: MetaOapg.properties.src_id
    dst_id: MetaOapg.properties.dst_id
    graph_id: MetaOapg.properties.graph_id
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["graph_id"]) -> MetaOapg.properties.graph_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["src_id"]) -> MetaOapg.properties.src_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dst_id"]) -> MetaOapg.properties.dst_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["graph_id", "src_id", "dst_id", "type", "id", "timestamp", "data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["graph_id"]) -> MetaOapg.properties.graph_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["src_id"]) -> MetaOapg.properties.src_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dst_id"]) -> MetaOapg.properties.dst_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["graph_id", "src_id", "dst_id", "type", "id", "timestamp", "data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        src_id: typing.Union[MetaOapg.properties.src_id, decimal.Decimal, int, ],
        dst_id: typing.Union[MetaOapg.properties.dst_id, decimal.Decimal, int, ],
        graph_id: typing.Union[MetaOapg.properties.graph_id, decimal.Decimal, int, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        timestamp: typing.Union[MetaOapg.properties.timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Edge':
        return super().__new__(
            cls,
            *_args,
            src_id=src_id,
            dst_id=dst_id,
            graph_id=graph_id,
            type=type,
            id=id,
            timestamp=timestamp,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )
