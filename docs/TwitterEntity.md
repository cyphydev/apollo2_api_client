# TwitterEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models import TwitterEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterEntity from a JSON string
twitter_entity_instance = TwitterEntity.from_json(json)
# print the JSON string representation of the object
print TwitterEntity.to_json()

# convert the object into a dict
twitter_entity_dict = twitter_entity_instance.to_dict()
# create an instance of TwitterEntity from a dict
twitter_entity_form_dict = twitter_entity.from_dict(twitter_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


