# apollo2_api_client.model.claim.Claim

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**provider** | str,  | str,  | The team (e.g., UIUC-DMG) who provides the enrichment. | 
**name** | str,  | str,  | The enrichment (e.g., Concern-Stance) name for the enrichment. | 
**tag** | str,  | str,  | The tag within the same (provider, name). | 
**version** | str,  | str,  | The version within the same (provider, name). | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] if omitted the server will use the default value of {}
**[type](#type)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] if omitted the server will use the default value of Claim
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | if omitted the server will use the default value of {}

# type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | if omitted the server will use the default value of Claim

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ClusterType](ClusterType.md) | [**ClusterType**](ClusterType.md) | [**ClusterType**](ClusterType.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

