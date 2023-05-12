# apollo2_api_client.EnrichmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrichments_meta_delete**](EnrichmentApi.md#enrichments_meta_delete) | **DELETE** /enrichments/meta | Enrichments Meta Delete
[**enrichments_meta_get**](EnrichmentApi.md#enrichments_meta_get) | **GET** /enrichments/meta | Enrichments Meta Get
[**enrichments_meta_post**](EnrichmentApi.md#enrichments_meta_post) | **POST** /enrichments/meta | Enrichments Meta Post


# **enrichments_meta_delete**
> str enrichments_meta_delete(name, provider, tag, version, force)

Enrichments Meta Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import os
import apollo2_api_client
from apollo2_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apollo2_api_client.EnrichmentApi(api_client)
    name = 'name_example' # str | 
    provider = 'provider_example' # str | 
    tag = 'tag_example' # str | 
    version = 'version_example' # str | 
    force = True # bool | 

    try:
        # Enrichments Meta Delete
        api_response = api_instance.enrichments_meta_delete(name, provider, tag, version, force)
        print("The response of EnrichmentApi->enrichments_meta_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrichmentApi->enrichments_meta_delete: %s\n" % e)
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
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrichments_meta_get**
> List[EnrichmentMeta] enrichments_meta_get(name=name, provider=provider, tag=tag, version=version)

Enrichments Meta Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import os
import apollo2_api_client
from apollo2_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apollo2_api_client.EnrichmentApi(api_client)
    name = 'name_example' # str |  (optional)
    provider = 'provider_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        # Enrichments Meta Get
        api_response = api_instance.enrichments_meta_get(name=name, provider=provider, tag=tag, version=version)
        print("The response of EnrichmentApi->enrichments_meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrichmentApi->enrichments_meta_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**List[EnrichmentMeta]**](EnrichmentMeta.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrichments_meta_post**
> str enrichments_meta_post(enrichment_meta)

Enrichments Meta Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import os
import apollo2_api_client
from apollo2_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apollo2_api_client.EnrichmentApi(api_client)
    enrichment_meta = apollo2_api_client.EnrichmentMeta() # EnrichmentMeta | 

    try:
        # Enrichments Meta Post
        api_response = api_instance.enrichments_meta_post(enrichment_meta)
        print("The response of EnrichmentApi->enrichments_meta_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrichmentApi->enrichments_meta_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_meta** | [**EnrichmentMeta**](EnrichmentMeta.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

