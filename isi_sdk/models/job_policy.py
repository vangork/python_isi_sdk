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


class JobPolicy(object):
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
        'description': 'str',
        'intervals': 'list[JobPolicyInterval]'
    }

    attribute_map = {
        'description': 'description',
        'intervals': 'intervals'
    }

    def __init__(self, description=None, intervals=None, _configuration=None):  # noqa: E501
        """JobPolicy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._intervals = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if intervals is not None:
            self.intervals = intervals

    @property
    def description(self):
        """Gets the description of this JobPolicy.  # noqa: E501

        A helpful human-readable description of the impact policy.  # noqa: E501

        :return: The description of this JobPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobPolicy.

        A helpful human-readable description of the impact policy.  # noqa: E501

        :param description: The description of this JobPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def intervals(self):
        """Gets the intervals of this JobPolicy.  # noqa: E501


        :return: The intervals of this JobPolicy.  # noqa: E501
        :rtype: list[JobPolicyInterval]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        """Sets the intervals of this JobPolicy.


        :param intervals: The intervals of this JobPolicy.  # noqa: E501
        :type: list[JobPolicyInterval]
        """

        self._intervals = intervals

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
        if issubclass(JobPolicy, dict):
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
        if not isinstance(other, JobPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobPolicy):
            return True

        return self.to_dict() != other.to_dict()
