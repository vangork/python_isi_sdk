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


class NodeStatusPowersuppliesNodeSupply(object):
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
        'chassis': 'int',
        'firmware': 'str',
        'good': 'str',
        'id': 'int',
        'name': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'chassis': 'chassis',
        'firmware': 'firmware',
        'good': 'good',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, chassis=None, firmware=None, good=None, id=None, name=None, status=None, type=None, _configuration=None):  # noqa: E501
        """NodeStatusPowersuppliesNodeSupply - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._chassis = None
        self._firmware = None
        self._good = None
        self._id = None
        self._name = None
        self._status = None
        self._type = None
        self.discriminator = None

        if chassis is not None:
            self.chassis = chassis
        if firmware is not None:
            self.firmware = firmware
        if good is not None:
            self.good = good
        self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def chassis(self):
        """Gets the chassis of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501

        Which node chassis is this power supply in.  # noqa: E501

        :return: The chassis of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :rtype: int
        """
        return self._chassis

    @chassis.setter
    def chassis(self, chassis):
        """Sets the chassis of this NodeStatusPowersuppliesNodeSupply.

        Which node chassis is this power supply in.  # noqa: E501

        :param chassis: The chassis of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                chassis is not None and chassis > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `chassis`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                chassis is not None and chassis < 0):  # noqa: E501
            raise ValueError("Invalid value for `chassis`, must be a value greater than or equal to `0`")  # noqa: E501

        self._chassis = chassis

    @property
    def firmware(self):
        """Gets the firmware of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501

        The current firmware revision of this power supply.  # noqa: E501

        :return: The firmware of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """Sets the firmware of this NodeStatusPowersuppliesNodeSupply.

        The current firmware revision of this power supply.  # noqa: E501

        :param firmware: The firmware of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                firmware is not None and len(firmware) > 255):
            raise ValueError("Invalid value for `firmware`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                firmware is not None and len(firmware) < 0):
            raise ValueError("Invalid value for `firmware`, length must be greater than or equal to `0`")  # noqa: E501

        self._firmware = firmware

    @property
    def good(self):
        """Gets the good of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501

        Is this power supply in a failure state.  # noqa: E501

        :return: The good of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :rtype: str
        """
        return self._good

    @good.setter
    def good(self, good):
        """Sets the good of this NodeStatusPowersuppliesNodeSupply.

        Is this power supply in a failure state.  # noqa: E501

        :param good: The good of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                good is not None and len(good) > 255):
            raise ValueError("Invalid value for `good`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                good is not None and len(good) < 0):
            raise ValueError("Invalid value for `good`, length must be greater than or equal to `0`")  # noqa: E501

        self._good = good

    @property
    def id(self):
        """Gets the id of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501

        Identifying index for this power supply.  # noqa: E501

        :return: The id of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeStatusPowersuppliesNodeSupply.

        Identifying index for this power supply.  # noqa: E501

        :param id: The id of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and id > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and id < 0):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501

        Complete identifying string for this power supply.  # noqa: E501

        :return: The name of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeStatusPowersuppliesNodeSupply.

        Complete identifying string for this power supply.  # noqa: E501

        :param name: The name of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501

        A descriptive status string for this power supply.  # noqa: E501

        :return: The status of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeStatusPowersuppliesNodeSupply.

        A descriptive status string for this power supply.  # noqa: E501

        :param status: The status of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                status is not None and len(status) > 255):
            raise ValueError("Invalid value for `status`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                status is not None and len(status) < 0):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `0`")  # noqa: E501

        self._status = status

    @property
    def type(self):
        """Gets the type of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501

        The type of this power supply.  # noqa: E501

        :return: The type of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeStatusPowersuppliesNodeSupply.

        The type of this power supply.  # noqa: E501

        :param type: The type of this NodeStatusPowersuppliesNodeSupply.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                type is not None and len(type) > 255):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                type is not None and len(type) < 0):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `0`")  # noqa: E501

        self._type = type

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
        if issubclass(NodeStatusPowersuppliesNodeSupply, dict):
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
        if not isinstance(other, NodeStatusPowersuppliesNodeSupply):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeStatusPowersuppliesNodeSupply):
            return True

        return self.to_dict() != other.to_dict()
