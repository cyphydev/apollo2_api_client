# apollo2_api_client.model.graph.Graph

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**provider** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**tag** | str,  | str,  |  | 
**type** | [**GraphType**](GraphType.md) | [**GraphType**](GraphType.md) |  | 
**version** | str,  | str,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[edges](#edges)** | list, tuple,  | tuple,  |  | [optional] 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] if omitted the server will use the default value of {}
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# edges

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Edge**](Edge.md) | [**Edge**](Edge.md) | [**Edge**](Edge.md) |  | 

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | if omitted the server will use the default value of {}

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

