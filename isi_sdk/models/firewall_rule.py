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


class FirewallRule(object):
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
        'action': 'str',
        'description': 'str',
        'dst_ports': 'PoliciesPolicyRuleDstPorts',
        'id': 'str',
        'index': 'int',
        'name': 'str',
        'protocol': 'str',
        'src_networks': 'list[str]',
        'src_ports': 'PoliciesPolicyRuleDstPorts'
    }

    attribute_map = {
        'action': 'action',
        'description': 'description',
        'dst_ports': 'dst_ports',
        'id': 'id',
        'index': 'index',
        'name': 'name',
        'protocol': 'protocol',
        'src_networks': 'src_networks',
        'src_ports': 'src_ports'
    }

    def __init__(self, action=None, description=None, dst_ports=None, id=None, index=None, name=None, protocol=None, src_networks=None, src_ports=None, _configuration=None):  # noqa: E501
        """FirewallRule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._description = None
        self._dst_ports = None
        self._id = None
        self._index = None
        self._name = None
        self._protocol = None
        self._src_networks = None
        self._src_ports = None
        self.discriminator = None

        self.action = action
        self.description = description
        self.dst_ports = dst_ports
        self.id = id
        self.index = index
        self.name = name
        self.protocol = protocol
        self.src_networks = src_networks
        self.src_ports = src_ports

    @property
    def action(self):
        """Gets the action of this FirewallRule.  # noqa: E501

        Rule action  # noqa: E501

        :return: The action of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this FirewallRule.

        Rule action  # noqa: E501

        :param action: The action of this FirewallRule.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["allow", "deny", "reject"]  # noqa: E501
        if (self._configuration.client_side_validation and
                action not in allowed_values):
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def description(self):
        """Gets the description of this FirewallRule.  # noqa: E501

        A description of the firewall rule.  # noqa: E501

        :return: The description of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FirewallRule.

        A description of the firewall rule.  # noqa: E501

        :param description: The description of this FirewallRule.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 128):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def dst_ports(self):
        """Gets the dst_ports of this FirewallRule.  # noqa: E501

        Customer specified protocols or OneFS default services's protocols for destination control  # noqa: E501

        :return: The dst_ports of this FirewallRule.  # noqa: E501
        :rtype: PoliciesPolicyRuleDstPorts
        """
        return self._dst_ports

    @dst_ports.setter
    def dst_ports(self, dst_ports):
        """Sets the dst_ports of this FirewallRule.

        Customer specified protocols or OneFS default services's protocols for destination control  # noqa: E501

        :param dst_ports: The dst_ports of this FirewallRule.  # noqa: E501
        :type: PoliciesPolicyRuleDstPorts
        """
        if self._configuration.client_side_validation and dst_ports is None:
            raise ValueError("Invalid value for `dst_ports`, must not be `None`")  # noqa: E501

        self._dst_ports = dst_ports

    @property
    def id(self):
        """Gets the id of this FirewallRule.  # noqa: E501

        Unique firewall rule ID   # noqa: E501

        :return: The id of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirewallRule.

        Unique firewall rule ID   # noqa: E501

        :param id: The id of this FirewallRule.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and len(id) > 66):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `66`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def index(self):
        """Gets the index of this FirewallRule.  # noqa: E501

        Firewall rule index in policy  # noqa: E501

        :return: The index of this FirewallRule.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this FirewallRule.

        Firewall rule index in policy  # noqa: E501

        :param index: The index of this FirewallRule.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                index is not None and index > 200):  # noqa: E501
            raise ValueError("Invalid value for `index`, must be a value less than or equal to `200`")  # noqa: E501
        if (self._configuration.client_side_validation and
                index is not None and index < 1):  # noqa: E501
            raise ValueError("Invalid value for `index`, must be a value greater than or equal to `1`")  # noqa: E501

        self._index = index

    @property
    def name(self):
        """Gets the name of this FirewallRule.  # noqa: E501

        The name of the firewall rule.  # noqa: E501

        :return: The name of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FirewallRule.

        The name of the firewall rule.  # noqa: E501

        :param name: The name of this FirewallRule.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 32):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and not re.search(r'^[0-9a-zA-Z_-]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[0-9a-zA-Z_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this FirewallRule.  # noqa: E501

        Firewall rule set on protocol  # noqa: E501

        :return: The protocol of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this FirewallRule.

        Firewall rule set on protocol  # noqa: E501

        :param protocol: The protocol of this FirewallRule.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["ALL", "TCP", "UDP", "ICMP", "ICMP6"]  # noqa: E501
        if (self._configuration.client_side_validation and
                protocol not in allowed_values):
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def src_networks(self):
        """Gets the src_networks of this FirewallRule.  # noqa: E501

        Source Networks  # noqa: E501

        :return: The src_networks of this FirewallRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._src_networks

    @src_networks.setter
    def src_networks(self, src_networks):
        """Sets the src_networks of this FirewallRule.

        Source Networks  # noqa: E501

        :param src_networks: The src_networks of this FirewallRule.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and src_networks is None:
            raise ValueError("Invalid value for `src_networks`, must not be `None`")  # noqa: E501

        self._src_networks = src_networks

    @property
    def src_ports(self):
        """Gets the src_ports of this FirewallRule.  # noqa: E501

        Customer specified protocols or OneFS default services's protocols for source control  # noqa: E501

        :return: The src_ports of this FirewallRule.  # noqa: E501
        :rtype: PoliciesPolicyRuleDstPorts
        """
        return self._src_ports

    @src_ports.setter
    def src_ports(self, src_ports):
        """Sets the src_ports of this FirewallRule.

        Customer specified protocols or OneFS default services's protocols for source control  # noqa: E501

        :param src_ports: The src_ports of this FirewallRule.  # noqa: E501
        :type: PoliciesPolicyRuleDstPorts
        """
        if self._configuration.client_side_validation and src_ports is None:
            raise ValueError("Invalid value for `src_ports`, must not be `None`")  # noqa: E501

        self._src_ports = src_ports

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
        if issubclass(FirewallRule, dict):
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
        if not isinstance(other, FirewallRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FirewallRule):
            return True

        return self.to_dict() != other.to_dict()
