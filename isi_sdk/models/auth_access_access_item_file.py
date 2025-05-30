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


class AuthAccessAccessItemFile(object):
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
        'effective_path': 'str',
        'file_permissions': 'AuthAccessAccessItemFileFilePermissions',
        'group': 'AuthAccessAccessItemFileGroup',
        'is_snapshot': 'bool',
        'owner': 'AuthAccessAccessItemFileGroup'
    }

    attribute_map = {
        'effective_path': 'effective_path',
        'file_permissions': 'file_permissions',
        'group': 'group',
        'is_snapshot': 'is_snapshot',
        'owner': 'owner'
    }

    def __init__(self, effective_path=None, file_permissions=None, group=None, is_snapshot=None, owner=None, _configuration=None):  # noqa: E501
        """AuthAccessAccessItemFile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._effective_path = None
        self._file_permissions = None
        self._group = None
        self._is_snapshot = None
        self._owner = None
        self.discriminator = None

        if effective_path is not None:
            self.effective_path = effective_path
        if file_permissions is not None:
            self.file_permissions = file_permissions
        if group is not None:
            self.group = group
        if is_snapshot is not None:
            self.is_snapshot = is_snapshot
        if owner is not None:
            self.owner = owner

    @property
    def effective_path(self):
        """Gets the effective_path of this AuthAccessAccessItemFile.  # noqa: E501

        Specifies absolute path in filesystem.  # noqa: E501

        :return: The effective_path of this AuthAccessAccessItemFile.  # noqa: E501
        :rtype: str
        """
        return self._effective_path

    @effective_path.setter
    def effective_path(self, effective_path):
        """Sets the effective_path of this AuthAccessAccessItemFile.

        Specifies absolute path in filesystem.  # noqa: E501

        :param effective_path: The effective_path of this AuthAccessAccessItemFile.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                effective_path is not None and len(effective_path) > 4096):
            raise ValueError("Invalid value for `effective_path`, length must be less than or equal to `4096`")  # noqa: E501
        if (self._configuration.client_side_validation and
                effective_path is not None and len(effective_path) < 0):
            raise ValueError("Invalid value for `effective_path`, length must be greater than or equal to `0`")  # noqa: E501

        self._effective_path = effective_path

    @property
    def file_permissions(self):
        """Gets the file_permissions of this AuthAccessAccessItemFile.  # noqa: E501

        Specifies the permissions that the user has on the file.  # noqa: E501

        :return: The file_permissions of this AuthAccessAccessItemFile.  # noqa: E501
        :rtype: AuthAccessAccessItemFileFilePermissions
        """
        return self._file_permissions

    @file_permissions.setter
    def file_permissions(self, file_permissions):
        """Sets the file_permissions of this AuthAccessAccessItemFile.

        Specifies the permissions that the user has on the file.  # noqa: E501

        :param file_permissions: The file_permissions of this AuthAccessAccessItemFile.  # noqa: E501
        :type: AuthAccessAccessItemFileFilePermissions
        """

        self._file_permissions = file_permissions

    @property
    def group(self):
        """Gets the group of this AuthAccessAccessItemFile.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The group of this AuthAccessAccessItemFile.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AuthAccessAccessItemFile.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param group: The group of this AuthAccessAccessItemFile.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._group = group

    @property
    def is_snapshot(self):
        """Gets the is_snapshot of this AuthAccessAccessItemFile.  # noqa: E501

        Specifies whether path is inside snapshot.  # noqa: E501

        :return: The is_snapshot of this AuthAccessAccessItemFile.  # noqa: E501
        :rtype: bool
        """
        return self._is_snapshot

    @is_snapshot.setter
    def is_snapshot(self, is_snapshot):
        """Sets the is_snapshot of this AuthAccessAccessItemFile.

        Specifies whether path is inside snapshot.  # noqa: E501

        :param is_snapshot: The is_snapshot of this AuthAccessAccessItemFile.  # noqa: E501
        :type: bool
        """

        self._is_snapshot = is_snapshot

    @property
    def owner(self):
        """Gets the owner of this AuthAccessAccessItemFile.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The owner of this AuthAccessAccessItemFile.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this AuthAccessAccessItemFile.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param owner: The owner of this AuthAccessAccessItemFile.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._owner = owner

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
        if issubclass(AuthAccessAccessItemFile, dict):
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
        if not isinstance(other, AuthAccessAccessItemFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthAccessAccessItemFile):
            return True

        return self.to_dict() != other.to_dict()
