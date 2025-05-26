# isi_sdk.PapiApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_papi_settings**](PapiApi.md#get_papi_settings) | **GET** /platform/18/papi/settings | 
[**update_papi_settings**](PapiApi.md#update_papi_settings) | **PUT** /platform/18/papi/settings | 


# **get_papi_settings**
> PapiSettings get_papi_settings()



List PAPI settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.PapiApi(isi_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_papi_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PapiApi->get_papi_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PapiSettings**](PapiSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_papi_settings**
> update_papi_settings(papi_settings)



Modify PAPI settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.PapiApi(isi_sdk.ApiClient(configuration))
papi_settings = isi_sdk.PapiSettingsExtended() # PapiSettingsExtended | 

try:
    api_instance.update_papi_settings(papi_settings)
except ApiException as e:
    print("Exception when calling PapiApi->update_papi_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **papi_settings** | [**PapiSettingsExtended**](PapiSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

