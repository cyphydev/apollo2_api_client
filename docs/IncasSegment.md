# IncasSegment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[IncasAnnotation]**](IncasAnnotation.md) |  | [optional] 
**description** | **str** |  | [optional] 
**extra_attributes** | [**List[IncasExtraAttribute]**](IncasExtraAttribute.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models.incas_segment import IncasSegment

# TODO update the JSON string below
json = "{}"
# create an instance of IncasSegment from a JSON string
incas_segment_instance = IncasSegment.from_json(json)
# print the JSON string representation of the object
print IncasSegment.to_json()

# convert the object into a dict
incas_segment_dict = incas_segment_instance.to_dict()
# create an instance of IncasSegment from a dict
incas_segment_form_dict = incas_segment.from_dict(incas_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


