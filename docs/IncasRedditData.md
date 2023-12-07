# IncasRedditData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** |  | [optional] 
**author_awardee_karma** | **int** |  | [optional] 
**author_awarder_karma** | **int** |  | [optional] 
**author_karma** | **int** |  | [optional] 
**comments** | **int** |  | [optional] 
**engagement_type** | **str** |  | [optional] 
**parent_post_id** | **str** |  | [optional] 
**reddit_post_id** | **str** |  | [optional] 
**subreddit** | **str** |  | [optional] 
**subreddit_subscribers** | **int** |  | [optional] 
**upvote_ratio** | **float** |  | [optional] 

## Example

```python
from apollo2_api_client.models.incas_reddit_data import IncasRedditData

# TODO update the JSON string below
json = "{}"
# create an instance of IncasRedditData from a JSON string
incas_reddit_data_instance = IncasRedditData.from_json(json)
# print the JSON string representation of the object
print IncasRedditData.to_json()

# convert the object into a dict
incas_reddit_data_dict = incas_reddit_data_instance.to_dict()
# create an instance of IncasRedditData from a dict
incas_reddit_data_form_dict = incas_reddit_data.from_dict(incas_reddit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


