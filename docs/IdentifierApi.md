# apollo2_api_client.IdentifierApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identifer_delete**](IdentifierApi.md#identifer_delete) | **GET** /identifer/delete | Identifer Delete
[**identifier_list**](IdentifierApi.md#identifier_list) | **GET** /identifier/list | Identifier List

# **identifer_delete**
> str identifer_delete(identifier)

Identifer Delete

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
api_instance = apollo2_api_client.IdentifierApi(apollo2_api_client.ApiClient(configuration))
identifier = 'identifier_example' # str | 

try:
    # Identifer Delete
    api_response = api_instance.identifer_delete(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->identifer_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identifier_list**
> list[str] identifier_list()

Identifier List

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
api_instance = apollo2_api_client.IdentifierApi(apollo2_api_client.ApiClient(configuration))

try:
    # Identifier List
    api_response = api_instance.identifier_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->identifier_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

