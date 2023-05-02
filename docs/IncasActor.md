# IncasActor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[IncasAnnotation]**](IncasAnnotation.md) |  | [optional] [default to []]
**extra_attributes** | [**List[IncasExtraAttribute]**](IncasExtraAttribute.md) |  | [optional] [default to []]
**media_resources** | [**List[IncasMediaResource]**](IncasMediaResource.md) |  | [optional] [default to []]
**segments** | [**List[IncasSegment]**](IncasSegment.md) |  | [optional] [default to []]
**actor_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**entity_type** | [**EntityType**](EntityType.md) |  | [optional] 
**expose_actor_info** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**knowledge_base_url** | **str** |  | [optional] 
**links** | [**IncasLinks**](IncasLinks.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models.incas_actor import IncasActor

# TODO update the JSON string below
json = "{}"
# create an instance of IncasActor from a JSON string
incas_actor_instance = IncasActor.from_json(json)
# print the JSON string representation of the object
print IncasActor.to_json()

# convert the object into a dict
incas_actor_dict = incas_actor_instance.to_dict()
# create an instance of IncasActor from a dict
incas_actor_form_dict = incas_actor.from_dict(incas_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


