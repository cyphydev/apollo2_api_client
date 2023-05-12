# apollo2_api_client.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_data_post**](AdminApi.md#admin_data_post) | **POST** /data | Admin Data Post
[**admin_flush**](AdminApi.md#admin_flush) | **DELETE** /dbflush | Admin Flush
[**status_get**](AdminApi.md#status_get) | **GET** /status | Status Get


# **admin_data_post**
> RawDataPostResponse admin_data_post(raw_data_post_request)

Admin Data Post

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
    api_instance = apollo2_api_client.AdminApi(api_client)
    raw_data_post_request = apollo2_api_client.RawDataPostRequest() # RawDataPostRequest | 

    try:
        # Admin Data Post
        api_response = api_instance.admin_data_post(raw_data_post_request)
        print("The response of AdminApi->admin_data_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_data_post_request** | [**RawDataPostRequest**](RawDataPostRequest.md)|  | 

### Return type

[**RawDataPostResponse**](RawDataPostResponse.md)

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

# **admin_flush**
> str admin_flush()

Admin Flush

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
    api_instance = apollo2_api_client.AdminApi(api_client)

    try:
        # Admin Flush
        api_response = api_instance.admin_flush()
        print("The response of AdminApi->admin_flush:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_flush: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> object status_get()

Status Get

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
    api_instance = apollo2_api_client.AdminApi(api_client)

    try:
        # Status Get
        api_response = api_instance.status_get()
        print("The response of AdminApi->status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

