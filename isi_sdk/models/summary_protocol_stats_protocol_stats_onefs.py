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


class SummaryProtocolStatsProtocolStatsOnefs(object):
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
        '_in': 'float',
        'out': 'float',
        'total': 'float'
    }

    attribute_map = {
        '_in': 'in',
        'out': 'out',
        'total': 'total'
    }

    def __init__(self, _in=None, out=None, total=None, _configuration=None):  # noqa: E501
        """SummaryProtocolStatsProtocolStatsOnefs - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__in = None
        self._out = None
        self._total = None
        self.discriminator = None

        self._in = _in
        self.out = out
        self.total = total

    @property
    def _in(self):
        """Gets the _in of this SummaryProtocolStatsProtocolStatsOnefs.  # noqa: E501

        OneFS throughput in MB/s in.  # noqa: E501

        :return: The _in of this SummaryProtocolStatsProtocolStatsOnefs.  # noqa: E501
        :rtype: float
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this SummaryProtocolStatsProtocolStatsOnefs.

        OneFS throughput in MB/s in.  # noqa: E501

        :param _in: The _in of this SummaryProtocolStatsProtocolStatsOnefs.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and _in is None:
            raise ValueError("Invalid value for `_in`, must not be `None`")  # noqa: E501

        self.__in = _in

    @property
    def out(self):
        """Gets the out of this SummaryProtocolStatsProtocolStatsOnefs.  # noqa: E501

        OneFS throughput in MB/s out.  # noqa: E501

        :return: The out of this SummaryProtocolStatsProtocolStatsOnefs.  # noqa: E501
        :rtype: float
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this SummaryProtocolStatsProtocolStatsOnefs.

        OneFS throughput in MB/s out.  # noqa: E501

        :param out: The out of this SummaryProtocolStatsProtocolStatsOnefs.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and out is None:
            raise ValueError("Invalid value for `out`, must not be `None`")  # noqa: E501

        self._out = out

    @property
    def total(self):
        """Gets the total of this SummaryProtocolStatsProtocolStatsOnefs.  # noqa: E501

        OneFS throughput in MB/s total.  # noqa: E501

        :return: The total of this SummaryProtocolStatsProtocolStatsOnefs.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SummaryProtocolStatsProtocolStatsOnefs.

        OneFS throughput in MB/s total.  # noqa: E501

        :param total: The total of this SummaryProtocolStatsProtocolStatsOnefs.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

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
        if issubclass(SummaryProtocolStatsProtocolStatsOnefs, dict):
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
        if not isinstance(other, SummaryProtocolStatsProtocolStatsOnefs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SummaryProtocolStatsProtocolStatsOnefs):
            return True

        return self.to_dict() != other.to_dict()
