# mips_api_client.SourceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**source_batch_get**](SourceApi.md#source_batch_get) | **POST** /source/get | Source Batch Get
[**source_count_get**](SourceApi.md#source_count_get) | **GET** /source/count | Source Count Get
[**source_enrichments_batch_delete**](SourceApi.md#source_enrichments_batch_delete) | **POST** /source/enrichments/delete | Source Enrichments Batch Delete
[**source_enrichments_batch_get**](SourceApi.md#source_enrichments_batch_get) | **POST** /source/enrichments/get | Source Enrichments Batch Get
[**source_enrichments_batch_post**](SourceApi.md#source_enrichments_batch_post) | **POST** /source/enrichments/submit | Source Enrichments Batch Post
[**source_get**](SourceApi.md#source_get) | **GET** /source | Source Get
[**source_id_delete**](SourceApi.md#source_id_delete) | **DELETE** /source/{id} | Source Id Delete
[**source_id_enrichments_delete**](SourceApi.md#source_id_enrichments_delete) | **DELETE** /source/{id}/enrichments | Source Id Enrichments Delete
[**source_id_enrichments_get**](SourceApi.md#source_id_enrichments_get) | **GET** /source/{id}/enrichments | Source Id Enrichments Get
[**source_id_enrichments_post**](SourceApi.md#source_id_enrichments_post) | **POST** /source/{id}/enrichments | Source Id Enrichments Post
[**source_id_forward_batch_translate**](SourceApi.md#source_id_forward_batch_translate) | **POST** /source/id/forward | Source Id Forward Batch Translate
[**source_id_forward_translate**](SourceApi.md#source_id_forward_translate) | **GET** /source/id/forward/{id} | Source Id Forward Translate
[**source_id_get**](SourceApi.md#source_id_get) | **GET** /source/{id} | Source Id Get
[**source_id_identifer_get**](SourceApi.md#source_id_identifer_get) | **GET** /source/{id}/identifer | Source Id Identifer Get
[**source_id_reverse_batch_translate**](SourceApi.md#source_id_reverse_batch_translate) | **POST** /source/id/reverse | Source Id Reverse Batch Translate
[**source_id_reverse_translate**](SourceApi.md#source_id_reverse_translate) | **GET** /source/id/reverse/{id} | Source Id Reverse Translate
[**source_identifer_delete**](SourceApi.md#source_identifer_delete) | **POST** /source/identifer/delete | Source Identifer Delete
[**source_identifer_post**](SourceApi.md#source_identifer_post) | **POST** /source/identifer/post | Source Identifer Post
[**source_max_id_get**](SourceApi.md#source_max_id_get) | **GET** /source/max_id | Source Max Id Get

# **source_batch_get**
> list[Source] source_batch_get(body, identifier=identifier)

Source Batch Get

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
body = mips_api_client.BatchGetRequest() # BatchGetRequest | 
identifier = 'identifier_example' # str |  (optional)

try:
    # Source Batch Get
    api_response = api_instance.source_batch_get(body, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchGetRequest**](BatchGetRequest.md)|  | 
 **identifier** | **str**|  | [optional] 

### Return type

[**list[Source]**](Source.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_count_get**
> int source_count_get(last=last, end=end, platform=platform, identifier=identifier)

Source Count Get

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
last = 56 # int |  (optional)
end = 56 # int |  (optional)
platform = mips_api_client.MediaType() # MediaType |  (optional)
identifier = 'identifier_example' # str |  (optional)

try:
    # Source Count Get
    api_response = api_instance.source_count_get(last=last, end=end, platform=platform, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **platform** | [**MediaType**](.md)|  | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_enrichments_batch_delete**
> str source_enrichments_batch_delete(body)

Source Enrichments Batch Delete

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
body = mips_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

try:
    # Source Enrichments Batch Delete
    api_response = api_instance.source_enrichments_batch_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_enrichments_batch_delete: %s\n" % e)
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

# **source_enrichments_batch_get**
> list[list[Enrichment]] source_enrichments_batch_get(body)

Source Enrichments Batch Get

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
body = mips_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

try:
    # Source Enrichments Batch Get
    api_response = api_instance.source_enrichments_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_enrichments_batch_get: %s\n" % e)
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

# **source_enrichments_batch_post**
> str source_enrichments_batch_post(body)

Source Enrichments Batch Post

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
body = NULL # dict(str, list[Enrichment]) | 

try:
    # Source Enrichments Batch Post
    api_response = api_instance.source_enrichments_batch_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_enrichments_batch_post: %s\n" % e)
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

# **source_get**
> list[Source] source_get(limit, last=last, end=end, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version, platform=platform, identifier=identifier)

Source Get

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
limit = 56 # int | 
last = -1 # int |  (optional) (default to -1)
end = 56 # int |  (optional)
with_enrichment = false # bool |  (optional) (default to false)
with_cluster = false # bool |  (optional) (default to false)
enrichment_name = 'enrichment_name_example' # str |  (optional)
enrichment_provider = 'enrichment_provider_example' # str |  (optional)
enrichment_tag = 'enrichment_tag_example' # str |  (optional)
enrichment_version = 'enrichment_version_example' # str |  (optional)
cluster_name = 'cluster_name_example' # str |  (optional)
cluster_provider = 'cluster_provider_example' # str |  (optional)
cluster_tag = 'cluster_tag_example' # str |  (optional)
cluster_version = 'cluster_version_example' # str |  (optional)
platform = mips_api_client.MediaType() # MediaType |  (optional)
identifier = 'identifier_example' # str |  (optional)

try:
    # Source Get
    api_response = api_instance.source_get(limit, last=last, end=end, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version, platform=platform, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | 
 **last** | **int**|  | [optional] [default to -1]
 **end** | **int**|  | [optional] 
 **with_enrichment** | **bool**|  | [optional] [default to false]
 **with_cluster** | **bool**|  | [optional] [default to false]
 **enrichment_name** | **str**|  | [optional] 
 **enrichment_provider** | **str**|  | [optional] 
 **enrichment_tag** | **str**|  | [optional] 
 **enrichment_version** | **str**|  | [optional] 
 **cluster_name** | **str**|  | [optional] 
 **cluster_provider** | **str**|  | [optional] 
 **cluster_tag** | **str**|  | [optional] 
 **cluster_version** | **str**|  | [optional] 
 **platform** | [**MediaType**](.md)|  | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

[**list[Source]**](Source.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_delete**
> str source_id_delete(id)

Source Id Delete

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Source Id Delete
    api_response = api_instance.source_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_id_delete: %s\n" % e)
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

# **source_id_enrichments_delete**
> str source_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)

Source Id Enrichments Delete

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 
name = 'name_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    # Source Id Enrichments Delete
    api_response = api_instance.source_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_id_enrichments_delete: %s\n" % e)
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

# **source_id_enrichments_get**
> list[Enrichment] source_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)

Source Id Enrichments Get

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 
name = 'name_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    # Source Id Enrichments Get
    api_response = api_instance.source_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_id_enrichments_get: %s\n" % e)
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

# **source_id_enrichments_post**
> str source_id_enrichments_post(body, id)

Source Id Enrichments Post

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
body = [mips_api_client.Enrichment()] # list[Enrichment] | 
id = 56 # int | 

try:
    # Source Id Enrichments Post
    api_response = api_instance.source_id_enrichments_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_id_enrichments_post: %s\n" % e)
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

# **source_id_forward_batch_translate**
> list[int] source_id_forward_batch_translate(body, platform=platform)

Source Id Forward Batch Translate

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
body = ['body_example'] # list[str] | 
platform = mips_api_client.MediaType() # MediaType |  (optional)

try:
    # Source Id Forward Batch Translate
    api_response = api_instance.source_id_forward_batch_translate(body, platform=platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_id_forward_batch_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **platform** | [**MediaType**](.md)|  | [optional] 

### Return type

**list[int]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_forward_translate**
> int source_id_forward_translate(id, platform=platform)

Source Id Forward Translate

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
id = 'id_example' # str | 
platform = mips_api_client.MediaType() # MediaType |  (optional)

try:
    # Source Id Forward Translate
    api_response = api_instance.source_id_forward_translate(id, platform=platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_id_forward_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform** | [**MediaType**](.md)|  | [optional] 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_get**
> Source source_id_get(id, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)

Source Id Get

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 
with_enrichment = false # bool |  (optional) (default to false)
with_cluster = false # bool |  (optional) (default to false)
enrichment_name = 'enrichment_name_example' # str |  (optional)
enrichment_provider = 'enrichment_provider_example' # str |  (optional)
enrichment_tag = 'enrichment_tag_example' # str |  (optional)
enrichment_version = 'enrichment_version_example' # str |  (optional)
cluster_name = 'cluster_name_example' # str |  (optional)
cluster_provider = 'cluster_provider_example' # str |  (optional)
cluster_tag = 'cluster_tag_example' # str |  (optional)
cluster_version = 'cluster_version_example' # str |  (optional)

try:
    # Source Id Get
    api_response = api_instance.source_id_get(id, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **with_enrichment** | **bool**|  | [optional] [default to false]
 **with_cluster** | **bool**|  | [optional] [default to false]
 **enrichment_name** | **str**|  | [optional] 
 **enrichment_provider** | **str**|  | [optional] 
 **enrichment_tag** | **str**|  | [optional] 
 **enrichment_version** | **str**|  | [optional] 
 **cluster_name** | **str**|  | [optional] 
 **cluster_provider** | **str**|  | [optional] 
 **cluster_tag** | **str**|  | [optional] 
 **cluster_version** | **str**|  | [optional] 

### Return type

[**Source**](Source.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_identifer_get**
> list[str] source_id_identifer_get(id)

Source Id Identifer Get

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Source Id Identifer Get
    api_response = api_instance.source_id_identifer_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_id_identifer_get: %s\n" % e)
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

# **source_id_reverse_batch_translate**
> list[str] source_id_reverse_batch_translate(body)

Source Id Reverse Batch Translate

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
body = [56] # list[int] | 

try:
    # Source Id Reverse Batch Translate
    api_response = api_instance.source_id_reverse_batch_translate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_id_reverse_batch_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | 

### Return type

**list[str]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_id_reverse_translate**
> str source_id_reverse_translate(id)

Source Id Reverse Translate

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Source Id Reverse Translate
    api_response = api_instance.source_id_reverse_translate(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_id_reverse_translate: %s\n" % e)
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

# **source_identifer_delete**
> str source_identifer_delete(body, identifier)

Source Identifer Delete

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
body = [56] # list[int] | 
identifier = 'identifier_example' # str | 

try:
    # Source Identifer Delete
    api_response = api_instance.source_identifer_delete(body, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_identifer_delete: %s\n" % e)
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

# **source_identifer_post**
> str source_identifer_post(body, identifier)

Source Identifer Post

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
body = [56] # list[int] | 
identifier = 'identifier_example' # str | 

try:
    # Source Identifer Post
    api_response = api_instance.source_identifer_post(body, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_identifer_post: %s\n" % e)
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

# **source_max_id_get**
> int source_max_id_get(platform=platform, identifier=identifier)

Source Max Id Get

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
api_instance = mips_api_client.SourceApi(mips_api_client.ApiClient(configuration))
platform = mips_api_client.MediaType() # MediaType |  (optional)
identifier = 'identifier_example' # str |  (optional)

try:
    # Source Max Id Get
    api_response = api_instance.source_max_id_get(platform=platform, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->source_max_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | [**MediaType**](.md)|  | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

