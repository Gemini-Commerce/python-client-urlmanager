# coding: utf-8

"""
    Url Manager Service

    The URL Manager service provides a set of APIs for managing URL rewrites within your application. URL rewriting is a technique used to modify the appearance or structure of URLs while maintaining the functionality and accessibility of the underlying resources.  The URL Manager service offers various operations to create, retrieve, update, and delete URL rewrite configurations. These configurations allow you to define rules that map incoming URLs to different paths or destinations based on specific criteria. By using URL rewriting, you can enhance the user experience, improve SEO (Search Engine Optimization), and manage complex URL structures effectively.  To get started with the URL Manager service, you need to integrate the provided Proto API into your application. The API supports various programming languages and frameworks, making it easy to incorporate URL rewriting functionality into your existing codebase.  Once integrated, you can utilize the different API methods to create, manage, and query URL rewrite configurations based on your application's requirements.  Refer to the API documentation for detailed information on the request and response formats, authentication requirements, and example usage of each API method.

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from typing import Any, Optional

from typing_extensions import Self

class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None,
                 key_type=None) -> None:
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiAttributeError(OpenApiException, AttributeError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Raised when an attribute reference or assignment fails.

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiAttributeError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(OpenApiException):

    def __init__(
        self, 
        status=None, 
        reason=None, 
        http_resp=None,
        *,
        body: Optional[str] = None,
        data: Optional[Any] = None,
    ) -> None:
        self.status = status
        self.reason = reason
        self.body = body
        self.data = data
        self.headers = None

        if http_resp:
            if self.status is None:
                self.status = http_resp.status
            if self.reason is None:
                self.reason = http_resp.reason
            if self.body is None:
                try:
                    self.body = http_resp.data.decode('utf-8')
                except Exception:
                    pass
            self.headers = http_resp.getheaders()

    @classmethod
    def from_response(
        cls, 
        *, 
        http_resp, 
        body: Optional[str], 
        data: Optional[Any],
    ) -> Self:
        if http_resp.status == 400:
            raise BadRequestException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 401:
            raise UnauthorizedException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 403:
            raise ForbiddenException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 404:
            raise NotFoundException(http_resp=http_resp, body=body, data=data)

        if 500 <= http_resp.status <= 599:
            raise ServiceException(http_resp=http_resp, body=body, data=data)
        raise ApiException(http_resp=http_resp, body=body, data=data)

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.data or self.body:
            error_message += "HTTP response body: {0}\n".format(self.data or self.body)

        return error_message


class BadRequestException(ApiException):
    pass


class NotFoundException(ApiException):
    pass


class UnauthorizedException(ApiException):
    pass


class ForbiddenException(ApiException):
    pass


class ServiceException(ApiException):
    pass


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
