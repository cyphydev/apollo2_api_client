# apollo2_api_client.model.incas_twitter_data.IncasTwitterData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**engagement_parent_id** | str,  | str,  |  | [optional] 
**engagement_type** | [**EngagementType**](EngagementType.md) | [**EngagementType**](EngagementType.md) |  | [optional] 
**follower_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**following_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**like_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[mentioned_users](#mentioned_users)** | list, tuple,  | tuple,  |  | [optional] 
**retweet_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tweet_id** | str,  | str,  |  | [optional] 
**twitter_author_screenname** | str,  | str,  |  | [optional] 
**twitter_user_id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mentioned_users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

