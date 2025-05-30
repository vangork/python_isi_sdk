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


class HealthcheckChecklistExtended(object):
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
        'description': 'str',
        'id': 'str',
        'internal': 'bool',
        'items': 'list[HealthcheckChecklistItem]'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'internal': 'internal',
        'items': 'items'
    }

    def __init__(self, description=None, id=None, internal=None, items=None, _configuration=None):  # noqa: E501
        """HealthcheckChecklistExtended - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._id = None
        self._internal = None
        self._items = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if internal is not None:
            self.internal = internal
        if items is not None:
            self.items = items

    @property
    def description(self):
        """Gets the description of this HealthcheckChecklistExtended.  # noqa: E501

        Description covering intended use  # noqa: E501

        :return: The description of this HealthcheckChecklistExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HealthcheckChecklistExtended.

        Description covering intended use  # noqa: E501

        :param description: The description of this HealthcheckChecklistExtended.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 8192):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `8192`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this HealthcheckChecklistExtended.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this HealthcheckChecklistExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthcheckChecklistExtended.

        Unique identifier  # noqa: E501

        :param id: The id of this HealthcheckChecklistExtended.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                id is not None and len(id) > 255):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and len(id) < 0):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def internal(self):
        """Gets the internal of this HealthcheckChecklistExtended.  # noqa: E501

        Hide checklist or not  # noqa: E501

        :return: The internal of this HealthcheckChecklistExtended.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this HealthcheckChecklistExtended.

        Hide checklist or not  # noqa: E501

        :param internal: The internal of this HealthcheckChecklistExtended.  # noqa: E501
        :type: bool
        """

        self._internal = internal

    @property
    def items(self):
        """Gets the items of this HealthcheckChecklistExtended.  # noqa: E501

        Items to be evaluated  # noqa: E501

        :return: The items of this HealthcheckChecklistExtended.  # noqa: E501
        :rtype: list[HealthcheckChecklistItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this HealthcheckChecklistExtended.

        Items to be evaluated  # noqa: E501

        :param items: The items of this HealthcheckChecklistExtended.  # noqa: E501
        :type: list[HealthcheckChecklistItem]
        """

        self._items = items

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
        if issubclass(HealthcheckChecklistExtended, dict):
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
        if not isinstance(other, HealthcheckChecklistExtended):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HealthcheckChecklistExtended):
            return True

        return self.to_dict() != other.to_dict()
