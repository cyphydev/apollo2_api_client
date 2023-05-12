# JsonEnrichmentMeta


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

## Example

```python
from apollo2_api_client.models.json_enrichment_meta import JsonEnrichmentMeta

# TODO update the JSON string below
json = "{}"
# create an instance of JsonEnrichmentMeta from a JSON string
json_enrichment_meta_instance = JsonEnrichmentMeta.from_json(json)
# print the JSON string representation of the object
print JsonEnrichmentMeta.to_json()

# convert the object into a dict
json_enrichment_meta_dict = json_enrichment_meta_instance.to_dict()
# create an instance of JsonEnrichmentMeta from a dict
json_enrichment_meta_form_dict = json_enrichment_meta.from_dict(json_enrichment_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


