# RawDataPostEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**Source**](Source.md) |  | 
**items** | [**List[Item]**](Item.md) |  | 

## Example

```python
from apollo2_api_client.models.raw_data_post_entry import RawDataPostEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RawDataPostEntry from a JSON string
raw_data_post_entry_instance = RawDataPostEntry.from_json(json)
# print the JSON string representation of the object
print RawDataPostEntry.to_json()

# convert the object into a dict
raw_data_post_entry_dict = raw_data_post_entry_instance.to_dict()
# create an instance of RawDataPostEntry from a dict
raw_data_post_entry_form_dict = raw_data_post_entry.from_dict(raw_data_post_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


