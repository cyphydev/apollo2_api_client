# Item


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**author** | **str** |  | 
**platform** | [**PlatformType**](PlatformType.md) |  | 
**time_published** | **int** |  | 
**sid** | **int** |  | [optional] 
**source_id** | **int** |  | [optional] 
**enrichments** | [**List[Enrichment]**](Enrichment.md) |  | [optional] [default to []]
**clusters** | [**List[ClusterMember]**](ClusterMember.md) |  | [optional] [default to []]
**media_items** | [**List[MediaItem]**](MediaItem.md) |  | [optional] [default to []]
**text** | **str** |  | [optional] 
**data** | [**Data**](Data.md) |  | 

## Example

```python
from apollo2_api_client.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print Item.to_json()

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_form_dict = item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


