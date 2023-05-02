# apollo2_api_client.MediaItemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**media_item_batch_get**](MediaItemApi.md#media_item_batch_get) | **POST** /media_item/get | Media Item Batch Get
[**media_item_count_get**](MediaItemApi.md#media_item_count_get) | **GET** /media_item/count | Media Item Count Get
[**media_item_get**](MediaItemApi.md#media_item_get) | **GET** /media_item | Media Item Get
[**media_item_id_delete**](MediaItemApi.md#media_item_id_delete) | **DELETE** /media_item/{id} | Media Item Id Delete
[**media_item_id_get**](MediaItemApi.md#media_item_id_get) | **GET** /media_item/{id} | Media Item Id Get
[**media_item_id_identifer_get**](MediaItemApi.md#media_item_id_identifer_get) | **GET** /media_item/{id}/identifer | Media Item Id Identifer Get
[**media_item_identifer_delete**](MediaItemApi.md#media_item_identifer_delete) | **POST** /media_item/identifer/delete | Media Item Identifer Delete
[**media_item_identifer_post**](MediaItemApi.md#media_item_identifer_post) | **POST** /media_item/identifer/post | Media Item Identifer Post
[**media_item_max_id_get**](MediaItemApi.md#media_item_max_id_get) | **GET** /media_item/max_id | Media Item Max Id Get


# **media_item_batch_get**
> List[MediaItem] media_item_batch_get(batch_media_get_request, identifier=identifier)

Media Item Batch Get

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
    api_instance = apollo2_api_client.MediaItemApi(api_client)
    batch_media_get_request = apollo2_api_client.BatchMediaGetRequest() # BatchMediaGetRequest | 
    identifier = 'identifier_example' # str |  (optional)

    try:
        # Media Item Batch Get
        api_response = api_instance.media_item_batch_get(batch_media_get_request, identifier=identifier)
        print("The response of MediaItemApi->media_item_batch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaItemApi->media_item_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_media_get_request** | [**BatchMediaGetRequest**](BatchMediaGetRequest.md)|  | 
 **identifier** | **str**|  | [optional] 

### Return type

[**List[MediaItem]**](MediaItem.md)

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

# **media_item_count_get**
> int media_item_count_get(last=last, end=end, identifier=identifier)

Media Item Count Get

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
    api_instance = apollo2_api_client.MediaItemApi(api_client)
    last = 56 # int |  (optional)
    end = 56 # int |  (optional)
    identifier = 'identifier_example' # str |  (optional)

    try:
        # Media Item Count Get
        api_response = api_instance.media_item_count_get(last=last, end=end, identifier=identifier)
        print("The response of MediaItemApi->media_item_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaItemApi->media_item_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
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

# **media_item_get**
> List[MediaItem] media_item_get(limit, last=last, end=end, identifier=identifier)

Media Item Get

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
    api_instance = apollo2_api_client.MediaItemApi(api_client)
    limit = 56 # int | 
    last = -1 # int |  (optional) (default to -1)
    end = 56 # int |  (optional)
    identifier = 'identifier_example' # str |  (optional)

    try:
        # Media Item Get
        api_response = api_instance.media_item_get(limit, last=last, end=end, identifier=identifier)
        print("The response of MediaItemApi->media_item_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaItemApi->media_item_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | 
 **last** | **int**|  | [optional] [default to -1]
 **end** | **int**|  | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

[**List[MediaItem]**](MediaItem.md)

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

# **media_item_id_delete**
> str media_item_id_delete(id)

Media Item Id Delete

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
    api_instance = apollo2_api_client.MediaItemApi(api_client)
    id = 56 # int | 

    try:
        # Media Item Id Delete
        api_response = api_instance.media_item_id_delete(id)
        print("The response of MediaItemApi->media_item_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaItemApi->media_item_id_delete: %s\n" % e)
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

# **media_item_id_get**
> MediaItem media_item_id_get(id)

Media Item Id Get

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
    api_instance = apollo2_api_client.MediaItemApi(api_client)
    id = 56 # int | 

    try:
        # Media Item Id Get
        api_response = api_instance.media_item_id_get(id)
        print("The response of MediaItemApi->media_item_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaItemApi->media_item_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MediaItem**](MediaItem.md)

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

# **media_item_id_identifer_get**
> List[str] media_item_id_identifer_get(id)

Media Item Id Identifer Get

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
    api_instance = apollo2_api_client.MediaItemApi(api_client)
    id = 56 # int | 

    try:
        # Media Item Id Identifer Get
        api_response = api_instance.media_item_id_identifer_get(id)
        print("The response of MediaItemApi->media_item_id_identifer_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaItemApi->media_item_id_identifer_get: %s\n" % e)
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

# **media_item_identifer_delete**
> str media_item_identifer_delete(identifier, request_body)

Media Item Identifer Delete

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
    api_instance = apollo2_api_client.MediaItemApi(api_client)
    identifier = 'identifier_example' # str | 
    request_body = [56] # List[int] | 

    try:
        # Media Item Identifer Delete
        api_response = api_instance.media_item_identifer_delete(identifier, request_body)
        print("The response of MediaItemApi->media_item_identifer_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaItemApi->media_item_identifer_delete: %s\n" % e)
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

# **media_item_identifer_post**
> str media_item_identifer_post(identifier, request_body)

Media Item Identifer Post

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
    api_instance = apollo2_api_client.MediaItemApi(api_client)
    identifier = 'identifier_example' # str | 
    request_body = [56] # List[int] | 

    try:
        # Media Item Identifer Post
        api_response = api_instance.media_item_identifer_post(identifier, request_body)
        print("The response of MediaItemApi->media_item_identifer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaItemApi->media_item_identifer_post: %s\n" % e)
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

# **media_item_max_id_get**
> int media_item_max_id_get(identifier=identifier)

Media Item Max Id Get

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
    api_instance = apollo2_api_client.MediaItemApi(api_client)
    identifier = 'identifier_example' # str |  (optional)

    try:
        # Media Item Max Id Get
        api_response = api_instance.media_item_max_id_get(identifier=identifier)
        print("The response of MediaItemApi->media_item_max_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaItemApi->media_item_max_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

