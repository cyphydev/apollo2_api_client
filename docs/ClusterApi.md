# apollo2_api_client.ClusterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_delete**](ClusterApi.md#cluster_delete) | **DELETE** /cluster | Cluster Delete
[**cluster_enrichments_batch_delete**](ClusterApi.md#cluster_enrichments_batch_delete) | **POST** /cluster/enrichments/delete | Cluster Enrichments Batch Delete
[**cluster_enrichments_batch_get**](ClusterApi.md#cluster_enrichments_batch_get) | **POST** /cluster/enrichments/get | Cluster Enrichments Batch Get
[**cluster_enrichments_batch_post**](ClusterApi.md#cluster_enrichments_batch_post) | **POST** /cluster/enrichments/submit | Cluster Enrichments Batch Post
[**cluster_get**](ClusterApi.md#cluster_get) | **GET** /cluster | Cluster Get
[**cluster_id_delete**](ClusterApi.md#cluster_id_delete) | **DELETE** /cluster/{id} | Cluster Id Delete
[**cluster_id_delete_members_post**](ClusterApi.md#cluster_id_delete_members_post) | **POST** /cluster/{id}/delete_members | Cluster Id Delete Members Post
[**cluster_id_edit_members_post**](ClusterApi.md#cluster_id_edit_members_post) | **POST** /cluster/{id}/edit_members | Cluster Id Edit Members Post
[**cluster_id_enrichments_delete**](ClusterApi.md#cluster_id_enrichments_delete) | **DELETE** /cluster/{id}/enrichments | Cluster Id Enrichments Delete
[**cluster_id_enrichments_get**](ClusterApi.md#cluster_id_enrichments_get) | **GET** /cluster/{id}/enrichments | Cluster Id Enrichments Get
[**cluster_id_enrichments_post**](ClusterApi.md#cluster_id_enrichments_post) | **POST** /cluster/{id}/enrichments | Cluster Id Enrichments Post
[**cluster_id_get**](ClusterApi.md#cluster_id_get) | **GET** /cluster/{id} | Cluster Id Get
[**cluster_id_identifier_get**](ClusterApi.md#cluster_id_identifier_get) | **GET** /cluster/{id}/identifier | Cluster Id Identifier Get
[**cluster_id_max_id_get**](ClusterApi.md#cluster_id_max_id_get) | **GET** /cluster/{id}/max_id | Cluster Id Max Id Get
[**cluster_id_members_count_get**](ClusterApi.md#cluster_id_members_count_get) | **GET** /cluster/{id}/members/count | Cluster Id Members Count Get
[**cluster_id_members_get**](ClusterApi.md#cluster_id_members_get) | **GET** /cluster/{id}/members | Cluster Id Members Get
[**cluster_identifier_delete**](ClusterApi.md#cluster_identifier_delete) | **POST** /cluster/identifier/delete | Cluster Identifier Delete
[**cluster_identifier_post**](ClusterApi.md#cluster_identifier_post) | **POST** /cluster/identifier/post | Cluster Identifier Post
[**cluster_post**](ClusterApi.md#cluster_post) | **POST** /cluster | Cluster Post


# **cluster_delete**
> str cluster_delete(name, provider, tag, version)

Cluster Delete

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    name = 'name_example' # str | 
    provider = 'provider_example' # str | 
    tag = 'tag_example' # str | 
    version = 'version_example' # str | 

    try:
        # Cluster Delete
        api_response = api_instance.cluster_delete(name, provider, tag, version)
        print("The response of ClusterApi->cluster_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **provider** | **str**|  | 
 **tag** | **str**|  | 
 **version** | **str**|  | 

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
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_enrichments_batch_delete**
> str cluster_enrichments_batch_delete(enrichments_batch_request)

Cluster Enrichments Batch Delete

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    enrichments_batch_request = apollo2_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

    try:
        # Cluster Enrichments Batch Delete
        api_response = api_instance.cluster_enrichments_batch_delete(enrichments_batch_request)
        print("The response of ClusterApi->cluster_enrichments_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_enrichments_batch_delete: %s\n" % e)
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
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_enrichments_batch_get**
> List[List[Enrichment]] cluster_enrichments_batch_get(enrichments_batch_request)

Cluster Enrichments Batch Get

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    enrichments_batch_request = apollo2_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

    try:
        # Cluster Enrichments Batch Get
        api_response = api_instance.cluster_enrichments_batch_get(enrichments_batch_request)
        print("The response of ClusterApi->cluster_enrichments_batch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_enrichments_batch_get: %s\n" % e)
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
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_enrichments_batch_post**
> str cluster_enrichments_batch_post(request_body)

Cluster Enrichments Batch Post

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    request_body = None # Dict[str, List[Enrichment]] | 

    try:
        # Cluster Enrichments Batch Post
        api_response = api_instance.cluster_enrichments_batch_post(request_body)
        print("The response of ClusterApi->cluster_enrichments_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_enrichments_batch_post: %s\n" % e)
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
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_get**
> List[Cluster] cluster_get(name=name, provider=provider, tag=tag, version=version, identifier=identifier, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)

Cluster Get

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    name = 'name_example' # str |  (optional)
    provider = 'provider_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    version = 'version_example' # str |  (optional)
    identifier = 'identifier_example' # str |  (optional)
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
        # Cluster Get
        api_response = api_instance.cluster_get(name=name, provider=provider, tag=tag, version=version, identifier=identifier, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)
        print("The response of ClusterApi->cluster_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **identifier** | **str**|  | [optional] 
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

[**List[Cluster]**](Cluster.md)

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

# **cluster_id_delete**
> str cluster_id_delete(id)

Cluster Id Delete

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    id = 56 # int | 

    try:
        # Cluster Id Delete
        api_response = api_instance.cluster_id_delete(id)
        print("The response of ClusterApi->cluster_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_delete: %s\n" % e)
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
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_delete_members_post**
> str cluster_id_delete_members_post(id, request_body)

Cluster Id Delete Members Post

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    id = 56 # int | 
    request_body = [56] # List[int] | 

    try:
        # Cluster Id Delete Members Post
        api_response = api_instance.cluster_id_delete_members_post(id, request_body)
        print("The response of ClusterApi->cluster_id_delete_members_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_delete_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**List[int]**](int.md)|  | 

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
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_edit_members_post**
> str cluster_id_edit_members_post(id, request_body)

Cluster Id Edit Members Post

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    id = 56 # int | 
    request_body = None # Dict[str, object] | 

    try:
        # Cluster Id Edit Members Post
        api_response = api_instance.cluster_id_edit_members_post(id, request_body)
        print("The response of ClusterApi->cluster_id_edit_members_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_edit_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_enrichments_delete**
> str cluster_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)

Cluster Id Enrichments Delete

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str |  (optional)
    provider = 'provider_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        # Cluster Id Enrichments Delete
        api_response = api_instance.cluster_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)
        print("The response of ClusterApi->cluster_id_enrichments_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_enrichments_delete: %s\n" % e)
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
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_enrichments_get**
> List[Enrichment] cluster_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)

Cluster Id Enrichments Get

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str |  (optional)
    provider = 'provider_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        # Cluster Id Enrichments Get
        api_response = api_instance.cluster_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)
        print("The response of ClusterApi->cluster_id_enrichments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_enrichments_get: %s\n" % e)
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
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_enrichments_post**
> str cluster_id_enrichments_post(id, enrichment)

Cluster Id Enrichments Post

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    id = 56 # int | 
    enrichment = [apollo2_api_client.Enrichment()] # List[Enrichment] | 

    try:
        # Cluster Id Enrichments Post
        api_response = api_instance.cluster_id_enrichments_post(id, enrichment)
        print("The response of ClusterApi->cluster_id_enrichments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_enrichments_post: %s\n" % e)
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
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_get**
> Cluster cluster_id_get(id, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)

Cluster Id Get

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
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
        # Cluster Id Get
        api_response = api_instance.cluster_id_get(id, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)
        print("The response of ClusterApi->cluster_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_get: %s\n" % e)
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

[**Cluster**](Cluster.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_identifier_get**
> List[str] cluster_id_identifier_get(id)

Cluster Id Identifier Get

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    id = 56 # int | 

    try:
        # Cluster Id Identifier Get
        api_response = api_instance.cluster_id_identifier_get(id)
        print("The response of ClusterApi->cluster_id_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_identifier_get: %s\n" % e)
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
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_max_id_get**
> int cluster_id_max_id_get(id)

Cluster Id Max Id Get

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    id = 56 # int | 

    try:
        # Cluster Id Max Id Get
        api_response = api_instance.cluster_id_max_id_get(id)
        print("The response of ClusterApi->cluster_id_max_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_max_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_members_count_get**
> int cluster_id_members_count_get(id)

Cluster Id Members Count Get

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    id = 56 # int | 

    try:
        # Cluster Id Members Count Get
        api_response = api_instance.cluster_id_members_count_get(id)
        print("The response of ClusterApi->cluster_id_members_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_members_get**
> List[ClusterMember] cluster_id_members_get(id, limit, last=last, end=end)

Cluster Id Members Get

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    id = 56 # int | 
    limit = 56 # int | 
    last = -1 # int |  (optional) (default to -1)
    end = 56 # int |  (optional)

    try:
        # Cluster Id Members Get
        api_response = api_instance.cluster_id_members_get(id, limit, last=last, end=end)
        print("The response of ClusterApi->cluster_id_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**|  | 
 **last** | **int**|  | [optional] [default to -1]
 **end** | **int**|  | [optional] 

### Return type

[**List[ClusterMember]**](ClusterMember.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_identifier_delete**
> str cluster_identifier_delete(identifier, request_body)

Cluster Identifier Delete

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    identifier = 'identifier_example' # str | 
    request_body = [56] # List[int] | 

    try:
        # Cluster Identifier Delete
        api_response = api_instance.cluster_identifier_delete(identifier, request_body)
        print("The response of ClusterApi->cluster_identifier_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_identifier_delete: %s\n" % e)
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
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_identifier_post**
> str cluster_identifier_post(identifier, request_body)

Cluster Identifier Post

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    identifier = 'identifier_example' # str | 
    request_body = [56] # List[int] | 

    try:
        # Cluster Identifier Post
        api_response = api_instance.cluster_identifier_post(identifier, request_body)
        print("The response of ClusterApi->cluster_identifier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_identifier_post: %s\n" % e)
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
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_post**
> int cluster_post(cluster)

Cluster Post

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
    api_instance = apollo2_api_client.ClusterApi(api_client)
    cluster = apollo2_api_client.Cluster() # Cluster | 

    try:
        # Cluster Post
        api_response = api_instance.cluster_post(cluster)
        print("The response of ClusterApi->cluster_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | [**Cluster**](Cluster.md)|  | 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

