# urlmanager.BasicOperationsApi

All URIs are relative to *https://urlmanager.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**url_manager_change_url_rewrite_request_path**](BasicOperationsApi.md#url_manager_change_url_rewrite_request_path) | **POST** /urlmanager/change_url_rewrite_request_path | Change Url Rewrite Request Path
[**url_manager_change_url_rewrite_request_path2**](BasicOperationsApi.md#url_manager_change_url_rewrite_request_path2) | **POST** /urlmanager.UrlManager/ChangeUrlRewriteRequestPath | Change Url Rewrite Request Path
[**url_manager_create_url_rewrite**](BasicOperationsApi.md#url_manager_create_url_rewrite) | **POST** /urlmanager/create_url_rewrite | Create Url Rewrite
[**url_manager_create_url_rewrite2**](BasicOperationsApi.md#url_manager_create_url_rewrite2) | **POST** /urlmanager.UrlManager/CreateUrlRewrite | Create Url Rewrite
[**url_manager_delete_url_rewrite**](BasicOperationsApi.md#url_manager_delete_url_rewrite) | **POST** /urlmanager/delete_url_rewrite | Delete Url Rewrite
[**url_manager_delete_url_rewrite2**](BasicOperationsApi.md#url_manager_delete_url_rewrite2) | **POST** /urlmanager.UrlManager/DeleteUrlRewrite | Delete Url Rewrite
[**url_manager_get_url_rewrite**](BasicOperationsApi.md#url_manager_get_url_rewrite) | **POST** /urlmanager/get_url_rewrite | Get Url Rewrite
[**url_manager_get_url_rewrite2**](BasicOperationsApi.md#url_manager_get_url_rewrite2) | **POST** /urlmanager.UrlManager/GetUrlRewrite | Get Url Rewrite
[**url_manager_list_url_rewrites**](BasicOperationsApi.md#url_manager_list_url_rewrites) | **POST** /urlmanager/list_url_rewrites | List Url Rewrites
[**url_manager_list_url_rewrites2**](BasicOperationsApi.md#url_manager_list_url_rewrites2) | **POST** /urlmanager.UrlManager/ListUrlRewrites | List Url Rewrites
[**url_manager_list_url_rewrites_by_target_paths**](BasicOperationsApi.md#url_manager_list_url_rewrites_by_target_paths) | **POST** /urlmanager/list_url_rewrites_by_target_paths | List Url Rewrites By Target Paths
[**url_manager_list_url_rewrites_by_target_paths2**](BasicOperationsApi.md#url_manager_list_url_rewrites_by_target_paths2) | **POST** /urlmanager.UrlManager/ListUrlRewritesByTargetPaths | List Url Rewrites By Target Paths
[**url_manager_resolve_url_rewrite**](BasicOperationsApi.md#url_manager_resolve_url_rewrite) | **POST** /urlmanager/resolve_url_rewrite | Resolve Url Rewrite
[**url_manager_resolve_url_rewrite2**](BasicOperationsApi.md#url_manager_resolve_url_rewrite2) | **POST** /urlmanager.UrlManager/ResolveUrlRewrite | Resolve Url Rewrite


# **url_manager_change_url_rewrite_request_path**
> object url_manager_change_url_rewrite_request_path(body)

Change Url Rewrite Request Path

Modify the request path of a specific URL rewrite configuration.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_change_url_rewrite_request_path_request import UrlmanagerChangeUrlRewriteRequestPathRequest
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerChangeUrlRewriteRequestPathRequest() # UrlmanagerChangeUrlRewriteRequestPathRequest | 

    try:
        # Change Url Rewrite Request Path
        api_response = api_instance.url_manager_change_url_rewrite_request_path(body)
        print("The response of BasicOperationsApi->url_manager_change_url_rewrite_request_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_change_url_rewrite_request_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerChangeUrlRewriteRequestPathRequest**](UrlmanagerChangeUrlRewriteRequestPathRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_change_url_rewrite_request_path2**
> object url_manager_change_url_rewrite_request_path2(body)

Change Url Rewrite Request Path

Modify the request path of a specific URL rewrite configuration.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_change_url_rewrite_request_path_request import UrlmanagerChangeUrlRewriteRequestPathRequest
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerChangeUrlRewriteRequestPathRequest() # UrlmanagerChangeUrlRewriteRequestPathRequest | 

    try:
        # Change Url Rewrite Request Path
        api_response = api_instance.url_manager_change_url_rewrite_request_path2(body)
        print("The response of BasicOperationsApi->url_manager_change_url_rewrite_request_path2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_change_url_rewrite_request_path2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerChangeUrlRewriteRequestPathRequest**](UrlmanagerChangeUrlRewriteRequestPathRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_create_url_rewrite**
> UrlmanagerUrlRewrite url_manager_create_url_rewrite(body)

Create Url Rewrite

Create a new URL rewrite configuration with customizable rules.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_create_url_rewrite_request import UrlmanagerCreateUrlRewriteRequest
from urlmanager.models.urlmanager_url_rewrite import UrlmanagerUrlRewrite
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerCreateUrlRewriteRequest() # UrlmanagerCreateUrlRewriteRequest | 

    try:
        # Create Url Rewrite
        api_response = api_instance.url_manager_create_url_rewrite(body)
        print("The response of BasicOperationsApi->url_manager_create_url_rewrite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_create_url_rewrite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerCreateUrlRewriteRequest**](UrlmanagerCreateUrlRewriteRequest.md)|  | 

### Return type

[**UrlmanagerUrlRewrite**](UrlmanagerUrlRewrite.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_create_url_rewrite2**
> UrlmanagerUrlRewrite url_manager_create_url_rewrite2(body)

Create Url Rewrite

Create a new URL rewrite configuration with customizable rules.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_create_url_rewrite_request import UrlmanagerCreateUrlRewriteRequest
from urlmanager.models.urlmanager_url_rewrite import UrlmanagerUrlRewrite
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerCreateUrlRewriteRequest() # UrlmanagerCreateUrlRewriteRequest | 

    try:
        # Create Url Rewrite
        api_response = api_instance.url_manager_create_url_rewrite2(body)
        print("The response of BasicOperationsApi->url_manager_create_url_rewrite2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_create_url_rewrite2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerCreateUrlRewriteRequest**](UrlmanagerCreateUrlRewriteRequest.md)|  | 

### Return type

[**UrlmanagerUrlRewrite**](UrlmanagerUrlRewrite.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_delete_url_rewrite**
> object url_manager_delete_url_rewrite(body)

Delete Url Rewrite

Delete an existing URL rewrite configuration.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_delete_url_rewrite_request import UrlmanagerDeleteUrlRewriteRequest
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerDeleteUrlRewriteRequest() # UrlmanagerDeleteUrlRewriteRequest | 

    try:
        # Delete Url Rewrite
        api_response = api_instance.url_manager_delete_url_rewrite(body)
        print("The response of BasicOperationsApi->url_manager_delete_url_rewrite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_delete_url_rewrite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerDeleteUrlRewriteRequest**](UrlmanagerDeleteUrlRewriteRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_delete_url_rewrite2**
> object url_manager_delete_url_rewrite2(body)

Delete Url Rewrite

Delete an existing URL rewrite configuration.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_delete_url_rewrite_request import UrlmanagerDeleteUrlRewriteRequest
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerDeleteUrlRewriteRequest() # UrlmanagerDeleteUrlRewriteRequest | 

    try:
        # Delete Url Rewrite
        api_response = api_instance.url_manager_delete_url_rewrite2(body)
        print("The response of BasicOperationsApi->url_manager_delete_url_rewrite2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_delete_url_rewrite2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerDeleteUrlRewriteRequest**](UrlmanagerDeleteUrlRewriteRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_get_url_rewrite**
> UrlmanagerUrlRewrite url_manager_get_url_rewrite(body)

Get Url Rewrite

Retrieve the details of a specific URL rewrite configuration.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_get_url_rewrite_request import UrlmanagerGetUrlRewriteRequest
from urlmanager.models.urlmanager_url_rewrite import UrlmanagerUrlRewrite
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerGetUrlRewriteRequest() # UrlmanagerGetUrlRewriteRequest | 

    try:
        # Get Url Rewrite
        api_response = api_instance.url_manager_get_url_rewrite(body)
        print("The response of BasicOperationsApi->url_manager_get_url_rewrite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_get_url_rewrite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerGetUrlRewriteRequest**](UrlmanagerGetUrlRewriteRequest.md)|  | 

### Return type

[**UrlmanagerUrlRewrite**](UrlmanagerUrlRewrite.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_get_url_rewrite2**
> UrlmanagerUrlRewrite url_manager_get_url_rewrite2(body)

Get Url Rewrite

Retrieve the details of a specific URL rewrite configuration.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_get_url_rewrite_request import UrlmanagerGetUrlRewriteRequest
from urlmanager.models.urlmanager_url_rewrite import UrlmanagerUrlRewrite
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerGetUrlRewriteRequest() # UrlmanagerGetUrlRewriteRequest | 

    try:
        # Get Url Rewrite
        api_response = api_instance.url_manager_get_url_rewrite2(body)
        print("The response of BasicOperationsApi->url_manager_get_url_rewrite2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_get_url_rewrite2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerGetUrlRewriteRequest**](UrlmanagerGetUrlRewriteRequest.md)|  | 

### Return type

[**UrlmanagerUrlRewrite**](UrlmanagerUrlRewrite.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_list_url_rewrites**
> UrlmanagerListUrlRewritesResponse url_manager_list_url_rewrites(body)

List Url Rewrites

Retrieve a list of all URL rewrite configurations in your application.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_list_url_rewrites_request import UrlmanagerListUrlRewritesRequest
from urlmanager.models.urlmanager_list_url_rewrites_response import UrlmanagerListUrlRewritesResponse
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerListUrlRewritesRequest() # UrlmanagerListUrlRewritesRequest | 

    try:
        # List Url Rewrites
        api_response = api_instance.url_manager_list_url_rewrites(body)
        print("The response of BasicOperationsApi->url_manager_list_url_rewrites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_list_url_rewrites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerListUrlRewritesRequest**](UrlmanagerListUrlRewritesRequest.md)|  | 

### Return type

[**UrlmanagerListUrlRewritesResponse**](UrlmanagerListUrlRewritesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_list_url_rewrites2**
> UrlmanagerListUrlRewritesResponse url_manager_list_url_rewrites2(body)

List Url Rewrites

Retrieve a list of all URL rewrite configurations in your application.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_list_url_rewrites_request import UrlmanagerListUrlRewritesRequest
from urlmanager.models.urlmanager_list_url_rewrites_response import UrlmanagerListUrlRewritesResponse
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerListUrlRewritesRequest() # UrlmanagerListUrlRewritesRequest | 

    try:
        # List Url Rewrites
        api_response = api_instance.url_manager_list_url_rewrites2(body)
        print("The response of BasicOperationsApi->url_manager_list_url_rewrites2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_list_url_rewrites2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerListUrlRewritesRequest**](UrlmanagerListUrlRewritesRequest.md)|  | 

### Return type

[**UrlmanagerListUrlRewritesResponse**](UrlmanagerListUrlRewritesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_list_url_rewrites_by_target_paths**
> UrlmanagerListUrlRewritesByTargetPathsRequest url_manager_list_url_rewrites_by_target_paths(body)

List Url Rewrites By Target Paths

Retrieve URL rewrite configurations based on target paths.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_list_url_rewrites_by_target_paths_request import UrlmanagerListUrlRewritesByTargetPathsRequest
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerListUrlRewritesByTargetPathsRequest() # UrlmanagerListUrlRewritesByTargetPathsRequest | 

    try:
        # List Url Rewrites By Target Paths
        api_response = api_instance.url_manager_list_url_rewrites_by_target_paths(body)
        print("The response of BasicOperationsApi->url_manager_list_url_rewrites_by_target_paths:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_list_url_rewrites_by_target_paths: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerListUrlRewritesByTargetPathsRequest**](UrlmanagerListUrlRewritesByTargetPathsRequest.md)|  | 

### Return type

[**UrlmanagerListUrlRewritesByTargetPathsRequest**](UrlmanagerListUrlRewritesByTargetPathsRequest.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_list_url_rewrites_by_target_paths2**
> UrlmanagerListUrlRewritesByTargetPathsRequest url_manager_list_url_rewrites_by_target_paths2(body)

List Url Rewrites By Target Paths

Retrieve URL rewrite configurations based on target paths.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_list_url_rewrites_by_target_paths_request import UrlmanagerListUrlRewritesByTargetPathsRequest
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerListUrlRewritesByTargetPathsRequest() # UrlmanagerListUrlRewritesByTargetPathsRequest | 

    try:
        # List Url Rewrites By Target Paths
        api_response = api_instance.url_manager_list_url_rewrites_by_target_paths2(body)
        print("The response of BasicOperationsApi->url_manager_list_url_rewrites_by_target_paths2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_list_url_rewrites_by_target_paths2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerListUrlRewritesByTargetPathsRequest**](UrlmanagerListUrlRewritesByTargetPathsRequest.md)|  | 

### Return type

[**UrlmanagerListUrlRewritesByTargetPathsRequest**](UrlmanagerListUrlRewritesByTargetPathsRequest.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_resolve_url_rewrite**
> UrlmanagerUrlRewrite url_manager_resolve_url_rewrite(body)

Resolve Url Rewrite

Resolve and retrieve the rewritten URL for a given input URL.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_resolve_url_rewrite_request import UrlmanagerResolveUrlRewriteRequest
from urlmanager.models.urlmanager_url_rewrite import UrlmanagerUrlRewrite
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerResolveUrlRewriteRequest() # UrlmanagerResolveUrlRewriteRequest | 

    try:
        # Resolve Url Rewrite
        api_response = api_instance.url_manager_resolve_url_rewrite(body)
        print("The response of BasicOperationsApi->url_manager_resolve_url_rewrite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_resolve_url_rewrite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerResolveUrlRewriteRequest**](UrlmanagerResolveUrlRewriteRequest.md)|  | 

### Return type

[**UrlmanagerUrlRewrite**](UrlmanagerUrlRewrite.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **url_manager_resolve_url_rewrite2**
> UrlmanagerUrlRewrite url_manager_resolve_url_rewrite2(body)

Resolve Url Rewrite

Resolve and retrieve the rewritten URL for a given input URL.

### Example

* Api Key Authentication (Authorization):

```python
import urlmanager
from urlmanager.models.urlmanager_resolve_url_rewrite_request import UrlmanagerResolveUrlRewriteRequest
from urlmanager.models.urlmanager_url_rewrite import UrlmanagerUrlRewrite
from urlmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://urlmanager.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = urlmanager.Configuration(
    host = "https://urlmanager.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with urlmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urlmanager.BasicOperationsApi(api_client)
    body = urlmanager.UrlmanagerResolveUrlRewriteRequest() # UrlmanagerResolveUrlRewriteRequest | 

    try:
        # Resolve Url Rewrite
        api_response = api_instance.url_manager_resolve_url_rewrite2(body)
        print("The response of BasicOperationsApi->url_manager_resolve_url_rewrite2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->url_manager_resolve_url_rewrite2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlmanagerResolveUrlRewriteRequest**](UrlmanagerResolveUrlRewriteRequest.md)|  | 

### Return type

[**UrlmanagerUrlRewrite**](UrlmanagerUrlRewrite.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

