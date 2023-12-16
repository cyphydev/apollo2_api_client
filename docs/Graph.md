# Graph


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**provider** | **str** |  | 
**tag** | **str** |  | 
**version** | **str** |  | 
**type** | [**GraphType**](GraphType.md) |  | 
**edges** | [**List[Edge]**](Edge.md) |  | [optional] [default to []]
**data** | **object** |  | [optional] 

## Example

```python
from apollo2_api_client.models import Graph

# TODO update the JSON string below
json = "{}"
# create an instance of Graph from a JSON string
graph_instance = Graph.from_json(json)
# print the JSON string representation of the object
print Graph.to_json()

# convert the object into a dict
graph_dict = graph_instance.to_dict()
# create an instance of Graph from a dict
graph_form_dict = graph.from_dict(graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


