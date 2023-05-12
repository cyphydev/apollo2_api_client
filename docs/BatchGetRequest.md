# BatchGetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 
**with_enrichment** | **bool** |  | [optional] 
**enrichment_name** | **str** |  | [optional] 
**enrichment_provider** | **str** |  | [optional] 
**enrichment_tag** | **str** |  | [optional] 
**enrichment_version** | **str** |  | [optional] 
**with_cluster** | **bool** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**cluster_provider** | **str** |  | [optional] 
**cluster_tag** | **str** |  | [optional] 
**cluster_version** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models.batch_get_request import BatchGetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchGetRequest from a JSON string
batch_get_request_instance = BatchGetRequest.from_json(json)
# print the JSON string representation of the object
print BatchGetRequest.to_json()

# convert the object into a dict
batch_get_request_dict = batch_get_request_instance.to_dict()
# create an instance of BatchGetRequest from a dict
batch_get_request_form_dict = batch_get_request.from_dict(batch_get_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


