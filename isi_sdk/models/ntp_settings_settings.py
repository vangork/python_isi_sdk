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


class NtpSettingsSettings(object):
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
        'chimers': 'int',
        'excluded': 'list[str]',
        'key_file': 'str'
    }

    attribute_map = {
        'chimers': 'chimers',
        'excluded': 'excluded',
        'key_file': 'key_file'
    }

    def __init__(self, chimers=None, excluded=None, key_file=None, _configuration=None):  # noqa: E501
        """NtpSettingsSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._chimers = None
        self._excluded = None
        self._key_file = None
        self.discriminator = None

        if chimers is not None:
            self.chimers = chimers
        if excluded is not None:
            self.excluded = excluded
        if key_file is not None:
            self.key_file = key_file

    @property
    def chimers(self):
        """Gets the chimers of this NtpSettingsSettings.  # noqa: E501

        Number of nodes that will contact the NTP servers.  # noqa: E501

        :return: The chimers of this NtpSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._chimers

    @chimers.setter
    def chimers(self, chimers):
        """Sets the chimers of this NtpSettingsSettings.

        Number of nodes that will contact the NTP servers.  # noqa: E501

        :param chimers: The chimers of this NtpSettingsSettings.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                chimers is not None and chimers < 1):  # noqa: E501
            raise ValueError("Invalid value for `chimers`, must be a value greater than or equal to `1`")  # noqa: E501

        self._chimers = chimers

    @property
    def excluded(self):
        """Gets the excluded of this NtpSettingsSettings.  # noqa: E501

        Node number (LNN) for nodes excluded from chimer duty.  # noqa: E501

        :return: The excluded of this NtpSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded

    @excluded.setter
    def excluded(self, excluded):
        """Sets the excluded of this NtpSettingsSettings.

        Node number (LNN) for nodes excluded from chimer duty.  # noqa: E501

        :param excluded: The excluded of this NtpSettingsSettings.  # noqa: E501
        :type: list[str]
        """

        self._excluded = excluded

    @property
    def key_file(self):
        """Gets the key_file of this NtpSettingsSettings.  # noqa: E501

        Path to NTP key file within /ifs.  # noqa: E501

        :return: The key_file of this NtpSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._key_file

    @key_file.setter
    def key_file(self, key_file):
        """Sets the key_file of this NtpSettingsSettings.

        Path to NTP key file within /ifs.  # noqa: E501

        :param key_file: The key_file of this NtpSettingsSettings.  # noqa: E501
        :type: str
        """

        self._key_file = key_file

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
        if issubclass(NtpSettingsSettings, dict):
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
        if not isinstance(other, NtpSettingsSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NtpSettingsSettings):
            return True

        return self.to_dict() != other.to_dict()
