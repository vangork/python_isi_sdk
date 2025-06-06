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


class NdmpDiagnosticsDiagnostics(object):
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
        'diag_level': 'int',
        'protocol_version': 'int',
        'trace_level': 'str'
    }

    attribute_map = {
        'diag_level': 'diag_level',
        'protocol_version': 'protocol_version',
        'trace_level': 'trace_level'
    }

    def __init__(self, diag_level=None, protocol_version=None, trace_level=None, _configuration=None):  # noqa: E501
        """NdmpDiagnosticsDiagnostics - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._diag_level = None
        self._protocol_version = None
        self._trace_level = None
        self.discriminator = None

        if diag_level is not None:
            self.diag_level = diag_level
        if protocol_version is not None:
            self.protocol_version = protocol_version
        if trace_level is not None:
            self.trace_level = trace_level

    @property
    def diag_level(self):
        """Gets the diag_level of this NdmpDiagnosticsDiagnostics.  # noqa: E501

        Diagnostics level for ndmp.  # noqa: E501

        :return: The diag_level of this NdmpDiagnosticsDiagnostics.  # noqa: E501
        :rtype: int
        """
        return self._diag_level

    @diag_level.setter
    def diag_level(self, diag_level):
        """Sets the diag_level of this NdmpDiagnosticsDiagnostics.

        Diagnostics level for ndmp.  # noqa: E501

        :param diag_level: The diag_level of this NdmpDiagnosticsDiagnostics.  # noqa: E501
        :type: int
        """

        self._diag_level = diag_level

    @property
    def protocol_version(self):
        """Gets the protocol_version of this NdmpDiagnosticsDiagnostics.  # noqa: E501

        The version of the ndmp protocol.  # noqa: E501

        :return: The protocol_version of this NdmpDiagnosticsDiagnostics.  # noqa: E501
        :rtype: int
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this NdmpDiagnosticsDiagnostics.

        The version of the ndmp protocol.  # noqa: E501

        :param protocol_version: The protocol_version of this NdmpDiagnosticsDiagnostics.  # noqa: E501
        :type: int
        """

        self._protocol_version = protocol_version

    @property
    def trace_level(self):
        """Gets the trace_level of this NdmpDiagnosticsDiagnostics.  # noqa: E501

        Trace level for ndmp.  # noqa: E501

        :return: The trace_level of this NdmpDiagnosticsDiagnostics.  # noqa: E501
        :rtype: str
        """
        return self._trace_level

    @trace_level.setter
    def trace_level(self, trace_level):
        """Sets the trace_level of this NdmpDiagnosticsDiagnostics.

        Trace level for ndmp.  # noqa: E501

        :param trace_level: The trace_level of this NdmpDiagnosticsDiagnostics.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "standard", "include-file-history", "log-file-history"]  # noqa: E501
        if (self._configuration.client_side_validation and
                trace_level not in allowed_values):
            raise ValueError(
                "Invalid value for `trace_level` ({0}), must be one of {1}"  # noqa: E501
                .format(trace_level, allowed_values)
            )

        self._trace_level = trace_level

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
        if issubclass(NdmpDiagnosticsDiagnostics, dict):
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
        if not isinstance(other, NdmpDiagnosticsDiagnostics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NdmpDiagnosticsDiagnostics):
            return True

        return self.to_dict() != other.to_dict()
