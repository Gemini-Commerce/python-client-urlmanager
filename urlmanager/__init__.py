# coding: utf-8

# flake8: noqa

"""
    Url Manager Service

    The URL Manager service provides a set of APIs for managing URL rewrites within your application. URL rewriting is a technique used to modify the appearance or structure of URLs while maintaining the functionality and accessibility of the underlying resources.  The URL Manager service offers various operations to create, retrieve, update, and delete URL rewrite configurations. These configurations allow you to define rules that map incoming URLs to different paths or destinations based on specific criteria. By using URL rewriting, you can enhance the user experience, improve SEO (Search Engine Optimization), and manage complex URL structures effectively.  To get started with the URL Manager service, you need to integrate the provided Proto API into your application. The API supports various programming languages and frameworks, making it easy to incorporate URL rewriting functionality into your existing codebase.  Once integrated, you can utilize the different API methods to create, manage, and query URL rewrite configurations based on your application's requirements.  Refer to the API documentation for detailed information on the request and response formats, authentication requirements, and example usage of each API method.

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.2.0"

# import apis into sdk package
from urlmanager.api.basic_operations_api import BasicOperationsApi

# import ApiClient
from urlmanager.api_response import ApiResponse
from urlmanager.api_client import ApiClient
from urlmanager.configuration import Configuration
from urlmanager.exceptions import OpenApiException
from urlmanager.exceptions import ApiTypeError
from urlmanager.exceptions import ApiValueError
from urlmanager.exceptions import ApiKeyError
from urlmanager.exceptions import ApiAttributeError
from urlmanager.exceptions import ApiException

# import models into sdk package
from urlmanager.models.get_url_rewrite_request_compound_identifier import GetUrlRewriteRequestCompoundIdentifier
from urlmanager.models.list_url_rewrites_request_filter import ListUrlRewritesRequestFilter
from urlmanager.models.protobuf_any import ProtobufAny
from urlmanager.models.rpc_status import RpcStatus
from urlmanager.models.url_rewrite_link_rel import UrlRewriteLinkRel
from urlmanager.models.url_rewrite_redirect_type import UrlRewriteRedirectType
from urlmanager.models.urlmanager_change_url_rewrite_request_path_request import UrlmanagerChangeUrlRewriteRequestPathRequest
from urlmanager.models.urlmanager_create_url_rewrite_request import UrlmanagerCreateUrlRewriteRequest
from urlmanager.models.urlmanager_delete_url_rewrite_request import UrlmanagerDeleteUrlRewriteRequest
from urlmanager.models.urlmanager_get_url_rewrite_request import UrlmanagerGetUrlRewriteRequest
from urlmanager.models.urlmanager_list_url_rewrites_by_target_paths_request import UrlmanagerListUrlRewritesByTargetPathsRequest
from urlmanager.models.urlmanager_list_url_rewrites_by_target_paths_response import UrlmanagerListUrlRewritesByTargetPathsResponse
from urlmanager.models.urlmanager_list_url_rewrites_request import UrlmanagerListUrlRewritesRequest
from urlmanager.models.urlmanager_list_url_rewrites_response import UrlmanagerListUrlRewritesResponse
from urlmanager.models.urlmanager_resolve_url_rewrite_request import UrlmanagerResolveUrlRewriteRequest
from urlmanager.models.urlmanager_url_rewrite import UrlmanagerUrlRewrite
