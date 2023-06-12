# Cluster

This is the unified interface for cluster output.

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
from apollo2_api_client.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print Cluster.to_json()

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_form_dict = cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


