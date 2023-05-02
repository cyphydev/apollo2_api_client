# TwitterEntities


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[TwitterAnnotation]**](TwitterAnnotation.md) |  | [optional] [default to []]
**hashtags** | [**List[TwitterHashtag]**](TwitterHashtag.md) |  | [optional] [default to []]
**mentions** | [**List[TwitterMention]**](TwitterMention.md) |  | [optional] [default to []]

## Example

```python
from apollo2_api_client.models.twitter_entities import TwitterEntities

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterEntities from a JSON string
twitter_entities_instance = TwitterEntities.from_json(json)
# print the JSON string representation of the object
print TwitterEntities.to_json()

# convert the object into a dict
twitter_entities_dict = twitter_entities_instance.to_dict()
# create an instance of TwitterEntities from a dict
twitter_entities_form_dict = twitter_entities.from_dict(twitter_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


