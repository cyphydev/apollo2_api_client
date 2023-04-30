# apollo2_api_client.model.item.Item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**author** | str,  | str,  |  | 
**id** | str,  | str,  |  | 
**time_published** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**platform** | [**MediaType**](MediaType.md) | [**MediaType**](MediaType.md) |  | 
**sid** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**source_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[enrichments](#enrichments)** | list, tuple,  | tuple,  |  | [optional] 
**[clusters](#clusters)** | list, tuple,  | tuple,  |  | [optional] 
**[media_items](#media_items)** | list, tuple,  | tuple,  |  | [optional] 
**text** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TwitterData](TwitterData.md) | [**TwitterData**](TwitterData.md) | [**TwitterData**](TwitterData.md) |  | 
[any_of_1](#any_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[IncasMessage](IncasMessage.md) | [**IncasMessage**](IncasMessage.md) | [**IncasMessage**](IncasMessage.md) |  | 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# enrichments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Enrichment**](Enrichment.md) | [**Enrichment**](Enrichment.md) | [**Enrichment**](Enrichment.md) |  | 

# clusters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClusterMember**](ClusterMember.md) | [**ClusterMember**](ClusterMember.md) | [**ClusterMember**](ClusterMember.md) |  | 

# media_items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MediaItem**](MediaItem.md) | [**MediaItem**](MediaItem.md) | [**MediaItem**](MediaItem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

