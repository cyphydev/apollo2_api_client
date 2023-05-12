# TwitterAttachment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_keys** | **List[str]** |  | [optional] [default to []]

## Example

```python
from apollo2_api_client.models.twitter_attachment import TwitterAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterAttachment from a JSON string
twitter_attachment_instance = TwitterAttachment.from_json(json)
# print the JSON string representation of the object
print TwitterAttachment.to_json()

# convert the object into a dict
twitter_attachment_dict = twitter_attachment_instance.to_dict()
# create an instance of TwitterAttachment from a dict
twitter_attachment_form_dict = twitter_attachment.from_dict(twitter_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


