# mips_api_client.ClusterApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_delete**](ClusterApi.md#cluster_delete) | **DELETE** /cluster | Cluster Delete
[**cluster_enrichments_batch_delete**](ClusterApi.md#cluster_enrichments_batch_delete) | **POST** /cluster/enrichments/delete | Cluster Enrichments Batch Delete
[**cluster_enrichments_batch_get**](ClusterApi.md#cluster_enrichments_batch_get) | **POST** /cluster/enrichments/get | Cluster Enrichments Batch Get
[**cluster_enrichments_batch_post**](ClusterApi.md#cluster_enrichments_batch_post) | **POST** /cluster/enrichments/submit | Cluster Enrichments Batch Post
[**cluster_get**](ClusterApi.md#cluster_get) | **GET** /cluster | Cluster Get
[**cluster_id_delete**](ClusterApi.md#cluster_id_delete) | **DELETE** /cluster/{id} | Cluster Id Delete
[**cluster_id_delete_members_post**](ClusterApi.md#cluster_id_delete_members_post) | **POST** /cluster/{id}/delete_members | Cluster Id Delete Members Post
[**cluster_id_enrichments_delete**](ClusterApi.md#cluster_id_enrichments_delete) | **DELETE** /cluster/{id}/enrichments | Cluster Id Enrichments Delete
[**cluster_id_enrichments_get**](ClusterApi.md#cluster_id_enrichments_get) | **GET** /cluster/{id}/enrichments | Cluster Id Enrichments Get
[**cluster_id_enrichments_post**](ClusterApi.md#cluster_id_enrichments_post) | **POST** /cluster/{id}/enrichments | Cluster Id Enrichments Post
[**cluster_id_get**](ClusterApi.md#cluster_id_get) | **GET** /cluster/{id} | Cluster Id Get
[**cluster_id_identifer_get**](ClusterApi.md#cluster_id_identifer_get) | **GET** /cluster/{id}/identifer | Cluster Id Identifer Get
[**cluster_id_members_get**](ClusterApi.md#cluster_id_members_get) | **GET** /cluster/{id}/members | Cluster Id Members Get
[**cluster_identifer_delete**](ClusterApi.md#cluster_identifer_delete) | **POST** /cluster/identifer/delete | Cluster Identifer Delete
[**cluster_identifer_post**](ClusterApi.md#cluster_identifer_post) | **POST** /cluster/identifer/post | Cluster Identifer Post
[**cluster_post**](ClusterApi.md#cluster_post) | **POST** /cluster | Cluster Post

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

# **cluster_enrichments_batch_delete**
> str cluster_enrichments_batch_delete(body)

Cluster Enrichments Batch Delete

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
body = mips_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

try:
    # Cluster Enrichments Batch Delete
    api_response = api_instance.cluster_enrichments_batch_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_enrichments_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrichmentsBatchRequest**](EnrichmentsBatchRequest.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_enrichments_batch_get**
> list[list[Enrichment]] cluster_enrichments_batch_get(body)

Cluster Enrichments Batch Get

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
body = mips_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

try:
    # Cluster Enrichments Batch Get
    api_response = api_instance.cluster_enrichments_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_enrichments_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrichmentsBatchRequest**](EnrichmentsBatchRequest.md)|  | 

### Return type

**list[list[Enrichment]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_enrichments_batch_post**
> str cluster_enrichments_batch_post(body)

Cluster Enrichments Batch Post

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
body = NULL # dict(str, list[Enrichment]) | 

try:
    # Cluster Enrichments Batch Post
    api_response = api_instance.cluster_enrichments_batch_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_enrichments_batch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, list[Enrichment])**](dict.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_get**
> list[Cluster] cluster_get(name=name, provider=provider, tag=tag, version=version, identifier=identifier)

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
identifier = 'identifier_example' # str |  (optional)

try:
    # Cluster Get
    api_response = api_instance.cluster_get(name=name, provider=provider, tag=tag, version=version, identifier=identifier)
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
 **identifier** | **str**|  | [optional] 

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

# **cluster_id_enrichments_delete**
> str cluster_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)

Cluster Id Enrichments Delete

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
name = 'name_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    # Cluster Id Enrichments Delete
    api_response = api_instance.cluster_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_id_enrichments_delete: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_enrichments_get**
> list[Enrichment] cluster_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)

Cluster Id Enrichments Get

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
name = 'name_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    # Cluster Id Enrichments Get
    api_response = api_instance.cluster_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_id_enrichments_get: %s\n" % e)
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

[**list[Enrichment]**](Enrichment.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_id_enrichments_post**
> str cluster_id_enrichments_post(body, id)

Cluster Id Enrichments Post

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
body = [mips_api_client.Enrichment()] # list[Enrichment] | 
id = 56 # int | 

try:
    # Cluster Id Enrichments Post
    api_response = api_instance.cluster_id_enrichments_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_id_enrichments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Enrichment]**](Enrichment.md)|  | 
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

# **cluster_id_identifer_get**
> list[str] cluster_id_identifer_get(id)

Cluster Id Identifer Get

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
    # Cluster Id Identifer Get
    api_response = api_instance.cluster_id_identifer_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_id_identifer_get: %s\n" % e)
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

# **cluster_identifer_delete**
> str cluster_identifer_delete(body, identifier)

Cluster Identifer Delete

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
identifier = 'identifier_example' # str | 

try:
    # Cluster Identifer Delete
    api_response = api_instance.cluster_identifer_delete(body, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_identifer_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | 
 **identifier** | **str**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_identifer_post**
> str cluster_identifer_post(body, identifier)

Cluster Identifer Post

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
identifier = 'identifier_example' # str | 

try:
    # Cluster Identifer Post
    api_response = api_instance.cluster_identifer_post(body, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_identifer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | 
 **identifier** | **str**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
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

