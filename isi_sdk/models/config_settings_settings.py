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


class ConfigSettingsSettings(object):
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
        'allocation_type': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'allocation_type': 'allocation_type',
        'enabled': 'enabled'
    }

    def __init__(self, allocation_type=None, enabled=None, _configuration=None):  # noqa: E501
        """ConfigSettingsSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allocation_type = None
        self._enabled = None
        self.discriminator = None

        if allocation_type is not None:
            self.allocation_type = allocation_type
        if enabled is not None:
            self.enabled = enabled

    @property
    def allocation_type(self):
        """Gets the allocation_type of this ConfigSettingsSettings.  # noqa: E501

        Identifies the current network type (dhcp or static) being used for this BMC LAN interface.  # noqa: E501

        :return: The allocation_type of this ConfigSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._allocation_type

    @allocation_type.setter
    def allocation_type(self, allocation_type):
        """Sets the allocation_type of this ConfigSettingsSettings.

        Identifies the current network type (dhcp or static) being used for this BMC LAN interface.  # noqa: E501

        :param allocation_type: The allocation_type of this ConfigSettingsSettings.  # noqa: E501
        :type: str
        """

        self._allocation_type = allocation_type

    @property
    def enabled(self):
        """Gets the enabled of this ConfigSettingsSettings.  # noqa: E501

        A True value indicates the Remote IPMI Management feature is currently enabled on the cluster.  # noqa: E501

        :return: The enabled of this ConfigSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConfigSettingsSettings.

        A True value indicates the Remote IPMI Management feature is currently enabled on the cluster.  # noqa: E501

        :param enabled: The enabled of this ConfigSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(ConfigSettingsSettings, dict):
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
        if not isinstance(other, ConfigSettingsSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigSettingsSettings):
            return True

        return self.to_dict() != other.to_dict()
