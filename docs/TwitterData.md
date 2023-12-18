# TwitterData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | [optional] [default to 'Twitter']
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

## Example

```python
from apollo2_api_client.models import TwitterData

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterData from a JSON string
twitter_data_instance = TwitterData.from_json(json)
# print the JSON string representation of the object
print TwitterData.to_json()

# convert the object into a dict
twitter_data_dict = twitter_data_instance.to_dict()
# create an instance of TwitterData from a dict
twitter_data_form_dict = twitter_data.from_dict(twitter_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


