# GeoLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**country_code** | **str** |  | [optional] 

## Example

```python
from apollo2_api_client.models import GeoLocation

# TODO update the JSON string below
json = "{}"
# create an instance of GeoLocation from a JSON string
geo_location_instance = GeoLocation.from_json(json)
# print the JSON string representation of the object
print GeoLocation.to_json()

# convert the object into a dict
geo_location_dict = geo_location_instance.to_dict()
# create an instance of GeoLocation from a dict
geo_location_form_dict = geo_location.from_dict(geo_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


