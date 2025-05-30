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


class SyncPolicyFileMatchingPattern(object):
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
        'or_criteria': 'list[SyncPolicyFileMatchingPatternOrCriteriaItem]'
    }

    attribute_map = {
        'or_criteria': 'or_criteria'
    }

    def __init__(self, or_criteria=None, _configuration=None):  # noqa: E501
        """SyncPolicyFileMatchingPattern - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._or_criteria = None
        self.discriminator = None

        if or_criteria is not None:
            self.or_criteria = or_criteria

    @property
    def or_criteria(self):
        """Gets the or_criteria of this SyncPolicyFileMatchingPattern.  # noqa: E501

        An array containing objects with \"and_criteria\" properties, each set of and_criteria will be logically OR'ed together to create the full file matching pattern.  # noqa: E501

        :return: The or_criteria of this SyncPolicyFileMatchingPattern.  # noqa: E501
        :rtype: list[SyncPolicyFileMatchingPatternOrCriteriaItem]
        """
        return self._or_criteria

    @or_criteria.setter
    def or_criteria(self, or_criteria):
        """Sets the or_criteria of this SyncPolicyFileMatchingPattern.

        An array containing objects with \"and_criteria\" properties, each set of and_criteria will be logically OR'ed together to create the full file matching pattern.  # noqa: E501

        :param or_criteria: The or_criteria of this SyncPolicyFileMatchingPattern.  # noqa: E501
        :type: list[SyncPolicyFileMatchingPatternOrCriteriaItem]
        """

        self._or_criteria = or_criteria

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
        if issubclass(SyncPolicyFileMatchingPattern, dict):
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
        if not isinstance(other, SyncPolicyFileMatchingPattern):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SyncPolicyFileMatchingPattern):
            return True

        return self.to_dict() != other.to_dict()
