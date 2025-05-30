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


class AuditLogs(object):
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
        'before': 'str',
        'blocker': 'list[AuditLogsBlockerItem]',
        'deletion': 'list[AuditLogsDeletionItem]',
        'status': 'str'
    }

    attribute_map = {
        'before': 'before',
        'blocker': 'blocker',
        'deletion': 'deletion',
        'status': 'status'
    }

    def __init__(self, before=None, blocker=None, deletion=None, status=None, _configuration=None):  # noqa: E501
        """AuditLogs - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._before = None
        self._blocker = None
        self._deletion = None
        self._status = None
        self.discriminator = None

        if before is not None:
            self.before = before
        if blocker is not None:
            self.blocker = blocker
        if deletion is not None:
            self.deletion = deletion
        if status is not None:
            self.status = status

    @property
    def before(self):
        """Gets the before of this AuditLogs.  # noqa: E501

        The date which the current purging process will delete logs before.  # noqa: E501

        :return: The before of this AuditLogs.  # noqa: E501
        :rtype: str
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this AuditLogs.

        The date which the current purging process will delete logs before.  # noqa: E501

        :param before: The before of this AuditLogs.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                before is not None and len(before) > 255):
            raise ValueError("Invalid value for `before`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                before is not None and len(before) < 0):
            raise ValueError("Invalid value for `before`, length must be greater than or equal to `0`")  # noqa: E501

        self._before = before

    @property
    def blocker(self):
        """Gets the blocker of this AuditLogs.  # noqa: E501

        The status ot the consumers that blocked the deletion.  # noqa: E501

        :return: The blocker of this AuditLogs.  # noqa: E501
        :rtype: list[AuditLogsBlockerItem]
        """
        return self._blocker

    @blocker.setter
    def blocker(self, blocker):
        """Sets the blocker of this AuditLogs.

        The status ot the consumers that blocked the deletion.  # noqa: E501

        :param blocker: The blocker of this AuditLogs.  # noqa: E501
        :type: list[AuditLogsBlockerItem]
        """

        self._blocker = blocker

    @property
    def deletion(self):
        """Gets the deletion of this AuditLogs.  # noqa: E501

        Deleted result on each node.  # noqa: E501

        :return: The deletion of this AuditLogs.  # noqa: E501
        :rtype: list[AuditLogsDeletionItem]
        """
        return self._deletion

    @deletion.setter
    def deletion(self, deletion):
        """Sets the deletion of this AuditLogs.

        Deleted result on each node.  # noqa: E501

        :param deletion: The deletion of this AuditLogs.  # noqa: E501
        :type: list[AuditLogsDeletionItem]
        """

        self._deletion = deletion

    @property
    def status(self):
        """Gets the status of this AuditLogs.  # noqa: E501

        Status of current manual purging.  # noqa: E501

        :return: The status of this AuditLogs.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuditLogs.

        Status of current manual purging.  # noqa: E501

        :param status: The status of this AuditLogs.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                status is not None and len(status) > 255):
            raise ValueError("Invalid value for `status`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                status is not None and len(status) < 0):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `0`")  # noqa: E501

        self._status = status

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
        if issubclass(AuditLogs, dict):
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
        if not isinstance(other, AuditLogs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditLogs):
            return True

        return self.to_dict() != other.to_dict()
