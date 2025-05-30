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


class UpgradeClusterFirmwareDeviceNodeDevice(object):
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
        'device': 'str',
        'mismatch': 'bool',
        'target_version': 'str',
        'type': 'str',
        'upgrade_status': 'str',
        'version': 'str'
    }

    attribute_map = {
        'device': 'device',
        'mismatch': 'mismatch',
        'target_version': 'target_version',
        'type': 'type',
        'upgrade_status': 'upgrade_status',
        'version': 'version'
    }

    def __init__(self, device=None, mismatch=None, target_version=None, type=None, upgrade_status=None, version=None, _configuration=None):  # noqa: E501
        """UpgradeClusterFirmwareDeviceNodeDevice - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device = None
        self._mismatch = None
        self._target_version = None
        self._type = None
        self._upgrade_status = None
        self._version = None
        self.discriminator = None

        if device is not None:
            self.device = device
        if mismatch is not None:
            self.mismatch = mismatch
        if target_version is not None:
            self.target_version = target_version
        if type is not None:
            self.type = type
        if upgrade_status is not None:
            self.upgrade_status = upgrade_status
        if version is not None:
            self.version = version

    @property
    def device(self):
        """Gets the device of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501

        The name of the device.  # noqa: E501

        :return: The device of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this UpgradeClusterFirmwareDeviceNodeDevice.

        The name of the device.  # noqa: E501

        :param device: The device of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                device is not None and len(device) > 128):
            raise ValueError("Invalid value for `device`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                device is not None and len(device) < 1):
            raise ValueError("Invalid value for `device`, length must be greater than or equal to `1`")  # noqa: E501

        self._device = device

    @property
    def mismatch(self):
        """Gets the mismatch of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501

        Is the firmware up-to-date for this component.  # noqa: E501

        :return: The mismatch of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :rtype: bool
        """
        return self._mismatch

    @mismatch.setter
    def mismatch(self, mismatch):
        """Sets the mismatch of this UpgradeClusterFirmwareDeviceNodeDevice.

        Is the firmware up-to-date for this component.  # noqa: E501

        :param mismatch: The mismatch of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :type: bool
        """

        self._mismatch = mismatch

    @property
    def target_version(self):
        """Gets the target_version of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501

        The target firmware version.  # noqa: E501

        :return: The target_version of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this UpgradeClusterFirmwareDeviceNodeDevice.

        The target firmware version.  # noqa: E501

        :param target_version: The target_version of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :type: str
        """

        self._target_version = target_version

    @property
    def type(self):
        """Gets the type of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501

        The device type.  # noqa: E501

        :return: The type of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpgradeClusterFirmwareDeviceNodeDevice.

        The device type.  # noqa: E501

        :param type: The type of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                type is not None and len(type) > 128):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def upgrade_status(self):
        """Gets the upgrade_status of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501

        The current state of the firmware upgrade for this component. One of the following values: 'queued', 'upgrading', 'upgraded', 'error' or 'null'.'null' indicates that the upgrade status is unknown.  # noqa: E501

        :return: The upgrade_status of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        """Sets the upgrade_status of this UpgradeClusterFirmwareDeviceNodeDevice.

        The current state of the firmware upgrade for this component. One of the following values: 'queued', 'upgrading', 'upgraded', 'error' or 'null'.'null' indicates that the upgrade status is unknown.  # noqa: E501

        :param upgrade_status: The upgrade_status of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                upgrade_status is not None and len(upgrade_status) > 128):
            raise ValueError("Invalid value for `upgrade_status`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                upgrade_status is not None and len(upgrade_status) < 1):
            raise ValueError("Invalid value for `upgrade_status`, length must be greater than or equal to `1`")  # noqa: E501

        self._upgrade_status = upgrade_status

    @property
    def version(self):
        """Gets the version of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501

        The current firmware version.  # noqa: E501

        :return: The version of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpgradeClusterFirmwareDeviceNodeDevice.

        The current firmware version.  # noqa: E501

        :param version: The version of this UpgradeClusterFirmwareDeviceNodeDevice.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                version is not None and len(version) > 128):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

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
        if issubclass(UpgradeClusterFirmwareDeviceNodeDevice, dict):
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
        if not isinstance(other, UpgradeClusterFirmwareDeviceNodeDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpgradeClusterFirmwareDeviceNodeDevice):
            return True

        return self.to_dict() != other.to_dict()
