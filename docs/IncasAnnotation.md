# IncasAnnotation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**offsets** | [**List[IncasOffset]**](IncasOffset.md) |  | [optional] 
**provider_name** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models import IncasAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of IncasAnnotation from a JSON string
incas_annotation_instance = IncasAnnotation.from_json(json)
# print the JSON string representation of the object
print IncasAnnotation.to_json()

# convert the object into a dict
incas_annotation_dict = incas_annotation_instance.to_dict()
# create an instance of IncasAnnotation from a dict
incas_annotation_form_dict = incas_annotation.from_dict(incas_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


