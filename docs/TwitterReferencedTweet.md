# TwitterReferencedTweet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models import TwitterReferencedTweet

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterReferencedTweet from a JSON string
twitter_referenced_tweet_instance = TwitterReferencedTweet.from_json(json)
# print the JSON string representation of the object
print TwitterReferencedTweet.to_json()

# convert the object into a dict
twitter_referenced_tweet_dict = twitter_referenced_tweet_instance.to_dict()
# create an instance of TwitterReferencedTweet from a dict
twitter_referenced_tweet_form_dict = twitter_referenced_tweet.from_dict(twitter_referenced_tweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


