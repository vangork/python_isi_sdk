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


class SmbSharePermission(object):
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
        'permission': 'str',
        'permission_type': 'str',
        'trustee': 'AuthAccessAccessItemFileGroup'
    }

    attribute_map = {
        'permission': 'permission',
        'permission_type': 'permission_type',
        'trustee': 'trustee'
    }

    def __init__(self, permission=None, permission_type=None, trustee=None, _configuration=None):  # noqa: E501
        """SmbSharePermission - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._permission = None
        self._permission_type = None
        self._trustee = None
        self.discriminator = None

        self.permission = permission
        self.permission_type = permission_type
        self.trustee = trustee

    @property
    def permission(self):
        """Gets the permission of this SmbSharePermission.  # noqa: E501

        Specifies the file system rights that are allowed or denied.  # noqa: E501

        :return: The permission of this SmbSharePermission.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this SmbSharePermission.

        Specifies the file system rights that are allowed or denied.  # noqa: E501

        :param permission: The permission of this SmbSharePermission.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and permission is None:
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501
        allowed_values = ["full", "change", "read"]  # noqa: E501
        if (self._configuration.client_side_validation and
                permission not in allowed_values):
            raise ValueError(
                "Invalid value for `permission` ({0}), must be one of {1}"  # noqa: E501
                .format(permission, allowed_values)
            )

        self._permission = permission

    @property
    def permission_type(self):
        """Gets the permission_type of this SmbSharePermission.  # noqa: E501

        Determines whether the permission is allowed or denied.  # noqa: E501

        :return: The permission_type of this SmbSharePermission.  # noqa: E501
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this SmbSharePermission.

        Determines whether the permission is allowed or denied.  # noqa: E501

        :param permission_type: The permission_type of this SmbSharePermission.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and permission_type is None:
            raise ValueError("Invalid value for `permission_type`, must not be `None`")  # noqa: E501
        allowed_values = ["allow", "deny"]  # noqa: E501
        if (self._configuration.client_side_validation and
                permission_type not in allowed_values):
            raise ValueError(
                "Invalid value for `permission_type` ({0}), must be one of {1}"  # noqa: E501
                .format(permission_type, allowed_values)
            )

        self._permission_type = permission_type

    @property
    def trustee(self):
        """Gets the trustee of this SmbSharePermission.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The trustee of this SmbSharePermission.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._trustee

    @trustee.setter
    def trustee(self, trustee):
        """Sets the trustee of this SmbSharePermission.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param trustee: The trustee of this SmbSharePermission.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """
        if self._configuration.client_side_validation and trustee is None:
            raise ValueError("Invalid value for `trustee`, must not be `None`")  # noqa: E501

        self._trustee = trustee

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
        if issubclass(SmbSharePermission, dict):
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
        if not isinstance(other, SmbSharePermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmbSharePermission):
            return True

        return self.to_dict() != other.to_dict()
