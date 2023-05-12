# Edge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**graph_id** | **int** |  | 
**src_id** | **int** |  | 
**dst_id** | **int** |  | 
**type** | **str** |  | 
**timestamp** | **int** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from apollo2_api_client.models.edge import Edge

# TODO update the JSON string below
json = "{}"
# create an instance of Edge from a JSON string
edge_instance = Edge.from_json(json)
# print the JSON string representation of the object
print Edge.to_json()

# convert the object into a dict
edge_dict = edge_instance.to_dict()
# create an instance of Edge from a dict
edge_form_dict = edge.from_dict(edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


