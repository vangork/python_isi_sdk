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


class SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem(object):
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
        'attribute_exists': 'bool',
        'case_sensitive': 'bool',
        'field': 'str',
        'operator': 'str',
        'type': 'str',
        'value': 'str',
        'whole_word': 'bool'
    }

    attribute_map = {
        'attribute_exists': 'attribute_exists',
        'case_sensitive': 'case_sensitive',
        'field': 'field',
        'operator': 'operator',
        'type': 'type',
        'value': 'value',
        'whole_word': 'whole_word'
    }

    def __init__(self, attribute_exists=None, case_sensitive=None, field=None, operator=None, type=None, value=None, whole_word=None, _configuration=None):  # noqa: E501
        """SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_exists = None
        self._case_sensitive = None
        self._field = None
        self._operator = None
        self._type = None
        self._value = None
        self._whole_word = None
        self.discriminator = None

        if attribute_exists is not None:
            self.attribute_exists = attribute_exists
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if field is not None:
            self.field = field
        if operator is not None:
            self.operator = operator
        self.type = type
        if value is not None:
            self.value = value
        if whole_word is not None:
            self.whole_word = whole_word

    @property
    def attribute_exists(self):
        """Gets the attribute_exists of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501

        For \"custom_attribute\" type criteria.  The file will match as long as the attribute named by \"field\" exists.  Default is true.  # noqa: E501

        :return: The attribute_exists of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :rtype: bool
        """
        return self._attribute_exists

    @attribute_exists.setter
    def attribute_exists(self, attribute_exists):
        """Sets the attribute_exists of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.

        For \"custom_attribute\" type criteria.  The file will match as long as the attribute named by \"field\" exists.  Default is true.  # noqa: E501

        :param attribute_exists: The attribute_exists of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :type: bool
        """

        self._attribute_exists = attribute_exists

    @property
    def case_sensitive(self):
        """Gets the case_sensitive of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501

        If true, the value comparison will be case sensitive.  Default is true.  # noqa: E501

        :return: The case_sensitive of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """Sets the case_sensitive of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.

        If true, the value comparison will be case sensitive.  Default is true.  # noqa: E501

        :param case_sensitive: The case_sensitive of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :type: bool
        """

        self._case_sensitive = case_sensitive

    @property
    def field(self):
        """Gets the field of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501

        The name of the file attribute to match on (only required if this is a custom_attribute type criterion).  Default is an empty string \"\".  # noqa: E501

        :return: The field of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.

        The name of the file attribute to match on (only required if this is a custom_attribute type criterion).  Default is an empty string \"\".  # noqa: E501

        :param field: The field of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                field is not None and len(field) > 255):
            raise ValueError("Invalid value for `field`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                field is not None and len(field) < 0):
            raise ValueError("Invalid value for `field`, length must be greater than or equal to `0`")  # noqa: E501

        self._field = field

    @property
    def operator(self):
        """Gets the operator of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501

        How to compare the specified attribute of each file to the specified value.  # noqa: E501

        :return: The operator of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.

        How to compare the specified attribute of each file to the specified value.  # noqa: E501

        :param operator: The operator of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def type(self):
        """Gets the type of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501

        The type of this criterion, that is, which file attribute to match on.  # noqa: E501

        :return: The type of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.

        The type of this criterion, that is, which file attribute to match on.  # noqa: E501

        :param type: The type of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["name", "path", "accessed_time", "accessed_before", "accessed_after", "birth_time", "birth_before", "birth_after", "changed_time", "changed_before", "changed_after", "size", "file_type", "posix_regex_name", "user_name", "user_id", "group_name", "group_id", "no_user", "no_group"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501

        The value to compare the specified attribute of each file to.  # noqa: E501

        :return: The value of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.

        The value to compare the specified attribute of each file to.  # noqa: E501

        :param value: The value of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def whole_word(self):
        """Gets the whole_word of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501

        If true, the attribute must match the entire word.  Default is true.  # noqa: E501

        :return: The whole_word of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :rtype: bool
        """
        return self._whole_word

    @whole_word.setter
    def whole_word(self, whole_word):
        """Sets the whole_word of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.

        If true, the attribute must match the entire word.  Default is true.  # noqa: E501

        :param whole_word: The whole_word of this SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem.  # noqa: E501
        :type: bool
        """

        self._whole_word = whole_word

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
        if issubclass(SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem, dict):
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
        if not isinstance(other, SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem):
            return True

        return self.to_dict() != other.to_dict()
