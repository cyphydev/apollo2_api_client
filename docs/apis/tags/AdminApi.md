<a name="__pageTop"></a>
# apollo2_api_client.apis.tags.admin_api.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_data_post**](#admin_data_post) | **post** /data | Admin Data Post
[**admin_flush**](#admin_flush) | **delete** /dbflush | Admin Flush
[**status_get**](#status_get) | **get** /status | Status Get

# **admin_data_post**
<a name="admin_data_post"></a>
> RawDataPostResponse admin_data_post(raw_data_post_request)

Admin Data Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import admin_api
from apollo2_api_client.model.raw_data_post_response import RawDataPostResponse
from apollo2_api_client.model.raw_data_post_request import RawDataPostRequest
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    body = RawDataPostRequest(
        override=False,
        data=[
            RawDataPostEntry(
                source=Source(
                    id="id_example",
                    type="type_example",
                    platform=MediaType("News"),
                    sid=1,
                    enrichments=[],
                    clusters=[],
                    name="name_example",
                    data=None,
                ),
                items=[
                    Item(
                        id="id_example",
                        author="author_example",
                        platform=MediaType("News"),
                        time_published=1,
                        sid=1,
                        source_id=1,
                        enrichments=[],
                        clusters=[],
                        media_items=[],
                        text="text_example",
                        data=None,
                    )
                ],
            )
        ],
    )
    try:
        # Admin Data Post
        api_response = api_instance.admin_data_post(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling AdminApi->admin_data_post: %s\n" % e)
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
[**RawDataPostRequest**](../../models/RawDataPostRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#admin_data_post.ApiResponseFor200) | Successful Response
201 | [ApiResponseFor201](#admin_data_post.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#admin_data_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#admin_data_post.ApiResponseFor422) | Validation Error

#### admin_data_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RawDataPostResponse**](../../models/RawDataPostResponse.md) |  | 


#### admin_data_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RawDataPostResponse**](../../models/RawDataPostResponse.md) |  | 


#### admin_data_post.ApiResponseFor400
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

#### admin_data_post.ApiResponseFor422
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

# **admin_flush**
<a name="admin_flush"></a>
> bool, date, datetime, dict, float, int, list, str, none_type admin_flush()

Admin Flush

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Admin Flush
        api_response = api_instance.admin_flush()
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling AdminApi->admin_flush: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#admin_flush.ApiResponseFor200) | Successful Response

#### admin_flush.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **status_get**
<a name="status_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type status_get()

Status Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Status Get
        api_response = api_instance.status_get()
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling AdminApi->status_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#status_get.ApiResponseFor200) | Successful Response

#### status_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

