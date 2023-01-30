# mips_api_client.EnrichmentApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrichments_meta_post**](EnrichmentApi.md#enrichments_meta_post) | **POST** /enrichments/meta | Enrichments Meta Post
[**generic_enrichments_meta_delete**](EnrichmentApi.md#generic_enrichments_meta_delete) | **DELETE** /enrichments/meta | Generic Enrichments Meta Delete
[**generic_enrichments_meta_get**](EnrichmentApi.md#generic_enrichments_meta_get) | **GET** /enrichments/meta | Generic Enrichments Meta Get

# **enrichments_meta_post**
> str enrichments_meta_post(body)

Enrichments Meta Post

### Example
```python
from __future__ import print_function
import time
import mips_api_client
from mips_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = mips_api_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = mips_api_client.EnrichmentApi(mips_api_client.ApiClient(configuration))
body = mips_api_client.EnrichmentMeta() # EnrichmentMeta | 

try:
    # Enrichments Meta Post
    api_response = api_instance.enrichments_meta_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->enrichments_meta_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrichmentMeta**](EnrichmentMeta.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generic_enrichments_meta_delete**
> str generic_enrichments_meta_delete(name, provider, tag, version, force)

Generic Enrichments Meta Delete

### Example
```python
from __future__ import print_function
import time
import mips_api_client
from mips_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = mips_api_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = mips_api_client.EnrichmentApi(mips_api_client.ApiClient(configuration))
name = 'name_example' # str | 
provider = 'provider_example' # str | 
tag = 'tag_example' # str | 
version = 'version_example' # str | 
force = true # bool | 

try:
    # Generic Enrichments Meta Delete
    api_response = api_instance.generic_enrichments_meta_delete(name, provider, tag, version, force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->generic_enrichments_meta_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **provider** | **str**|  | 
 **tag** | **str**|  | 
 **version** | **str**|  | 
 **force** | **bool**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generic_enrichments_meta_get**
> list[EnrichmentMeta] generic_enrichments_meta_get(name=name, provider=provider, tag=tag, version=version)

Generic Enrichments Meta Get

### Example
```python
from __future__ import print_function
import time
import mips_api_client
from mips_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = mips_api_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = mips_api_client.EnrichmentApi(mips_api_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    # Generic Enrichments Meta Get
    api_response = api_instance.generic_enrichments_meta_get(name=name, provider=provider, tag=tag, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->generic_enrichments_meta_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**list[EnrichmentMeta]**](EnrichmentMeta.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

