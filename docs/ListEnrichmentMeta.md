# ListEnrichmentMeta


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
from apollo2_api_client.models.list_enrichment_meta import ListEnrichmentMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ListEnrichmentMeta from a JSON string
list_enrichment_meta_instance = ListEnrichmentMeta.from_json(json)
# print the JSON string representation of the object
print ListEnrichmentMeta.to_json()

# convert the object into a dict
list_enrichment_meta_dict = list_enrichment_meta_instance.to_dict()
# create an instance of ListEnrichmentMeta from a dict
list_enrichment_meta_form_dict = list_enrichment_meta.from_dict(list_enrichment_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


