# apollo2_api_client.model.incas_media_resource.IncasMediaResource

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_bio** | str,  | str,  |  | [optional] 
**account_id** | str,  | str,  |  | [optional] 
**account_status** | str,  | str,  |  | [optional] 
**account_type** | [**AccountType**](AccountType.md) | [**AccountType**](AccountType.md) |  | [optional] 
**[display_names](#display_names)** | list, tuple,  | tuple,  |  | [optional] 
**follower_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**friends_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[hashedUser_names](#hashedUser_names)** | list, tuple,  | tuple,  |  | [optional] 
**language** | str,  | str,  |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**[user_names](#user_names)** | list, tuple,  | tuple,  |  | [optional] 
**verified** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# display_names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# hashedUser_names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# user_names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

