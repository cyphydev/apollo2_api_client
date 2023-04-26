# mips_api_client.GraphApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_tag_delete**](GraphApi.md#edge_tag_delete) | **DELETE** /graph/edge/tag/delete | Edge Tag Delete
[**edge_tag_edge_get**](GraphApi.md#edge_tag_edge_get) | **GET** /graph/tag/edge/{id} | Edge Tag Edge Get
[**edge_tag_graph_id_get**](GraphApi.md#edge_tag_graph_id_get) | **GET** /graph/tag/graph/{id} | Edge Tag Graph Id Get
[**edge_tag_post**](GraphApi.md#edge_tag_post) | **POST** /graph/edge/tag/post | Edge Tag Post
[**graph_get**](GraphApi.md#graph_get) | **GET** /graph | Graph Get
[**graph_id_delete**](GraphApi.md#graph_id_delete) | **DELETE** /graph/{id} | Graph Id Delete
[**graph_id_delete_edges_post**](GraphApi.md#graph_id_delete_edges_post) | **POST** /graph/{id}/delete_edges | Graph Id Delete Edges Post
[**graph_id_edges_get**](GraphApi.md#graph_id_edges_get) | **GET** /graph/{id}/edges | Graph Id Edges Get
[**graph_id_edit_edges_post**](GraphApi.md#graph_id_edit_edges_post) | **POST** /graph/{id}/edit_edges | Graph Id Edit Edges Post
[**graph_id_get**](GraphApi.md#graph_id_get) | **GET** /graph/{id} | Graph Id Get
[**graph_post**](GraphApi.md#graph_post) | **POST** /graph | Graph Post

# **edge_tag_delete**
> str edge_tag_delete(body, tag_name)

Edge Tag Delete

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
body = [mips_api_client.Edge()] # list[Edge] | 
tag_name = 'tag_name_example' # str | 

try:
    # Edge Tag Delete
    api_response = api_instance.edge_tag_delete(body, tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->edge_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Edge]**](Edge.md)|  | 
 **tag_name** | **str**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_tag_edge_get**
> list[str] edge_tag_edge_get(graph_id, src_id, dst_id, edge_type)

Edge Tag Edge Get

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
graph_id = 56 # int | 
src_id = 56 # int | 
dst_id = 56 # int | 
edge_type = 'edge_type_example' # str | 

try:
    # Edge Tag Edge Get
    api_response = api_instance.edge_tag_edge_get(graph_id, src_id, dst_id, edge_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->edge_tag_edge_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **int**|  | 
 **src_id** | **int**|  | 
 **dst_id** | **int**|  | 
 **edge_type** | **str**|  | 

### Return type

**list[str]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_tag_graph_id_get**
> list[str] edge_tag_graph_id_get(id)

Edge Tag Graph Id Get

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Edge Tag Graph Id Get
    api_response = api_instance.edge_tag_graph_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->edge_tag_graph_id_get: %s\n" % e)
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

# **edge_tag_post**
> str edge_tag_post(body, tag_name)

Edge Tag Post

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
body = [mips_api_client.Edge()] # list[Edge] | 
tag_name = 'tag_name_example' # str | 

try:
    # Edge Tag Post
    api_response = api_instance.edge_tag_post(body, tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->edge_tag_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Edge]**](Edge.md)|  | 
 **tag_name** | **str**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_get**
> list[Graph] graph_get(name=name, provider=provider, tag=tag, version=version)

Graph Get

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    # Graph Get
    api_response = api_instance.graph_get(name=name, provider=provider, tag=tag, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->graph_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**list[Graph]**](Graph.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_id_delete**
> str graph_id_delete(id)

Graph Id Delete

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Graph Id Delete
    api_response = api_instance.graph_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->graph_id_delete: %s\n" % e)
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

# **graph_id_delete_edges_post**
> str graph_id_delete_edges_post(body, id)

Graph Id Delete Edges Post

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
body = [mips_api_client.Edge()] # list[Edge] | 
id = 56 # int | 

try:
    # Graph Id Delete Edges Post
    api_response = api_instance.graph_id_delete_edges_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->graph_id_delete_edges_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Edge]**](Edge.md)|  | 
 **id** | **int**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_id_edges_get**
> list[Edge] graph_id_edges_get(id, limit, last=last, end=end, tag_name=tag_name)

Graph Id Edges Get

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 
limit = 56 # int | 
last = -1 # int |  (optional) (default to -1)
end = 56 # int |  (optional)
tag_name = 'tag_name_example' # str |  (optional)

try:
    # Graph Id Edges Get
    api_response = api_instance.graph_id_edges_get(id, limit, last=last, end=end, tag_name=tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->graph_id_edges_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**|  | 
 **last** | **int**|  | [optional] [default to -1]
 **end** | **int**|  | [optional] 
 **tag_name** | **str**|  | [optional] 

### Return type

[**list[Edge]**](Edge.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_id_edit_edges_post**
> str graph_id_edit_edges_post(body, id, tag_name=tag_name)

Graph Id Edit Edges Post

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
body = [mips_api_client.Edge()] # list[Edge] | 
id = 56 # int | 
tag_name = 'tag_name_example' # str |  (optional)

try:
    # Graph Id Edit Edges Post
    api_response = api_instance.graph_id_edit_edges_post(body, id, tag_name=tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->graph_id_edit_edges_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Edge]**](Edge.md)|  | 
 **id** | **int**|  | 
 **tag_name** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_id_get**
> Graph graph_id_get(id)

Graph Id Get

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Graph Id Get
    api_response = api_instance.graph_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->graph_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_post**
> str graph_post(body)

Graph Post

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
api_instance = mips_api_client.GraphApi(mips_api_client.ApiClient(configuration))
body = mips_api_client.Graph() # Graph | 

try:
    # Graph Post
    api_response = api_instance.graph_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->graph_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Graph**](Graph.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

