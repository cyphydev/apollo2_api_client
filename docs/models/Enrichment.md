# apollo2_api_client.model.enrichment.Enrichment

This is the unified interface for message enrichment output.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This is the unified interface for message enrichment output. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CategoryEnrichment](CategoryEnrichment.md) | [**CategoryEnrichment**](CategoryEnrichment.md) | [**CategoryEnrichment**](CategoryEnrichment.md) |  | 
[NumericalEnrichment](NumericalEnrichment.md) | [**NumericalEnrichment**](NumericalEnrichment.md) | [**NumericalEnrichment**](NumericalEnrichment.md) |  | 
[ArrayEnrichment](ArrayEnrichment.md) | [**ArrayEnrichment**](ArrayEnrichment.md) | [**ArrayEnrichment**](ArrayEnrichment.md) |  | 
[TextEnrichment](TextEnrichment.md) | [**TextEnrichment**](TextEnrichment.md) | [**TextEnrichment**](TextEnrichment.md) |  | 
[ListEnrichment](ListEnrichment.md) | [**ListEnrichment**](ListEnrichment.md) | [**ListEnrichment**](ListEnrichment.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

