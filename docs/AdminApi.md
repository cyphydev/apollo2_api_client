# apollo2_api_client.AdminApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_data_post**](AdminApi.md#admin_data_post) | **POST** /data | Admin Data Post
[**admin_flush**](AdminApi.md#admin_flush) | **DELETE** /dbflush | Admin Flush
[**status_get**](AdminApi.md#status_get) | **GET** /status | Status Get

# **admin_data_post**
> RawDataPostResponse admin_data_post(body)

Admin Data Post

### Example
```python
from __future__ import print_function
import time
import apollo2_api_client
from apollo2_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = apollo2_api_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = apollo2_api_client.AdminApi(apollo2_api_client.ApiClient(configuration))
body = apollo2_api_client.RawDataPostRequest() # RawDataPostRequest | 

try:
    # Admin Data Post
    api_response = api_instance.admin_data_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RawDataPostRequest**](RawDataPostRequest.md)|  | 

### Return type

[**RawDataPostResponse**](RawDataPostResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_flush**
> object admin_flush()

Admin Flush

### Example
```python
from __future__ import print_function
import time
import apollo2_api_client
from apollo2_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = apollo2_api_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = apollo2_api_client.AdminApi(apollo2_api_client.ApiClient(configuration))

try:
    # Admin Flush
    api_response = api_instance.admin_flush()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_flush: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> object status_get()

Status Get

### Example
```python
from __future__ import print_function
import time
import apollo2_api_client
from apollo2_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = apollo2_api_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = apollo2_api_client.AdminApi(apollo2_api_client.ApiClient(configuration))

try:
    # Status Get
    api_response = api_instance.status_get()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

