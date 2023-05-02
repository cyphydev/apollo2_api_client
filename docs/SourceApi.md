# apollo2_api_client.SourceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**source_batch_get**](SourceApi.md#source_batch_get) | **POST** /source/get | Source Batch Get
[**source_count_get**](SourceApi.md#source_count_get) | **GET** /source/count | Source Count Get
[**source_enrichments_batch_delete**](SourceApi.md#source_enrichments_batch_delete) | **POST** /source/enrichments/delete | Source Enrichments Batch Delete
[**source_enrichments_batch_get**](SourceApi.md#source_enrichments_batch_get) | **POST** /source/enrichments/get | Source Enrichments Batch Get
[**source_enrichments_batch_post**](SourceApi.md#source_enrichments_batch_post) | **POST** /source/enrichments/submit | Source Enrichments Batch Post
[**source_get**](SourceApi.md#source_get) | **GET** /source | Source Get
[**source_id_delete**](SourceApi.md#source_id_delete) | **DELETE** /source/{id} | Source Id Delete
[**source_id_enrichments_delete**](SourceApi.md#source_id_enrichments_delete) | **DELETE** /source/{id}/enrichments | Source Id Enrichments Delete
[**source_id_enrichments_get**](SourceApi.md#source_id_enrichments_get) | **GET** /source/{id}/enrichments | Source Id Enrichments Get
[**source_id_enrichments_post**](SourceApi.md#source_id_enrichments_post) | **POST** /source/{id}/enrichments | Source Id Enrichments Post
[**source_id_forward_batch_translate**](SourceApi.md#source_id_forward_batch_translate) | **POST** /source/id/forward | Source Id Forward Batch Translate
[**source_id_forward_translate**](SourceApi.md#source_id_forward_translate) | **GET** /source/id/forward/{id} | Source Id Forward Translate
[**source_id_get**](SourceApi.md#source_id_get) | **GET** /source/{id} | Source Id Get
[**source_id_identifer_get**](SourceApi.md#source_id_identifer_get) | **GET** /source/{id}/identifer | Source Id Identifer Get
[**source_id_reverse_batch_translate**](SourceApi.md#source_id_reverse_batch_translate) | **POST** /source/id/reverse | Source Id Reverse Batch Translate
[**source_id_reverse_translate**](SourceApi.md#source_id_reverse_translate) | **GET** /source/id/reverse/{id} | Source Id Reverse Translate
[**source_identifer_delete**](SourceApi.md#source_identifer_delete) | **POST** /source/identifer/delete | Source Identifer Delete
[**source_identifer_post**](SourceApi.md#source_identifer_post) | **POST** /source/identifer/post | Source Identifer Post
[**source_max_id_get**](SourceApi.md#source_max_id_get) | **GET** /source/max_id | Source Max Id Get


# **source_batch_get**
> List[Source] source_batch_get(batch_get_request, identifier=identifier)

Source Batch Get

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    batch_get_request = apollo2_api_client.BatchGetRequest() # BatchGetRequest | 
    identifier = 'identifier_example' # str |  (optional)

    try:
        # Source Batch Get
        api_response = api_instance.source_batch_get(batch_get_request, identifier=identifier)
        print("The response of SourceApi->source_batch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_get_request** | [**BatchGetRequest**](BatchGetRequest.md)|  | 
 **identifier** | **str**|  | [optional] 

### Return type

[**List[Source]**](Source.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_count_get**
> int source_count_get(last=last, end=end, platform=platform, identifier=identifier)

Source Count Get

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    last = 56 # int |  (optional)
    end = 56 # int |  (optional)
    platform = apollo2_api_client.PlatformType() # PlatformType |  (optional)
    identifier = 'identifier_example' # str |  (optional)

    try:
        # Source Count Get
        api_response = api_instance.source_count_get(last=last, end=end, platform=platform, identifier=identifier)
        print("The response of SourceApi->source_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **platform** | [**PlatformType**](.md)|  | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

**int**

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

# **source_enrichments_batch_delete**
> str source_enrichments_batch_delete(enrichments_batch_request)

Source Enrichments Batch Delete

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    enrichments_batch_request = apollo2_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

    try:
        # Source Enrichments Batch Delete
        api_response = api_instance.source_enrichments_batch_delete(enrichments_batch_request)
        print("The response of SourceApi->source_enrichments_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_enrichments_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichments_batch_request** | [**EnrichmentsBatchRequest**](EnrichmentsBatchRequest.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_enrichments_batch_get**
> List[List[Enrichment]] source_enrichments_batch_get(enrichments_batch_request)

Source Enrichments Batch Get

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    enrichments_batch_request = apollo2_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

    try:
        # Source Enrichments Batch Get
        api_response = api_instance.source_enrichments_batch_get(enrichments_batch_request)
        print("The response of SourceApi->source_enrichments_batch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_enrichments_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichments_batch_request** | [**EnrichmentsBatchRequest**](EnrichmentsBatchRequest.md)|  | 

### Return type

**List[List[Enrichment]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_enrichments_batch_post**
> str source_enrichments_batch_post(request_body)

Source Enrichments Batch Post

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    request_body = None # Dict[str, List[Enrichment]] | 

    try:
        # Source Enrichments Batch Post
        api_response = api_instance.source_enrichments_batch_post(request_body)
        print("The response of SourceApi->source_enrichments_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_enrichments_batch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, List[Enrichment]]**](List.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_get**
> List[Source] source_get(limit, last=last, end=end, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version, platform=platform, identifier=identifier)

Source Get

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    limit = 56 # int | 
    last = -1 # int |  (optional) (default to -1)
    end = 56 # int |  (optional)
    with_enrichment = False # bool |  (optional) (default to False)
    with_cluster = False # bool |  (optional) (default to False)
    enrichment_name = 'enrichment_name_example' # str |  (optional)
    enrichment_provider = 'enrichment_provider_example' # str |  (optional)
    enrichment_tag = 'enrichment_tag_example' # str |  (optional)
    enrichment_version = 'enrichment_version_example' # str |  (optional)
    cluster_name = 'cluster_name_example' # str |  (optional)
    cluster_provider = 'cluster_provider_example' # str |  (optional)
    cluster_tag = 'cluster_tag_example' # str |  (optional)
    cluster_version = 'cluster_version_example' # str |  (optional)
    platform = apollo2_api_client.PlatformType() # PlatformType |  (optional)
    identifier = 'identifier_example' # str |  (optional)

    try:
        # Source Get
        api_response = api_instance.source_get(limit, last=last, end=end, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version, platform=platform, identifier=identifier)
        print("The response of SourceApi->source_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | 
 **last** | **int**|  | [optional] [default to -1]
 **end** | **int**|  | [optional] 
 **with_enrichment** | **bool**|  | [optional] [default to False]
 **with_cluster** | **bool**|  | [optional] [default to False]
 **enrichment_name** | **str**|  | [optional] 
 **enrichment_provider** | **str**|  | [optional] 
 **enrichment_tag** | **str**|  | [optional] 
 **enrichment_version** | **str**|  | [optional] 
 **cluster_name** | **str**|  | [optional] 
 **cluster_provider** | **str**|  | [optional] 
 **cluster_tag** | **str**|  | [optional] 
 **cluster_version** | **str**|  | [optional] 
 **platform** | [**PlatformType**](.md)|  | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

[**List[Source]**](Source.md)

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

# **source_id_delete**
> str source_id_delete(id)

Source Id Delete

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    id = 56 # int | 

    try:
        # Source Id Delete
        api_response = api_instance.source_id_delete(id)
        print("The response of SourceApi->source_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**str**

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

# **source_id_enrichments_delete**
> str source_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)

Source Id Enrichments Delete

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str |  (optional)
    provider = 'provider_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        # Source Id Enrichments Delete
        api_response = api_instance.source_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)
        print("The response of SourceApi->source_id_enrichments_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_id_enrichments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_enrichments_get**
> List[Enrichment] source_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)

Source Id Enrichments Get

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str |  (optional)
    provider = 'provider_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        # Source Id Enrichments Get
        api_response = api_instance.source_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)
        print("The response of SourceApi->source_id_enrichments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_id_enrichments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**List[Enrichment]**](Enrichment.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_enrichments_post**
> str source_id_enrichments_post(id, enrichment)

Source Id Enrichments Post

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    id = 56 # int | 
    enrichment = [apollo2_api_client.Enrichment()] # List[Enrichment] | 

    try:
        # Source Id Enrichments Post
        api_response = api_instance.source_id_enrichments_post(id, enrichment)
        print("The response of SourceApi->source_id_enrichments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_id_enrichments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **enrichment** | [**List[Enrichment]**](Enrichment.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_forward_batch_translate**
> List[int] source_id_forward_batch_translate(request_body, platform=platform)

Source Id Forward Batch Translate

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    platform = apollo2_api_client.PlatformType() # PlatformType |  (optional)

    try:
        # Source Id Forward Batch Translate
        api_response = api_instance.source_id_forward_batch_translate(request_body, platform=platform)
        print("The response of SourceApi->source_id_forward_batch_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_id_forward_batch_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **platform** | [**PlatformType**](.md)|  | [optional] 

### Return type

**List[int]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_forward_translate**
> int source_id_forward_translate(id, platform=platform)

Source Id Forward Translate

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    id = 'id_example' # str | 
    platform = apollo2_api_client.PlatformType() # PlatformType |  (optional)

    try:
        # Source Id Forward Translate
        api_response = api_instance.source_id_forward_translate(id, platform=platform)
        print("The response of SourceApi->source_id_forward_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_id_forward_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform** | [**PlatformType**](.md)|  | [optional] 

### Return type

**int**

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

# **source_id_get**
> Source source_id_get(id, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)

Source Id Get

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    id = 56 # int | 
    with_enrichment = False # bool |  (optional) (default to False)
    with_cluster = False # bool |  (optional) (default to False)
    enrichment_name = 'enrichment_name_example' # str |  (optional)
    enrichment_provider = 'enrichment_provider_example' # str |  (optional)
    enrichment_tag = 'enrichment_tag_example' # str |  (optional)
    enrichment_version = 'enrichment_version_example' # str |  (optional)
    cluster_name = 'cluster_name_example' # str |  (optional)
    cluster_provider = 'cluster_provider_example' # str |  (optional)
    cluster_tag = 'cluster_tag_example' # str |  (optional)
    cluster_version = 'cluster_version_example' # str |  (optional)

    try:
        # Source Id Get
        api_response = api_instance.source_id_get(id, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)
        print("The response of SourceApi->source_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **with_enrichment** | **bool**|  | [optional] [default to False]
 **with_cluster** | **bool**|  | [optional] [default to False]
 **enrichment_name** | **str**|  | [optional] 
 **enrichment_provider** | **str**|  | [optional] 
 **enrichment_tag** | **str**|  | [optional] 
 **enrichment_version** | **str**|  | [optional] 
 **cluster_name** | **str**|  | [optional] 
 **cluster_provider** | **str**|  | [optional] 
 **cluster_tag** | **str**|  | [optional] 
 **cluster_version** | **str**|  | [optional] 

### Return type

[**Source**](Source.md)

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

# **source_id_identifer_get**
> List[str] source_id_identifer_get(id)

Source Id Identifer Get

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    id = 56 # int | 

    try:
        # Source Id Identifer Get
        api_response = api_instance.source_id_identifer_get(id)
        print("The response of SourceApi->source_id_identifer_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_id_identifer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**List[str]**

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

# **source_id_reverse_batch_translate**
> List[str] source_id_reverse_batch_translate(request_body)

Source Id Reverse Batch Translate

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    request_body = [56] # List[int] | 

    try:
        # Source Id Reverse Batch Translate
        api_response = api_instance.source_id_reverse_batch_translate(request_body)
        print("The response of SourceApi->source_id_reverse_batch_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_id_reverse_batch_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

**List[str]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_reverse_translate**
> str source_id_reverse_translate(id)

Source Id Reverse Translate

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    id = 56 # int | 

    try:
        # Source Id Reverse Translate
        api_response = api_instance.source_id_reverse_translate(id)
        print("The response of SourceApi->source_id_reverse_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_id_reverse_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**str**

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

# **source_identifer_delete**
> str source_identifer_delete(identifier, request_body)

Source Identifer Delete

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    identifier = 'identifier_example' # str | 
    request_body = [56] # List[int] | 

    try:
        # Source Identifer Delete
        api_response = api_instance.source_identifer_delete(identifier, request_body)
        print("The response of SourceApi->source_identifer_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_identifer_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_identifer_post**
> str source_identifer_post(identifier, request_body)

Source Identifer Post

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    identifier = 'identifier_example' # str | 
    request_body = [56] # List[int] | 

    try:
        # Source Identifer Post
        api_response = api_instance.source_identifer_post(identifier, request_body)
        print("The response of SourceApi->source_identifer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_identifer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_max_id_get**
> int source_max_id_get(platform=platform, identifier=identifier)

Source Max Id Get

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
    api_instance = apollo2_api_client.SourceApi(api_client)
    platform = apollo2_api_client.PlatformType() # PlatformType |  (optional)
    identifier = 'identifier_example' # str |  (optional)

    try:
        # Source Max Id Get
        api_response = api_instance.source_max_id_get(platform=platform, identifier=identifier)
        print("The response of SourceApi->source_max_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_max_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | [**PlatformType**](.md)|  | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

**int**

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

