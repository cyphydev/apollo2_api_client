# ArrayEnrichment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The enrichment (e.g., name for the enrichment. | 
**provider** | **str** | The team who provides the enrichment. | 
**tag** | **str** | The tag within the same (provider, name). | 
**version** | **str** | The version within the same (provider, name). | 
**type** | [**EnrichmentType**](EnrichmentType.md) |  | [optional] 
**value** | **List[float]** |  | 
**confidence** | **List[float]** | The confidence that this enrichment is correct, expressed as a percentage between 0.0 and 1.0 | [optional] 

## Example

```python
from apollo2_api_client.models.array_enrichment import ArrayEnrichment

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayEnrichment from a JSON string
array_enrichment_instance = ArrayEnrichment.from_json(json)
# print the JSON string representation of the object
print ArrayEnrichment.to_json()

# convert the object into a dict
array_enrichment_dict = array_enrichment_instance.to_dict()
# create an instance of ArrayEnrichment from a dict
array_enrichment_form_dict = array_enrichment.from_dict(array_enrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


