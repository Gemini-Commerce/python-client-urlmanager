# urlmanager_client
The URL Manager service provides a set of APIs for managing URL rewrites within your application. URL rewriting is a technique used to modify the appearance or structure of URLs while maintaining the functionality and accessibility of the underlying resources.

The URL Manager service offers various operations to create, retrieve, update, and delete URL rewrite configurations. These configurations allow you to define rules that map incoming URLs to different paths or destinations based on specific criteria. By using URL rewriting, you can enhance the user experience, improve SEO (Search Engine Optimization), and manage complex URL structures effectively.

To get started with the URL Manager service, you need to integrate the provided Proto API into your application. The API supports various programming languages and frameworks, making it easy to incorporate URL rewriting functionality into your existing codebase.

Once integrated, you can utilize the different API methods to create, manage, and query URL rewrite configurations based on your application's requirements.

Refer to the API documentation for detailed information on the request and response formats, authentication requirements, and example usage of each API method.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.2.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Gemini-Commerce/python-client-urlmanager.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Gemini-Commerce/python-client-urlmanager.git`)

Then import the package:
```python
import urlmanager
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import urlmanager
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import urlmanager
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
    except ApiException as e:
        print("Exception when calling BasicOperationsApi->url_manager_change_url_rewrite_request_path: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://urlmanager.api.gogemini.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BasicOperationsApi* | [**url_manager_change_url_rewrite_request_path**](docs/BasicOperationsApi.md#url_manager_change_url_rewrite_request_path) | **POST** /urlmanager/change_url_rewrite_request_path | Change Url Rewrite Request Path
*BasicOperationsApi* | [**url_manager_change_url_rewrite_request_path2**](docs/BasicOperationsApi.md#url_manager_change_url_rewrite_request_path2) | **POST** /urlmanager.UrlManager/ChangeUrlRewriteRequestPath | Change Url Rewrite Request Path
*BasicOperationsApi* | [**url_manager_create_url_rewrite**](docs/BasicOperationsApi.md#url_manager_create_url_rewrite) | **POST** /urlmanager/create_url_rewrite | Create Url Rewrite
*BasicOperationsApi* | [**url_manager_create_url_rewrite2**](docs/BasicOperationsApi.md#url_manager_create_url_rewrite2) | **POST** /urlmanager.UrlManager/CreateUrlRewrite | Create Url Rewrite
*BasicOperationsApi* | [**url_manager_delete_url_rewrite**](docs/BasicOperationsApi.md#url_manager_delete_url_rewrite) | **POST** /urlmanager/delete_url_rewrite | Delete Url Rewrite
*BasicOperationsApi* | [**url_manager_delete_url_rewrite2**](docs/BasicOperationsApi.md#url_manager_delete_url_rewrite2) | **POST** /urlmanager.UrlManager/DeleteUrlRewrite | Delete Url Rewrite
*BasicOperationsApi* | [**url_manager_get_url_rewrite**](docs/BasicOperationsApi.md#url_manager_get_url_rewrite) | **POST** /urlmanager/get_url_rewrite | Get Url Rewrite
*BasicOperationsApi* | [**url_manager_get_url_rewrite2**](docs/BasicOperationsApi.md#url_manager_get_url_rewrite2) | **POST** /urlmanager.UrlManager/GetUrlRewrite | Get Url Rewrite
*BasicOperationsApi* | [**url_manager_list_url_rewrites**](docs/BasicOperationsApi.md#url_manager_list_url_rewrites) | **POST** /urlmanager/list_url_rewrites | List Url Rewrites
*BasicOperationsApi* | [**url_manager_list_url_rewrites2**](docs/BasicOperationsApi.md#url_manager_list_url_rewrites2) | **POST** /urlmanager.UrlManager/ListUrlRewrites | List Url Rewrites
*BasicOperationsApi* | [**url_manager_list_url_rewrites_by_target_paths**](docs/BasicOperationsApi.md#url_manager_list_url_rewrites_by_target_paths) | **POST** /urlmanager/list_url_rewrites_by_target_paths | List Url Rewrites By Target Paths
*BasicOperationsApi* | [**url_manager_list_url_rewrites_by_target_paths2**](docs/BasicOperationsApi.md#url_manager_list_url_rewrites_by_target_paths2) | **POST** /urlmanager.UrlManager/ListUrlRewritesByTargetPaths | List Url Rewrites By Target Paths
*BasicOperationsApi* | [**url_manager_resolve_url_rewrite**](docs/BasicOperationsApi.md#url_manager_resolve_url_rewrite) | **POST** /urlmanager/resolve_url_rewrite | Resolve Url Rewrite
*BasicOperationsApi* | [**url_manager_resolve_url_rewrite2**](docs/BasicOperationsApi.md#url_manager_resolve_url_rewrite2) | **POST** /urlmanager.UrlManager/ResolveUrlRewrite | Resolve Url Rewrite


## Documentation For Models

 - [GetUrlRewriteRequestCompoundIdentifier](docs/GetUrlRewriteRequestCompoundIdentifier.md)
 - [ListUrlRewritesRequestFilter](docs/ListUrlRewritesRequestFilter.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [UrlRewriteLinkRel](docs/UrlRewriteLinkRel.md)
 - [UrlRewriteRedirectType](docs/UrlRewriteRedirectType.md)
 - [UrlmanagerChangeUrlRewriteRequestPathRequest](docs/UrlmanagerChangeUrlRewriteRequestPathRequest.md)
 - [UrlmanagerCreateUrlRewriteRequest](docs/UrlmanagerCreateUrlRewriteRequest.md)
 - [UrlmanagerDeleteUrlRewriteRequest](docs/UrlmanagerDeleteUrlRewriteRequest.md)
 - [UrlmanagerGetUrlRewriteRequest](docs/UrlmanagerGetUrlRewriteRequest.md)
 - [UrlmanagerListUrlRewritesByTargetPathsRequest](docs/UrlmanagerListUrlRewritesByTargetPathsRequest.md)
 - [UrlmanagerListUrlRewritesByTargetPathsResponse](docs/UrlmanagerListUrlRewritesByTargetPathsResponse.md)
 - [UrlmanagerListUrlRewritesRequest](docs/UrlmanagerListUrlRewritesRequest.md)
 - [UrlmanagerListUrlRewritesResponse](docs/UrlmanagerListUrlRewritesResponse.md)
 - [UrlmanagerResolveUrlRewriteRequest](docs/UrlmanagerResolveUrlRewriteRequest.md)
 - [UrlmanagerUrlRewrite](docs/UrlmanagerUrlRewrite.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="standardAuthorization"></a>
### standardAuthorization

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A


## Author

info@gemini-commerce.com


