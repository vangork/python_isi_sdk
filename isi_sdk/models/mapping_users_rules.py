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


class MappingUsersRules(object):
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
        'rules': 'MappingUsersRulesRules'
    }

    attribute_map = {
        'rules': 'rules'
    }

    def __init__(self, rules=None, _configuration=None):  # noqa: E501
        """MappingUsersRules - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rules = None
        self.discriminator = None

        if rules is not None:
            self.rules = rules

    @property
    def rules(self):
        """Gets the rules of this MappingUsersRules.  # noqa: E501

        Specifies the properties for user mapping rules.  # noqa: E501

        :return: The rules of this MappingUsersRules.  # noqa: E501
        :rtype: MappingUsersRulesRules
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this MappingUsersRules.

        Specifies the properties for user mapping rules.  # noqa: E501

        :param rules: The rules of this MappingUsersRules.  # noqa: E501
        :type: MappingUsersRulesRules
        """

        self._rules = rules

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
        if issubclass(MappingUsersRules, dict):
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
        if not isinstance(other, MappingUsersRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MappingUsersRules):
            return True

        return self.to_dict() != other.to_dict()
