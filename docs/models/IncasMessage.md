# apollo2_api_client.model.incas_message.IncasMessage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[annotations](#annotations)** | list, tuple,  | tuple,  |  | [optional] 
**[data_tags](#data_tags)** | list, tuple,  | tuple,  |  | [optional] 
**[embedded_urls](#embedded_urls)** | list, tuple,  | tuple,  |  | [optional] 
**[extra_attributes](#extra_attributes)** | list, tuple,  | tuple,  |  | [optional] 
**[image_urls](#image_urls)** | list, tuple,  | tuple,  |  | [optional] 
**[segments](#segments)** | list, tuple,  | tuple,  |  | [optional] 
**author** | str,  | str,  |  | [optional] 
**content_text** | str,  | str,  |  | [optional] 
**geolocation** | [**GeoLocation**](GeoLocation.md) | [**GeoLocation**](GeoLocation.md) |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**language** | str,  | str,  |  | [optional] 
**media_type** | [**MediaType**](MediaType.md) | [**MediaType**](MediaType.md) |  | [optional] 
**media_type_attributes** | [**IncasOneOfMediaTypeAttributes**](IncasOneOfMediaTypeAttributes.md) | [**IncasOneOfMediaTypeAttributes**](IncasOneOfMediaTypeAttributes.md) |  | [optional] 
**[mentioned_users](#mentioned_users)** | list, tuple,  | tuple,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**time_published** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**translated_content_text** | str,  | str,  |  | [optional] 
**translated_title** | str,  | str,  |  | [optional] 
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

# data_tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# embedded_urls

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# extra_attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IncasExtraAttribute**](IncasExtraAttribute.md) | [**IncasExtraAttribute**](IncasExtraAttribute.md) | [**IncasExtraAttribute**](IncasExtraAttribute.md) |  | 

# image_urls

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# segments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IncasSegment**](IncasSegment.md) | [**IncasSegment**](IncasSegment.md) | [**IncasSegment**](IncasSegment.md) |  | 

# mentioned_users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

