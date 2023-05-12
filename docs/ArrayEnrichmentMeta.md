# ArrayEnrichmentMeta


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
**label_map** | **Dict[str, int]** | The mapping from label to index. | 

## Example

```python
from apollo2_api_client.models.array_enrichment_meta import ArrayEnrichmentMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayEnrichmentMeta from a JSON string
array_enrichment_meta_instance = ArrayEnrichmentMeta.from_json(json)
# print the JSON string representation of the object
print ArrayEnrichmentMeta.to_json()

# convert the object into a dict
array_enrichment_meta_dict = array_enrichment_meta_instance.to_dict()
# create an instance of ArrayEnrichmentMeta from a dict
array_enrichment_meta_form_dict = array_enrichment_meta.from_dict(array_enrichment_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


