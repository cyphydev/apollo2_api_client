# ModifyMediaAttachmentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[int]** |  | 
**media_ids** | **List[int]** |  | 
**data** | **List[object]** |  | [optional] 
**ignore_missing_when_deleting** | **bool** |  | [optional] [default to True]

## Example

```python
from apollo2_api_client.models import ModifyMediaAttachmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyMediaAttachmentRequest from a JSON string
modify_media_attachment_request_instance = ModifyMediaAttachmentRequest.from_json(json)
# print the JSON string representation of the object
print ModifyMediaAttachmentRequest.to_json()

# convert the object into a dict
modify_media_attachment_request_dict = modify_media_attachment_request_instance.to_dict()
# create an instance of ModifyMediaAttachmentRequest from a dict
modify_media_attachment_request_form_dict = modify_media_attachment_request.from_dict(modify_media_attachment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


