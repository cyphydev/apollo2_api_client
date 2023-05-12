# RawDataPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override** | **bool** |  | [optional] [default to False]
**data** | [**List[RawDataPostEntry]**](RawDataPostEntry.md) |  | 

## Example

```python
from apollo2_api_client.models.raw_data_post_request import RawDataPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RawDataPostRequest from a JSON string
raw_data_post_request_instance = RawDataPostRequest.from_json(json)
# print the JSON string representation of the object
print RawDataPostRequest.to_json()

# convert the object into a dict
raw_data_post_request_dict = raw_data_post_request_instance.to_dict()
# create an instance of RawDataPostRequest from a dict
raw_data_post_request_form_dict = raw_data_post_request.from_dict(raw_data_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


