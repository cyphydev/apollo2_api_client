# mips_api_client.MediaItemApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**media_item_batch_get**](MediaItemApi.md#media_item_batch_get) | **POST** /media_item/get | Media Item Batch Get
[**media_item_count_get**](MediaItemApi.md#media_item_count_get) | **GET** /media_item/count | Media Item Count Get
[**media_item_get**](MediaItemApi.md#media_item_get) | **GET** /media_item | Media Item Get
[**media_item_id_delete**](MediaItemApi.md#media_item_id_delete) | **DELETE** /media_item/{id} | Media Item Id Delete
[**media_item_id_get**](MediaItemApi.md#media_item_id_get) | **GET** /media_item/{id} | Media Item Id Get
[**media_item_max_id_get**](MediaItemApi.md#media_item_max_id_get) | **GET** /media_item/max_id | Media Item Max Id Get
[**media_item_tag_delete**](MediaItemApi.md#media_item_tag_delete) | **POST** /media_item/tag/delete | Media Item Tag Delete
[**media_item_tag_node_id_get**](MediaItemApi.md#media_item_tag_node_id_get) | **GET** /media_item/id/tag | Media Item Tag Node Id Get
[**media_item_tag_post**](MediaItemApi.md#media_item_tag_post) | **POST** /media_item/tag/post | Media Item Tag Post

# **media_item_batch_get**
> list[MediaItem] media_item_batch_get(body)

Media Item Batch Get

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
api_instance = mips_api_client.MediaItemApi(mips_api_client.ApiClient(configuration))
body = mips_api_client.BatchMediaGetRequest() # BatchMediaGetRequest | 

try:
    # Media Item Batch Get
    api_response = api_instance.media_item_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaItemApi->media_item_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchMediaGetRequest**](BatchMediaGetRequest.md)|  | 

### Return type

[**list[MediaItem]**](MediaItem.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_item_count_get**
> int media_item_count_get(last=last, end=end, tag_name=tag_name)

Media Item Count Get

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
api_instance = mips_api_client.MediaItemApi(mips_api_client.ApiClient(configuration))
last = 56 # int |  (optional)
end = 56 # int |  (optional)
tag_name = 'tag_name_example' # str |  (optional)

try:
    # Media Item Count Get
    api_response = api_instance.media_item_count_get(last=last, end=end, tag_name=tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaItemApi->media_item_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **tag_name** | **str**|  | [optional] 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_item_get**
> list[MediaItem] media_item_get(limit, last=last, end=end, tag_name=tag_name)

Media Item Get

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
api_instance = mips_api_client.MediaItemApi(mips_api_client.ApiClient(configuration))
limit = 56 # int | 
last = -1 # int |  (optional) (default to -1)
end = 56 # int |  (optional)
tag_name = 'tag_name_example' # str |  (optional)

try:
    # Media Item Get
    api_response = api_instance.media_item_get(limit, last=last, end=end, tag_name=tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaItemApi->media_item_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | 
 **last** | **int**|  | [optional] [default to -1]
 **end** | **int**|  | [optional] 
 **tag_name** | **str**|  | [optional] 

### Return type

[**list[MediaItem]**](MediaItem.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_item_id_delete**
> str media_item_id_delete(id)

Media Item Id Delete

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
api_instance = mips_api_client.MediaItemApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Media Item Id Delete
    api_response = api_instance.media_item_id_delete(id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_item_id_get**
> MediaItem media_item_id_get(id)

Media Item Id Get

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
api_instance = mips_api_client.MediaItemApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Media Item Id Get
    api_response = api_instance.media_item_id_get(id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_item_max_id_get**
> int media_item_max_id_get(tag_name=tag_name)

Media Item Max Id Get

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
api_instance = mips_api_client.MediaItemApi(mips_api_client.ApiClient(configuration))
tag_name = 'tag_name_example' # str |  (optional)

try:
    # Media Item Max Id Get
    api_response = api_instance.media_item_max_id_get(tag_name=tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaItemApi->media_item_max_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**|  | [optional] 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_item_tag_delete**
> str media_item_tag_delete(body, tag_name)

Media Item Tag Delete

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
api_instance = mips_api_client.MediaItemApi(mips_api_client.ApiClient(configuration))
body = [56] # list[int] | 
tag_name = 'tag_name_example' # str | 

try:
    # Media Item Tag Delete
    api_response = api_instance.media_item_tag_delete(body, tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaItemApi->media_item_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | 
 **tag_name** | **str**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_item_tag_node_id_get**
> list[str] media_item_tag_node_id_get(id)

Media Item Tag Node Id Get

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
api_instance = mips_api_client.MediaItemApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Media Item Tag Node Id Get
    api_response = api_instance.media_item_tag_node_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaItemApi->media_item_tag_node_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**list[str]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_item_tag_post**
> str media_item_tag_post(body, tag_name)

Media Item Tag Post

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
api_instance = mips_api_client.MediaItemApi(mips_api_client.ApiClient(configuration))
body = [56] # list[int] | 
tag_name = 'tag_name_example' # str | 

try:
    # Media Item Tag Post
    api_response = api_instance.media_item_tag_post(body, tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaItemApi->media_item_tag_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | 
 **tag_name** | **str**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

