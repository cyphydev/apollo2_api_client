# TwitterEditControls


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**editable_until** | **str** |  | [optional] 
**edits_remaining** | **int** |  | [optional] 
**is_edit_eligible** | **bool** |  | [optional] 

## Example

```python
from apollo2_api_client.models.twitter_edit_controls import TwitterEditControls

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterEditControls from a JSON string
twitter_edit_controls_instance = TwitterEditControls.from_json(json)
# print the JSON string representation of the object
print TwitterEditControls.to_json()

# convert the object into a dict
twitter_edit_controls_dict = twitter_edit_controls_instance.to_dict()
# create an instance of TwitterEditControls from a dict
twitter_edit_controls_form_dict = twitter_edit_controls.from_dict(twitter_edit_controls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


