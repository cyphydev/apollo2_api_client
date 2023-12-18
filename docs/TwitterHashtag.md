# TwitterHashtag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | [optional] 
**start** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models import TwitterHashtag

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterHashtag from a JSON string
twitter_hashtag_instance = TwitterHashtag.from_json(json)
# print the JSON string representation of the object
print TwitterHashtag.to_json()

# convert the object into a dict
twitter_hashtag_dict = twitter_hashtag_instance.to_dict()
# create an instance of TwitterHashtag from a dict
twitter_hashtag_form_dict = twitter_hashtag.from_dict(twitter_hashtag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


