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


class SummaryProtocolStats(object):
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
        'protocol_stats': 'SummaryProtocolStatsProtocolStats'
    }

    attribute_map = {
        'protocol_stats': 'protocol-stats'
    }

    def __init__(self, protocol_stats=None, _configuration=None):  # noqa: E501
        """SummaryProtocolStats - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._protocol_stats = None
        self.discriminator = None

        if protocol_stats is not None:
            self.protocol_stats = protocol_stats

    @property
    def protocol_stats(self):
        """Gets the protocol_stats of this SummaryProtocolStats.  # noqa: E501

          # noqa: E501

        :return: The protocol_stats of this SummaryProtocolStats.  # noqa: E501
        :rtype: SummaryProtocolStatsProtocolStats
        """
        return self._protocol_stats

    @protocol_stats.setter
    def protocol_stats(self, protocol_stats):
        """Sets the protocol_stats of this SummaryProtocolStats.

          # noqa: E501

        :param protocol_stats: The protocol_stats of this SummaryProtocolStats.  # noqa: E501
        :type: SummaryProtocolStatsProtocolStats
        """

        self._protocol_stats = protocol_stats

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
        if issubclass(SummaryProtocolStats, dict):
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
        if not isinstance(other, SummaryProtocolStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SummaryProtocolStats):
            return True

        return self.to_dict() != other.to_dict()
