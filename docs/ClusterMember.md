# ClusterMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**cluster_id** | **int** |  | 
**node_id** | **int** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from apollo2_api_client.models.cluster_member import ClusterMember

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMember from a JSON string
cluster_member_instance = ClusterMember.from_json(json)
# print the JSON string representation of the object
print ClusterMember.to_json()

# convert the object into a dict
cluster_member_dict = cluster_member_instance.to_dict()
# create an instance of ClusterMember from a dict
cluster_member_form_dict = cluster_member.from_dict(cluster_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


