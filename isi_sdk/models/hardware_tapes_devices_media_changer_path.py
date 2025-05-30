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


class HardwareTapesDevicesMediaChangerPath(object):
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
        'lun': 'int',
        'devname': 'str',
        'opencount': 'int',
        'passname': 'str',
        'path': 'str',
        'portid': 'str',
        'state': 'str',
        'wwpn': 'str'
    }

    attribute_map = {
        'lun': 'LUN',
        'devname': 'devname',
        'opencount': 'opencount',
        'passname': 'passname',
        'path': 'path',
        'portid': 'portid',
        'state': 'state',
        'wwpn': 'wwpn'
    }

    def __init__(self, lun=None, devname=None, opencount=None, passname=None, path=None, portid=None, state=None, wwpn=None, _configuration=None):  # noqa: E501
        """HardwareTapesDevicesMediaChangerPath - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._lun = None
        self._devname = None
        self._opencount = None
        self._passname = None
        self._path = None
        self._portid = None
        self._state = None
        self._wwpn = None
        self.discriminator = None

        if lun is not None:
            self.lun = lun
        if devname is not None:
            self.devname = devname
        if opencount is not None:
            self.opencount = opencount
        if passname is not None:
            self.passname = passname
        if path is not None:
            self.path = path
        if portid is not None:
            self.portid = portid
        if state is not None:
            self.state = state
        if wwpn is not None:
            self.wwpn = wwpn

    @property
    def lun(self):
        """Gets the lun of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501

        Logic unit number of the device on the path  # noqa: E501

        :return: The lun of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :rtype: int
        """
        return self._lun

    @lun.setter
    def lun(self, lun):
        """Sets the lun of this HardwareTapesDevicesMediaChangerPath.

        Logic unit number of the device on the path  # noqa: E501

        :param lun: The lun of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :type: int
        """

        self._lun = lun

    @property
    def devname(self):
        """Gets the devname of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501

        Device driver file name  # noqa: E501

        :return: The devname of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :rtype: str
        """
        return self._devname

    @devname.setter
    def devname(self, devname):
        """Sets the devname of this HardwareTapesDevicesMediaChangerPath.

        Device driver file name  # noqa: E501

        :param devname: The devname of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :type: str
        """

        self._devname = devname

    @property
    def opencount(self):
        """Gets the opencount of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501

        Number of open  # noqa: E501

        :return: The opencount of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :rtype: int
        """
        return self._opencount

    @opencount.setter
    def opencount(self, opencount):
        """Sets the opencount of this HardwareTapesDevicesMediaChangerPath.

        Number of open  # noqa: E501

        :param opencount: The opencount of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :type: int
        """

        self._opencount = opencount

    @property
    def passname(self):
        """Gets the passname of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501

        Pass through device driver file name  # noqa: E501

        :return: The passname of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :rtype: str
        """
        return self._passname

    @passname.setter
    def passname(self, passname):
        """Sets the passname of this HardwareTapesDevicesMediaChangerPath.

        Pass through device driver file name  # noqa: E501

        :param passname: The passname of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :type: str
        """

        self._passname = passname

    @property
    def path(self):
        """Gets the path of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501

        Path of the device  # noqa: E501

        :return: The path of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HardwareTapesDevicesMediaChangerPath.

        Path of the device  # noqa: E501

        :param path: The path of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def portid(self):
        """Gets the portid of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501

        Port ID on the path  # noqa: E501

        :return: The portid of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :rtype: str
        """
        return self._portid

    @portid.setter
    def portid(self, portid):
        """Sets the portid of this HardwareTapesDevicesMediaChangerPath.

        Port ID on the path  # noqa: E501

        :param portid: The portid of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :type: str
        """

        self._portid = portid

    @property
    def state(self):
        """Gets the state of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501

        path state  # noqa: E501

        :return: The state of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this HardwareTapesDevicesMediaChangerPath.

        path state  # noqa: E501

        :param state: The state of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def wwpn(self):
        """Gets the wwpn of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501

        World wide port name  # noqa: E501

        :return: The wwpn of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :rtype: str
        """
        return self._wwpn

    @wwpn.setter
    def wwpn(self, wwpn):
        """Sets the wwpn of this HardwareTapesDevicesMediaChangerPath.

        World wide port name  # noqa: E501

        :param wwpn: The wwpn of this HardwareTapesDevicesMediaChangerPath.  # noqa: E501
        :type: str
        """

        self._wwpn = wwpn

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
        if issubclass(HardwareTapesDevicesMediaChangerPath, dict):
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
        if not isinstance(other, HardwareTapesDevicesMediaChangerPath):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HardwareTapesDevicesMediaChangerPath):
            return True

        return self.to_dict() != other.to_dict()
