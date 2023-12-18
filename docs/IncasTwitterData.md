# IncasTwitterData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engagement_parent_id** | **str** |  | [optional] 
**engagement_type** | [**EngagementType**](EngagementType.md) |  | [optional] 
**follower_count** | **int** |  | [optional] 
**following_count** | **int** |  | [optional] 
**like_count** | **int** |  | [optional] 
**mentioned_users** | **List[str]** |  | [optional] 
**retweet_count** | **int** |  | [optional] 
**tweet_id** | **str** |  | [optional] 
**twitter_author_screenname** | **str** |  | [optional] 
**twitter_user_id** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models import IncasTwitterData

# TODO update the JSON string below
json = "{}"
# create an instance of IncasTwitterData from a JSON string
incas_twitter_data_instance = IncasTwitterData.from_json(json)
# print the JSON string representation of the object
print IncasTwitterData.to_json()

# convert the object into a dict
incas_twitter_data_dict = incas_twitter_data_instance.to_dict()
# create an instance of IncasTwitterData from a dict
incas_twitter_data_form_dict = incas_twitter_data.from_dict(incas_twitter_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


