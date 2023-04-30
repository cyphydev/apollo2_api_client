<a name="__pageTop"></a>
# apollo2_api_client.apis.tags.item_api.ItemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**item_attach_media_post**](#item_attach_media_post) | **post** /item/attach_media | Item Attach Media Post
[**item_batch_get**](#item_batch_get) | **post** /item/get | Item Batch Get
[**item_count_get**](#item_count_get) | **get** /item/count | Item Count Get
[**item_detach_media_post**](#item_detach_media_post) | **post** /item/detach_media | Item Detach Media Post
[**item_enrichments_batch_delete**](#item_enrichments_batch_delete) | **post** /item/enrichments/delete | Item Enrichments Batch Delete
[**item_enrichments_batch_get**](#item_enrichments_batch_get) | **post** /item/enrichments/get | Item Enrichments Batch Get
[**item_enrichments_batch_post**](#item_enrichments_batch_post) | **post** /item/enrichments/submit | Item Enrichments Batch Post
[**item_get**](#item_get) | **get** /item | Item Get
[**item_id_delete**](#item_id_delete) | **delete** /item/{id} | Item Id Delete
[**item_id_enrichments_delete**](#item_id_enrichments_delete) | **delete** /item/{id}/enrichments | Item Id Enrichments Delete
[**item_id_enrichments_get**](#item_id_enrichments_get) | **get** /item/{id}/enrichments | Item Id Enrichments Get
[**item_id_enrichments_post**](#item_id_enrichments_post) | **post** /item/{id}/enrichments | Item Id Enrichments Post
[**item_id_forward_batch_translate**](#item_id_forward_batch_translate) | **post** /item/id/forward | Item Id Forward Batch Translate
[**item_id_forward_translate**](#item_id_forward_translate) | **get** /item/id/forward/{id} | Item Id Forward Translate
[**item_id_get**](#item_id_get) | **get** /item/{id} | Item Id Get
[**item_id_identifer_get**](#item_id_identifer_get) | **get** /item/{id}/identifer | Item Id Identifer Get
[**item_id_reverse_batch_translate**](#item_id_reverse_batch_translate) | **post** /item/id/reverse | Item Id Reverse Batch Translate
[**item_id_reverse_translate**](#item_id_reverse_translate) | **get** /item/id/reverse/{id} | Item Id Reverse Translate
[**item_identifer_delete**](#item_identifer_delete) | **post** /item/identifer/delete | Item Identifer Delete
[**item_identifer_post**](#item_identifer_post) | **post** /item/identifer/post | Item Identifer Post
[**item_max_id_get**](#item_max_id_get) | **get** /item/max_id | Item Max Id Get

# **item_attach_media_post**
<a name="item_attach_media_post"></a>
> str item_attach_media_post(modify_media_attachment_request)

Item Attach Media Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
from apollo2_api_client.model.modify_media_attachment_request import ModifyMediaAttachmentRequest
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    body = ModifyMediaAttachmentRequest(
        item_ids=[
            1
        ],
        media_ids=[
            1
        ],
        data=[
            dict()
        ],
        ignore_missing_when_deleting=True,
    )
    try:
        # Item Attach Media Post
        api_response = api_instance.item_attach_media_post(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_attach_media_post: %s\n" % e)
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
[**ModifyMediaAttachmentRequest**](../../models/ModifyMediaAttachmentRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#item_attach_media_post.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#item_attach_media_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#item_attach_media_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#item_attach_media_post.ApiResponseFor422) | Validation Error

#### item_attach_media_post.ApiResponseFor200
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

#### item_attach_media_post.ApiResponseFor400
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

#### item_attach_media_post.ApiResponseFor404
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

#### item_attach_media_post.ApiResponseFor422
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

# **item_batch_get**
<a name="item_batch_get"></a>
> [Item] item_batch_get(batch_get_request)

Item Batch Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
from apollo2_api_client.model.item import Item
from apollo2_api_client.model.batch_get_request import BatchGetRequest
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
    api_instance = item_api.ItemApi(api_client)

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
        # Item Batch Get
        api_response = api_instance.item_batch_get(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_batch_get: %s\n" % e)

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
        # Item Batch Get
        api_response = api_instance.item_batch_get(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_batch_get: %s\n" % e)
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
200 | [ApiResponseFor200](#item_batch_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_batch_get.ApiResponseFor422) | Validation Error

#### item_batch_get.ApiResponseFor200
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
[**Item**]({{complexTypePrefix}}Item.md) | [**Item**]({{complexTypePrefix}}Item.md) | [**Item**]({{complexTypePrefix}}Item.md) |  | 

#### item_batch_get.ApiResponseFor422
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

# **item_count_get**
<a name="item_count_get"></a>
> int item_count_get()

Item Count Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only optional values
    query_params = {
        'last': 1,
        'end': 1,
        'platform': MediaType("News"),
        'identifier': "identifier_example",
        'inclusive_begin_datetime': "1970-01-01T00:00:00.00Z",
        'exclusive_end_datetime': "1970-01-01T00:00:00.00Z",
    }
    try:
        # Item Count Get
        api_response = api_instance.item_count_get(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_count_get: %s\n" % e)
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
inclusive_begin_datetime | InclusiveBeginDatetimeSchema | | optional
exclusive_end_datetime | ExclusiveEndDatetimeSchema | | optional


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

# InclusiveBeginDatetimeSchema

%Y-%m-%dT%H:%M:%S%z

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | %Y-%m-%dT%H:%M:%S%z | value must conform to RFC-3339 date-time

# ExclusiveEndDatetimeSchema

%Y-%m-%dT%H:%M:%S%z

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | %Y-%m-%dT%H:%M:%S%z | value must conform to RFC-3339 date-time

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#item_count_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_count_get.ApiResponseFor422) | Validation Error

#### item_count_get.ApiResponseFor200
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

#### item_count_get.ApiResponseFor422
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

# **item_detach_media_post**
<a name="item_detach_media_post"></a>
> str item_detach_media_post(modify_media_attachment_request)

Item Detach Media Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
from apollo2_api_client.model.modify_media_attachment_request import ModifyMediaAttachmentRequest
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    body = ModifyMediaAttachmentRequest(
        item_ids=[
            1
        ],
        media_ids=[
            1
        ],
        data=[
            dict()
        ],
        ignore_missing_when_deleting=True,
    )
    try:
        # Item Detach Media Post
        api_response = api_instance.item_detach_media_post(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_detach_media_post: %s\n" % e)
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
[**ModifyMediaAttachmentRequest**](../../models/ModifyMediaAttachmentRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#item_detach_media_post.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#item_detach_media_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#item_detach_media_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#item_detach_media_post.ApiResponseFor422) | Validation Error

#### item_detach_media_post.ApiResponseFor200
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

#### item_detach_media_post.ApiResponseFor400
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

#### item_detach_media_post.ApiResponseFor404
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

#### item_detach_media_post.ApiResponseFor422
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

# **item_enrichments_batch_delete**
<a name="item_enrichments_batch_delete"></a>
> str item_enrichments_batch_delete(enrichments_batch_request)

Item Enrichments Batch Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

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
        # Item Enrichments Batch Delete
        api_response = api_instance.item_enrichments_batch_delete(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_enrichments_batch_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#item_enrichments_batch_delete.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#item_enrichments_batch_delete.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#item_enrichments_batch_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#item_enrichments_batch_delete.ApiResponseFor422) | Validation Error

#### item_enrichments_batch_delete.ApiResponseFor200
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

#### item_enrichments_batch_delete.ApiResponseFor400
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

#### item_enrichments_batch_delete.ApiResponseFor404
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

#### item_enrichments_batch_delete.ApiResponseFor422
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

# **item_enrichments_batch_get**
<a name="item_enrichments_batch_get"></a>
> [[Enrichment]] item_enrichments_batch_get(enrichments_batch_request)

Item Enrichments Batch Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

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
        # Item Enrichments Batch Get
        api_response = api_instance.item_enrichments_batch_get(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_enrichments_batch_get: %s\n" % e)
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
200 | [ApiResponseFor200](#item_enrichments_batch_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#item_enrichments_batch_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#item_enrichments_batch_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#item_enrichments_batch_get.ApiResponseFor422) | Validation Error

#### item_enrichments_batch_get.ApiResponseFor200
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

#### item_enrichments_batch_get.ApiResponseFor400
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

#### item_enrichments_batch_get.ApiResponseFor404
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

#### item_enrichments_batch_get.ApiResponseFor422
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

# **item_enrichments_batch_post**
<a name="item_enrichments_batch_post"></a>
> str item_enrichments_batch_post(request_body)

Item Enrichments Batch Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict(
        "key": [
            Enrichment(None)
        ],
    )
    try:
        # Item Enrichments Batch Post
        api_response = api_instance.item_enrichments_batch_post(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_enrichments_batch_post: %s\n" % e)
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
200 | [ApiResponseFor200](#item_enrichments_batch_post.ApiResponseFor200) | Successful Response
201 | [ApiResponseFor201](#item_enrichments_batch_post.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#item_enrichments_batch_post.ApiResponseFor400) | Bad Request
409 | [ApiResponseFor409](#item_enrichments_batch_post.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#item_enrichments_batch_post.ApiResponseFor422) | Validation Error

#### item_enrichments_batch_post.ApiResponseFor200
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

#### item_enrichments_batch_post.ApiResponseFor201
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

#### item_enrichments_batch_post.ApiResponseFor400
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

#### item_enrichments_batch_post.ApiResponseFor409
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

#### item_enrichments_batch_post.ApiResponseFor422
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

# **item_get**
<a name="item_get"></a>
> [Item] item_get(limit)

Item Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
from apollo2_api_client.model.item import Item
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'limit': 1,
    }
    try:
        # Item Get
        api_response = api_instance.item_get(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_get: %s\n" % e)

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
        'inclusive_begin_datetime': "1970-01-01T00:00:00.00Z",
        'exclusive_end_datetime': "1970-01-01T00:00:00.00Z",
    }
    try:
        # Item Get
        api_response = api_instance.item_get(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_get: %s\n" % e)
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
inclusive_begin_datetime | InclusiveBeginDatetimeSchema | | optional
exclusive_end_datetime | ExclusiveEndDatetimeSchema | | optional


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

# InclusiveBeginDatetimeSchema

%Y-%m-%dT%H:%M:%S%z

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | %Y-%m-%dT%H:%M:%S%z | value must conform to RFC-3339 date-time

# ExclusiveEndDatetimeSchema

%Y-%m-%dT%H:%M:%S%z

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | %Y-%m-%dT%H:%M:%S%z | value must conform to RFC-3339 date-time

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#item_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_get.ApiResponseFor422) | Validation Error

#### item_get.ApiResponseFor200
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
[**Item**]({{complexTypePrefix}}Item.md) | [**Item**]({{complexTypePrefix}}Item.md) | [**Item**]({{complexTypePrefix}}Item.md) |  | 

#### item_get.ApiResponseFor422
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

# **item_id_delete**
<a name="item_id_delete"></a>
> str item_id_delete(id)

Item Id Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Item Id Delete
        api_response = api_instance.item_id_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#item_id_delete.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_id_delete.ApiResponseFor422) | Validation Error

#### item_id_delete.ApiResponseFor200
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

#### item_id_delete.ApiResponseFor422
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

# **item_id_enrichments_delete**
<a name="item_id_enrichments_delete"></a>
> str item_id_enrichments_delete(id)

Item Id Enrichments Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
    }
    try:
        # Item Id Enrichments Delete
        api_response = api_instance.item_id_enrichments_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_enrichments_delete: %s\n" % e)

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
        # Item Id Enrichments Delete
        api_response = api_instance.item_id_enrichments_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_enrichments_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#item_id_enrichments_delete.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#item_id_enrichments_delete.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#item_id_enrichments_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#item_id_enrichments_delete.ApiResponseFor422) | Validation Error

#### item_id_enrichments_delete.ApiResponseFor200
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

#### item_id_enrichments_delete.ApiResponseFor400
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

#### item_id_enrichments_delete.ApiResponseFor404
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

#### item_id_enrichments_delete.ApiResponseFor422
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

# **item_id_enrichments_get**
<a name="item_id_enrichments_get"></a>
> [Enrichment] item_id_enrichments_get(id)

Item Id Enrichments Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
    }
    try:
        # Item Id Enrichments Get
        api_response = api_instance.item_id_enrichments_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_enrichments_get: %s\n" % e)

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
        # Item Id Enrichments Get
        api_response = api_instance.item_id_enrichments_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_enrichments_get: %s\n" % e)
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
200 | [ApiResponseFor200](#item_id_enrichments_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#item_id_enrichments_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#item_id_enrichments_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#item_id_enrichments_get.ApiResponseFor422) | Validation Error

#### item_id_enrichments_get.ApiResponseFor200
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

#### item_id_enrichments_get.ApiResponseFor400
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

#### item_id_enrichments_get.ApiResponseFor404
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

#### item_id_enrichments_get.ApiResponseFor422
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

# **item_id_enrichments_post**
<a name="item_id_enrichments_post"></a>
> str item_id_enrichments_post(idenrichment)

Item Id Enrichments Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = [
        Enrichment(None)
    ]
    try:
        # Item Id Enrichments Post
        api_response = api_instance.item_id_enrichments_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_enrichments_post: %s\n" % e)
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
200 | [ApiResponseFor200](#item_id_enrichments_post.ApiResponseFor200) | Successful Response
201 | [ApiResponseFor201](#item_id_enrichments_post.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#item_id_enrichments_post.ApiResponseFor400) | Bad Request
409 | [ApiResponseFor409](#item_id_enrichments_post.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#item_id_enrichments_post.ApiResponseFor422) | Validation Error

#### item_id_enrichments_post.ApiResponseFor200
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

#### item_id_enrichments_post.ApiResponseFor201
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

#### item_id_enrichments_post.ApiResponseFor400
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

#### item_id_enrichments_post.ApiResponseFor409
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

#### item_id_enrichments_post.ApiResponseFor422
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

# **item_id_forward_batch_translate**
<a name="item_id_forward_batch_translate"></a>
> [int] item_id_forward_batch_translate(request_body)

Item Id Forward Batch Translate

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = [
        "request_body_example"
    ]
    try:
        # Item Id Forward Batch Translate
        api_response = api_instance.item_id_forward_batch_translate(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_forward_batch_translate: %s\n" % e)

    # example passing only optional values
    query_params = {
        'platform': MediaType("News"),
    }
    body = [
        "request_body_example"
    ]
    try:
        # Item Id Forward Batch Translate
        api_response = api_instance.item_id_forward_batch_translate(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_forward_batch_translate: %s\n" % e)
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
200 | [ApiResponseFor200](#item_id_forward_batch_translate.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_id_forward_batch_translate.ApiResponseFor422) | Validation Error

#### item_id_forward_batch_translate.ApiResponseFor200
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

#### item_id_forward_batch_translate.ApiResponseFor422
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

# **item_id_forward_translate**
<a name="item_id_forward_translate"></a>
> int item_id_forward_translate(id)

Item Id Forward Translate

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    try:
        # Item Id Forward Translate
        api_response = api_instance.item_id_forward_translate(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_forward_translate: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'platform': MediaType("News"),
    }
    try:
        # Item Id Forward Translate
        api_response = api_instance.item_id_forward_translate(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_forward_translate: %s\n" % e)
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
200 | [ApiResponseFor200](#item_id_forward_translate.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_id_forward_translate.ApiResponseFor422) | Validation Error

#### item_id_forward_translate.ApiResponseFor200
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

#### item_id_forward_translate.ApiResponseFor422
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

# **item_id_get**
<a name="item_id_get"></a>
> Item item_id_get(id)

Item Id Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
from apollo2_api_client.model.item import Item
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
    }
    try:
        # Item Id Get
        api_response = api_instance.item_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_get: %s\n" % e)

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
        # Item Id Get
        api_response = api_instance.item_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_get: %s\n" % e)
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
200 | [ApiResponseFor200](#item_id_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_id_get.ApiResponseFor422) | Validation Error

#### item_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Item**](../../models/Item.md) |  | 


#### item_id_get.ApiResponseFor422
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

# **item_id_identifer_get**
<a name="item_id_identifer_get"></a>
> [str] item_id_identifer_get(id)

Item Id Identifer Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Item Id Identifer Get
        api_response = api_instance.item_id_identifer_get(
            path_params=path_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_identifer_get: %s\n" % e)
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
200 | [ApiResponseFor200](#item_id_identifer_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_id_identifer_get.ApiResponseFor422) | Validation Error

#### item_id_identifer_get.ApiResponseFor200
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

#### item_id_identifer_get.ApiResponseFor422
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

# **item_id_reverse_batch_translate**
<a name="item_id_reverse_batch_translate"></a>
> [str] item_id_reverse_batch_translate(request_body)

Item Id Reverse Batch Translate

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    body = [
        1
    ]
    try:
        # Item Id Reverse Batch Translate
        api_response = api_instance.item_id_reverse_batch_translate(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_reverse_batch_translate: %s\n" % e)
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
200 | [ApiResponseFor200](#item_id_reverse_batch_translate.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_id_reverse_batch_translate.ApiResponseFor422) | Validation Error

#### item_id_reverse_batch_translate.ApiResponseFor200
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

#### item_id_reverse_batch_translate.ApiResponseFor422
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

# **item_id_reverse_translate**
<a name="item_id_reverse_translate"></a>
> str item_id_reverse_translate(id)

Item Id Reverse Translate

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Item Id Reverse Translate
        api_response = api_instance.item_id_reverse_translate(
            path_params=path_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_id_reverse_translate: %s\n" % e)
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
200 | [ApiResponseFor200](#item_id_reverse_translate.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_id_reverse_translate.ApiResponseFor422) | Validation Error

#### item_id_reverse_translate.ApiResponseFor200
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

#### item_id_reverse_translate.ApiResponseFor422
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

# **item_identifer_delete**
<a name="item_identifer_delete"></a>
> str item_identifer_delete(identifierrequest_body)

Item Identifer Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'identifier': "identifier_example",
    }
    body = [
        1
    ]
    try:
        # Item Identifer Delete
        api_response = api_instance.item_identifer_delete(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_identifer_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#item_identifer_delete.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_identifer_delete.ApiResponseFor422) | Validation Error

#### item_identifer_delete.ApiResponseFor200
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

#### item_identifer_delete.ApiResponseFor422
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

# **item_identifer_post**
<a name="item_identifer_post"></a>
> str item_identifer_post(identifierrequest_body)

Item Identifer Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'identifier': "identifier_example",
    }
    body = [
        1
    ]
    try:
        # Item Identifer Post
        api_response = api_instance.item_identifer_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_identifer_post: %s\n" % e)
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
200 | [ApiResponseFor200](#item_identifer_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_identifer_post.ApiResponseFor422) | Validation Error

#### item_identifer_post.ApiResponseFor200
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

#### item_identifer_post.ApiResponseFor422
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

# **item_max_id_get**
<a name="item_max_id_get"></a>
> int item_max_id_get()

Item Max Id Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import item_api
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
    api_instance = item_api.ItemApi(api_client)

    # example passing only optional values
    query_params = {
        'platform': MediaType("News"),
        'identifier': "identifier_example",
        'inclusive_begin_datetime': "1970-01-01T00:00:00.00Z",
        'exclusive_end_datetime': "1970-01-01T00:00:00.00Z",
    }
    try:
        # Item Max Id Get
        api_response = api_instance.item_max_id_get(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling ItemApi->item_max_id_get: %s\n" % e)
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
inclusive_begin_datetime | InclusiveBeginDatetimeSchema | | optional
exclusive_end_datetime | ExclusiveEndDatetimeSchema | | optional


# PlatformSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**MediaType**](../../models/MediaType.md) |  | 


# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# InclusiveBeginDatetimeSchema

%Y-%m-%dT%H:%M:%S%z

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | %Y-%m-%dT%H:%M:%S%z | value must conform to RFC-3339 date-time

# ExclusiveEndDatetimeSchema

%Y-%m-%dT%H:%M:%S%z

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | %Y-%m-%dT%H:%M:%S%z | value must conform to RFC-3339 date-time

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#item_max_id_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#item_max_id_get.ApiResponseFor422) | Validation Error

#### item_max_id_get.ApiResponseFor200
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

#### item_max_id_get.ApiResponseFor422
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

