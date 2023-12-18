# IncasMediaResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_bio** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**account_status** | **str** |  | [optional] 
**account_type** | [**AccountType**](AccountType.md) |  | [optional] 
**display_names** | **List[str]** |  | [optional] 
**follower_count** | **int** |  | [optional] 
**friends_count** | **int** |  | [optional] 
**hashed_user_names** | **List[str]** |  | [optional] 
**language** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user_names** | **List[str]** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from apollo2_api_client.models import IncasMediaResource

# TODO update the JSON string below
json = "{}"
# create an instance of IncasMediaResource from a JSON string
incas_media_resource_instance = IncasMediaResource.from_json(json)
# print the JSON string representation of the object
print IncasMediaResource.to_json()

# convert the object into a dict
incas_media_resource_dict = incas_media_resource_instance.to_dict()
# create an instance of IncasMediaResource from a dict
incas_media_resource_form_dict = incas_media_resource.from_dict(incas_media_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


