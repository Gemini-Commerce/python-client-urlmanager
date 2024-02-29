# coding: utf-8

"""
    Url Manager Service

    The URL Manager service provides a set of APIs for managing URL rewrites within your application. URL rewriting is a technique used to modify the appearance or structure of URLs while maintaining the functionality and accessibility of the underlying resources.  The URL Manager service offers various operations to create, retrieve, update, and delete URL rewrite configurations. These configurations allow you to define rules that map incoming URLs to different paths or destinations based on specific criteria. By using URL rewriting, you can enhance the user experience, improve SEO (Search Engine Optimization), and manage complex URL structures effectively.  To get started with the URL Manager service, you need to integrate the provided Proto API into your application. The API supports various programming languages and frameworks, making it easy to incorporate URL rewriting functionality into your existing codebase.  Once integrated, you can utilize the different API methods to create, manage, and query URL rewrite configurations based on your application's requirements.  Refer to the API documentation for detailed information on the request and response formats, authentication requirements, and example usage of each API method.

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from urlmanager.models.urlmanager_list_url_rewrites_request import UrlmanagerListUrlRewritesRequest

class TestUrlmanagerListUrlRewritesRequest(unittest.TestCase):
    """UrlmanagerListUrlRewritesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UrlmanagerListUrlRewritesRequest:
        """Test UrlmanagerListUrlRewritesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UrlmanagerListUrlRewritesRequest`
        """
        model = UrlmanagerListUrlRewritesRequest()
        if include_optional:
            return UrlmanagerListUrlRewritesRequest(
                tenant_id = '',
                filter = urlmanager.models.list_url_rewrites_request_filter.ListUrlRewritesRequestFilter(
                    context = '', 
                    request_path = '', 
                    target_path = '', 
                    redirect_type = 'RedirectType_UNKNOWN', ),
                page_size = 56,
                page_token = ''
            )
        else:
            return UrlmanagerListUrlRewritesRequest(
        )
        """

    def testUrlmanagerListUrlRewritesRequest(self):
        """Test UrlmanagerListUrlRewritesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
