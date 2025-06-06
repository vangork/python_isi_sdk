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


class ThrottlingSettingsSettings(object):
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
        'allowed_cpu_threshold': 'int',
        'system_cpu_load_threshold': 'int'
    }

    attribute_map = {
        'allowed_cpu_threshold': 'allowed_cpu_threshold',
        'system_cpu_load_threshold': 'system_cpu_load_threshold'
    }

    def __init__(self, allowed_cpu_threshold=None, system_cpu_load_threshold=None, _configuration=None):  # noqa: E501
        """ThrottlingSettingsSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allowed_cpu_threshold = None
        self._system_cpu_load_threshold = None
        self.discriminator = None

        if allowed_cpu_threshold is not None:
            self.allowed_cpu_threshold = allowed_cpu_threshold
        if system_cpu_load_threshold is not None:
            self.system_cpu_load_threshold = system_cpu_load_threshold

    @property
    def allowed_cpu_threshold(self):
        """Gets the allowed_cpu_threshold of this ThrottlingSettingsSettings.  # noqa: E501

        Allowed CPU percentage threshold for the Datamover  # noqa: E501

        :return: The allowed_cpu_threshold of this ThrottlingSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._allowed_cpu_threshold

    @allowed_cpu_threshold.setter
    def allowed_cpu_threshold(self, allowed_cpu_threshold):
        """Sets the allowed_cpu_threshold of this ThrottlingSettingsSettings.

        Allowed CPU percentage threshold for the Datamover  # noqa: E501

        :param allowed_cpu_threshold: The allowed_cpu_threshold of this ThrottlingSettingsSettings.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                allowed_cpu_threshold is not None and allowed_cpu_threshold > 100):  # noqa: E501
            raise ValueError("Invalid value for `allowed_cpu_threshold`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                allowed_cpu_threshold is not None and allowed_cpu_threshold < 1):  # noqa: E501
            raise ValueError("Invalid value for `allowed_cpu_threshold`, must be a value greater than or equal to `1`")  # noqa: E501

        self._allowed_cpu_threshold = allowed_cpu_threshold

    @property
    def system_cpu_load_threshold(self):
        """Gets the system_cpu_load_threshold of this ThrottlingSettingsSettings.  # noqa: E501

        System CPU load threshold at which Datamover will backoff (if consuming above the allowed CPU percentage)  # noqa: E501

        :return: The system_cpu_load_threshold of this ThrottlingSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._system_cpu_load_threshold

    @system_cpu_load_threshold.setter
    def system_cpu_load_threshold(self, system_cpu_load_threshold):
        """Sets the system_cpu_load_threshold of this ThrottlingSettingsSettings.

        System CPU load threshold at which Datamover will backoff (if consuming above the allowed CPU percentage)  # noqa: E501

        :param system_cpu_load_threshold: The system_cpu_load_threshold of this ThrottlingSettingsSettings.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                system_cpu_load_threshold is not None and system_cpu_load_threshold > 100):  # noqa: E501
            raise ValueError("Invalid value for `system_cpu_load_threshold`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                system_cpu_load_threshold is not None and system_cpu_load_threshold < 1):  # noqa: E501
            raise ValueError("Invalid value for `system_cpu_load_threshold`, must be a value greater than or equal to `1`")  # noqa: E501

        self._system_cpu_load_threshold = system_cpu_load_threshold

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
        if issubclass(ThrottlingSettingsSettings, dict):
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
        if not isinstance(other, ThrottlingSettingsSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThrottlingSettingsSettings):
            return True

        return self.to_dict() != other.to_dict()
