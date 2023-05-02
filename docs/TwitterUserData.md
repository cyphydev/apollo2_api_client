# TwitterUserData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**pinned_tweet_id** | **str** |  | [optional] 
**profile_image_url** | **str** |  | [optional] 
**protected** | **bool** |  | [optional] 
**public_metrics** | [**TwitterPublicMetrics**](TwitterPublicMetrics.md) |  | [optional] 
**username** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from apollo2_api_client.models.twitter_user_data import TwitterUserData

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterUserData from a JSON string
twitter_user_data_instance = TwitterUserData.from_json(json)
# print the JSON string representation of the object
print TwitterUserData.to_json()

# convert the object into a dict
twitter_user_data_dict = twitter_user_data_instance.to_dict()
# create an instance of TwitterUserData from a dict
twitter_user_data_form_dict = twitter_user_data.from_dict(twitter_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


