# TwitterDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models import TwitterDomain

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterDomain from a JSON string
twitter_domain_instance = TwitterDomain.from_json(json)
# print the JSON string representation of the object
print TwitterDomain.to_json()

# convert the object into a dict
twitter_domain_dict = twitter_domain_instance.to_dict()
# create an instance of TwitterDomain from a dict
twitter_domain_form_dict = twitter_domain.from_dict(twitter_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


