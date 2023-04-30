<a name="__pageTop"></a>
# apollo2_api_client.apis.tags.source_api.SourceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**source_batch_get**](#source_batch_get) | **post** /source/get | Source Batch Get
[**source_count_get**](#source_count_get) | **get** /source/count | Source Count Get
[**source_enrichments_batch_delete**](#source_enrichments_batch_delete) | **post** /source/enrichments/delete | Source Enrichments Batch Delete
[**source_enrichments_batch_get**](#source_enrichments_batch_get) | **post** /source/enrichments/get | Source Enrichments Batch Get
[**source_enrichments_batch_post**](#source_enrichments_batch_post) | **post** /source/enrichments/submit | Source Enrichments Batch Post
[**source_get**](#source_get) | **get** /source | Source Get
[**source_id_delete**](#source_id_delete) | **delete** /source/{id} | Source Id Delete
[**source_id_enrichments_delete**](#source_id_enrichments_delete) | **delete** /source/{id}/enrichments | Source Id Enrichments Delete
[**source_id_enrichments_get**](#source_id_enrichments_get) | **get** /source/{id}/enrichments | Source Id Enrichments Get
[**source_id_enrichments_post**](#source_id_enrichments_post) | **post** /source/{id}/enrichments | Source Id Enrichments Post
[**source_id_forward_batch_translate**](#source_id_forward_batch_translate) | **post** /source/id/forward | Source Id Forward Batch Translate
[**source_id_forward_translate**](#source_id_forward_translate) | **get** /source/id/forward/{id} | Source Id Forward Translate
[**source_id_get**](#source_id_get) | **get** /source/{id} | Source Id Get
[**source_id_identifer_get**](#source_id_identifer_get) | **get** /source/{id}/identifer | Source Id Identifer Get
[**source_id_reverse_batch_translate**](#source_id_reverse_batch_translate) | **post** /source/id/reverse | Source Id Reverse Batch Translate
[**source_id_reverse_translate**](#source_id_reverse_translate) | **get** /source/id/reverse/{id} | Source Id Reverse Translate
[**source_identifer_delete**](#source_identifer_delete) | **post** /source/identifer/delete | Source Identifer Delete
[**source_identifer_post**](#source_identifer_post) | **post** /source/identifer/post | Source Identifer Post
[**source_max_id_get**](#source_max_id_get) | **get** /source/max_id | Source Max Id Get

# **source_batch_get**
<a name="source_batch_get"></a>
> [Source] source_batch_get(batch_get_request)

Source Batch Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
from apollo2_api_client.model.batch_get_request import BatchGetRequest
from apollo2_api_client.model.source import Source
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = BatchGetRequest(
        ids=[
            1
        ],
        with_enrichment=True,
        enrichment_name="enrichment_name_example",
        enrichment_provider="enrichment_provider_example",
        enrichment_tag="enrichment_tag_example",
        enrichment_version="enrichment_version_example",
        with_cluster=True,
        cluster_name="cluster_name_example",
        cluster_provider="cluster_provider_example",
        cluster_tag="cluster_tag_example",
        cluster_version="cluster_version_example",
    )
    try:
        # Source Batch Get
        api_response = api_instance.source_batch_get(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_batch_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'identifier': "identifier_example",
    }
    body = BatchGetRequest(
        ids=[
            1
        ],
        with_enrichment=True,
        enrichment_name="enrichment_name_example",
        enrichment_provider="enrichment_provider_example",
        enrichment_tag="enrichment_tag_example",
        enrichment_version="enrichment_version_example",
        with_cluster=True,
        cluster_name="cluster_name_example",
        cluster_provider="cluster_provider_example",
        cluster_tag="cluster_tag_example",
        cluster_version="cluster_version_example",
    )
    try:
        # Source Batch Get
        api_response = api_instance.source_batch_get(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_batch_get: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchGetRequest**](../../models/BatchGetRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifier | IdentifierSchema | | optional


# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#source_batch_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_batch_get.ApiResponseFor422) | Validation Error

#### source_batch_get.ApiResponseFor200
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
[**Source**]({{complexTypePrefix}}Source.md) | [**Source**]({{complexTypePrefix}}Source.md) | [**Source**]({{complexTypePrefix}}Source.md) |  | 

#### source_batch_get.ApiResponseFor422
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

# **source_count_get**
<a name="source_count_get"></a>
> int source_count_get()

Source Count Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
from apollo2_api_client.model.media_type import MediaType
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only optional values
    query_params = {
        'last': 1,
        'end': 1,
        'platform': MediaType("News"),
        'identifier': "identifier_example",
    }
    try:
        # Source Count Get
        api_response = api_instance.source_count_get(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_count_get: %s\n" % e)
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
last | LastSchema | | optional
end | EndSchema | | optional
platform | PlatformSchema | | optional
identifier | IdentifierSchema | | optional


# LastSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PlatformSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**MediaType**](../../models/MediaType.md) |  | 


# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#source_count_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_count_get.ApiResponseFor422) | Validation Error

#### source_count_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

#### source_count_get.ApiResponseFor422
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

# **source_enrichments_batch_delete**
<a name="source_enrichments_batch_delete"></a>
> str source_enrichments_batch_delete(enrichments_batch_request)

Source Enrichments Batch Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

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
        # Source Enrichments Batch Delete
        api_response = api_instance.source_enrichments_batch_delete(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_enrichments_batch_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#source_enrichments_batch_delete.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#source_enrichments_batch_delete.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#source_enrichments_batch_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#source_enrichments_batch_delete.ApiResponseFor422) | Validation Error

#### source_enrichments_batch_delete.ApiResponseFor200
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

#### source_enrichments_batch_delete.ApiResponseFor400
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

#### source_enrichments_batch_delete.ApiResponseFor404
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

#### source_enrichments_batch_delete.ApiResponseFor422
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

# **source_enrichments_batch_get**
<a name="source_enrichments_batch_get"></a>
> [[Enrichment]] source_enrichments_batch_get(enrichments_batch_request)

Source Enrichments Batch Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

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
        # Source Enrichments Batch Get
        api_response = api_instance.source_enrichments_batch_get(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_enrichments_batch_get: %s\n" % e)
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
200 | [ApiResponseFor200](#source_enrichments_batch_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#source_enrichments_batch_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#source_enrichments_batch_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#source_enrichments_batch_get.ApiResponseFor422) | Validation Error

#### source_enrichments_batch_get.ApiResponseFor200
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

#### source_enrichments_batch_get.ApiResponseFor400
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

#### source_enrichments_batch_get.ApiResponseFor404
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

#### source_enrichments_batch_get.ApiResponseFor422
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

# **source_enrichments_batch_post**
<a name="source_enrichments_batch_post"></a>
> str source_enrichments_batch_post(request_body)

Source Enrichments Batch Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict(
        "key": [
            Enrichment(None)
        ],
    )
    try:
        # Source Enrichments Batch Post
        api_response = api_instance.source_enrichments_batch_post(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_enrichments_batch_post: %s\n" % e)
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
200 | [ApiResponseFor200](#source_enrichments_batch_post.ApiResponseFor200) | Successful Response
201 | [ApiResponseFor201](#source_enrichments_batch_post.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#source_enrichments_batch_post.ApiResponseFor400) | Bad Request
409 | [ApiResponseFor409](#source_enrichments_batch_post.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#source_enrichments_batch_post.ApiResponseFor422) | Validation Error

#### source_enrichments_batch_post.ApiResponseFor200
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

#### source_enrichments_batch_post.ApiResponseFor201
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

#### source_enrichments_batch_post.ApiResponseFor400
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

#### source_enrichments_batch_post.ApiResponseFor409
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

#### source_enrichments_batch_post.ApiResponseFor422
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

# **source_get**
<a name="source_get"></a>
> [Source] source_get(limit)

Source Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
from apollo2_api_client.model.media_type import MediaType
from apollo2_api_client.model.source import Source
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'limit': 1,
    }
    try:
        # Source Get
        api_response = api_instance.source_get(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'limit': 1,
        'last': -1,
        'end': 1,
        'with_enrichment': False,
        'with_cluster': False,
        'enrichment_name': "enrichment_name_example",
        'enrichment_provider': "enrichment_provider_example",
        'enrichment_tag': "enrichment_tag_example",
        'enrichment_version': "enrichment_version_example",
        'cluster_name': "cluster_name_example",
        'cluster_provider': "cluster_provider_example",
        'cluster_tag': "cluster_tag_example",
        'cluster_version': "cluster_version_example",
        'platform': MediaType("News"),
        'identifier': "identifier_example",
    }
    try:
        # Source Get
        api_response = api_instance.source_get(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_get: %s\n" % e)
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
limit | LimitSchema | | 
last | LastSchema | | optional
end | EndSchema | | optional
with_enrichment | WithEnrichmentSchema | | optional
with_cluster | WithClusterSchema | | optional
enrichment_name | EnrichmentNameSchema | | optional
enrichment_provider | EnrichmentProviderSchema | | optional
enrichment_tag | EnrichmentTagSchema | | optional
enrichment_version | EnrichmentVersionSchema | | optional
cluster_name | ClusterNameSchema | | optional
cluster_provider | ClusterProviderSchema | | optional
cluster_tag | ClusterTagSchema | | optional
cluster_version | ClusterVersionSchema | | optional
platform | PlatformSchema | | optional
identifier | IdentifierSchema | | optional


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

# WithEnrichmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# WithClusterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# EnrichmentNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EnrichmentProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EnrichmentTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EnrichmentVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PlatformSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**MediaType**](../../models/MediaType.md) |  | 


# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#source_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_get.ApiResponseFor422) | Validation Error

#### source_get.ApiResponseFor200
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
[**Source**]({{complexTypePrefix}}Source.md) | [**Source**]({{complexTypePrefix}}Source.md) | [**Source**]({{complexTypePrefix}}Source.md) |  | 

#### source_get.ApiResponseFor422
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

# **source_id_delete**
<a name="source_id_delete"></a>
> str source_id_delete(id)

Source Id Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Source Id Delete
        api_response = api_instance.source_id_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#source_id_delete.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_id_delete.ApiResponseFor422) | Validation Error

#### source_id_delete.ApiResponseFor200
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

#### source_id_delete.ApiResponseFor422
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

# **source_id_enrichments_delete**
<a name="source_id_enrichments_delete"></a>
> str source_id_enrichments_delete(id)

Source Id Enrichments Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
    }
    try:
        # Source Id Enrichments Delete
        api_response = api_instance.source_id_enrichments_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_enrichments_delete: %s\n" % e)

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
        # Source Id Enrichments Delete
        api_response = api_instance.source_id_enrichments_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_enrichments_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#source_id_enrichments_delete.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#source_id_enrichments_delete.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#source_id_enrichments_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#source_id_enrichments_delete.ApiResponseFor422) | Validation Error

#### source_id_enrichments_delete.ApiResponseFor200
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

#### source_id_enrichments_delete.ApiResponseFor400
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

#### source_id_enrichments_delete.ApiResponseFor404
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

#### source_id_enrichments_delete.ApiResponseFor422
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

# **source_id_enrichments_get**
<a name="source_id_enrichments_get"></a>
> [Enrichment] source_id_enrichments_get(id)

Source Id Enrichments Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
    }
    try:
        # Source Id Enrichments Get
        api_response = api_instance.source_id_enrichments_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_enrichments_get: %s\n" % e)

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
        # Source Id Enrichments Get
        api_response = api_instance.source_id_enrichments_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_enrichments_get: %s\n" % e)
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
200 | [ApiResponseFor200](#source_id_enrichments_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#source_id_enrichments_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#source_id_enrichments_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#source_id_enrichments_get.ApiResponseFor422) | Validation Error

#### source_id_enrichments_get.ApiResponseFor200
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

#### source_id_enrichments_get.ApiResponseFor400
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

#### source_id_enrichments_get.ApiResponseFor404
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

#### source_id_enrichments_get.ApiResponseFor422
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

# **source_id_enrichments_post**
<a name="source_id_enrichments_post"></a>
> str source_id_enrichments_post(idenrichment)

Source Id Enrichments Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = [
        Enrichment(None)
    ]
    try:
        # Source Id Enrichments Post
        api_response = api_instance.source_id_enrichments_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_enrichments_post: %s\n" % e)
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
200 | [ApiResponseFor200](#source_id_enrichments_post.ApiResponseFor200) | Successful Response
201 | [ApiResponseFor201](#source_id_enrichments_post.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#source_id_enrichments_post.ApiResponseFor400) | Bad Request
409 | [ApiResponseFor409](#source_id_enrichments_post.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#source_id_enrichments_post.ApiResponseFor422) | Validation Error

#### source_id_enrichments_post.ApiResponseFor200
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

#### source_id_enrichments_post.ApiResponseFor201
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

#### source_id_enrichments_post.ApiResponseFor400
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

#### source_id_enrichments_post.ApiResponseFor409
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

#### source_id_enrichments_post.ApiResponseFor422
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

# **source_id_forward_batch_translate**
<a name="source_id_forward_batch_translate"></a>
> [int] source_id_forward_batch_translate(request_body)

Source Id Forward Batch Translate

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
from apollo2_api_client.model.media_type import MediaType
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = [
        "request_body_example"
    ]
    try:
        # Source Id Forward Batch Translate
        api_response = api_instance.source_id_forward_batch_translate(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_forward_batch_translate: %s\n" % e)

    # example passing only optional values
    query_params = {
        'platform': MediaType("News"),
    }
    body = [
        "request_body_example"
    ]
    try:
        # Source Id Forward Batch Translate
        api_response = api_instance.source_id_forward_batch_translate(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_forward_batch_translate: %s\n" % e)
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
items | str,  | str,  |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
platform | PlatformSchema | | optional


# PlatformSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**MediaType**](../../models/MediaType.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#source_id_forward_batch_translate.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_id_forward_batch_translate.ApiResponseFor422) | Validation Error

#### source_id_forward_batch_translate.ApiResponseFor200
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
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

#### source_id_forward_batch_translate.ApiResponseFor422
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

# **source_id_forward_translate**
<a name="source_id_forward_translate"></a>
> int source_id_forward_translate(id)

Source Id Forward Translate

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
from apollo2_api_client.model.media_type import MediaType
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    try:
        # Source Id Forward Translate
        api_response = api_instance.source_id_forward_translate(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_forward_translate: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'platform': MediaType("News"),
    }
    try:
        # Source Id Forward Translate
        api_response = api_instance.source_id_forward_translate(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_forward_translate: %s\n" % e)
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
platform | PlatformSchema | | optional


# PlatformSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**MediaType**](../../models/MediaType.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#source_id_forward_translate.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_id_forward_translate.ApiResponseFor422) | Validation Error

#### source_id_forward_translate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

#### source_id_forward_translate.ApiResponseFor422
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

# **source_id_get**
<a name="source_id_get"></a>
> Source source_id_get(id)

Source Id Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
from apollo2_api_client.model.source import Source
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
    }
    try:
        # Source Id Get
        api_response = api_instance.source_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    query_params = {
        'with_enrichment': False,
        'with_cluster': False,
        'enrichment_name': "enrichment_name_example",
        'enrichment_provider': "enrichment_provider_example",
        'enrichment_tag': "enrichment_tag_example",
        'enrichment_version': "enrichment_version_example",
        'cluster_name': "cluster_name_example",
        'cluster_provider': "cluster_provider_example",
        'cluster_tag': "cluster_tag_example",
        'cluster_version': "cluster_version_example",
    }
    try:
        # Source Id Get
        api_response = api_instance.source_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_get: %s\n" % e)
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
with_enrichment | WithEnrichmentSchema | | optional
with_cluster | WithClusterSchema | | optional
enrichment_name | EnrichmentNameSchema | | optional
enrichment_provider | EnrichmentProviderSchema | | optional
enrichment_tag | EnrichmentTagSchema | | optional
enrichment_version | EnrichmentVersionSchema | | optional
cluster_name | ClusterNameSchema | | optional
cluster_provider | ClusterProviderSchema | | optional
cluster_tag | ClusterTagSchema | | optional
cluster_version | ClusterVersionSchema | | optional


# WithEnrichmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# WithClusterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# EnrichmentNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EnrichmentProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EnrichmentTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EnrichmentVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterVersionSchema

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
200 | [ApiResponseFor200](#source_id_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_id_get.ApiResponseFor422) | Validation Error

#### source_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Source**](../../models/Source.md) |  | 


#### source_id_get.ApiResponseFor422
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

# **source_id_identifer_get**
<a name="source_id_identifer_get"></a>
> [str] source_id_identifer_get(id)

Source Id Identifer Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Source Id Identifer Get
        api_response = api_instance.source_id_identifer_get(
            path_params=path_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_identifer_get: %s\n" % e)
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
200 | [ApiResponseFor200](#source_id_identifer_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_id_identifer_get.ApiResponseFor422) | Validation Error

#### source_id_identifer_get.ApiResponseFor200
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

#### source_id_identifer_get.ApiResponseFor422
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

# **source_id_reverse_batch_translate**
<a name="source_id_reverse_batch_translate"></a>
> [str] source_id_reverse_batch_translate(request_body)

Source Id Reverse Batch Translate

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    body = [
        1
    ]
    try:
        # Source Id Reverse Batch Translate
        api_response = api_instance.source_id_reverse_batch_translate(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_reverse_batch_translate: %s\n" % e)
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
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#source_id_reverse_batch_translate.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_id_reverse_batch_translate.ApiResponseFor422) | Validation Error

#### source_id_reverse_batch_translate.ApiResponseFor200
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

#### source_id_reverse_batch_translate.ApiResponseFor422
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

# **source_id_reverse_translate**
<a name="source_id_reverse_translate"></a>
> str source_id_reverse_translate(id)

Source Id Reverse Translate

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Source Id Reverse Translate
        api_response = api_instance.source_id_reverse_translate(
            path_params=path_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_id_reverse_translate: %s\n" % e)
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
200 | [ApiResponseFor200](#source_id_reverse_translate.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_id_reverse_translate.ApiResponseFor422) | Validation Error

#### source_id_reverse_translate.ApiResponseFor200
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

#### source_id_reverse_translate.ApiResponseFor422
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

# **source_identifer_delete**
<a name="source_identifer_delete"></a>
> str source_identifer_delete(identifierrequest_body)

Source Identifer Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'identifier': "identifier_example",
    }
    body = [
        1
    ]
    try:
        # Source Identifer Delete
        api_response = api_instance.source_identifer_delete(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_identifer_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#source_identifer_delete.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_identifer_delete.ApiResponseFor422) | Validation Error

#### source_identifer_delete.ApiResponseFor200
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

#### source_identifer_delete.ApiResponseFor422
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

# **source_identifer_post**
<a name="source_identifer_post"></a>
> str source_identifer_post(identifierrequest_body)

Source Identifer Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'identifier': "identifier_example",
    }
    body = [
        1
    ]
    try:
        # Source Identifer Post
        api_response = api_instance.source_identifer_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_identifer_post: %s\n" % e)
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
200 | [ApiResponseFor200](#source_identifer_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_identifer_post.ApiResponseFor422) | Validation Error

#### source_identifer_post.ApiResponseFor200
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

#### source_identifer_post.ApiResponseFor422
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

# **source_max_id_get**
<a name="source_max_id_get"></a>
> int source_max_id_get()

Source Max Id Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import source_api
from apollo2_api_client.model.media_type import MediaType
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
    api_instance = source_api.SourceApi(api_client)

    # example passing only optional values
    query_params = {
        'platform': MediaType("News"),
        'identifier': "identifier_example",
    }
    try:
        # Source Max Id Get
        api_response = api_instance.source_max_id_get(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling SourceApi->source_max_id_get: %s\n" % e)
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
platform | PlatformSchema | | optional
identifier | IdentifierSchema | | optional


# PlatformSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**MediaType**](../../models/MediaType.md) |  | 


# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#source_max_id_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#source_max_id_get.ApiResponseFor422) | Validation Error

#### source_max_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

#### source_max_id_get.ApiResponseFor422
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

