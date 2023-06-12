# VisualTopic


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** | The enrichment (e.g., Concern-Stance) name for the enrichment. | 
**provider** | **str** | The team (e.g., UIUC-DMG) who provides the enrichment. | 
**tag** | **str** | The tag within the same (provider, name). | 
**version** | **str** | The version within the same (provider, name). | 
**enrichments** | [**List[Enrichment]**](Enrichment.md) |  | [optional] [default to []]
**clusters** | [**List[ClusterMember]**](ClusterMember.md) |  | [optional] [default to []]
**data** | **object** |  | [optional] 
**type** | [**ClusterType**](ClusterType.md) |  | [optional] 

## Example

```python
from apollo2_api_client.models.visual_topic import VisualTopic

# TODO update the JSON string below
json = "{}"
# create an instance of VisualTopic from a JSON string
visual_topic_instance = VisualTopic.from_json(json)
# print the JSON string representation of the object
print VisualTopic.to_json()

# convert the object into a dict
visual_topic_dict = visual_topic_instance.to_dict()
# create an instance of VisualTopic from a dict
visual_topic_form_dict = visual_topic.from_dict(visual_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


