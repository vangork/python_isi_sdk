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


class ClusterDrain(object):
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
        'drain_nodes': 'list[int]',
        'task': 'str'
    }

    attribute_map = {
        'action': 'action',
        'drain_nodes': 'drain_nodes',
        'task': 'task'
    }

    def __init__(self, action=None, drain_nodes=None, task=None, _configuration=None):  # noqa: E501
        """ClusterDrain - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._drain_nodes = None
        self._task = None
        self.discriminator = None

        self.action = action
        self.drain_nodes = drain_nodes
        self.task = task

    @property
    def action(self):
        """Gets the action of this ClusterDrain.  # noqa: E501

        The desired drain action, ex. delay or skip.  # noqa: E501

        :return: The action of this ClusterDrain.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ClusterDrain.

        The desired drain action, ex. delay or skip.  # noqa: E501

        :param action: The action of this ClusterDrain.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["delay", "skip"]  # noqa: E501
        if (self._configuration.client_side_validation and
                action not in allowed_values):
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def drain_nodes(self):
        """Gets the drain_nodes of this ClusterDrain.  # noqa: E501

        The nodes to alter drain action in the existing upgrade.For skip action only, 'all' is valid.   # noqa: E501

        :return: The drain_nodes of this ClusterDrain.  # noqa: E501
        :rtype: list[int]
        """
        return self._drain_nodes

    @drain_nodes.setter
    def drain_nodes(self, drain_nodes):
        """Sets the drain_nodes of this ClusterDrain.

        The nodes to alter drain action in the existing upgrade.For skip action only, 'all' is valid.   # noqa: E501

        :param drain_nodes: The drain_nodes of this ClusterDrain.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and drain_nodes is None:
            raise ValueError("Invalid value for `drain_nodes`, must not be `None`")  # noqa: E501

        self._drain_nodes = drain_nodes

    @property
    def task(self):
        """Gets the task of this ClusterDrain.  # noqa: E501

        The desired drain task, ex. add or remove nodes.  # noqa: E501

        :return: The task of this ClusterDrain.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this ClusterDrain.

        The desired drain task, ex. add or remove nodes.  # noqa: E501

        :param task: The task of this ClusterDrain.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and task is None:
            raise ValueError("Invalid value for `task`, must not be `None`")  # noqa: E501
        allowed_values = ["add", "remove"]  # noqa: E501
        if (self._configuration.client_side_validation and
                task not in allowed_values):
            raise ValueError(
                "Invalid value for `task` ({0}), must be one of {1}"  # noqa: E501
                .format(task, allowed_values)
            )

        self._task = task

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
        if issubclass(ClusterDrain, dict):
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
        if not isinstance(other, ClusterDrain):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterDrain):
            return True

        return self.to_dict() != other.to_dict()
