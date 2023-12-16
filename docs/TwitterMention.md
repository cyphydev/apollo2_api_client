# TwitterMention


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**start** | **int** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models import TwitterMention

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterMention from a JSON string
twitter_mention_instance = TwitterMention.from_json(json)
# print the JSON string representation of the object
print TwitterMention.to_json()

# convert the object into a dict
twitter_mention_dict = twitter_mention_instance.to_dict()
# create an instance of TwitterMention from a dict
twitter_mention_form_dict = twitter_mention.from_dict(twitter_mention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


