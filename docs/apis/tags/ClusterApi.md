<a name="__pageTop"></a>
# apollo2_api_client.apis.tags.cluster_api.ClusterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_delete**](#cluster_delete) | **delete** /cluster | Cluster Delete
[**cluster_enrichments_batch_delete**](#cluster_enrichments_batch_delete) | **post** /cluster/enrichments/delete | Cluster Enrichments Batch Delete
[**cluster_enrichments_batch_get**](#cluster_enrichments_batch_get) | **post** /cluster/enrichments/get | Cluster Enrichments Batch Get
[**cluster_enrichments_batch_post**](#cluster_enrichments_batch_post) | **post** /cluster/enrichments/submit | Cluster Enrichments Batch Post
[**cluster_get**](#cluster_get) | **get** /cluster | Cluster Get
[**cluster_id_delete**](#cluster_id_delete) | **delete** /cluster/{id} | Cluster Id Delete
[**cluster_id_delete_members_post**](#cluster_id_delete_members_post) | **post** /cluster/{id}/delete_members | Cluster Id Delete Members Post
[**cluster_id_enrichments_delete**](#cluster_id_enrichments_delete) | **delete** /cluster/{id}/enrichments | Cluster Id Enrichments Delete
[**cluster_id_enrichments_get**](#cluster_id_enrichments_get) | **get** /cluster/{id}/enrichments | Cluster Id Enrichments Get
[**cluster_id_enrichments_post**](#cluster_id_enrichments_post) | **post** /cluster/{id}/enrichments | Cluster Id Enrichments Post
[**cluster_id_get**](#cluster_id_get) | **get** /cluster/{id} | Cluster Id Get
[**cluster_id_identifer_get**](#cluster_id_identifer_get) | **get** /cluster/{id}/identifer | Cluster Id Identifer Get
[**cluster_id_members_get**](#cluster_id_members_get) | **get** /cluster/{id}/members | Cluster Id Members Get
[**cluster_identifer_delete**](#cluster_identifer_delete) | **post** /cluster/identifer/delete | Cluster Identifer Delete
[**cluster_identifer_post**](#cluster_identifer_post) | **post** /cluster/identifer/post | Cluster Identifer Post
[**cluster_post**](#cluster_post) | **post** /cluster | Cluster Post

# **cluster_delete**
<a name="cluster_delete"></a>
> str cluster_delete(nameprovidertagversion)

Cluster Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'name': "name_example",
        'provider': "provider_example",
        'tag': "tag_example",
        'version': "version_example",
    }
    try:
        # Cluster Delete
        api_response = api_instance.cluster_delete(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
provider | ProviderSchema | | 
tag | TagSchema | | 
version | VersionSchema | | 


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_delete.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#cluster_delete.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#cluster_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#cluster_delete.ApiResponseFor422) | Validation Error

#### cluster_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_enrichments_batch_delete**
<a name="cluster_enrichments_batch_delete"></a>
> str cluster_enrichments_batch_delete(enrichments_batch_request)

Cluster Enrichments Batch Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.enrichments_batch_request import EnrichmentsBatchRequest
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    body = EnrichmentsBatchRequest(
        ids=[
            1
        ],
        name="name_example",
        provider="provider_example",
        tag="tag_example",
        version="version_example",
    )
    try:
        # Cluster Enrichments Batch Delete
        api_response = api_instance.cluster_enrichments_batch_delete(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_enrichments_batch_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnrichmentsBatchRequest**](../../models/EnrichmentsBatchRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_enrichments_batch_delete.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#cluster_enrichments_batch_delete.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#cluster_enrichments_batch_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#cluster_enrichments_batch_delete.ApiResponseFor422) | Validation Error

#### cluster_enrichments_batch_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_enrichments_batch_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_enrichments_batch_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_enrichments_batch_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_enrichments_batch_get**
<a name="cluster_enrichments_batch_get"></a>
> [[Enrichment]] cluster_enrichments_batch_get(enrichments_batch_request)

Cluster Enrichments Batch Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.enrichments_batch_request import EnrichmentsBatchRequest
from apollo2_api_client.model.enrichment import Enrichment
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    body = EnrichmentsBatchRequest(
        ids=[
            1
        ],
        name="name_example",
        provider="provider_example",
        tag="tag_example",
        version="version_example",
    )
    try:
        # Cluster Enrichments Batch Get
        api_response = api_instance.cluster_enrichments_batch_get(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_enrichments_batch_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnrichmentsBatchRequest**](../../models/EnrichmentsBatchRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_enrichments_batch_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#cluster_enrichments_batch_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#cluster_enrichments_batch_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#cluster_enrichments_batch_get.ApiResponseFor422) | Validation Error

#### cluster_enrichments_batch_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Enrichment**]({{complexTypePrefix}}Enrichment.md) | [**Enrichment**]({{complexTypePrefix}}Enrichment.md) | [**Enrichment**]({{complexTypePrefix}}Enrichment.md) |  | 

#### cluster_enrichments_batch_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_enrichments_batch_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_enrichments_batch_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_enrichments_batch_post**
<a name="cluster_enrichments_batch_post"></a>
> str cluster_enrichments_batch_post(request_body)

Cluster Enrichments Batch Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.enrichment import Enrichment
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict(
        "key": [
            Enrichment(None)
        ],
    )
    try:
        # Cluster Enrichments Batch Post
        api_response = api_instance.cluster_enrichments_batch_post(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_enrichments_batch_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Enrichment**]({{complexTypePrefix}}Enrichment.md) | [**Enrichment**]({{complexTypePrefix}}Enrichment.md) | [**Enrichment**]({{complexTypePrefix}}Enrichment.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_enrichments_batch_post.ApiResponseFor200) | Successful Response
201 | [ApiResponseFor201](#cluster_enrichments_batch_post.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#cluster_enrichments_batch_post.ApiResponseFor400) | Bad Request
409 | [ApiResponseFor409](#cluster_enrichments_batch_post.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#cluster_enrichments_batch_post.ApiResponseFor422) | Validation Error

#### cluster_enrichments_batch_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_enrichments_batch_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_enrichments_batch_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_enrichments_batch_post.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_enrichments_batch_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_get**
<a name="cluster_get"></a>
> [Cluster] cluster_get()

Cluster Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.cluster import Cluster
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'provider': "provider_example",
        'tag': "tag_example",
        'version': "version_example",
        'identifier': "identifier_example",
    }
    try:
        # Cluster Get
        api_response = api_instance.cluster_get(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional
provider | ProviderSchema | | optional
tag | TagSchema | | optional
version | VersionSchema | | optional
identifier | IdentifierSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#cluster_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#cluster_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#cluster_get.ApiResponseFor422) | Validation Error

#### cluster_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Cluster**]({{complexTypePrefix}}Cluster.md) | [**Cluster**]({{complexTypePrefix}}Cluster.md) | [**Cluster**]({{complexTypePrefix}}Cluster.md) |  | 

#### cluster_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_id_delete**
<a name="cluster_id_delete"></a>
> str cluster_id_delete(id)

Cluster Id Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Cluster Id Delete
        api_response = api_instance.cluster_id_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_id_delete.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#cluster_id_delete.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#cluster_id_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#cluster_id_delete.ApiResponseFor422) | Validation Error

#### cluster_id_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_id_delete_members_post**
<a name="cluster_id_delete_members_post"></a>
> str cluster_id_delete_members_post(idrequest_body)

Cluster Id Delete Members Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = [
        1
    ]
    try:
        # Cluster Id Delete Members Post
        api_response = api_instance.cluster_id_delete_members_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_delete_members_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_id_delete_members_post.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#cluster_id_delete_members_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#cluster_id_delete_members_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#cluster_id_delete_members_post.ApiResponseFor422) | Validation Error

#### cluster_id_delete_members_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_delete_members_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_delete_members_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_delete_members_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_id_enrichments_delete**
<a name="cluster_id_enrichments_delete"></a>
> str cluster_id_enrichments_delete(id)

Cluster Id Enrichments Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
    }
    try:
        # Cluster Id Enrichments Delete
        api_response = api_instance.cluster_id_enrichments_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_enrichments_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    query_params = {
        'name': "name_example",
        'provider': "provider_example",
        'tag': "tag_example",
        'version': "version_example",
    }
    try:
        # Cluster Id Enrichments Delete
        api_response = api_instance.cluster_id_enrichments_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_enrichments_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional
provider | ProviderSchema | | optional
tag | TagSchema | | optional
version | VersionSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_id_enrichments_delete.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#cluster_id_enrichments_delete.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#cluster_id_enrichments_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#cluster_id_enrichments_delete.ApiResponseFor422) | Validation Error

#### cluster_id_enrichments_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_enrichments_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_enrichments_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_enrichments_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_id_enrichments_get**
<a name="cluster_id_enrichments_get"></a>
> [Enrichment] cluster_id_enrichments_get(id)

Cluster Id Enrichments Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.enrichment import Enrichment
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
    }
    try:
        # Cluster Id Enrichments Get
        api_response = api_instance.cluster_id_enrichments_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_enrichments_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    query_params = {
        'name': "name_example",
        'provider': "provider_example",
        'tag': "tag_example",
        'version': "version_example",
    }
    try:
        # Cluster Id Enrichments Get
        api_response = api_instance.cluster_id_enrichments_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_enrichments_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional
provider | ProviderSchema | | optional
tag | TagSchema | | optional
version | VersionSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_id_enrichments_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#cluster_id_enrichments_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#cluster_id_enrichments_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#cluster_id_enrichments_get.ApiResponseFor422) | Validation Error

#### cluster_id_enrichments_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Enrichment**]({{complexTypePrefix}}Enrichment.md) | [**Enrichment**]({{complexTypePrefix}}Enrichment.md) | [**Enrichment**]({{complexTypePrefix}}Enrichment.md) |  | 

#### cluster_id_enrichments_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_enrichments_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_enrichments_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_id_enrichments_post**
<a name="cluster_id_enrichments_post"></a>
> str cluster_id_enrichments_post(idenrichment)

Cluster Id Enrichments Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.enrichment import Enrichment
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = [
        Enrichment(None)
    ]
    try:
        # Cluster Id Enrichments Post
        api_response = api_instance.cluster_id_enrichments_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_enrichments_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Enrichment**]({{complexTypePrefix}}Enrichment.md) | [**Enrichment**]({{complexTypePrefix}}Enrichment.md) | [**Enrichment**]({{complexTypePrefix}}Enrichment.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_id_enrichments_post.ApiResponseFor200) | Successful Response
201 | [ApiResponseFor201](#cluster_id_enrichments_post.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#cluster_id_enrichments_post.ApiResponseFor400) | Bad Request
409 | [ApiResponseFor409](#cluster_id_enrichments_post.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#cluster_id_enrichments_post.ApiResponseFor422) | Validation Error

#### cluster_id_enrichments_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_enrichments_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_enrichments_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_enrichments_post.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_enrichments_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_id_get**
<a name="cluster_id_get"></a>
> Cluster cluster_id_get(id)

Cluster Id Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.cluster import Cluster
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Cluster Id Get
        api_response = api_instance.cluster_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_id_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#cluster_id_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#cluster_id_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#cluster_id_get.ApiResponseFor422) | Validation Error

#### cluster_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Cluster**](../../models/Cluster.md) |  | 


#### cluster_id_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_id_identifer_get**
<a name="cluster_id_identifer_get"></a>
> [str] cluster_id_identifer_get(id)

Cluster Id Identifer Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Cluster Id Identifer Get
        api_response = api_instance.cluster_id_identifer_get(
            path_params=path_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_identifer_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_id_identifer_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#cluster_id_identifer_get.ApiResponseFor422) | Validation Error

#### cluster_id_identifer_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### cluster_id_identifer_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_id_members_get**
<a name="cluster_id_members_get"></a>
> [ClusterMember] cluster_id_members_get(idlimit)

Cluster Id Members Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from apollo2_api_client.model.cluster_member import ClusterMember
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
        'limit': 1,
    }
    try:
        # Cluster Id Members Get
        api_response = api_instance.cluster_id_members_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_members_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    query_params = {
        'limit': 1,
        'last': -1,
        'end': 1,
    }
    try:
        # Cluster Id Members Get
        api_response = api_instance.cluster_id_members_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_id_members_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | 
last | LastSchema | | optional
end | EndSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of -1

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_id_members_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#cluster_id_members_get.ApiResponseFor422) | Validation Error

#### cluster_id_members_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClusterMember**]({{complexTypePrefix}}ClusterMember.md) | [**ClusterMember**]({{complexTypePrefix}}ClusterMember.md) | [**ClusterMember**]({{complexTypePrefix}}ClusterMember.md) |  | 

#### cluster_id_members_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_identifer_delete**
<a name="cluster_identifer_delete"></a>
> str cluster_identifer_delete(identifierrequest_body)

Cluster Identifer Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'identifier': "identifier_example",
    }
    body = [
        1
    ]
    try:
        # Cluster Identifer Delete
        api_response = api_instance.cluster_identifer_delete(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_identifer_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifier | IdentifierSchema | | 


# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_identifer_delete.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#cluster_identifer_delete.ApiResponseFor422) | Validation Error

#### cluster_identifer_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_identifer_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_identifer_post**
<a name="cluster_identifer_post"></a>
> str cluster_identifer_post(identifierrequest_body)

Cluster Identifer Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'identifier': "identifier_example",
    }
    body = [
        1
    ]
    try:
        # Cluster Identifer Post
        api_response = api_instance.cluster_identifer_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_identifer_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifier | IdentifierSchema | | 


# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_identifer_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#cluster_identifer_post.ApiResponseFor422) | Validation Error

#### cluster_identifer_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_identifer_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cluster_post**
<a name="cluster_post"></a>
> str cluster_post(cluster)

Cluster Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import cluster_api
from apollo2_api_client.model.cluster import Cluster
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_api.ClusterApi(api_client)

    # example passing only required values which don't have defaults set
    body = Cluster(None)
    try:
        # Cluster Post
        api_response = api_instance.cluster_post(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ClusterApi->cluster_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Cluster**](../../models/Cluster.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cluster_post.ApiResponseFor200) | Successful Response
201 | [ApiResponseFor201](#cluster_post.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#cluster_post.ApiResponseFor400) | Bad Request
409 | [ApiResponseFor409](#cluster_post.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#cluster_post.ApiResponseFor422) | Validation Error

#### cluster_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

#### cluster_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_post.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### cluster_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

