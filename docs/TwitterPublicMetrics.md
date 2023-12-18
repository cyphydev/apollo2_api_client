# TwitterPublicMetrics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**like_count** | **int** |  | [optional] 
**quote_count** | **int** |  | [optional] 
**reply_count** | **int** |  | [optional] 
**retweet_count** | **int** |  | [optional] 
**followers_count** | **int** |  | [optional] 
**following_count** | **int** |  | [optional] 
**listed_count** | **int** |  | [optional] 
**tweet_count** | **int** |  | [optional] 

## Example

```python
from apollo2_api_client.models import TwitterPublicMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterPublicMetrics from a JSON string
twitter_public_metrics_instance = TwitterPublicMetrics.from_json(json)
# print the JSON string representation of the object
print TwitterPublicMetrics.to_json()

# convert the object into a dict
twitter_public_metrics_dict = twitter_public_metrics_instance.to_dict()
# create an instance of TwitterPublicMetrics from a dict
twitter_public_metrics_form_dict = twitter_public_metrics.from_dict(twitter_public_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


