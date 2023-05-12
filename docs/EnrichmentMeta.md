# EnrichmentMeta

This is the unified interface for message enrichment algorithm meta information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the enrichment algorithm. | 
**name** | **str** | The enrichment name for the enrichment. | 
**provider** | **str** | The team who provides the enrichment. | 
**tag** | **str** | The tag within the same (provider, name). | 
**version** | **str** | The version within the same (provider, name). | 
**data** | **object** |  | [optional] 
**type** | [**EnrichmentType**](EnrichmentType.md) |  | [optional] 
**categories** | **List[str]** | The list of categories for the enrichment. | 
**label_map** | **Dict[str, int]** | The mapping from label to index. | 

## Example

```python
from apollo2_api_client.models.enrichment_meta import EnrichmentMeta

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentMeta from a JSON string
enrichment_meta_instance = EnrichmentMeta.from_json(json)
# print the JSON string representation of the object
print EnrichmentMeta.to_json()

# convert the object into a dict
enrichment_meta_dict = enrichment_meta_instance.to_dict()
# create an instance of EnrichmentMeta from a dict
enrichment_meta_form_dict = enrichment_meta.from_dict(enrichment_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


