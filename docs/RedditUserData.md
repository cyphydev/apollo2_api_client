# RedditUserData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | [optional] [default to 'Reddit']

## Example

```python
from apollo2_api_client.models.reddit_user_data import RedditUserData

# TODO update the JSON string below
json = "{}"
# create an instance of RedditUserData from a JSON string
reddit_user_data_instance = RedditUserData.from_json(json)
# print the JSON string representation of the object
print RedditUserData.to_json()

# convert the object into a dict
reddit_user_data_dict = reddit_user_data_instance.to_dict()
# create an instance of RedditUserData from a dict
reddit_user_data_form_dict = reddit_user_data.from_dict(reddit_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


