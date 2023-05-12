# NumericalEnrichment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The enrichment (e.g., name for the enrichment. | 
**provider** | **str** | The team who provides the enrichment. | 
**tag** | **str** | The tag within the same (provider, name). | 
**version** | **str** | The version within the same (provider, name). | 
**type** | [**EnrichmentType**](EnrichmentType.md) |  | [optional] 
**value** | **float** |  | 
**confidence** | **float** | The confidence that this enrichment is correct, expressed as a percentage between 0.0 and 1.0 | [optional] 

## Example

```python
from apollo2_api_client.models.numerical_enrichment import NumericalEnrichment

# TODO update the JSON string below
json = "{}"
# create an instance of NumericalEnrichment from a JSON string
numerical_enrichment_instance = NumericalEnrichment.from_json(json)
# print the JSON string representation of the object
print NumericalEnrichment.to_json()

# convert the object into a dict
numerical_enrichment_dict = numerical_enrichment_instance.to_dict()
# create an instance of NumericalEnrichment from a dict
numerical_enrichment_form_dict = numerical_enrichment.from_dict(numerical_enrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


