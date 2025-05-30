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


class SettingsMappingMappingSettings(object):
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
        'cache_entry_expiry': 'int',
        'gid_range_enabled': 'bool',
        'gid_range_max': 'int',
        'gid_range_min': 'int',
        'gid_range_next': 'int',
        'uid_range_enabled': 'bool',
        'uid_range_max': 'int',
        'uid_range_min': 'int',
        'uid_range_next': 'int'
    }

    attribute_map = {
        'cache_entry_expiry': 'cache_entry_expiry',
        'gid_range_enabled': 'gid_range_enabled',
        'gid_range_max': 'gid_range_max',
        'gid_range_min': 'gid_range_min',
        'gid_range_next': 'gid_range_next',
        'uid_range_enabled': 'uid_range_enabled',
        'uid_range_max': 'uid_range_max',
        'uid_range_min': 'uid_range_min',
        'uid_range_next': 'uid_range_next'
    }

    def __init__(self, cache_entry_expiry=None, gid_range_enabled=None, gid_range_max=None, gid_range_min=None, gid_range_next=None, uid_range_enabled=None, uid_range_max=None, uid_range_min=None, uid_range_next=None, _configuration=None):  # noqa: E501
        """SettingsMappingMappingSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cache_entry_expiry = None
        self._gid_range_enabled = None
        self._gid_range_max = None
        self._gid_range_min = None
        self._gid_range_next = None
        self._uid_range_enabled = None
        self._uid_range_max = None
        self._uid_range_min = None
        self._uid_range_next = None
        self.discriminator = None

        if cache_entry_expiry is not None:
            self.cache_entry_expiry = cache_entry_expiry
        if gid_range_enabled is not None:
            self.gid_range_enabled = gid_range_enabled
        if gid_range_max is not None:
            self.gid_range_max = gid_range_max
        if gid_range_min is not None:
            self.gid_range_min = gid_range_min
        if gid_range_next is not None:
            self.gid_range_next = gid_range_next
        if uid_range_enabled is not None:
            self.uid_range_enabled = uid_range_enabled
        if uid_range_max is not None:
            self.uid_range_max = uid_range_max
        if uid_range_min is not None:
            self.uid_range_min = uid_range_min
        if uid_range_next is not None:
            self.uid_range_next = uid_range_next

    @property
    def cache_entry_expiry(self):
        """Gets the cache_entry_expiry of this SettingsMappingMappingSettings.  # noqa: E501

        Specifies the cache expiry in seconds of the idmapper.  # noqa: E501

        :return: The cache_entry_expiry of this SettingsMappingMappingSettings.  # noqa: E501
        :rtype: int
        """
        return self._cache_entry_expiry

    @cache_entry_expiry.setter
    def cache_entry_expiry(self, cache_entry_expiry):
        """Sets the cache_entry_expiry of this SettingsMappingMappingSettings.

        Specifies the cache expiry in seconds of the idmapper.  # noqa: E501

        :param cache_entry_expiry: The cache_entry_expiry of this SettingsMappingMappingSettings.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                cache_entry_expiry is not None and cache_entry_expiry > 15552000):  # noqa: E501
            raise ValueError("Invalid value for `cache_entry_expiry`, must be a value less than or equal to `15552000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                cache_entry_expiry is not None and cache_entry_expiry < 0):  # noqa: E501
            raise ValueError("Invalid value for `cache_entry_expiry`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cache_entry_expiry = cache_entry_expiry

    @property
    def gid_range_enabled(self):
        """Gets the gid_range_enabled of this SettingsMappingMappingSettings.  # noqa: E501

        If true, allocates GIDs from a fixed range.  # noqa: E501

        :return: The gid_range_enabled of this SettingsMappingMappingSettings.  # noqa: E501
        :rtype: bool
        """
        return self._gid_range_enabled

    @gid_range_enabled.setter
    def gid_range_enabled(self, gid_range_enabled):
        """Sets the gid_range_enabled of this SettingsMappingMappingSettings.

        If true, allocates GIDs from a fixed range.  # noqa: E501

        :param gid_range_enabled: The gid_range_enabled of this SettingsMappingMappingSettings.  # noqa: E501
        :type: bool
        """

        self._gid_range_enabled = gid_range_enabled

    @property
    def gid_range_max(self):
        """Gets the gid_range_max of this SettingsMappingMappingSettings.  # noqa: E501

        Specifies the ending number for a fixed range from which GIDs are allocated.  # noqa: E501

        :return: The gid_range_max of this SettingsMappingMappingSettings.  # noqa: E501
        :rtype: int
        """
        return self._gid_range_max

    @gid_range_max.setter
    def gid_range_max(self, gid_range_max):
        """Sets the gid_range_max of this SettingsMappingMappingSettings.

        Specifies the ending number for a fixed range from which GIDs are allocated.  # noqa: E501

        :param gid_range_max: The gid_range_max of this SettingsMappingMappingSettings.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                gid_range_max is not None and gid_range_max > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `gid_range_max`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self._configuration.client_side_validation and
                gid_range_max is not None and gid_range_max < 0):  # noqa: E501
            raise ValueError("Invalid value for `gid_range_max`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gid_range_max = gid_range_max

    @property
    def gid_range_min(self):
        """Gets the gid_range_min of this SettingsMappingMappingSettings.  # noqa: E501

        Specifies the starting number for a fixed range from which GIDs are allocated.  # noqa: E501

        :return: The gid_range_min of this SettingsMappingMappingSettings.  # noqa: E501
        :rtype: int
        """
        return self._gid_range_min

    @gid_range_min.setter
    def gid_range_min(self, gid_range_min):
        """Sets the gid_range_min of this SettingsMappingMappingSettings.

        Specifies the starting number for a fixed range from which GIDs are allocated.  # noqa: E501

        :param gid_range_min: The gid_range_min of this SettingsMappingMappingSettings.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                gid_range_min is not None and gid_range_min > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `gid_range_min`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self._configuration.client_side_validation and
                gid_range_min is not None and gid_range_min < 0):  # noqa: E501
            raise ValueError("Invalid value for `gid_range_min`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gid_range_min = gid_range_min

    @property
    def gid_range_next(self):
        """Gets the gid_range_next of this SettingsMappingMappingSettings.  # noqa: E501

        Specifies the next GID to allocate.  # noqa: E501

        :return: The gid_range_next of this SettingsMappingMappingSettings.  # noqa: E501
        :rtype: int
        """
        return self._gid_range_next

    @gid_range_next.setter
    def gid_range_next(self, gid_range_next):
        """Sets the gid_range_next of this SettingsMappingMappingSettings.

        Specifies the next GID to allocate.  # noqa: E501

        :param gid_range_next: The gid_range_next of this SettingsMappingMappingSettings.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                gid_range_next is not None and gid_range_next > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `gid_range_next`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self._configuration.client_side_validation and
                gid_range_next is not None and gid_range_next < 0):  # noqa: E501
            raise ValueError("Invalid value for `gid_range_next`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gid_range_next = gid_range_next

    @property
    def uid_range_enabled(self):
        """Gets the uid_range_enabled of this SettingsMappingMappingSettings.  # noqa: E501

        If true, allocates UIDs from a fixed range.  # noqa: E501

        :return: The uid_range_enabled of this SettingsMappingMappingSettings.  # noqa: E501
        :rtype: bool
        """
        return self._uid_range_enabled

    @uid_range_enabled.setter
    def uid_range_enabled(self, uid_range_enabled):
        """Sets the uid_range_enabled of this SettingsMappingMappingSettings.

        If true, allocates UIDs from a fixed range.  # noqa: E501

        :param uid_range_enabled: The uid_range_enabled of this SettingsMappingMappingSettings.  # noqa: E501
        :type: bool
        """

        self._uid_range_enabled = uid_range_enabled

    @property
    def uid_range_max(self):
        """Gets the uid_range_max of this SettingsMappingMappingSettings.  # noqa: E501

        Specifies the ending number for a fixed range from which UIDs are allocated.  # noqa: E501

        :return: The uid_range_max of this SettingsMappingMappingSettings.  # noqa: E501
        :rtype: int
        """
        return self._uid_range_max

    @uid_range_max.setter
    def uid_range_max(self, uid_range_max):
        """Sets the uid_range_max of this SettingsMappingMappingSettings.

        Specifies the ending number for a fixed range from which UIDs are allocated.  # noqa: E501

        :param uid_range_max: The uid_range_max of this SettingsMappingMappingSettings.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                uid_range_max is not None and uid_range_max > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `uid_range_max`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self._configuration.client_side_validation and
                uid_range_max is not None and uid_range_max < 0):  # noqa: E501
            raise ValueError("Invalid value for `uid_range_max`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uid_range_max = uid_range_max

    @property
    def uid_range_min(self):
        """Gets the uid_range_min of this SettingsMappingMappingSettings.  # noqa: E501

        Specifies the starting number for a fixed range from which UIDs are allocated.  # noqa: E501

        :return: The uid_range_min of this SettingsMappingMappingSettings.  # noqa: E501
        :rtype: int
        """
        return self._uid_range_min

    @uid_range_min.setter
    def uid_range_min(self, uid_range_min):
        """Sets the uid_range_min of this SettingsMappingMappingSettings.

        Specifies the starting number for a fixed range from which UIDs are allocated.  # noqa: E501

        :param uid_range_min: The uid_range_min of this SettingsMappingMappingSettings.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                uid_range_min is not None and uid_range_min > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `uid_range_min`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self._configuration.client_side_validation and
                uid_range_min is not None and uid_range_min < 0):  # noqa: E501
            raise ValueError("Invalid value for `uid_range_min`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uid_range_min = uid_range_min

    @property
    def uid_range_next(self):
        """Gets the uid_range_next of this SettingsMappingMappingSettings.  # noqa: E501

        Specifies the next UID to allocate.  # noqa: E501

        :return: The uid_range_next of this SettingsMappingMappingSettings.  # noqa: E501
        :rtype: int
        """
        return self._uid_range_next

    @uid_range_next.setter
    def uid_range_next(self, uid_range_next):
        """Sets the uid_range_next of this SettingsMappingMappingSettings.

        Specifies the next UID to allocate.  # noqa: E501

        :param uid_range_next: The uid_range_next of this SettingsMappingMappingSettings.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                uid_range_next is not None and uid_range_next > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `uid_range_next`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self._configuration.client_side_validation and
                uid_range_next is not None and uid_range_next < 0):  # noqa: E501
            raise ValueError("Invalid value for `uid_range_next`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uid_range_next = uid_range_next

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
        if issubclass(SettingsMappingMappingSettings, dict):
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
        if not isinstance(other, SettingsMappingMappingSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsMappingMappingSettings):
            return True

        return self.to_dict() != other.to_dict()
