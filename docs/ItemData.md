# ItemData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**TwitterAttachment**](TwitterAttachment.md) |  | [optional] 
**context_annotations** | [**List[TwitterContextAnnotation]**](TwitterContextAnnotation.md) |  | [optional] [default to []]
**author_id** | **str** |  | [optional] 
**conversation_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**edit_controls** | [**TwitterEditControls**](TwitterEditControls.md) |  | [optional] 
**edit_history_tweet_ids** | **List[str]** |  | [optional] [default to []]
**entities** | [**TwitterEntities**](TwitterEntities.md) |  | [optional] 
**id** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**possibly_sensitive** | **bool** |  | [optional] 
**public_metrics** | [**TwitterPublicMetrics**](TwitterPublicMetrics.md) |  | [optional] 
**reference_tweets** | [**List[TwitterReferencedTweet]**](TwitterReferencedTweet.md) |  | [optional] [default to []]
**reply_settings** | **str** |  | [optional] 
**tweet_id** | **str** |  | [optional] 
**twitter_author_screenname** | **str** |  | [optional] 
**twitter_user_id** | **str** |  | [optional] 
**annotations** | [**List[IncasAnnotation]**](IncasAnnotation.md) |  | [optional] [default to []]
**data_tags** | **List[str]** |  | [optional] [default to []]
**embedded_urls** | **List[str]** |  | [optional] [default to []]
**extra_attributes** | [**List[IncasExtraAttribute]**](IncasExtraAttribute.md) |  | [optional] [default to []]
**image_urls** | **List[str]** |  | [optional] [default to []]
**segments** | [**List[IncasSegment]**](IncasSegment.md) |  | [optional] [default to []]
**author** | **str** |  | [optional] 
**content_text** | **str** |  | [optional] 
**geolocation** | [**GeoLocation**](GeoLocation.md) |  | [optional] 
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
from apollo2_api_client.models.data import ItemData

# TODO update the JSON string below
json = "{}"
# create an instance of ItemData from a JSON string
data_instance = ItemData.from_json(json)
# print the JSON string representation of the object
print ItemData.to_json()

# convert the object into a dict
data_dict = data_instance.to_dict()
# create an instance of ItemData from a dict
data_form_dict = data.from_dict(data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


