# TwitterAnnotation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | [optional] 
**normalized_text** | **str** |  | [optional] 
**probability** | **float** |  | [optional] 
**start** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models import TwitterAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterAnnotation from a JSON string
twitter_annotation_instance = TwitterAnnotation.from_json(json)
# print the JSON string representation of the object
print TwitterAnnotation.to_json()

# convert the object into a dict
twitter_annotation_dict = twitter_annotation_instance.to_dict()
# create an instance of TwitterAnnotation from a dict
twitter_annotation_form_dict = twitter_annotation.from_dict(twitter_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


