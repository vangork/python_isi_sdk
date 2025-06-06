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


class ProvidersSamlServicesSettingsSettings(object):
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
        'sso_enabled': 'bool'
    }

    attribute_map = {
        'sso_enabled': 'sso_enabled'
    }

    def __init__(self, sso_enabled=None, _configuration=None):  # noqa: E501
        """ProvidersSamlServicesSettingsSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sso_enabled = None
        self.discriminator = None

        if sso_enabled is not None:
            self.sso_enabled = sso_enabled

    @property
    def sso_enabled(self):
        """Gets the sso_enabled of this ProvidersSamlServicesSettingsSettings.  # noqa: E501

        Indicates whether Single Sign On is enabled for the access zone.  # noqa: E501

        :return: The sso_enabled of this ProvidersSamlServicesSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._sso_enabled

    @sso_enabled.setter
    def sso_enabled(self, sso_enabled):
        """Sets the sso_enabled of this ProvidersSamlServicesSettingsSettings.

        Indicates whether Single Sign On is enabled for the access zone.  # noqa: E501

        :param sso_enabled: The sso_enabled of this ProvidersSamlServicesSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._sso_enabled = sso_enabled

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
        if issubclass(ProvidersSamlServicesSettingsSettings, dict):
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
        if not isinstance(other, ProvidersSamlServicesSettingsSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProvidersSamlServicesSettingsSettings):
            return True

        return self.to_dict() != other.to_dict()
