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


class TwitterEditControls(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            editable_until = schemas.StrSchema
            edits_remaining = schemas.IntSchema
            is_edit_eligible = schemas.BoolSchema
            __annotations__ = {
                "editable_until": editable_until,
                "edits_remaining": edits_remaining,
                "is_edit_eligible": is_edit_eligible,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editable_until"]) -> MetaOapg.properties.editable_until: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edits_remaining"]) -> MetaOapg.properties.edits_remaining: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_edit_eligible"]) -> MetaOapg.properties.is_edit_eligible: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["editable_until", "edits_remaining", "is_edit_eligible", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editable_until"]) -> typing.Union[MetaOapg.properties.editable_until, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edits_remaining"]) -> typing.Union[MetaOapg.properties.edits_remaining, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_edit_eligible"]) -> typing.Union[MetaOapg.properties.is_edit_eligible, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["editable_until", "edits_remaining", "is_edit_eligible", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        editable_until: typing.Union[MetaOapg.properties.editable_until, str, schemas.Unset] = schemas.unset,
        edits_remaining: typing.Union[MetaOapg.properties.edits_remaining, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        is_edit_eligible: typing.Union[MetaOapg.properties.is_edit_eligible, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TwitterEditControls':
        return super().__new__(
            cls,
            *_args,
            editable_until=editable_until,
            edits_remaining=edits_remaining,
            is_edit_eligible=is_edit_eligible,
            _configuration=_configuration,
            **kwargs,
        )
