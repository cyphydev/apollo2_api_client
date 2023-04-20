# mips_api_client.TagApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tag_name_delete**](TagApi.md#tag_name_delete) | **GET** /tag/delete | Tag Name Delete

# **tag_name_delete**
> str tag_name_delete(tag_name)

Tag Name Delete

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
api_instance = mips_api_client.TagApi(mips_api_client.ApiClient(configuration))
tag_name = 'tag_name_example' # str | 

try:
    # Tag Name Delete
    api_response = api_instance.tag_name_delete(tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tag_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

