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


class ThrottlingBwRules(object):
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
        'bandwidth_rules': 'list[ThrottlingBwRulesBandwidthRule]'
    }

    attribute_map = {
        'bandwidth_rules': 'bandwidth-rules'
    }

    def __init__(self, bandwidth_rules=None, _configuration=None):  # noqa: E501
        """ThrottlingBwRules - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth_rules = None
        self.discriminator = None

        if bandwidth_rules is not None:
            self.bandwidth_rules = bandwidth_rules

    @property
    def bandwidth_rules(self):
        """Gets the bandwidth_rules of this ThrottlingBwRules.  # noqa: E501


        :return: The bandwidth_rules of this ThrottlingBwRules.  # noqa: E501
        :rtype: list[ThrottlingBwRulesBandwidthRule]
        """
        return self._bandwidth_rules

    @bandwidth_rules.setter
    def bandwidth_rules(self, bandwidth_rules):
        """Sets the bandwidth_rules of this ThrottlingBwRules.


        :param bandwidth_rules: The bandwidth_rules of this ThrottlingBwRules.  # noqa: E501
        :type: list[ThrottlingBwRulesBandwidthRule]
        """

        self._bandwidth_rules = bandwidth_rules

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
        if issubclass(ThrottlingBwRules, dict):
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
        if not isinstance(other, ThrottlingBwRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThrottlingBwRules):
            return True

        return self.to_dict() != other.to_dict()
