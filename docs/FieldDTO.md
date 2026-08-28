# FieldDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from catalog_client.models.field_dto import FieldDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDTO from a JSON string
field_dto_instance = FieldDTO.from_json(json)
# print the JSON string representation of the object
print(FieldDTO.to_json())

# convert the object into a dict
field_dto_dict = field_dto_instance.to_dict()
# create an instance of FieldDTO from a dict
field_dto_from_dict = FieldDTO.from_dict(field_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


