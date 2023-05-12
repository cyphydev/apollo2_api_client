# IncasMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | [optional] [default to 'Incas']
**annotations** | [**List[IncasAnnotation]**](IncasAnnotation.md) |  | [optional] [default to []]
**data_tags** | **List[str]** |  | [optional] [default to []]
**embedded_urls** | **List[str]** |  | [optional] [default to []]
**extra_attributes** | [**List[IncasExtraAttribute]**](IncasExtraAttribute.md) |  | [optional] [default to []]
**image_urls** | **List[str]** |  | [optional] [default to []]
**segments** | [**List[IncasSegment]**](IncasSegment.md) |  | [optional] [default to []]
**author** | **str** |  | [optional] 
**content_text** | **str** |  | [optional] 
**geolocation** | [**GeoLocation**](GeoLocation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**media_type** | [**PlatformType**](PlatformType.md) |  | [optional] 
**media_type_attributes** | [**IncasOneOfMediaTypeAttributes**](IncasOneOfMediaTypeAttributes.md) |  | [optional] 
**mentioned_users** | **List[object]** |  | [optional] 
**name** | **str** |  | [optional] 
**time_published** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**translated_content_text** | **str** |  | [optional] 
**translated_title** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models.incas_message import IncasMessage

# TODO update the JSON string below
json = "{}"
# create an instance of IncasMessage from a JSON string
incas_message_instance = IncasMessage.from_json(json)
# print the JSON string representation of the object
print IncasMessage.to_json()

# convert the object into a dict
incas_message_dict = incas_message_instance.to_dict()
# create an instance of IncasMessage from a dict
incas_message_form_dict = incas_message.from_dict(incas_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


