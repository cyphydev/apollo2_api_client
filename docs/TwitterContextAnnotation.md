# TwitterContextAnnotation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**TwitterDomain**](TwitterDomain.md) |  | [optional] 
**entity** | [**TwitterEntity**](TwitterEntity.md) |  | [optional] 

## Example

```python
from apollo2_api_client.models import TwitterContextAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterContextAnnotation from a JSON string
twitter_context_annotation_instance = TwitterContextAnnotation.from_json(json)
# print the JSON string representation of the object
print TwitterContextAnnotation.to_json()

# convert the object into a dict
twitter_context_annotation_dict = twitter_context_annotation_instance.to_dict()
# create an instance of TwitterContextAnnotation from a dict
twitter_context_annotation_form_dict = twitter_context_annotation.from_dict(twitter_context_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


