# apollo2_api_client.ItemApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**item_attach_media_post**](ItemApi.md#item_attach_media_post) | **POST** /item/attach_media | Item Attach Media Post
[**item_batch_get**](ItemApi.md#item_batch_get) | **POST** /item/get | Item Batch Get
[**item_count_get**](ItemApi.md#item_count_get) | **GET** /item/count | Item Count Get
[**item_detach_media_post**](ItemApi.md#item_detach_media_post) | **POST** /item/detach_media | Item Detach Media Post
[**item_enrichments_batch_delete**](ItemApi.md#item_enrichments_batch_delete) | **POST** /item/enrichments/delete | Item Enrichments Batch Delete
[**item_enrichments_batch_get**](ItemApi.md#item_enrichments_batch_get) | **POST** /item/enrichments/get | Item Enrichments Batch Get
[**item_enrichments_batch_post**](ItemApi.md#item_enrichments_batch_post) | **POST** /item/enrichments/submit | Item Enrichments Batch Post
[**item_get**](ItemApi.md#item_get) | **GET** /item | Item Get
[**item_id_delete**](ItemApi.md#item_id_delete) | **DELETE** /item/{id} | Item Id Delete
[**item_id_enrichments_delete**](ItemApi.md#item_id_enrichments_delete) | **DELETE** /item/{id}/enrichments | Item Id Enrichments Delete
[**item_id_enrichments_get**](ItemApi.md#item_id_enrichments_get) | **GET** /item/{id}/enrichments | Item Id Enrichments Get
[**item_id_enrichments_post**](ItemApi.md#item_id_enrichments_post) | **POST** /item/{id}/enrichments | Item Id Enrichments Post
[**item_id_forward_batch_translate**](ItemApi.md#item_id_forward_batch_translate) | **POST** /item/id/forward | Item Id Forward Batch Translate
[**item_id_forward_translate**](ItemApi.md#item_id_forward_translate) | **GET** /item/id/forward/{id} | Item Id Forward Translate
[**item_id_get**](ItemApi.md#item_id_get) | **GET** /item/{id} | Item Id Get
[**item_id_identifer_get**](ItemApi.md#item_id_identifer_get) | **GET** /item/{id}/identifer | Item Id Identifer Get
[**item_id_reverse_batch_translate**](ItemApi.md#item_id_reverse_batch_translate) | **POST** /item/id/reverse | Item Id Reverse Batch Translate
[**item_id_reverse_translate**](ItemApi.md#item_id_reverse_translate) | **GET** /item/id/reverse/{id} | Item Id Reverse Translate
[**item_identifer_delete**](ItemApi.md#item_identifer_delete) | **POST** /item/identifer/delete | Item Identifer Delete
[**item_identifer_post**](ItemApi.md#item_identifer_post) | **POST** /item/identifer/post | Item Identifer Post
[**item_max_id_get**](ItemApi.md#item_max_id_get) | **GET** /item/max_id | Item Max Id Get

# **item_attach_media_post**
> str item_attach_media_post(body)

Item Attach Media Post

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = apollo2_api_client.ModifyMediaAttachmentRequest() # ModifyMediaAttachmentRequest | 

try:
    # Item Attach Media Post
    api_response = api_instance.item_attach_media_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_attach_media_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyMediaAttachmentRequest**](ModifyMediaAttachmentRequest.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_batch_get**
> list[Item] item_batch_get(body, identifier=identifier)

Item Batch Get

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = apollo2_api_client.BatchGetRequest() # BatchGetRequest | 
identifier = 'identifier_example' # str |  (optional)

try:
    # Item Batch Get
    api_response = api_instance.item_batch_get(body, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchGetRequest**](BatchGetRequest.md)|  | 
 **identifier** | **str**|  | [optional] 

### Return type

[**list[Item]**](Item.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_count_get**
> int item_count_get(last=last, end=end, platform=platform, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)

Item Count Get

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
last = 56 # int |  (optional)
end = 56 # int |  (optional)
platform = apollo2_api_client.MediaType() # MediaType |  (optional)
identifier = 'identifier_example' # str |  (optional)
inclusive_begin_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)
exclusive_end_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)

try:
    # Item Count Get
    api_response = api_instance.item_count_get(last=last, end=end, platform=platform, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **platform** | [**MediaType**](.md)|  | [optional] 
 **identifier** | **str**|  | [optional] 
 **inclusive_begin_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 
 **exclusive_end_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_detach_media_post**
> str item_detach_media_post(body)

Item Detach Media Post

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = apollo2_api_client.ModifyMediaAttachmentRequest() # ModifyMediaAttachmentRequest | 

try:
    # Item Detach Media Post
    api_response = api_instance.item_detach_media_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_detach_media_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyMediaAttachmentRequest**](ModifyMediaAttachmentRequest.md)|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_enrichments_batch_delete**
> str item_enrichments_batch_delete(body)

Item Enrichments Batch Delete

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = apollo2_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

try:
    # Item Enrichments Batch Delete
    api_response = api_instance.item_enrichments_batch_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_enrichments_batch_delete: %s\n" % e)
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

# **item_enrichments_batch_get**
> list[list[Enrichment]] item_enrichments_batch_get(body)

Item Enrichments Batch Get

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = apollo2_api_client.EnrichmentsBatchRequest() # EnrichmentsBatchRequest | 

try:
    # Item Enrichments Batch Get
    api_response = api_instance.item_enrichments_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_enrichments_batch_get: %s\n" % e)
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

# **item_enrichments_batch_post**
> str item_enrichments_batch_post(body)

Item Enrichments Batch Post

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = NULL # dict(str, list[Enrichment]) | 

try:
    # Item Enrichments Batch Post
    api_response = api_instance.item_enrichments_batch_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_enrichments_batch_post: %s\n" % e)
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

# **item_get**
> list[Item] item_get(limit, last=last, end=end, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version, platform=platform, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)

Item Get

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
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
platform = apollo2_api_client.MediaType() # MediaType |  (optional)
identifier = 'identifier_example' # str |  (optional)
inclusive_begin_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)
exclusive_end_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)

try:
    # Item Get
    api_response = api_instance.item_get(limit, last=last, end=end, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version, platform=platform, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_get: %s\n" % e)
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
 **inclusive_begin_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 
 **exclusive_end_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 

### Return type

[**list[Item]**](Item.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_id_delete**
> str item_id_delete(id)

Item Id Delete

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Item Id Delete
    api_response = api_instance.item_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_id_delete: %s\n" % e)
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

# **item_id_enrichments_delete**
> str item_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)

Item Id Enrichments Delete

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
id = 56 # int | 
name = 'name_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    # Item Id Enrichments Delete
    api_response = api_instance.item_id_enrichments_delete(id, name=name, provider=provider, tag=tag, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_id_enrichments_delete: %s\n" % e)
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

# **item_id_enrichments_get**
> list[Enrichment] item_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)

Item Id Enrichments Get

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
id = 56 # int | 
name = 'name_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    # Item Id Enrichments Get
    api_response = api_instance.item_id_enrichments_get(id, name=name, provider=provider, tag=tag, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_id_enrichments_get: %s\n" % e)
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

# **item_id_enrichments_post**
> str item_id_enrichments_post(body, id)

Item Id Enrichments Post

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = [apollo2_api_client.Enrichment()] # list[Enrichment] | 
id = 56 # int | 

try:
    # Item Id Enrichments Post
    api_response = api_instance.item_id_enrichments_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_id_enrichments_post: %s\n" % e)
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

# **item_id_forward_batch_translate**
> list[int] item_id_forward_batch_translate(body, platform=platform)

Item Id Forward Batch Translate

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = ['body_example'] # list[str] | 
platform = apollo2_api_client.MediaType() # MediaType |  (optional)

try:
    # Item Id Forward Batch Translate
    api_response = api_instance.item_id_forward_batch_translate(body, platform=platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_id_forward_batch_translate: %s\n" % e)
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

# **item_id_forward_translate**
> int item_id_forward_translate(id, platform=platform)

Item Id Forward Translate

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
id = 'id_example' # str | 
platform = apollo2_api_client.MediaType() # MediaType |  (optional)

try:
    # Item Id Forward Translate
    api_response = api_instance.item_id_forward_translate(id, platform=platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_id_forward_translate: %s\n" % e)
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

# **item_id_get**
> Item item_id_get(id, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)

Item Id Get

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
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
    # Item Id Get
    api_response = api_instance.item_id_get(id, with_enrichment=with_enrichment, with_cluster=with_cluster, enrichment_name=enrichment_name, enrichment_provider=enrichment_provider, enrichment_tag=enrichment_tag, enrichment_version=enrichment_version, cluster_name=cluster_name, cluster_provider=cluster_provider, cluster_tag=cluster_tag, cluster_version=cluster_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_id_get: %s\n" % e)
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

[**Item**](Item.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_id_identifer_get**
> list[str] item_id_identifer_get(id)

Item Id Identifer Get

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Item Id Identifer Get
    api_response = api_instance.item_id_identifer_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_id_identifer_get: %s\n" % e)
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

# **item_id_reverse_batch_translate**
> list[str] item_id_reverse_batch_translate(body)

Item Id Reverse Batch Translate

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = [56] # list[int] | 

try:
    # Item Id Reverse Batch Translate
    api_response = api_instance.item_id_reverse_batch_translate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_id_reverse_batch_translate: %s\n" % e)
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

# **item_id_reverse_translate**
> str item_id_reverse_translate(id)

Item Id Reverse Translate

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Item Id Reverse Translate
    api_response = api_instance.item_id_reverse_translate(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_id_reverse_translate: %s\n" % e)
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

# **item_identifer_delete**
> str item_identifer_delete(body, identifier)

Item Identifer Delete

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = [56] # list[int] | 
identifier = 'identifier_example' # str | 

try:
    # Item Identifer Delete
    api_response = api_instance.item_identifer_delete(body, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_identifer_delete: %s\n" % e)
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

# **item_identifer_post**
> str item_identifer_post(body, identifier)

Item Identifer Post

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
body = [56] # list[int] | 
identifier = 'identifier_example' # str | 

try:
    # Item Identifer Post
    api_response = api_instance.item_identifer_post(body, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_identifer_post: %s\n" % e)
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

# **item_max_id_get**
> int item_max_id_get(platform=platform, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)

Item Max Id Get

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
api_instance = apollo2_api_client.ItemApi(apollo2_api_client.ApiClient(configuration))
platform = apollo2_api_client.MediaType() # MediaType |  (optional)
identifier = 'identifier_example' # str |  (optional)
inclusive_begin_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)
exclusive_end_datetime = '2013-10-20T19:20:30+01:00' # datetime | %Y-%m-%dT%H:%M:%S%z (optional)

try:
    # Item Max Id Get
    api_response = api_instance.item_max_id_get(platform=platform, identifier=identifier, inclusive_begin_datetime=inclusive_begin_datetime, exclusive_end_datetime=exclusive_end_datetime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_max_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | [**MediaType**](.md)|  | [optional] 
 **identifier** | **str**|  | [optional] 
 **inclusive_begin_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 
 **exclusive_end_datetime** | **datetime**| %Y-%m-%dT%H:%M:%S%z | [optional] 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

