<a name="__pageTop"></a>
# apollo2_api_client.apis.tags.enrichment_api.EnrichmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrichments_meta_delete**](#enrichments_meta_delete) | **delete** /enrichments/meta | Enrichments Meta Delete
[**enrichments_meta_get**](#enrichments_meta_get) | **get** /enrichments/meta | Enrichments Meta Get
[**enrichments_meta_post**](#enrichments_meta_post) | **post** /enrichments/meta | Enrichments Meta Post

# **enrichments_meta_delete**
<a name="enrichments_meta_delete"></a>
> str enrichments_meta_delete(nameprovidertagversionforce)

Enrichments Meta Delete

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import enrichment_api
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
    api_instance = enrichment_api.EnrichmentApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'name': "name_example",
        'provider': "provider_example",
        'tag': "tag_example",
        'version': "version_example",
        'force': True,
    }
    try:
        # Enrichments Meta Delete
        api_response = api_instance.enrichments_meta_delete(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling EnrichmentApi->enrichments_meta_delete: %s\n" % e)
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
force | ForceSchema | | 


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

# ForceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#enrichments_meta_delete.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#enrichments_meta_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#enrichments_meta_delete.ApiResponseFor422) | Validation Error

#### enrichments_meta_delete.ApiResponseFor200
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

#### enrichments_meta_delete.ApiResponseFor404
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

#### enrichments_meta_delete.ApiResponseFor422
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

# **enrichments_meta_get**
<a name="enrichments_meta_get"></a>
> [EnrichmentMeta] enrichments_meta_get()

Enrichments Meta Get

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import enrichment_api
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from apollo2_api_client.model.enrichment_meta import EnrichmentMeta
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
    api_instance = enrichment_api.EnrichmentApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'provider': "provider_example",
        'tag': "tag_example",
        'version': "version_example",
    }
    try:
        # Enrichments Meta Get
        api_response = api_instance.enrichments_meta_get(
            query_params=query_params,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling EnrichmentApi->enrichments_meta_get: %s\n" % e)
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
200 | [ApiResponseFor200](#enrichments_meta_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#enrichments_meta_get.ApiResponseFor422) | Validation Error

#### enrichments_meta_get.ApiResponseFor200
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
[**EnrichmentMeta**]({{complexTypePrefix}}EnrichmentMeta.md) | [**EnrichmentMeta**]({{complexTypePrefix}}EnrichmentMeta.md) | [**EnrichmentMeta**]({{complexTypePrefix}}EnrichmentMeta.md) |  | 

#### enrichments_meta_get.ApiResponseFor422
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

# **enrichments_meta_post**
<a name="enrichments_meta_post"></a>
> str enrichments_meta_post(enrichment_meta)

Enrichments Meta Post

### Example

* Api Key Authentication (APIKeyHeader):
```python
import apollo2_api_client
from apollo2_api_client.apis.tags import enrichment_api
from apollo2_api_client.model.http_validation_error import HTTPValidationError
from apollo2_api_client.model.enrichment_meta import EnrichmentMeta
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
    api_instance = enrichment_api.EnrichmentApi(api_client)

    # example passing only required values which don't have defaults set
    body = EnrichmentMeta(None)
    try:
        # Enrichments Meta Post
        api_response = api_instance.enrichments_meta_post(
            body=body,
        )
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling EnrichmentApi->enrichments_meta_post: %s\n" % e)
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
[**EnrichmentMeta**](../../models/EnrichmentMeta.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#enrichments_meta_post.ApiResponseFor200) | Successful Response
201 | [ApiResponseFor201](#enrichments_meta_post.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#enrichments_meta_post.ApiResponseFor400) | Bad Request
409 | [ApiResponseFor409](#enrichments_meta_post.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#enrichments_meta_post.ApiResponseFor422) | Validation Error

#### enrichments_meta_post.ApiResponseFor200
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

#### enrichments_meta_post.ApiResponseFor201
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

#### enrichments_meta_post.ApiResponseFor400
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

#### enrichments_meta_post.ApiResponseFor409
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

#### enrichments_meta_post.ApiResponseFor422
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

