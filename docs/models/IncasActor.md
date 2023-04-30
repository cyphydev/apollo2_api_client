# apollo2_api_client.model.incas_actor.IncasActor

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[annotations](#annotations)** | list, tuple,  | tuple,  |  | [optional] 
**[extra_attributes](#extra_attributes)** | list, tuple,  | tuple,  |  | [optional] 
**[media_resources](#media_resources)** | list, tuple,  | tuple,  |  | [optional] 
**[segments](#segments)** | list, tuple,  | tuple,  |  | [optional] 
**actor_name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**entity_type** | [**EntityType**](EntityType.md) | [**EntityType**](EntityType.md) |  | [optional] 
**expose_actor_info** | bool,  | BoolClass,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**knowledge_base_url** | str,  | str,  |  | [optional] 
**links** | [**IncasLinks**](IncasLinks.md) | [**IncasLinks**](IncasLinks.md) |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# annotations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IncasAnnotation**](IncasAnnotation.md) | [**IncasAnnotation**](IncasAnnotation.md) | [**IncasAnnotation**](IncasAnnotation.md) |  | 

# extra_attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IncasExtraAttribute**](IncasExtraAttribute.md) | [**IncasExtraAttribute**](IncasExtraAttribute.md) | [**IncasExtraAttribute**](IncasExtraAttribute.md) |  | 

# media_resources

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IncasMediaResource**](IncasMediaResource.md) | [**IncasMediaResource**](IncasMediaResource.md) | [**IncasMediaResource**](IncasMediaResource.md) |  | 

# segments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IncasSegment**](IncasSegment.md) | [**IncasSegment**](IncasSegment.md) | [**IncasSegment**](IncasSegment.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

