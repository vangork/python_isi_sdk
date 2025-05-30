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


class NodeStatusNodeNvram(object):
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
        'batteries': 'list[NodeStatusNvramNodeBattery]',
        'battery_count': 'int',
        'charge_status': 'str',
        'charge_status_number': 'int',
        'device': 'str',
        'present': 'bool',
        'present_flash': 'bool',
        'present_size': 'int',
        'present_type': 'str',
        'ship_mode': 'int',
        'supported': 'bool',
        'supported_flash': 'bool',
        'supported_size': 'int',
        'supported_type': 'str'
    }

    attribute_map = {
        'batteries': 'batteries',
        'battery_count': 'battery_count',
        'charge_status': 'charge_status',
        'charge_status_number': 'charge_status_number',
        'device': 'device',
        'present': 'present',
        'present_flash': 'present_flash',
        'present_size': 'present_size',
        'present_type': 'present_type',
        'ship_mode': 'ship_mode',
        'supported': 'supported',
        'supported_flash': 'supported_flash',
        'supported_size': 'supported_size',
        'supported_type': 'supported_type'
    }

    def __init__(self, batteries=None, battery_count=None, charge_status=None, charge_status_number=None, device=None, present=None, present_flash=None, present_size=None, present_type=None, ship_mode=None, supported=None, supported_flash=None, supported_size=None, supported_type=None, _configuration=None):  # noqa: E501
        """NodeStatusNodeNvram - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._batteries = None
        self._battery_count = None
        self._charge_status = None
        self._charge_status_number = None
        self._device = None
        self._present = None
        self._present_flash = None
        self._present_size = None
        self._present_type = None
        self._ship_mode = None
        self._supported = None
        self._supported_flash = None
        self._supported_size = None
        self._supported_type = None
        self.discriminator = None

        if batteries is not None:
            self.batteries = batteries
        if battery_count is not None:
            self.battery_count = battery_count
        if charge_status is not None:
            self.charge_status = charge_status
        if charge_status_number is not None:
            self.charge_status_number = charge_status_number
        if device is not None:
            self.device = device
        if present is not None:
            self.present = present
        if present_flash is not None:
            self.present_flash = present_flash
        if present_size is not None:
            self.present_size = present_size
        if present_type is not None:
            self.present_type = present_type
        if ship_mode is not None:
            self.ship_mode = ship_mode
        if supported is not None:
            self.supported = supported
        if supported_flash is not None:
            self.supported_flash = supported_flash
        if supported_size is not None:
            self.supported_size = supported_size
        if supported_type is not None:
            self.supported_type = supported_type

    @property
    def batteries(self):
        """Gets the batteries of this NodeStatusNodeNvram.  # noqa: E501

        This node's NVRAM battery status information.  # noqa: E501

        :return: The batteries of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: list[NodeStatusNvramNodeBattery]
        """
        return self._batteries

    @batteries.setter
    def batteries(self, batteries):
        """Sets the batteries of this NodeStatusNodeNvram.

        This node's NVRAM battery status information.  # noqa: E501

        :param batteries: The batteries of this NodeStatusNodeNvram.  # noqa: E501
        :type: list[NodeStatusNvramNodeBattery]
        """

        self._batteries = batteries

    @property
    def battery_count(self):
        """Gets the battery_count of this NodeStatusNodeNvram.  # noqa: E501

        This node's NVRAM battery count. On failure: -1, otherwise 1 or 2.  # noqa: E501

        :return: The battery_count of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: int
        """
        return self._battery_count

    @battery_count.setter
    def battery_count(self, battery_count):
        """Sets the battery_count of this NodeStatusNodeNvram.

        This node's NVRAM battery count. On failure: -1, otherwise 1 or 2.  # noqa: E501

        :param battery_count: The battery_count of this NodeStatusNodeNvram.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                battery_count is not None and battery_count > 2):  # noqa: E501
            raise ValueError("Invalid value for `battery_count`, must be a value less than or equal to `2`")  # noqa: E501
        if (self._configuration.client_side_validation and
                battery_count is not None and battery_count < -1):  # noqa: E501
            raise ValueError("Invalid value for `battery_count`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._battery_count = battery_count

    @property
    def charge_status(self):
        """Gets the charge_status of this NodeStatusNodeNvram.  # noqa: E501

        This node's NVRAM battery charge status, as a color.  # noqa: E501

        :return: The charge_status of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: str
        """
        return self._charge_status

    @charge_status.setter
    def charge_status(self, charge_status):
        """Sets the charge_status of this NodeStatusNodeNvram.

        This node's NVRAM battery charge status, as a color.  # noqa: E501

        :param charge_status: The charge_status of this NodeStatusNodeNvram.  # noqa: E501
        :type: str
        """
        allowed_values = ["BLACK", "GREEN", "YELLOW", "RED", "UNKNOWN", "Not supported"]  # noqa: E501
        if (self._configuration.client_side_validation and
                charge_status not in allowed_values):
            raise ValueError(
                "Invalid value for `charge_status` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_status, allowed_values)
            )

        self._charge_status = charge_status

    @property
    def charge_status_number(self):
        """Gets the charge_status_number of this NodeStatusNodeNvram.  # noqa: E501

        This node's NVRAM battery charge status, as a number. Error or not supported: -1. BR_BLACK: 0. BR_GREEN: 1. BR_YELLOW: 2. BR_RED: 3.  # noqa: E501

        :return: The charge_status_number of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: int
        """
        return self._charge_status_number

    @charge_status_number.setter
    def charge_status_number(self, charge_status_number):
        """Sets the charge_status_number of this NodeStatusNodeNvram.

        This node's NVRAM battery charge status, as a number. Error or not supported: -1. BR_BLACK: 0. BR_GREEN: 1. BR_YELLOW: 2. BR_RED: 3.  # noqa: E501

        :param charge_status_number: The charge_status_number of this NodeStatusNodeNvram.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                charge_status_number is not None and charge_status_number > 3):  # noqa: E501
            raise ValueError("Invalid value for `charge_status_number`, must be a value less than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                charge_status_number is not None and charge_status_number < -1):  # noqa: E501
            raise ValueError("Invalid value for `charge_status_number`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._charge_status_number = charge_status_number

    @property
    def device(self):
        """Gets the device of this NodeStatusNodeNvram.  # noqa: E501

        This node's NVRAM device name with path.  # noqa: E501

        :return: The device of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this NodeStatusNodeNvram.

        This node's NVRAM device name with path.  # noqa: E501

        :param device: The device of this NodeStatusNodeNvram.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                device is not None and len(device) > 255):
            raise ValueError("Invalid value for `device`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                device is not None and len(device) < 0):
            raise ValueError("Invalid value for `device`, length must be greater than or equal to `0`")  # noqa: E501

        self._device = device

    @property
    def present(self):
        """Gets the present of this NodeStatusNodeNvram.  # noqa: E501

        This node has NVRAM.  # noqa: E501

        :return: The present of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """Sets the present of this NodeStatusNodeNvram.

        This node has NVRAM.  # noqa: E501

        :param present: The present of this NodeStatusNodeNvram.  # noqa: E501
        :type: bool
        """

        self._present = present

    @property
    def present_flash(self):
        """Gets the present_flash of this NodeStatusNodeNvram.  # noqa: E501

        This node has NVRAM with flash storage.  # noqa: E501

        :return: The present_flash of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: bool
        """
        return self._present_flash

    @present_flash.setter
    def present_flash(self, present_flash):
        """Sets the present_flash of this NodeStatusNodeNvram.

        This node has NVRAM with flash storage.  # noqa: E501

        :param present_flash: The present_flash of this NodeStatusNodeNvram.  # noqa: E501
        :type: bool
        """

        self._present_flash = present_flash

    @property
    def present_size(self):
        """Gets the present_size of this NodeStatusNodeNvram.  # noqa: E501

        The size of the NVRAM, in bytes.  # noqa: E501

        :return: The present_size of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: int
        """
        return self._present_size

    @present_size.setter
    def present_size(self, present_size):
        """Sets the present_size of this NodeStatusNodeNvram.

        The size of the NVRAM, in bytes.  # noqa: E501

        :param present_size: The present_size of this NodeStatusNodeNvram.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                present_size is not None and present_size > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `present_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                present_size is not None and present_size < 0):  # noqa: E501
            raise ValueError("Invalid value for `present_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._present_size = present_size

    @property
    def present_type(self):
        """Gets the present_type of this NodeStatusNodeNvram.  # noqa: E501

        This node's NVRAM type.  # noqa: E501

        :return: The present_type of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: str
        """
        return self._present_type

    @present_type.setter
    def present_type(self, present_type):
        """Sets the present_type of this NodeStatusNodeNvram.

        This node's NVRAM type.  # noqa: E501

        :param present_type: The present_type of this NodeStatusNodeNvram.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                present_type is not None and len(present_type) > 255):
            raise ValueError("Invalid value for `present_type`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                present_type is not None and len(present_type) < 0):
            raise ValueError("Invalid value for `present_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._present_type = present_type

    @property
    def ship_mode(self):
        """Gets the ship_mode of this NodeStatusNodeNvram.  # noqa: E501

        This node's current ship mode state for NVRAM batteries. If not supported or on failure: -1. Disabled: 0. Enabled: 1.  # noqa: E501

        :return: The ship_mode of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: int
        """
        return self._ship_mode

    @ship_mode.setter
    def ship_mode(self, ship_mode):
        """Sets the ship_mode of this NodeStatusNodeNvram.

        This node's current ship mode state for NVRAM batteries. If not supported or on failure: -1. Disabled: 0. Enabled: 1.  # noqa: E501

        :param ship_mode: The ship_mode of this NodeStatusNodeNvram.  # noqa: E501
        :type: int
        """

        self._ship_mode = ship_mode

    @property
    def supported(self):
        """Gets the supported of this NodeStatusNodeNvram.  # noqa: E501

        This node supports NVRAM.  # noqa: E501

        :return: The supported of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        """Sets the supported of this NodeStatusNodeNvram.

        This node supports NVRAM.  # noqa: E501

        :param supported: The supported of this NodeStatusNodeNvram.  # noqa: E501
        :type: bool
        """

        self._supported = supported

    @property
    def supported_flash(self):
        """Gets the supported_flash of this NodeStatusNodeNvram.  # noqa: E501

        This node supports NVRAM with flash storage.  # noqa: E501

        :return: The supported_flash of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: bool
        """
        return self._supported_flash

    @supported_flash.setter
    def supported_flash(self, supported_flash):
        """Sets the supported_flash of this NodeStatusNodeNvram.

        This node supports NVRAM with flash storage.  # noqa: E501

        :param supported_flash: The supported_flash of this NodeStatusNodeNvram.  # noqa: E501
        :type: bool
        """

        self._supported_flash = supported_flash

    @property
    def supported_size(self):
        """Gets the supported_size of this NodeStatusNodeNvram.  # noqa: E501

        The maximum size of the NVRAM, in bytes.  # noqa: E501

        :return: The supported_size of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: int
        """
        return self._supported_size

    @supported_size.setter
    def supported_size(self, supported_size):
        """Sets the supported_size of this NodeStatusNodeNvram.

        The maximum size of the NVRAM, in bytes.  # noqa: E501

        :param supported_size: The supported_size of this NodeStatusNodeNvram.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                supported_size is not None and supported_size > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `supported_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                supported_size is not None and supported_size < 0):  # noqa: E501
            raise ValueError("Invalid value for `supported_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._supported_size = supported_size

    @property
    def supported_type(self):
        """Gets the supported_type of this NodeStatusNodeNvram.  # noqa: E501

        This node's supported NVRAM type.  # noqa: E501

        :return: The supported_type of this NodeStatusNodeNvram.  # noqa: E501
        :rtype: str
        """
        return self._supported_type

    @supported_type.setter
    def supported_type(self, supported_type):
        """Sets the supported_type of this NodeStatusNodeNvram.

        This node's supported NVRAM type.  # noqa: E501

        :param supported_type: The supported_type of this NodeStatusNodeNvram.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                supported_type is not None and len(supported_type) > 255):
            raise ValueError("Invalid value for `supported_type`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                supported_type is not None and len(supported_type) < 0):
            raise ValueError("Invalid value for `supported_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._supported_type = supported_type

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
        if issubclass(NodeStatusNodeNvram, dict):
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
        if not isinstance(other, NodeStatusNodeNvram):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeStatusNodeNvram):
            return True

        return self.to_dict() != other.to_dict()
