# mips_api_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_get**](DefaultApi.md#ping_get) | **GET** /ping | Ping Get

# **ping_get**
> str ping_get()

Ping Get

### Example
```python
from __future__ import print_function
import time
import mips_api_client
from mips_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mips_api_client.DefaultApi()

try:
    # Ping Get
    api_response = api_instance.ping_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ping_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

