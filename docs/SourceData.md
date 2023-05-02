# SourceData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**pinned_tweet_id** | **str** |  | [optional] 
**profile_image_url** | **str** |  | [optional] 
**protected** | **bool** |  | [optional] 
**public_metrics** | [**TwitterPublicMetrics**](TwitterPublicMetrics.md) |  | [optional] 
**username** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**annotations** | [**List[IncasAnnotation]**](IncasAnnotation.md) |  | [optional] [default to []]
**extra_attributes** | [**List[IncasExtraAttribute]**](IncasExtraAttribute.md) |  | [optional] [default to []]
**media_resources** | [**List[IncasMediaResource]**](IncasMediaResource.md) |  | [optional] [default to []]
**segments** | [**List[IncasSegment]**](IncasSegment.md) |  | [optional] [default to []]
**actor_name** | **str** |  | [optional] 
**entity_type** | [**EntityType**](EntityType.md) |  | [optional] 
**expose_actor_info** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**knowledge_base_url** | **str** |  | [optional] 
**links** | [**IncasLinks**](IncasLinks.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models.data1 import SourceData

# TODO update the JSON string below
json = "{}"
# create an instance of SourceData from a JSON string
data1_instance = SourceData.from_json(json)
# print the JSON string representation of the object
print SourceData.to_json()

# convert the object into a dict
data1_dict = data1_instance.to_dict()
# create an instance of SourceData from a dict
data1_form_dict = data1.from_dict(data1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


