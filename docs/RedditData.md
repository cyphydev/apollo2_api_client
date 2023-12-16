# RedditData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | [optional] [default to 'Reddit']

## Example

```python
from apollo2_api_client.models import RedditData

# TODO update the JSON string below
json = "{}"
# create an instance of RedditData from a JSON string
reddit_data_instance = RedditData.from_json(json)
# print the JSON string representation of the object
print RedditData.to_json()

# convert the object into a dict
reddit_data_dict = reddit_data_instance.to_dict()
# create an instance of RedditData from a dict
reddit_data_form_dict = reddit_data.from_dict(reddit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


