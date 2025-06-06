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


class ClusterFirmwareDeviceNode(object):
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
        'error': 'str',
        'id': 'int',
        'lnn': 'int',
        'node_unavailable': 'bool',
        'package': 'list[UpgradeClusterFirmwareDeviceNodePackageItem]',
        'status': 'int'
    }

    attribute_map = {
        'devices': 'devices',
        'error': 'error',
        'id': 'id',
        'lnn': 'lnn',
        'node_unavailable': 'node_unavailable',
        'package': 'package',
        'status': 'status'
    }

    def __init__(self, devices=None, error=None, id=None, lnn=None, node_unavailable=None, package=None, status=None, _configuration=None):  # noqa: E501
        """ClusterFirmwareDeviceNode - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._devices = None
        self._error = None
        self._id = None
        self._lnn = None
        self._node_unavailable = None
        self._package = None
        self._status = None
        self.discriminator = None

        if devices is not None:
            self.devices = devices
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if node_unavailable is not None:
            self.node_unavailable = node_unavailable
        if package is not None:
            self.package = package
        if status is not None:
            self.status = status

    @property
    def devices(self):
        """Gets the devices of this ClusterFirmwareDeviceNode.  # noqa: E501

        List of the firmware status for hardware components on the node.  # noqa: E501

        :return: The devices of this ClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: list[UpgradeClusterFirmwareDeviceNodeDevice]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this ClusterFirmwareDeviceNode.

        List of the firmware status for hardware components on the node.  # noqa: E501

        :param devices: The devices of this ClusterFirmwareDeviceNode.  # noqa: E501
        :type: list[UpgradeClusterFirmwareDeviceNodeDevice]
        """

        self._devices = devices

    @property
    def error(self):
        """Gets the error of this ClusterFirmwareDeviceNode.  # noqa: E501

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :return: The error of this ClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ClusterFirmwareDeviceNode.

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :param error: The error of this ClusterFirmwareDeviceNode.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                error is not None and len(error) > 8192):
            raise ValueError("Invalid value for `error`, length must be less than or equal to `8192`")  # noqa: E501
        if (self._configuration.client_side_validation and
                error is not None and len(error) < 0):
            raise ValueError("Invalid value for `error`, length must be greater than or equal to `0`")  # noqa: E501

        self._error = error

    @property
    def id(self):
        """Gets the id of this ClusterFirmwareDeviceNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this ClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterFirmwareDeviceNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this ClusterFirmwareDeviceNode.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                id is not None and id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and id < 0):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this ClusterFirmwareDeviceNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this ClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this ClusterFirmwareDeviceNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this ClusterFirmwareDeviceNode.  # noqa: E501
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
        """Gets the node_unavailable of this ClusterFirmwareDeviceNode.  # noqa: E501

        Node is unavailable.  # noqa: E501

        :return: The node_unavailable of this ClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: bool
        """
        return self._node_unavailable

    @node_unavailable.setter
    def node_unavailable(self, node_unavailable):
        """Sets the node_unavailable of this ClusterFirmwareDeviceNode.

        Node is unavailable.  # noqa: E501

        :param node_unavailable: The node_unavailable of this ClusterFirmwareDeviceNode.  # noqa: E501
        :type: bool
        """

        self._node_unavailable = node_unavailable

    @property
    def package(self):
        """Gets the package of this ClusterFirmwareDeviceNode.  # noqa: E501

        List of the firmware binary information for the installed firmware package.  # noqa: E501

        :return: The package of this ClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: list[UpgradeClusterFirmwareDeviceNodePackageItem]
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this ClusterFirmwareDeviceNode.

        List of the firmware binary information for the installed firmware package.  # noqa: E501

        :param package: The package of this ClusterFirmwareDeviceNode.  # noqa: E501
        :type: list[UpgradeClusterFirmwareDeviceNodePackageItem]
        """

        self._package = package

    @property
    def status(self):
        """Gets the status of this ClusterFirmwareDeviceNode.  # noqa: E501

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :return: The status of this ClusterFirmwareDeviceNode.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterFirmwareDeviceNode.

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :param status: The status of this ClusterFirmwareDeviceNode.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                status is not None and status > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self._configuration.client_side_validation and
                status is not None and status < 0):  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value greater than or equal to `0`")  # noqa: E501

        self._status = status

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
        if issubclass(ClusterFirmwareDeviceNode, dict):
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
        if not isinstance(other, ClusterFirmwareDeviceNode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterFirmwareDeviceNode):
            return True

        return self.to_dict() != other.to_dict()
