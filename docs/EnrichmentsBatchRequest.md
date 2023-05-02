# EnrichmentsBatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 
**name** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models.enrichments_batch_request import EnrichmentsBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentsBatchRequest from a JSON string
enrichments_batch_request_instance = EnrichmentsBatchRequest.from_json(json)
# print the JSON string representation of the object
print EnrichmentsBatchRequest.to_json()

# convert the object into a dict
enrichments_batch_request_dict = enrichments_batch_request_instance.to_dict()
# create an instance of EnrichmentsBatchRequest from a dict
enrichments_batch_request_form_dict = enrichments_batch_request.from_dict(enrichments_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


