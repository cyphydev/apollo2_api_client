# JsonEnrichment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The enrichment (e.g., name for the enrichment. | 
**provider** | **str** | The team who provides the enrichment. | 
**tag** | **str** | The tag within the same (provider, name). | 
**version** | **str** | The version within the same (provider, name). | 
**type** | [**EnrichmentType**](EnrichmentType.md) |  | [optional] 
**value** | **object** |  | 

## Example

```python
from apollo2_api_client.models.json_enrichment import JsonEnrichment

# TODO update the JSON string below
json = "{}"
# create an instance of JsonEnrichment from a JSON string
json_enrichment_instance = JsonEnrichment.from_json(json)
# print the JSON string representation of the object
print JsonEnrichment.to_json()

# convert the object into a dict
json_enrichment_dict = json_enrichment_instance.to_dict()
# create an instance of JsonEnrichment from a dict
json_enrichment_form_dict = json_enrichment.from_dict(json_enrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


