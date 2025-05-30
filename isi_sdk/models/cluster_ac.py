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


class ClusterAc(object):
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
        'exclude_sn': 'list[str]',
        'include_sn': 'list[str]'
    }

    attribute_map = {
        'exclude_sn': 'exclude_sn',
        'include_sn': 'include_sn'
    }

    def __init__(self, exclude_sn=None, include_sn=None, _configuration=None):  # noqa: E501
        """ClusterAc - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._exclude_sn = None
        self._include_sn = None
        self.discriminator = None

        if exclude_sn is not None:
            self.exclude_sn = exclude_sn
        if include_sn is not None:
            self.include_sn = include_sn

    @property
    def exclude_sn(self):
        """Gets the exclude_sn of this ClusterAc.  # noqa: E501

        List of the node serial number.  # noqa: E501

        :return: The exclude_sn of this ClusterAc.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_sn

    @exclude_sn.setter
    def exclude_sn(self, exclude_sn):
        """Sets the exclude_sn of this ClusterAc.

        List of the node serial number.  # noqa: E501

        :param exclude_sn: The exclude_sn of this ClusterAc.  # noqa: E501
        :type: list[str]
        """

        self._exclude_sn = exclude_sn

    @property
    def include_sn(self):
        """Gets the include_sn of this ClusterAc.  # noqa: E501

        List of the node serial number.  # noqa: E501

        :return: The include_sn of this ClusterAc.  # noqa: E501
        :rtype: list[str]
        """
        return self._include_sn

    @include_sn.setter
    def include_sn(self, include_sn):
        """Sets the include_sn of this ClusterAc.

        List of the node serial number.  # noqa: E501

        :param include_sn: The include_sn of this ClusterAc.  # noqa: E501
        :type: list[str]
        """

        self._include_sn = include_sn

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
        if issubclass(ClusterAc, dict):
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
        if not isinstance(other, ClusterAc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterAc):
            return True

        return self.to_dict() != other.to_dict()
