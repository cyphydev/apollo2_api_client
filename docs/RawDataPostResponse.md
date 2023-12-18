# RawDataPostResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id_map** | **Dict[str, int]** |  | 
**item_id_map** | **Dict[str, int]** |  | 
**media_item_id_map** | **Dict[str, int]** |  | 

## Example

```python
from apollo2_api_client.models import RawDataPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RawDataPostResponse from a JSON string
raw_data_post_response_instance = RawDataPostResponse.from_json(json)
# print the JSON string representation of the object
print RawDataPostResponse.to_json()

# convert the object into a dict
raw_data_post_response_dict = raw_data_post_response_instance.to_dict()
# create an instance of RawDataPostResponse from a dict
raw_data_post_response_form_dict = raw_data_post_response.from_dict(raw_data_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


