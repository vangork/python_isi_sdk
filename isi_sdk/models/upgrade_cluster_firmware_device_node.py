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


class UpgradeClusterFirmwareDeviceNode(object):
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
        'devices': 'list[UpgradeClusterFirmwareDeviceNodeDevice]',
        'lnn': 'int',
        'node_unavailable': 'bool',
        'package': 'list[UpgradeClusterFirmwareDeviceNodePackageItem]'
    }

    attribute_map = {
        'devices': 'devices',
        'lnn': 'lnn',
        'node_unavailable': 'node_unavailable',
        'package': 'package'
    }

    def __init__(self, devices=None, lnn=None, node_unavailable=None, package=None, _configuration=None):  # noqa: E501
        """UpgradeClusterFirmwareDeviceNode - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._devices = None
        self._lnn = None
        self._node_unavailable = None
        self._package = None
        self.discriminator = None

        if devices is not None:
            self.devices = devices
        if lnn is not None:
            self.lnn = lnn
        if node_unavailable is not None:
            self.node_unavailable = node_unavailable
        if package is not None:
            self.package = package

    @property
    def devices(self):
        """Gets the devices of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501

        List of the firmware status for hardware components on the node.  # noqa: E501

        :return: The devices of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: list[UpgradeClusterFirmwareDeviceNodeDevice]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this UpgradeClusterFirmwareDeviceNode.

        List of the firmware status for hardware components on the node.  # noqa: E501

        :param devices: The devices of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501
        :type: list[UpgradeClusterFirmwareDeviceNodeDevice]
        """

        self._devices = devices

    @property
    def lnn(self):
        """Gets the lnn of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501

        The lnn of the node.  # noqa: E501

        :return: The lnn of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this UpgradeClusterFirmwareDeviceNode.

        The lnn of the node.  # noqa: E501

        :param lnn: The lnn of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                lnn is not None and lnn > 65535):  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                lnn is not None and lnn < 1):  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def node_unavailable(self):
        """Gets the node_unavailable of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501

        Node is unavailable.  # noqa: E501

        :return: The node_unavailable of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: bool
        """
        return self._node_unavailable

    @node_unavailable.setter
    def node_unavailable(self, node_unavailable):
        """Sets the node_unavailable of this UpgradeClusterFirmwareDeviceNode.

        Node is unavailable.  # noqa: E501

        :param node_unavailable: The node_unavailable of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501
        :type: bool
        """

        self._node_unavailable = node_unavailable

    @property
    def package(self):
        """Gets the package of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501

        List of the firmware binary information for the installed firmware package.  # noqa: E501

        :return: The package of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: list[UpgradeClusterFirmwareDeviceNodePackageItem]
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this UpgradeClusterFirmwareDeviceNode.

        List of the firmware binary information for the installed firmware package.  # noqa: E501

        :param package: The package of this UpgradeClusterFirmwareDeviceNode.  # noqa: E501
        :type: list[UpgradeClusterFirmwareDeviceNodePackageItem]
        """

        self._package = package

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
        if issubclass(UpgradeClusterFirmwareDeviceNode, dict):
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
        if not isinstance(other, UpgradeClusterFirmwareDeviceNode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpgradeClusterFirmwareDeviceNode):
            return True

        return self.to_dict() != other.to_dict()
