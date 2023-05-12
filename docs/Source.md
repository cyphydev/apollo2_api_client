# Source


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**platform** | [**PlatformType**](PlatformType.md) |  | 
**sid** | **int** |  | [optional] 
**enrichments** | [**List[Enrichment]**](Enrichment.md) |  | [optional] [default to []]
**clusters** | [**List[ClusterMember]**](ClusterMember.md) |  | [optional] [default to []]
**name** | **str** |  | [optional] 
**data** | [**SourceData**](SourceData.md) |  | 

## Example

```python
from apollo2_api_client.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print Source.to_json()

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_form_dict = source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


