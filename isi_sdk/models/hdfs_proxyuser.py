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


class HdfsProxyuser(object):
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
        'id': 'str',
        'members': 'list[AuthAccessAccessItemFileGroup]',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'members': 'members',
        'name': 'name'
    }

    def __init__(self, id=None, members=None, name=None, _configuration=None):  # noqa: E501
        """HdfsProxyuser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._members = None
        self._name = None
        self.discriminator = None

        self.id = id
        self.members = members
        self.name = name

    @property
    def id(self):
        """Gets the id of this HdfsProxyuser.  # noqa: E501

        The ID of the role.  # noqa: E501

        :return: The id of this HdfsProxyuser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HdfsProxyuser.

        The ID of the role.  # noqa: E501

        :param id: The id of this HdfsProxyuser.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def members(self):
        """Gets the members of this HdfsProxyuser.  # noqa: E501

        Users or groups impersonated by proxyuser.  # noqa: E501

        :return: The members of this HdfsProxyuser.  # noqa: E501
        :rtype: list[AuthAccessAccessItemFileGroup]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this HdfsProxyuser.

        Users or groups impersonated by proxyuser.  # noqa: E501

        :param members: The members of this HdfsProxyuser.  # noqa: E501
        :type: list[AuthAccessAccessItemFileGroup]
        """
        if self._configuration.client_side_validation and members is None:
            raise ValueError("Invalid value for `members`, must not be `None`")  # noqa: E501

        self._members = members

    @property
    def name(self):
        """Gets the name of this HdfsProxyuser.  # noqa: E501

        The name of the proxyuser.  # noqa: E501

        :return: The name of this HdfsProxyuser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HdfsProxyuser.

        The name of the proxyuser.  # noqa: E501

        :param name: The name of this HdfsProxyuser.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(HdfsProxyuser, dict):
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
        if not isinstance(other, HdfsProxyuser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HdfsProxyuser):
            return True

        return self.to_dict() != other.to_dict()
