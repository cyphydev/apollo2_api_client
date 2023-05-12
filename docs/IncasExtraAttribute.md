# IncasExtraAttribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**attribute_key** | **str** |  | [optional] 
**attribute_value** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models.incas_extra_attribute import IncasExtraAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of IncasExtraAttribute from a JSON string
incas_extra_attribute_instance = IncasExtraAttribute.from_json(json)
# print the JSON string representation of the object
print IncasExtraAttribute.to_json()

# convert the object into a dict
incas_extra_attribute_dict = incas_extra_attribute_instance.to_dict()
# create an instance of IncasExtraAttribute from a dict
incas_extra_attribute_form_dict = incas_extra_attribute.from_dict(incas_extra_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


