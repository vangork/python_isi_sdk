# isi_sdk.MetadataiqApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadataiq_reset_item**](MetadataiqApi.md#create_metadataiq_reset_item) | **POST** /platform/21/metadataiq/reset | 
[**delete_metadataiq_reset**](MetadataiqApi.md#delete_metadataiq_reset) | **DELETE** /platform/21/metadataiq/reset | 
[**get_metadataiq_certificate**](MetadataiqApi.md#get_metadataiq_certificate) | **GET** /platform/22/metadataiq/certificate | 
[**get_metadataiq_settings**](MetadataiqApi.md#get_metadataiq_settings) | **GET** /platform/21/metadataiq/settings | 
[**get_metadataiq_status**](MetadataiqApi.md#get_metadataiq_status) | **GET** /platform/22/metadataiq/status | 
[**update_metadataiq_settings**](MetadataiqApi.md#update_metadataiq_settings) | **PUT** /platform/21/metadataiq/settings | 


# **create_metadataiq_reset_item**
> Empty create_metadataiq_reset_item(metadataiq_reset_item)



Resend all metadata under the configured path to the database from a new snapshot. While this operation is in progress, it will block incremental updates to the database.

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
api_instance = isi_sdk.MetadataiqApi(isi_sdk.ApiClient(configuration))
metadataiq_reset_item = isi_sdk.Empty() # Empty | 

try:
    api_response = api_instance.create_metadataiq_reset_item(metadataiq_reset_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataiqApi->create_metadataiq_reset_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadataiq_reset_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadataiq_reset**
> delete_metadataiq_reset()



Reset MetadataIQ to factory defaults. This means the daemons are disabled, the settings are reset, and any artifacts on cluster are cleared.

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
api_instance = isi_sdk.MetadataiqApi(isi_sdk.ApiClient(configuration))

try:
    api_instance.delete_metadataiq_reset()
except ApiException as e:
    print("Exception when calling MetadataiqApi->delete_metadataiq_reset: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadataiq_certificate**
> MetadataiqCertificate get_metadataiq_certificate()



Retrieve a Metadataiq CA certificate.

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
api_instance = isi_sdk.MetadataiqApi(isi_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_metadataiq_certificate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataiqApi->get_metadataiq_certificate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataiqCertificate**](MetadataiqCertificate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadataiq_settings**
> MetadataiqSettings get_metadataiq_settings()



View MetadataIQ settings.

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
api_instance = isi_sdk.MetadataiqApi(isi_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_metadataiq_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataiqApi->get_metadataiq_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataiqSettings**](MetadataiqSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadataiq_status**
> MetadataiqStatus get_metadataiq_status()



View MetadataIQ current Cycle Status.

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
api_instance = isi_sdk.MetadataiqApi(isi_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_metadataiq_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataiqApi->get_metadataiq_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataiqStatus**](MetadataiqStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadataiq_settings**
> update_metadataiq_settings(metadataiq_settings)



Modify a subset of MetadataIQ settings.

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
api_instance = isi_sdk.MetadataiqApi(isi_sdk.ApiClient(configuration))
metadataiq_settings = isi_sdk.MetadataiqSettingsSettings() # MetadataiqSettingsSettings | 

try:
    api_instance.update_metadataiq_settings(metadataiq_settings)
except ApiException as e:
    print("Exception when calling MetadataiqApi->update_metadataiq_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadataiq_settings** | [**MetadataiqSettingsSettings**](MetadataiqSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

