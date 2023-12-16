# CategoryEnrichmentMeta


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

## Example

```python
from apollo2_api_client.models import CategoryEnrichmentMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryEnrichmentMeta from a JSON string
category_enrichment_meta_instance = CategoryEnrichmentMeta.from_json(json)
# print the JSON string representation of the object
print CategoryEnrichmentMeta.to_json()

# convert the object into a dict
category_enrichment_meta_dict = category_enrichment_meta_instance.to_dict()
# create an instance of CategoryEnrichmentMeta from a dict
category_enrichment_meta_form_dict = category_enrichment_meta.from_dict(category_enrichment_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


