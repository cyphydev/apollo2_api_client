# MediaItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | [**MediaItemType**](MediaItemType.md) |  | 
**content** | **str** |  | 

## Example

```python
from apollo2_api_client.models import MediaItem

# TODO update the JSON string below
json = "{}"
# create an instance of MediaItem from a JSON string
media_item_instance = MediaItem.from_json(json)
# print the JSON string representation of the object
print MediaItem.to_json()

# convert the object into a dict
media_item_dict = media_item_instance.to_dict()
# create an instance of MediaItem from a dict
media_item_form_dict = media_item.from_dict(media_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


