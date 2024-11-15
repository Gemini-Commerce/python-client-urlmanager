# coding: utf-8

"""
    Url Manager Service

    The URL Manager service provides a set of APIs for managing URL rewrites within your application. URL rewriting is a technique used to modify the appearance or structure of URLs while maintaining the functionality and accessibility of the underlying resources.  The URL Manager service offers various operations to create, retrieve, update, and delete URL rewrite configurations. These configurations allow you to define rules that map incoming URLs to different paths or destinations based on specific criteria. By using URL rewriting, you can enhance the user experience, improve SEO (Search Engine Optimization), and manage complex URL structures effectively.  To get started with the URL Manager service, you need to integrate the provided Proto API into your application. The API supports various programming languages and frameworks, making it easy to incorporate URL rewriting functionality into your existing codebase.  Once integrated, you can utilize the different API methods to create, manage, and query URL rewrite configurations based on your application's requirements.  Refer to the API documentation for detailed information on the request and response formats, authentication requirements, and example usage of each API method.

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UrlRewriteLinkRel(str, Enum):
    """
    UrlRewriteLinkRel
    """

    """
    allowed enum values
    """
    LINK_REL_UNKNOWN = 'LinkRel_UNKNOWN'
    LINK_REL_NONE = 'LinkRel_NONE'
    LINK_REL_CANONICAL = 'LinkRel_CANONICAL'
    LINK_REL_ALTERNATE = 'LinkRel_ALTERNATE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UrlRewriteLinkRel from a JSON string"""
        return cls(json.loads(json_str))


