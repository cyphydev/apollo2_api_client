# Claim


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
from apollo2_api_client.models import Claim

# TODO update the JSON string below
json = "{}"
# create an instance of Claim from a JSON string
claim_instance = Claim.from_json(json)
# print the JSON string representation of the object
print Claim.to_json()

# convert the object into a dict
claim_dict = claim_instance.to_dict()
# create an instance of Claim from a dict
claim_form_dict = claim.from_dict(claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


