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


class HealthcheckAutoupdateAutoupdate(object):
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
        'compliance_update': 'bool',
        'enabled': 'bool',
        'last_failed_upgrade_package': 'str',
        'number_of_failed_upgrades': 'int'
    }

    attribute_map = {
        'compliance_update': 'compliance_update',
        'enabled': 'enabled',
        'last_failed_upgrade_package': 'last_failed_upgrade_package',
        'number_of_failed_upgrades': 'number_of_failed_upgrades'
    }

    def __init__(self, compliance_update=None, enabled=None, last_failed_upgrade_package=None, number_of_failed_upgrades=None, _configuration=None):  # noqa: E501
        """HealthcheckAutoupdateAutoupdate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compliance_update = None
        self._enabled = None
        self._last_failed_upgrade_package = None
        self._number_of_failed_upgrades = None
        self.discriminator = None

        if compliance_update is not None:
            self.compliance_update = compliance_update
        if enabled is not None:
            self.enabled = enabled
        if last_failed_upgrade_package is not None:
            self.last_failed_upgrade_package = last_failed_upgrade_package
        if number_of_failed_upgrades is not None:
            self.number_of_failed_upgrades = number_of_failed_upgrades

    @property
    def compliance_update(self):
        """Gets the compliance_update of this HealthcheckAutoupdateAutoupdate.  # noqa: E501

        Enable flag for compliance mode.  # noqa: E501

        :return: The compliance_update of this HealthcheckAutoupdateAutoupdate.  # noqa: E501
        :rtype: bool
        """
        return self._compliance_update

    @compliance_update.setter
    def compliance_update(self, compliance_update):
        """Sets the compliance_update of this HealthcheckAutoupdateAutoupdate.

        Enable flag for compliance mode.  # noqa: E501

        :param compliance_update: The compliance_update of this HealthcheckAutoupdateAutoupdate.  # noqa: E501
        :type: bool
        """

        self._compliance_update = compliance_update

    @property
    def enabled(self):
        """Gets the enabled of this HealthcheckAutoupdateAutoupdate.  # noqa: E501

        Autoupdate enable flag.  # noqa: E501

        :return: The enabled of this HealthcheckAutoupdateAutoupdate.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this HealthcheckAutoupdateAutoupdate.

        Autoupdate enable flag.  # noqa: E501

        :param enabled: The enabled of this HealthcheckAutoupdateAutoupdate.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def last_failed_upgrade_package(self):
        """Gets the last_failed_upgrade_package of this HealthcheckAutoupdateAutoupdate.  # noqa: E501

        The name of the last failed upgrade package.  # noqa: E501

        :return: The last_failed_upgrade_package of this HealthcheckAutoupdateAutoupdate.  # noqa: E501
        :rtype: str
        """
        return self._last_failed_upgrade_package

    @last_failed_upgrade_package.setter
    def last_failed_upgrade_package(self, last_failed_upgrade_package):
        """Sets the last_failed_upgrade_package of this HealthcheckAutoupdateAutoupdate.

        The name of the last failed upgrade package.  # noqa: E501

        :param last_failed_upgrade_package: The last_failed_upgrade_package of this HealthcheckAutoupdateAutoupdate.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                last_failed_upgrade_package is not None and len(last_failed_upgrade_package) > 255):
            raise ValueError("Invalid value for `last_failed_upgrade_package`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                last_failed_upgrade_package is not None and len(last_failed_upgrade_package) < 0):
            raise ValueError("Invalid value for `last_failed_upgrade_package`, length must be greater than or equal to `0`")  # noqa: E501

        self._last_failed_upgrade_package = last_failed_upgrade_package

    @property
    def number_of_failed_upgrades(self):
        """Gets the number_of_failed_upgrades of this HealthcheckAutoupdateAutoupdate.  # noqa: E501

        Number of failed upgrade attempts.  # noqa: E501

        :return: The number_of_failed_upgrades of this HealthcheckAutoupdateAutoupdate.  # noqa: E501
        :rtype: int
        """
        return self._number_of_failed_upgrades

    @number_of_failed_upgrades.setter
    def number_of_failed_upgrades(self, number_of_failed_upgrades):
        """Sets the number_of_failed_upgrades of this HealthcheckAutoupdateAutoupdate.

        Number of failed upgrade attempts.  # noqa: E501

        :param number_of_failed_upgrades: The number_of_failed_upgrades of this HealthcheckAutoupdateAutoupdate.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                number_of_failed_upgrades is not None and number_of_failed_upgrades > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `number_of_failed_upgrades`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self._configuration.client_side_validation and
                number_of_failed_upgrades is not None and number_of_failed_upgrades < 0):  # noqa: E501
            raise ValueError("Invalid value for `number_of_failed_upgrades`, must be a value greater than or equal to `0`")  # noqa: E501

        self._number_of_failed_upgrades = number_of_failed_upgrades

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
        if issubclass(HealthcheckAutoupdateAutoupdate, dict):
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
        if not isinstance(other, HealthcheckAutoupdateAutoupdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HealthcheckAutoupdateAutoupdate):
            return True

        return self.to_dict() != other.to_dict()
