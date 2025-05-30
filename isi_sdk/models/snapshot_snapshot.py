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


class SnapshotSnapshot(object):
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
        'alias': 'str',
        'expires': 'int',
        'name': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'expires': 'expires',
        'name': 'name'
    }

    def __init__(self, alias=None, expires=None, name=None, _configuration=None):  # noqa: E501
        """SnapshotSnapshot - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alias = None
        self._expires = None
        self._name = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if expires is not None:
            self.expires = expires
        if name is not None:
            self.name = name

    @property
    def alias(self):
        """Gets the alias of this SnapshotSnapshot.  # noqa: E501

        Alias name to create for this snapshot. If null, remove any alias.  # noqa: E501

        :return: The alias of this SnapshotSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this SnapshotSnapshot.

        Alias name to create for this snapshot. If null, remove any alias.  # noqa: E501

        :param alias: The alias of this SnapshotSnapshot.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                alias is not None and len(alias) < 0):
            raise ValueError("Invalid value for `alias`, length must be greater than or equal to `0`")  # noqa: E501

        self._alias = alias

    @property
    def expires(self):
        """Gets the expires of this SnapshotSnapshot.  # noqa: E501

        The Unix Epoch time the snapshot will expire and be eligible for automatic deletion.  # noqa: E501

        :return: The expires of this SnapshotSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this SnapshotSnapshot.

        The Unix Epoch time the snapshot will expire and be eligible for automatic deletion.  # noqa: E501

        :param expires: The expires of this SnapshotSnapshot.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                expires is not None and expires > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `expires`, must be a value less than or equal to `4294967295`")  # noqa: E501

        self._expires = expires

    @property
    def name(self):
        """Gets the name of this SnapshotSnapshot.  # noqa: E501

        The user or system supplied snapshot name. This will be null for snapshots pending delete.  # noqa: E501

        :return: The name of this SnapshotSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotSnapshot.

        The user or system supplied snapshot name. This will be null for snapshots pending delete.  # noqa: E501

        :param name: The name of this SnapshotSnapshot.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

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
        if issubclass(SnapshotSnapshot, dict):
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
        if not isinstance(other, SnapshotSnapshot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotSnapshot):
            return True

        return self.to_dict() != other.to_dict()
