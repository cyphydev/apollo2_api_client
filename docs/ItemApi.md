# apollo2_api_client.ItemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**item_attach_media_post**](ItemApi.md#item_attach_media_post) | **POST** /item/attach_media | Item Attach Media Post
[**item_batch_get**](ItemApi.md#item_batch_get) | **POST** /item/get | Item Batch Get
[**item_count_get**](ItemApi.md#item_count_get) | **GET** /item/count | Item Count Get
[**item_detach_media_post**](ItemApi.md#item_detach_media_post) | **POST** /item/detach_media | Item Detach Media Post
[**item_enrichments_batch_delete**](ItemApi.md#item_enrichments_batch_delete) | **POST** /item/enrichments/delete | Item Enrichments Batch Delete
[**item_enrichments_batch_get**](ItemApi.md#item_enrichments_batch_get) | **POST** /item/enrichments/get | Item Enrichments Batch Get
[**item_enrichments_batch_post**](ItemApi.md#item_enrichments_batch_post) | **POST** /item/enrichments/submit | Item Enrichments Batch Post
[**item_get**](ItemApi.md#item_get) | **GET** /item | Item Get
[**item_id_delete**](ItemApi.md#item_id_delete) | **DELETE** /item/{id} | Item Id Delete
[**item_id_enrichments_delete**](ItemApi.md#item_id_enrichments_delete) | **DELETE** /item/{id}/enrichments | Item Id Enrichments Delete
[**item_id_enrichments_get**](ItemApi.md#item_id_enrichments_get) | **GET** /item/{id}/enrichments | Item Id Enrichments Get
[**item_id_enrichments_post**](ItemApi.md#item_id_enrichments_post) | **POST** /item/{id}/enrichments | Item Id Enrichments Post
[**item_id_forward_batch_translate**](ItemApi.md#item_id_forward_batch_translate) | **POST** /item/id/forward | Item Id Forward Batch Translate
[**item_id_forward_batch_translate_map**](ItemApi.md#item_id_forward_batch_translate_map) | **POST** /item/id/forward/map | Item Id Forward Batch Translate Map
[**item_id_forward_translate**](ItemApi.md#item_id_forward_translate) | **GET** /item/id/forward/{id} | Item Id Forward Translate
[**item_id_get**](ItemApi.md#item_id_get) | **GET** /item/{id} | Item Id Get
[**item_id_identifier_get**](ItemApi.md#item_id_identifier_get) | **GET** /item/{id}/identifier | Item Id Identifier Get
[**item_id_reverse_batch_translate**](ItemApi.md#item_id_reverse_batch_translate) | **POST** /item/id/reverse | Item Id Reverse Batch Translate
[**item_id_reverse_batch_translate_map**](ItemApi.md#item_id_reverse_batch_translate_map) | **POST** /item/id/reverse/map | Item Id Reverse Batch Translate Map
[**item_id_reverse_translate**](ItemApi.md#item_id_reverse_translate) | **GET** /item/id/reverse/{id} | Item Id Reverse Translate
[**item_identifier_delete**](ItemApi.md#item_identifier_delete) | **POST** /item/identifier/delete | Item Identifier Delete
[**item_identifier_post**](ItemApi.md#item_identifier_post) | **POST** /item/identifier/post | Item Identifier Post
[**item_list_get**](ItemApi.md#item_list_get) | **GET** /item/list | Item List Get
[**item_max_id_get**](ItemApi.md#item_max_id_get) | **GET** /item/max_id | Item Max Id Get
[**item_univ_id_forward_batch_translate**](ItemApi.md#item_univ_id_forward_batch_translate) | **POST** /item/univ_id/forward | Item Univ Id Forward Batch Translate
[**item_univ_id_forward_batch_translate_map**](ItemApi.md#item_univ_id_forward_batch_translate_map) | **POST** /item/univ_id/forward/map | Item Univ Id Forward Batch Translate Map
[**item_univ_id_forward_translate**](ItemApi.md#item_univ_id_forward_translate) | **GET** /item/univ_id/forward/{univ_id} | Item Univ Id Forward Translate
[**item_univ_id_reverse_batch_translate**](ItemApi.md#item_univ_id_reverse_batch_translate) | **POST** /item/univ_id/reverse | Item Univ Id Reverse Batch Translate
[**item_univ_id_reverse_batch_translate_map**](ItemApi.md#item_univ_id_reverse_batch_translate_map) | **POST** /item/univ_id/reverse/map | Item Univ Id Reverse Batch Translate Map
[**item_univ_id_reverse_translate**](ItemApi.md#item_univ_id_reverse_translate) | **GET** /item/univ_id/reverse/{id} | Item Univ Id Reverse Translate


# **item_attach_media_post**
> str item_attach_media_post(modify_media_attachment_request)

Item Attach Media Post

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    modify_media_attachment_request = apollo2_api_client.ModifyMediaAttachmentRequest() # ModifyMediaAttachmentRequest | 

    try:
        # Item Attach Media Post
        api_response = api_instance.item_attach_media_post(modify_media_attachment_request)
        print("The response of ItemApi->item_attach_media_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_attach_media_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_media_attachment_request** | [**ModifyMediaAttachmentRequest**](ModifyMediaAttachmentRequest.md)|  | 

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

# **item_batch_get**
> List[Item] item_batch_get(batch_get_request)

Item Batch Get

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    batch_get_request = apollo2_api_client.BatchGetRequest() # BatchGetRequest | 

    try:
        # Item Batch Get
        api_response = api_instance.item_batch_get(batch_get_request)
        print("The response of ItemApi->item_batch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_get_request** | [**BatchGetRequest**](BatchGetRequest.md)|  | 

### Return type

[**List[Item]**](Item.md)

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

# **item_count_get**
> int item_count_get(last=last, end=end, platform=platform, actor_ids=actor_ids, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)

Item Count Get

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    last = 56 # int |  (optional)
    end = 56 # int |  (optional)
    platform = 'platform_example' # str |  (optional)
    actor_ids = 'actor_ids_example' # str |  (optional)
    identifier = 'identifier_example' # str |  (optional)
    inclusive_begin_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)
    exclusive_end_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)

    try:
        # Item Count Get
        api_response = api_instance.item_count_get(last=last, end=end, platform=platform, actor_ids=actor_ids, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)
        print("The response of ItemApi->item_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **platform** | **str**|  | [optional] 
 **actor_ids** | **str**|  | [optional] 
 **identifier** | **str**|  | [optional] 
 **inclusive_begin_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 
 **exclusive_end_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 

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

# **item_detach_media_post**
> str item_detach_media_post(modify_media_attachment_request)

Item Detach Media Post

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    modify_media_attachment_request = apollo2_api_client.ModifyMediaAttachmentRequest() # ModifyMediaAttachmentRequest | 

    try:
        # Item Detach Media Post
        api_response = api_instance.item_detach_media_post(modify_media_attachment_request)
        print("The response of ItemApi->item_detach_media_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_detach_media_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_media_attachment_request** | [**ModifyMediaAttachmentRequest**](ModifyMediaAttachmentRequest.md)|  | 

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

# **item_enrichments_batch_delete**
> str item_enrichments_batch_delete(enrichments_batch_request)

Item Enrichments Batch Delete

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    enrichments_batch_request = apollo2_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

    try:
        # Item Enrichments Batch Delete
        api_response = api_instance.item_enrichments_batch_delete(enrichments_batch_request)
        print("The response of ItemApi->item_enrichments_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_enrichments_batch_delete: %s\n" % e)
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

# **item_enrichments_batch_get**
> List[List[Enrichment]] item_enrichments_batch_get(enrichments_batch_request)

Item Enrichments Batch Get

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    enrichments_batch_request = apollo2_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

    try:
        # Item Enrichments Batch Get
        api_response = api_instance.item_enrichments_batch_get(enrichments_batch_request)
        print("The response of ItemApi->item_enrichments_batch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_enrichments_batch_get: %s\n" % e)
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

# **item_enrichments_batch_post**
> str item_enrichments_batch_post(request_body)

Item Enrichments Batch Post

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    request_body = None # Dict[str, List[Enrichment]] | 

    try:
        # Item Enrichments Batch Post
        api_response = api_instance.item_enrichments_batch_post(request_body)
        print("The response of ItemApi->item_enrichments_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_enrichments_batch_post: %s\n" % e)
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

# **item_get**
> List[Item] item_get(limit, last=last, end=end, actor_ids=actor_ids, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version, platform=platform, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)

Item Get

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    limit = 56 # int | 
    last = -1 # int |  (optional) (default to -1)
    end = 56 # int |  (optional)
    actor_ids = 'actor_ids_example' # str |  (optional)
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
    platform = 'platform_example' # str |  (optional)
    identifier = 'identifier_example' # str |  (optional)
    inclusive_begin_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)
    exclusive_end_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)

    try:
        # Item Get
        api_response = api_instance.item_get(limit, last=last, end=end, actor_ids=actor_ids, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version, platform=platform, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)
        print("The response of ItemApi->item_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | 
 **last** | **int**|  | [optional] [default to -1]
 **end** | **int**|  | [optional] 
 **actor_ids** | **str**|  | [optional] 
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
 **platform** | **str**|  | [optional] 
 **identifier** | **str**|  | [optional] 
 **inclusive_begin_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 
 **exclusive_end_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 

### Return type

[**List[Item]**](Item.md)

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

# **item_id_delete**
> str item_id_delete(id)

Item Id Delete

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    id = 56 # int | 

    try:
        # Item Id Delete
        api_response = api_instance.item_id_delete(id)
        print("The response of ItemApi->item_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_delete: %s\n" % e)
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

# **item_id_enrichments_delete**
> str item_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)

Item Id Enrichments Delete

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str |  (optional)
    provider = 'provider_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        # Item Id Enrichments Delete
        api_response = api_instance.item_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)
        print("The response of ItemApi->item_id_enrichments_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_enrichments_delete: %s\n" % e)
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

# **item_id_enrichments_get**
> List[Enrichment] item_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)

Item Id Enrichments Get

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str |  (optional)
    provider = 'provider_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        # Item Id Enrichments Get
        api_response = api_instance.item_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)
        print("The response of ItemApi->item_id_enrichments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_enrichments_get: %s\n" % e)
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

# **item_id_enrichments_post**
> str item_id_enrichments_post(id, enrichment)

Item Id Enrichments Post

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    id = 56 # int | 
    enrichment = [apollo2_api_client.Enrichment()] # List[Enrichment] | 

    try:
        # Item Id Enrichments Post
        api_response = api_instance.item_id_enrichments_post(id, enrichment)
        print("The response of ItemApi->item_id_enrichments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_enrichments_post: %s\n" % e)
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

# **item_id_forward_batch_translate**
> List[int] item_id_forward_batch_translate(request_body, platform=platform)

Item Id Forward Batch Translate

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    platform = apollo2_api_client.PlatformType() # PlatformType |  (optional)

    try:
        # Item Id Forward Batch Translate
        api_response = api_instance.item_id_forward_batch_translate(request_body, platform=platform)
        print("The response of ItemApi->item_id_forward_batch_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_forward_batch_translate: %s\n" % e)
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
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_id_forward_batch_translate_map**
> Dict[str, int] item_id_forward_batch_translate_map(request_body, strict=strict, platform=platform)

Item Id Forward Batch Translate Map

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    strict = False # bool |  (optional) (default to False)
    platform = apollo2_api_client.PlatformType() # PlatformType |  (optional)

    try:
        # Item Id Forward Batch Translate Map
        api_response = api_instance.item_id_forward_batch_translate_map(request_body, strict=strict, platform=platform)
        print("The response of ItemApi->item_id_forward_batch_translate_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_forward_batch_translate_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **strict** | **bool**|  | [optional] [default to False]
 **platform** | [**PlatformType**](.md)|  | [optional] 

### Return type

**Dict[str, int]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_id_forward_translate**
> int item_id_forward_translate(id, platform=platform)

Item Id Forward Translate

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    id = 'id_example' # str | 
    platform = apollo2_api_client.PlatformType() # PlatformType |  (optional)

    try:
        # Item Id Forward Translate
        api_response = api_instance.item_id_forward_translate(id, platform=platform)
        print("The response of ItemApi->item_id_forward_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_forward_translate: %s\n" % e)
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
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_id_get**
> Item item_id_get(id, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)

Item Id Get

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
    api_instance = apollo2_api_client.ItemApi(api_client)
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
        # Item Id Get
        api_response = api_instance.item_id_get(id, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)
        print("The response of ItemApi->item_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_get: %s\n" % e)
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

[**Item**](Item.md)

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

# **item_id_identifier_get**
> List[str] item_id_identifier_get(id)

Item Id Identifier Get

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    id = 56 # int | 

    try:
        # Item Id Identifier Get
        api_response = api_instance.item_id_identifier_get(id)
        print("The response of ItemApi->item_id_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_identifier_get: %s\n" % e)
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

# **item_id_reverse_batch_translate**
> List[str] item_id_reverse_batch_translate(request_body)

Item Id Reverse Batch Translate

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    request_body = [56] # List[int] | 

    try:
        # Item Id Reverse Batch Translate
        api_response = api_instance.item_id_reverse_batch_translate(request_body)
        print("The response of ItemApi->item_id_reverse_batch_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_reverse_batch_translate: %s\n" % e)
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
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_id_reverse_batch_translate_map**
> Dict[str, str] item_id_reverse_batch_translate_map(request_body)

Item Id Reverse Batch Translate Map

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    request_body = [56] # List[int] | 

    try:
        # Item Id Reverse Batch Translate Map
        api_response = api_instance.item_id_reverse_batch_translate_map(request_body)
        print("The response of ItemApi->item_id_reverse_batch_translate_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_reverse_batch_translate_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

**Dict[str, str]**

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

# **item_id_reverse_translate**
> str item_id_reverse_translate(id)

Item Id Reverse Translate

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    id = 56 # int | 

    try:
        # Item Id Reverse Translate
        api_response = api_instance.item_id_reverse_translate(id)
        print("The response of ItemApi->item_id_reverse_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_id_reverse_translate: %s\n" % e)
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
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_identifier_delete**
> str item_identifier_delete(identifier, request_body)

Item Identifier Delete

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    identifier = 'identifier_example' # str | 
    request_body = [56] # List[int] | 

    try:
        # Item Identifier Delete
        api_response = api_instance.item_identifier_delete(identifier, request_body)
        print("The response of ItemApi->item_identifier_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_identifier_delete: %s\n" % e)
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

# **item_identifier_post**
> str item_identifier_post(identifier, request_body)

Item Identifier Post

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    identifier = 'identifier_example' # str | 
    request_body = [56] # List[int] | 

    try:
        # Item Identifier Post
        api_response = api_instance.item_identifier_post(identifier, request_body)
        print("The response of ItemApi->item_identifier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_identifier_post: %s\n" % e)
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

# **item_list_get**
> List[int] item_list_get(limit, last=last, end=end, platform=platform, actor_ids=actor_ids, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)

Item List Get

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    limit = 56 # int | 
    last = -1 # int |  (optional) (default to -1)
    end = 56 # int |  (optional)
    platform = 'platform_example' # str |  (optional)
    actor_ids = 'actor_ids_example' # str |  (optional)
    identifier = 'identifier_example' # str |  (optional)
    inclusive_begin_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)
    exclusive_end_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)

    try:
        # Item List Get
        api_response = api_instance.item_list_get(limit, last=last, end=end, platform=platform, actor_ids=actor_ids, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)
        print("The response of ItemApi->item_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | 
 **last** | **int**|  | [optional] [default to -1]
 **end** | **int**|  | [optional] 
 **platform** | **str**|  | [optional] 
 **actor_ids** | **str**|  | [optional] 
 **identifier** | **str**|  | [optional] 
 **inclusive_begin_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 
 **exclusive_end_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 

### Return type

**List[int]**

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

# **item_max_id_get**
> int item_max_id_get(platform=platform, identifier=identifier, actor_ids=actor_ids, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)

Item Max Id Get

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    platform = 'platform_example' # str |  (optional)
    identifier = 'identifier_example' # str |  (optional)
    actor_ids = 'actor_ids_example' # str |  (optional)
    inclusive_begin_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)
    exclusive_end_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)

    try:
        # Item Max Id Get
        api_response = api_instance.item_max_id_get(platform=platform, identifier=identifier, actor_ids=actor_ids, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)
        print("The response of ItemApi->item_max_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_max_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  | [optional] 
 **identifier** | **str**|  | [optional] 
 **actor_ids** | **str**|  | [optional] 
 **inclusive_begin_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 
 **exclusive_end_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 

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

# **item_univ_id_forward_batch_translate**
> List[List[int]] item_univ_id_forward_batch_translate(request_body)

Item Univ Id Forward Batch Translate

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Item Univ Id Forward Batch Translate
        api_response = api_instance.item_univ_id_forward_batch_translate(request_body)
        print("The response of ItemApi->item_univ_id_forward_batch_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_univ_id_forward_batch_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[List[int]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_univ_id_forward_batch_translate_map**
> Dict[str, List[int]] item_univ_id_forward_batch_translate_map(request_body, strict=strict)

Item Univ Id Forward Batch Translate Map

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    strict = False # bool |  (optional) (default to False)

    try:
        # Item Univ Id Forward Batch Translate Map
        api_response = api_instance.item_univ_id_forward_batch_translate_map(request_body, strict=strict)
        print("The response of ItemApi->item_univ_id_forward_batch_translate_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_univ_id_forward_batch_translate_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **strict** | **bool**|  | [optional] [default to False]

### Return type

**Dict[str, List[int]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_univ_id_forward_translate**
> List[int] item_univ_id_forward_translate(univ_id)

Item Univ Id Forward Translate

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    univ_id = 'univ_id_example' # str | 

    try:
        # Item Univ Id Forward Translate
        api_response = api_instance.item_univ_id_forward_translate(univ_id)
        print("The response of ItemApi->item_univ_id_forward_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_univ_id_forward_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **univ_id** | **str**|  | 

### Return type

**List[int]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_univ_id_reverse_batch_translate**
> List[str] item_univ_id_reverse_batch_translate(request_body)

Item Univ Id Reverse Batch Translate

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    request_body = [56] # List[int] | 

    try:
        # Item Univ Id Reverse Batch Translate
        api_response = api_instance.item_univ_id_reverse_batch_translate(request_body)
        print("The response of ItemApi->item_univ_id_reverse_batch_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_univ_id_reverse_batch_translate: %s\n" % e)
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
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_univ_id_reverse_batch_translate_map**
> Dict[str, str] item_univ_id_reverse_batch_translate_map(request_body, strict=strict)

Item Univ Id Reverse Batch Translate Map

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    request_body = [56] # List[int] | 
    strict = False # bool |  (optional) (default to False)

    try:
        # Item Univ Id Reverse Batch Translate Map
        api_response = api_instance.item_univ_id_reverse_batch_translate_map(request_body, strict=strict)
        print("The response of ItemApi->item_univ_id_reverse_batch_translate_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_univ_id_reverse_batch_translate_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)|  | 
 **strict** | **bool**|  | [optional] [default to False]

### Return type

**Dict[str, str]**

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

# **item_univ_id_reverse_translate**
> str item_univ_id_reverse_translate(id)

Item Univ Id Reverse Translate

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
    api_instance = apollo2_api_client.ItemApi(api_client)
    id = 56 # int | 

    try:
        # Item Univ Id Reverse Translate
        api_response = api_instance.item_univ_id_reverse_translate(id)
        print("The response of ItemApi->item_univ_id_reverse_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_univ_id_reverse_translate: %s\n" % e)
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
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

