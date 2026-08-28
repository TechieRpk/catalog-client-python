# catalog_client.DatasetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset**](DatasetsApi.md#create_dataset) | **POST** /datasets | 
[**delete_dataset**](DatasetsApi.md#delete_dataset) | **DELETE** /datasets/{id} | 
[**get_dataset**](DatasetsApi.md#get_dataset) | **GET** /datasets/{id} | 
[**list_datasets**](DatasetsApi.md#list_datasets) | **GET** /datasets | 
[**update_dataset**](DatasetsApi.md#update_dataset) | **PUT** /datasets/{id} | 


# **create_dataset**
> DatasetDTO create_dataset(dataset_dto)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import catalog_client
from catalog_client.models.dataset_dto import DatasetDTO
from catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = catalog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = catalog_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_client.DatasetsApi(api_client)
    dataset_dto = catalog_client.DatasetDTO() # DatasetDTO | 

    try:
        api_response = api_instance.create_dataset(dataset_dto)
        print("The response of DatasetsApi->create_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->create_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_dto** | [**DatasetDTO**](DatasetDTO.md)|  | 

### Return type

[**DatasetDTO**](DatasetDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | createDataset 201 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> delete_dataset(id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import catalog_client
from catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = catalog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = catalog_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_client.DatasetsApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_dataset(id)
    except Exception as e:
        print("Exception when calling DatasetsApi->delete_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | deleteDataset 204 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> DatasetDTO get_dataset(id)

### Example


```python
import catalog_client
from catalog_client.models.dataset_dto import DatasetDTO
from catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = catalog_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_client.DatasetsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_dataset(id)
        print("The response of DatasetsApi->get_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DatasetDTO**](DatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getDataset 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datasets**
> List[DatasetDTO] list_datasets()

### Example


```python
import catalog_client
from catalog_client.models.dataset_dto import DatasetDTO
from catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = catalog_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_client.DatasetsApi(api_client)

    try:
        api_response = api_instance.list_datasets()
        print("The response of DatasetsApi->list_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->list_datasets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DatasetDTO]**](DatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listDatasets 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> DatasetDTO update_dataset(id, dataset_dto)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import catalog_client
from catalog_client.models.dataset_dto import DatasetDTO
from catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = catalog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = catalog_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = catalog_client.DatasetsApi(api_client)
    id = 56 # int | 
    dataset_dto = catalog_client.DatasetDTO() # DatasetDTO | 

    try:
        api_response = api_instance.update_dataset(id, dataset_dto)
        print("The response of DatasetsApi->update_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->update_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **dataset_dto** | [**DatasetDTO**](DatasetDTO.md)|  | 

### Return type

[**DatasetDTO**](DatasetDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateDataset 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

