# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 22
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk.configuration import Configuration


class IdResolutionDomainsPath(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'domain': 'str',
        'path': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'path': 'path'
    }

    def __init__(self, domain=None, path=None, _configuration=None):  # noqa: E501
        """IdResolutionDomainsPath - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain = None
        self._path = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if path is not None:
            self.path = path

    @property
    def domain(self):
        """Gets the domain of this IdResolutionDomainsPath.  # noqa: E501

        Domain ID. The domain ID assigned to a directory.  # noqa: E501

        :return: The domain of this IdResolutionDomainsPath.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this IdResolutionDomainsPath.

        Domain ID. The domain ID assigned to a directory.  # noqa: E501

        :param domain: The domain of this IdResolutionDomainsPath.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                domain is not None and len(domain) > 255):
            raise ValueError("Invalid value for `domain`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                domain is not None and len(domain) < 0):
            raise ValueError("Invalid value for `domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._domain = domain

    @property
    def path(self):
        """Gets the path of this IdResolutionDomainsPath.  # noqa: E501

        The full path associated with the domain id. null if the domain id cannot be resolved to a path.  # noqa: E501

        :return: The path of this IdResolutionDomainsPath.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this IdResolutionDomainsPath.

        The full path associated with the domain id. null if the domain id cannot be resolved to a path.  # noqa: E501

        :param path: The path of this IdResolutionDomainsPath.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                path is not None and len(path) > 4096):
            raise ValueError("Invalid value for `path`, length must be less than or equal to `4096`")  # noqa: E501
        if (self._configuration.client_side_validation and
                path is not None and len(path) < 0):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `0`")  # noqa: E501

        self._path = path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IdResolutionDomainsPath, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IdResolutionDomainsPath):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdResolutionDomainsPath):
            return True

        return self.to_dict() != other.to_dict()
