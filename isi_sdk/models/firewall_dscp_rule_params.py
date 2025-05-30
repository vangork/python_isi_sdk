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


class FirewallDscpRuleParams(object):
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
        'dscp_value': 'int',
        'dst_ports': 'FirewallDscpRuleParamsDstPorts',
        'src_ports': 'FirewallDscpRuleParamsDstPorts'
    }

    attribute_map = {
        'dscp_value': 'dscp_value',
        'dst_ports': 'dst_ports',
        'src_ports': 'src_ports'
    }

    def __init__(self, dscp_value=None, dst_ports=None, src_ports=None, _configuration=None):  # noqa: E501
        """FirewallDscpRuleParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dscp_value = None
        self._dst_ports = None
        self._src_ports = None
        self.discriminator = None

        if dscp_value is not None:
            self.dscp_value = dscp_value
        if dst_ports is not None:
            self.dst_ports = dst_ports
        if src_ports is not None:
            self.src_ports = src_ports

    @property
    def dscp_value(self):
        """Gets the dscp_value of this FirewallDscpRuleParams.  # noqa: E501

        The DSCP value of the DSCP rule  # noqa: E501

        :return: The dscp_value of this FirewallDscpRuleParams.  # noqa: E501
        :rtype: int
        """
        return self._dscp_value

    @dscp_value.setter
    def dscp_value(self, dscp_value):
        """Sets the dscp_value of this FirewallDscpRuleParams.

        The DSCP value of the DSCP rule  # noqa: E501

        :param dscp_value: The dscp_value of this FirewallDscpRuleParams.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                dscp_value is not None and dscp_value > 65535):  # noqa: E501
            raise ValueError("Invalid value for `dscp_value`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                dscp_value is not None and dscp_value < 0):  # noqa: E501
            raise ValueError("Invalid value for `dscp_value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._dscp_value = dscp_value

    @property
    def dst_ports(self):
        """Gets the dst_ports of this FirewallDscpRuleParams.  # noqa: E501

        Specified port number for destination control.  # noqa: E501

        :return: The dst_ports of this FirewallDscpRuleParams.  # noqa: E501
        :rtype: FirewallDscpRuleParamsDstPorts
        """
        return self._dst_ports

    @dst_ports.setter
    def dst_ports(self, dst_ports):
        """Sets the dst_ports of this FirewallDscpRuleParams.

        Specified port number for destination control.  # noqa: E501

        :param dst_ports: The dst_ports of this FirewallDscpRuleParams.  # noqa: E501
        :type: FirewallDscpRuleParamsDstPorts
        """

        self._dst_ports = dst_ports

    @property
    def src_ports(self):
        """Gets the src_ports of this FirewallDscpRuleParams.  # noqa: E501

        Specified port number for source control.  # noqa: E501

        :return: The src_ports of this FirewallDscpRuleParams.  # noqa: E501
        :rtype: FirewallDscpRuleParamsDstPorts
        """
        return self._src_ports

    @src_ports.setter
    def src_ports(self, src_ports):
        """Sets the src_ports of this FirewallDscpRuleParams.

        Specified port number for source control.  # noqa: E501

        :param src_ports: The src_ports of this FirewallDscpRuleParams.  # noqa: E501
        :type: FirewallDscpRuleParamsDstPorts
        """

        self._src_ports = src_ports

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
        if issubclass(FirewallDscpRuleParams, dict):
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
        if not isinstance(other, FirewallDscpRuleParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FirewallDscpRuleParams):
            return True

        return self.to_dict() != other.to_dict()
