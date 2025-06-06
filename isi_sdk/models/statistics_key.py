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


class StatisticsKey(object):
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
        'aggregation_type': 'str',
        'base_name': 'str',
        'default_cache_time': 'int',
        'description': 'str',
        'key': 'str',
        'policies': 'list[StatisticsKeyPolicy]',
        'policy_cache_time': 'int',
        'real_name': 'str',
        'scope': 'str',
        'type': 'str',
        'units': 'str'
    }

    attribute_map = {
        'aggregation_type': 'aggregation_type',
        'base_name': 'base_name',
        'default_cache_time': 'default_cache_time',
        'description': 'description',
        'key': 'key',
        'policies': 'policies',
        'policy_cache_time': 'policy_cache_time',
        'real_name': 'real_name',
        'scope': 'scope',
        'type': 'type',
        'units': 'units'
    }

    def __init__(self, aggregation_type=None, base_name=None, default_cache_time=None, description=None, key=None, policies=None, policy_cache_time=None, real_name=None, scope=None, type=None, units=None, _configuration=None):  # noqa: E501
        """StatisticsKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._aggregation_type = None
        self._base_name = None
        self._default_cache_time = None
        self._description = None
        self._key = None
        self._policies = None
        self._policy_cache_time = None
        self._real_name = None
        self._scope = None
        self._type = None
        self._units = None
        self.discriminator = None

        self.aggregation_type = aggregation_type
        if base_name is not None:
            self.base_name = base_name
        self.default_cache_time = default_cache_time
        self.description = description
        self.key = key
        if policies is not None:
            self.policies = policies
        if policy_cache_time is not None:
            self.policy_cache_time = policy_cache_time
        if real_name is not None:
            self.real_name = real_name
        self.scope = scope
        self.type = type
        self.units = units

    @property
    def aggregation_type(self):
        """Gets the aggregation_type of this StatisticsKey.  # noqa: E501

        Type of aggregation used in down-sampling.  # noqa: E501

        :return: The aggregation_type of this StatisticsKey.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """Sets the aggregation_type of this StatisticsKey.

        Type of aggregation used in down-sampling.  # noqa: E501

        :param aggregation_type: The aggregation_type of this StatisticsKey.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and aggregation_type is None:
            raise ValueError("Invalid value for `aggregation_type`, must not be `None`")  # noqa: E501
        allowed_values = ["last", "min", "max", "avg", "sum", "custom"]  # noqa: E501
        if (self._configuration.client_side_validation and
                aggregation_type not in allowed_values):
            raise ValueError(
                "Invalid value for `aggregation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_type, allowed_values)
            )

        self._aggregation_type = aggregation_type

    @property
    def base_name(self):
        """Gets the base_name of this StatisticsKey.  # noqa: E501

        Name of key this keys is derived from, if any.  # noqa: E501

        :return: The base_name of this StatisticsKey.  # noqa: E501
        :rtype: str
        """
        return self._base_name

    @base_name.setter
    def base_name(self, base_name):
        """Sets the base_name of this StatisticsKey.

        Name of key this keys is derived from, if any.  # noqa: E501

        :param base_name: The base_name of this StatisticsKey.  # noqa: E501
        :type: str
        """

        self._base_name = base_name

    @property
    def default_cache_time(self):
        """Gets the default_cache_time of this StatisticsKey.  # noqa: E501

        Default time in seconds system will used cached values.  # noqa: E501

        :return: The default_cache_time of this StatisticsKey.  # noqa: E501
        :rtype: int
        """
        return self._default_cache_time

    @default_cache_time.setter
    def default_cache_time(self, default_cache_time):
        """Sets the default_cache_time of this StatisticsKey.

        Default time in seconds system will used cached values.  # noqa: E501

        :param default_cache_time: The default_cache_time of this StatisticsKey.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and default_cache_time is None:
            raise ValueError("Invalid value for `default_cache_time`, must not be `None`")  # noqa: E501

        self._default_cache_time = default_cache_time

    @property
    def description(self):
        """Gets the description of this StatisticsKey.  # noqa: E501

        Description of statistics key.  # noqa: E501

        :return: The description of this StatisticsKey.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StatisticsKey.

        Description of statistics key.  # noqa: E501

        :param description: The description of this StatisticsKey.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def key(self):
        """Gets the key of this StatisticsKey.  # noqa: E501

        Key name.  # noqa: E501

        :return: The key of this StatisticsKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this StatisticsKey.

        Key name.  # noqa: E501

        :param key: The key of this StatisticsKey.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def policies(self):
        """Gets the policies of this StatisticsKey.  # noqa: E501

        List of effective history policies for key.  # noqa: E501

        :return: The policies of this StatisticsKey.  # noqa: E501
        :rtype: list[StatisticsKeyPolicy]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this StatisticsKey.

        List of effective history policies for key.  # noqa: E501

        :param policies: The policies of this StatisticsKey.  # noqa: E501
        :type: list[StatisticsKeyPolicy]
        """

        self._policies = policies

    @property
    def policy_cache_time(self):
        """Gets the policy_cache_time of this StatisticsKey.  # noqa: E501

        Configured time in seconds system will used cached values.  # noqa: E501

        :return: The policy_cache_time of this StatisticsKey.  # noqa: E501
        :rtype: int
        """
        return self._policy_cache_time

    @policy_cache_time.setter
    def policy_cache_time(self, policy_cache_time):
        """Sets the policy_cache_time of this StatisticsKey.

        Configured time in seconds system will used cached values.  # noqa: E501

        :param policy_cache_time: The policy_cache_time of this StatisticsKey.  # noqa: E501
        :type: int
        """

        self._policy_cache_time = policy_cache_time

    @property
    def real_name(self):
        """Gets the real_name of this StatisticsKey.  # noqa: E501

        Name of real key if this is an alias.  # noqa: E501

        :return: The real_name of this StatisticsKey.  # noqa: E501
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """Sets the real_name of this StatisticsKey.

        Name of real key if this is an alias.  # noqa: E501

        :param real_name: The real_name of this StatisticsKey.  # noqa: E501
        :type: str
        """

        self._real_name = real_name

    @property
    def scope(self):
        """Gets the scope of this StatisticsKey.  # noqa: E501

        Scope of key.  # noqa: E501

        :return: The scope of this StatisticsKey.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this StatisticsKey.

        Scope of key.  # noqa: E501

        :param scope: The scope of this StatisticsKey.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501
        allowed_values = ["cluster", "node"]  # noqa: E501
        if (self._configuration.client_side_validation and
                scope not in allowed_values):
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def type(self):
        """Gets the type of this StatisticsKey.  # noqa: E501

        Data type of key values.  # noqa: E501

        :return: The type of this StatisticsKey.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StatisticsKey.

        Data type of key values.  # noqa: E501

        :param type: The type of this StatisticsKey.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def units(self):
        """Gets the units of this StatisticsKey.  # noqa: E501

        Units of key values.  # noqa: E501

        :return: The units of this StatisticsKey.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this StatisticsKey.

        Units of key values.  # noqa: E501

        :param units: The units of this StatisticsKey.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501

        self._units = units

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
        if issubclass(StatisticsKey, dict):
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
        if not isinstance(other, StatisticsKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatisticsKey):
            return True

        return self.to_dict() != other.to_dict()
