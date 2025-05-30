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


class EventAlertConditionCreateParams(object):
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
        'channels': 'list[str]',
        'condition': 'str',
        'name': 'str'
    }

    attribute_map = {
        'channels': 'channels',
        'condition': 'condition',
        'name': 'name'
    }

    def __init__(self, channels=None, condition=None, name=None, _configuration=None):  # noqa: E501
        """EventAlertConditionCreateParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._channels = None
        self._condition = None
        self._name = None
        self.discriminator = None

        self.channels = channels
        self.condition = condition
        self.name = name

    @property
    def channels(self):
        """Gets the channels of this EventAlertConditionCreateParams.  # noqa: E501

        Channels for alert.  # noqa: E501

        :return: The channels of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this EventAlertConditionCreateParams.

        Channels for alert.  # noqa: E501

        :param channels: The channels of this EventAlertConditionCreateParams.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and channels is None:
            raise ValueError("Invalid value for `channels`, must not be `None`")  # noqa: E501

        self._channels = channels

    @property
    def condition(self):
        """Gets the condition of this EventAlertConditionCreateParams.  # noqa: E501

        Trigger condition for alert.  # noqa: E501

        :return: The condition of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this EventAlertConditionCreateParams.

        Trigger condition for alert.  # noqa: E501

        :param condition: The condition of this EventAlertConditionCreateParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and condition is None:
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501
        allowed_values = ["NEW", "NEW EVENTS", "ONGOING", "SEVERITY INCREASE", "SEVERITY DECREASE", "RESOLVED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                condition not in allowed_values):
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def name(self):
        """Gets the name of this EventAlertConditionCreateParams.  # noqa: E501

        Unique identifier.  # noqa: E501

        :return: The name of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventAlertConditionCreateParams.

        Unique identifier.  # noqa: E501

        :param name: The name of this EventAlertConditionCreateParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

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
        if issubclass(EventAlertConditionCreateParams, dict):
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
        if not isinstance(other, EventAlertConditionCreateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventAlertConditionCreateParams):
            return True

        return self.to_dict() != other.to_dict()
