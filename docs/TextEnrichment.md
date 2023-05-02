# TextEnrichment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The enrichment (e.g., name for the enrichment. | 
**provider** | **str** | The team who provides the enrichment. | 
**tag** | **str** | The tag within the same (provider, name). | 
**version** | **str** | The version within the same (provider, name). | 
**type** | [**EnrichmentType**](EnrichmentType.md) |  | [optional] 
**value** | **str** |  | 
**confidence** | **float** | The confidence that this enrichment is correct, expressed as a percentage between 0.0 and 1.0 | [optional] 

## Example

```python
from apollo2_api_client.models.text_enrichment import TextEnrichment

# TODO update the JSON string below
json = "{}"
# create an instance of TextEnrichment from a JSON string
text_enrichment_instance = TextEnrichment.from_json(json)
# print the JSON string representation of the object
print TextEnrichment.to_json()

# convert the object into a dict
text_enrichment_dict = text_enrichment_instance.to_dict()
# create an instance of TextEnrichment from a dict
text_enrichment_form_dict = text_enrichment.from_dict(text_enrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


