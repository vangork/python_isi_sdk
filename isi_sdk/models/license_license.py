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


class LicenseLicense(object):
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
        'days_since_expiry': 'int',
        'days_to_expiry': 'int',
        'expiration': 'str',
        'expired_alert': 'bool',
        'expiring_alert': 'bool',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'tiers': 'list[LicenseLicenseTier]'
    }

    attribute_map = {
        'days_since_expiry': 'days_since_expiry',
        'days_to_expiry': 'days_to_expiry',
        'expiration': 'expiration',
        'expired_alert': 'expired_alert',
        'expiring_alert': 'expiring_alert',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'tiers': 'tiers'
    }

    def __init__(self, days_since_expiry=None, days_to_expiry=None, expiration=None, expired_alert=None, expiring_alert=None, id=None, name=None, status=None, tiers=None, _configuration=None):  # noqa: E501
        """LicenseLicense - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._days_since_expiry = None
        self._days_to_expiry = None
        self._expiration = None
        self._expired_alert = None
        self._expiring_alert = None
        self._id = None
        self._name = None
        self._status = None
        self._tiers = None
        self.discriminator = None

        if days_since_expiry is not None:
            self.days_since_expiry = days_since_expiry
        if days_to_expiry is not None:
            self.days_to_expiry = days_to_expiry
        if expiration is not None:
            self.expiration = expiration
        self.expired_alert = expired_alert
        self.expiring_alert = expiring_alert
        self.id = id
        self.name = name
        self.status = status
        self.tiers = tiers

    @property
    def days_since_expiry(self):
        """Gets the days_since_expiry of this LicenseLicense.  # noqa: E501

        Number of days since a license expired.  # noqa: E501

        :return: The days_since_expiry of this LicenseLicense.  # noqa: E501
        :rtype: int
        """
        return self._days_since_expiry

    @days_since_expiry.setter
    def days_since_expiry(self, days_since_expiry):
        """Sets the days_since_expiry of this LicenseLicense.

        Number of days since a license expired.  # noqa: E501

        :param days_since_expiry: The days_since_expiry of this LicenseLicense.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                days_since_expiry is not None and days_since_expiry > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `days_since_expiry`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self._configuration.client_side_validation and
                days_since_expiry is not None and days_since_expiry < 0):  # noqa: E501
            raise ValueError("Invalid value for `days_since_expiry`, must be a value greater than or equal to `0`")  # noqa: E501

        self._days_since_expiry = days_since_expiry

    @property
    def days_to_expiry(self):
        """Gets the days_to_expiry of this LicenseLicense.  # noqa: E501

        Number of days before a license expires.  # noqa: E501

        :return: The days_to_expiry of this LicenseLicense.  # noqa: E501
        :rtype: int
        """
        return self._days_to_expiry

    @days_to_expiry.setter
    def days_to_expiry(self, days_to_expiry):
        """Sets the days_to_expiry of this LicenseLicense.

        Number of days before a license expires.  # noqa: E501

        :param days_to_expiry: The days_to_expiry of this LicenseLicense.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                days_to_expiry is not None and days_to_expiry > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `days_to_expiry`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self._configuration.client_side_validation and
                days_to_expiry is not None and days_to_expiry < 0):  # noqa: E501
            raise ValueError("Invalid value for `days_to_expiry`, must be a value greater than or equal to `0`")  # noqa: E501

        self._days_to_expiry = days_to_expiry

    @property
    def expiration(self):
        """Gets the expiration of this LicenseLicense.  # noqa: E501

        Date of license expiry. Format is YYYY-MM-DD. It is not included if there is no expiration. Feature is considered expired at end of this day. The cluster time is used to determine expiry.  # noqa: E501

        :return: The expiration of this LicenseLicense.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this LicenseLicense.

        Date of license expiry. Format is YYYY-MM-DD. It is not included if there is no expiration. Feature is considered expired at end of this day. The cluster time is used to determine expiry.  # noqa: E501

        :param expiration: The expiration of this LicenseLicense.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                expiration is not None and len(expiration) > 10):
            raise ValueError("Invalid value for `expiration`, length must be less than or equal to `10`")  # noqa: E501
        if (self._configuration.client_side_validation and
                expiration is not None and len(expiration) < 10):
            raise ValueError("Invalid value for `expiration`, length must be greater than or equal to `10`")  # noqa: E501
        if (self._configuration.client_side_validation and
                expiration is not None and not re.search(r'^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$', expiration)):  # noqa: E501
            raise ValueError(r"Invalid value for `expiration`, must be a follow pattern or equal to `/^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/`")  # noqa: E501

        self._expiration = expiration

    @property
    def expired_alert(self):
        """Gets the expired_alert of this LicenseLicense.  # noqa: E501

        True when we are generating an alert that this feature has expired.  # noqa: E501

        :return: The expired_alert of this LicenseLicense.  # noqa: E501
        :rtype: bool
        """
        return self._expired_alert

    @expired_alert.setter
    def expired_alert(self, expired_alert):
        """Sets the expired_alert of this LicenseLicense.

        True when we are generating an alert that this feature has expired.  # noqa: E501

        :param expired_alert: The expired_alert of this LicenseLicense.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and expired_alert is None:
            raise ValueError("Invalid value for `expired_alert`, must not be `None`")  # noqa: E501

        self._expired_alert = expired_alert

    @property
    def expiring_alert(self):
        """Gets the expiring_alert of this LicenseLicense.  # noqa: E501

        True when we are generating an alert that this feature is expiring.  # noqa: E501

        :return: The expiring_alert of this LicenseLicense.  # noqa: E501
        :rtype: bool
        """
        return self._expiring_alert

    @expiring_alert.setter
    def expiring_alert(self, expiring_alert):
        """Sets the expiring_alert of this LicenseLicense.

        True when we are generating an alert that this feature is expiring.  # noqa: E501

        :param expiring_alert: The expiring_alert of this LicenseLicense.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and expiring_alert is None:
            raise ValueError("Invalid value for `expiring_alert`, must not be `None`")  # noqa: E501

        self._expiring_alert = expiring_alert

    @property
    def id(self):
        """Gets the id of this LicenseLicense.  # noqa: E501

        Name of the licensed feature.  # noqa: E501

        :return: The id of this LicenseLicense.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LicenseLicense.

        Name of the licensed feature.  # noqa: E501

        :param id: The id of this LicenseLicense.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and len(id) > 50):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and not re.search(r'.+', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/.+/`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this LicenseLicense.  # noqa: E501

        Name of the licensed feature.  # noqa: E501

        :return: The name of this LicenseLicense.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LicenseLicense.

        Name of the licensed feature.  # noqa: E501

        :param name: The name of this LicenseLicense.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 50):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and not re.search(r'.+', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/.+/`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this LicenseLicense.  # noqa: E501

        Current status of the license.  # noqa: E501

        :return: The status of this LicenseLicense.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LicenseLicense.

        Current status of the license.  # noqa: E501

        :param status: The status of this LicenseLicense.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Unlicensed", "Licensed", "Expired", "Evaluation", "Evaluation Expired"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tiers(self):
        """Gets the tiers of this LicenseLicense.  # noqa: E501

        Tiered License details.  # noqa: E501

        :return: The tiers of this LicenseLicense.  # noqa: E501
        :rtype: list[LicenseLicenseTier]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this LicenseLicense.

        Tiered License details.  # noqa: E501

        :param tiers: The tiers of this LicenseLicense.  # noqa: E501
        :type: list[LicenseLicenseTier]
        """
        if self._configuration.client_side_validation and tiers is None:
            raise ValueError("Invalid value for `tiers`, must not be `None`")  # noqa: E501

        self._tiers = tiers

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
        if issubclass(LicenseLicense, dict):
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
        if not isinstance(other, LicenseLicense):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicenseLicense):
            return True

        return self.to_dict() != other.to_dict()
