<a name="__pageTop"></a>
# apollo2_api_client.apis.tags.default_api.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_get**](#ping_get) | **get** /ping | Ping Get

# **ping_get**
<a name="ping_get"></a>
> str ping_get()

Ping Get

### Example

```python
import apollo2_api_client
from apollo2_api_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apollo2_api_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apollo2_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Ping Get
        api_response = api_instance.ping_get()
        pprint(api_response)
    except apollo2_api_client.ApiException as e:
        print("Exception when calling DefaultApi->ping_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ping_get.ApiResponseFor200) | Successful Response

#### ping_get.ApiResponseFor200
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

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

