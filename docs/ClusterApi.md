# mips_api_client.ClusterApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_delete**](ClusterApi.md#cluster_delete) | **DELETE** /cluster | Cluster Delete
[**cluster_get**](ClusterApi.md#cluster_get) | **GET** /cluster | Cluster Get
[**cluster_id_delete**](ClusterApi.md#cluster_id_delete) | **DELETE** /cluster/{id} | Cluster Id Delete
[**cluster_id_delete_members_post**](ClusterApi.md#cluster_id_delete_members_post) | **POST** /cluster/{id}/delete_members | Cluster Id Delete Members Post
[**cluster_id_get**](ClusterApi.md#cluster_id_get) | **GET** /cluster/{id} | Cluster Id Get
[**cluster_id_members_get**](ClusterApi.md#cluster_id_members_get) | **GET** /cluster/{id}/members | Cluster Id Members Get
[**cluster_post**](ClusterApi.md#cluster_post) | **POST** /cluster | Cluster Post
[**cluster_tag_delete**](ClusterApi.md#cluster_tag_delete) | **POST** /cluster/tag/delete | Cluster Tag Delete
[**cluster_tag_id_get**](ClusterApi.md#cluster_tag_id_get) | **GET** /cluster/tag/{id} | Cluster Tag Id Get
[**cluster_tag_post**](ClusterApi.md#cluster_tag_post) | **POST** /cluster/tag/post | Cluster Tag Post

# **cluster_delete**
> str cluster_delete(name, provider, tag, version)

Cluster Delete

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
api_instance = mips_api_client.ClusterApi(mips_api_client.ApiClient(configuration))
name = 'name_example' # str | 
provider = 'provider_example' # str | 
tag = 'tag_example' # str | 
version = 'version_example' # str | 

try:
    # Cluster Delete
    api_response = api_instance.cluster_delete(name, provider, tag, version)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_get**
> list[Cluster] cluster_get(name=name, provider=provider, tag=tag, version=version, tag_name=tag_name)

Cluster Get

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
api_instance = mips_api_client.ClusterApi(mips_api_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
version = 'version_example' # str |  (optional)
tag_name = 'tag_name_example' # str |  (optional)

try:
    # Cluster Get
    api_response = api_instance.cluster_get(name=name, provider=provider, tag=tag, version=version, tag_name=tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **tag_name** | **str**|  | [optional] 

### Return type

[**list[Cluster]**](Cluster.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_delete**
> str cluster_id_delete(id)

Cluster Id Delete

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
api_instance = mips_api_client.ClusterApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Cluster Id Delete
    api_response = api_instance.cluster_id_delete(id)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_delete_members_post**
> str cluster_id_delete_members_post(body, id)

Cluster Id Delete Members Post

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
api_instance = mips_api_client.ClusterApi(mips_api_client.ApiClient(configuration))
body = [56] # list[int] | 
id = 56 # int | 

try:
    # Cluster Id Delete Members Post
    api_response = api_instance.cluster_id_delete_members_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_id_delete_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | 
 **id** | **int**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_get**
> Cluster cluster_id_get(id)

Cluster Id Get

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
api_instance = mips_api_client.ClusterApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Cluster Id Get
    api_response = api_instance.cluster_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_members_get**
> list[ClusterMember] cluster_id_members_get(id, limit, last=last, end=end)

Cluster Id Members Get

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
api_instance = mips_api_client.ClusterApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 
limit = 56 # int | 
last = -1 # int |  (optional) (default to -1)
end = 56 # int |  (optional)

try:
    # Cluster Id Members Get
    api_response = api_instance.cluster_id_members_get(id, limit, last=last, end=end)
    pprint(api_response)
except ApiException as e:
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

[**list[ClusterMember]**](ClusterMember.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_post**
> str cluster_post(body)

Cluster Post

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
api_instance = mips_api_client.ClusterApi(mips_api_client.ApiClient(configuration))
body = mips_api_client.Cluster() # Cluster | 

try:
    # Cluster Post
    api_response = api_instance.cluster_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cluster**](Cluster.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_tag_delete**
> str cluster_tag_delete(body, tag_name)

Cluster Tag Delete

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
api_instance = mips_api_client.ClusterApi(mips_api_client.ApiClient(configuration))
body = [56] # list[int] | 
tag_name = 'tag_name_example' # str | 

try:
    # Cluster Tag Delete
    api_response = api_instance.cluster_tag_delete(body, tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_tag_delete: %s\n" % e)
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

# **cluster_tag_id_get**
> list[str] cluster_tag_id_get(id)

Cluster Tag Id Get

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
api_instance = mips_api_client.ClusterApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Cluster Tag Id Get
    api_response = api_instance.cluster_tag_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_tag_id_get: %s\n" % e)
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

# **cluster_tag_post**
> str cluster_tag_post(body, tag_name)

Cluster Tag Post

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
api_instance = mips_api_client.ClusterApi(mips_api_client.ApiClient(configuration))
body = [56] # list[int] | 
tag_name = 'tag_name_example' # str | 

try:
    # Cluster Tag Post
    api_response = api_instance.cluster_tag_post(body, tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_tag_post: %s\n" % e)
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

