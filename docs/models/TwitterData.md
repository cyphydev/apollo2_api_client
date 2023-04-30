# apollo2_api_client.model.twitter_data.TwitterData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**attachments** | [**TwitterAttachment**](TwitterAttachment.md) | [**TwitterAttachment**](TwitterAttachment.md) |  | [optional] 
**[context_annotations](#context_annotations)** | list, tuple,  | tuple,  |  | [optional] 
**author_id** | str,  | str,  |  | [optional] 
**conversation_id** | str,  | str,  |  | [optional] 
**created_at** | str,  | str,  |  | [optional] 
**edit_controls** | [**TwitterEditControls**](TwitterEditControls.md) | [**TwitterEditControls**](TwitterEditControls.md) |  | [optional] 
**[edit_history_tweet_ids](#edit_history_tweet_ids)** | list, tuple,  | tuple,  |  | [optional] 
**entities** | [**TwitterEntities**](TwitterEntities.md) | [**TwitterEntities**](TwitterEntities.md) |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**lang** | str,  | str,  |  | [optional] 
**possibly_sensitive** | bool,  | BoolClass,  |  | [optional] 
**public_metrics** | [**TwitterPublicMetrics**](TwitterPublicMetrics.md) | [**TwitterPublicMetrics**](TwitterPublicMetrics.md) |  | [optional] 
**[reference_tweets](#reference_tweets)** | list, tuple,  | tuple,  |  | [optional] 
**reply_settings** | str,  | str,  |  | [optional] 
**tweet_id** | str,  | str,  |  | [optional] 
**twitter_author_screenname** | str,  | str,  |  | [optional] 
**twitter_user_id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# context_annotations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TwitterContextAnnotation**](TwitterContextAnnotation.md) | [**TwitterContextAnnotation**](TwitterContextAnnotation.md) | [**TwitterContextAnnotation**](TwitterContextAnnotation.md) |  | 

# edit_history_tweet_ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reference_tweets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TwitterReferencedTweet**](TwitterReferencedTweet.md) | [**TwitterReferencedTweet**](TwitterReferencedTweet.md) | [**TwitterReferencedTweet**](TwitterReferencedTweet.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

