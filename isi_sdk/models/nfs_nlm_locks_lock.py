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


class NfsNlmLocksLock(object):
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
        'client': 'str',
        'client_id': 'str',
        'created': 'int',
        'id': 'str',
        'lin': 'str',
        'lock_type': 'str',
        'path': 'str',
        'range': 'list[int]'
    }

    attribute_map = {
        'client': 'client',
        'client_id': 'client_id',
        'created': 'created',
        'id': 'id',
        'lin': 'lin',
        'lock_type': 'lock_type',
        'path': 'path',
        'range': 'range'
    }

    def __init__(self, client=None, client_id=None, created=None, id=None, lin=None, lock_type=None, path=None, range=None, _configuration=None):  # noqa: E501
        """NfsNlmLocksLock - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client = None
        self._client_id = None
        self._created = None
        self._id = None
        self._lin = None
        self._lock_type = None
        self._path = None
        self._range = None
        self.discriminator = None

        if client is not None:
            self.client = client
        if client_id is not None:
            self.client_id = client_id
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if lin is not None:
            self.lin = lin
        if lock_type is not None:
            self.lock_type = lock_type
        if path is not None:
            self.path = path
        if range is not None:
            self.range = range

    @property
    def client(self):
        """Gets the client of this NfsNlmLocksLock.  # noqa: E501

        Specifies the client host name and IP address.  # noqa: E501

        :return: The client of this NfsNlmLocksLock.  # noqa: E501
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this NfsNlmLocksLock.

        Specifies the client host name and IP address.  # noqa: E501

        :param client: The client of this NfsNlmLocksLock.  # noqa: E501
        :type: str
        """

        self._client = client

    @property
    def client_id(self):
        """Gets the client_id of this NfsNlmLocksLock.  # noqa: E501

        Specifies the client ID.  # noqa: E501

        :return: The client_id of this NfsNlmLocksLock.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this NfsNlmLocksLock.

        Specifies the client ID.  # noqa: E501

        :param client_id: The client_id of this NfsNlmLocksLock.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def created(self):
        """Gets the created of this NfsNlmLocksLock.  # noqa: E501

        Specifies the UNIX EPoch time that the lock was created.  # noqa: E501

        :return: The created of this NfsNlmLocksLock.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NfsNlmLocksLock.

        Specifies the UNIX EPoch time that the lock was created.  # noqa: E501

        :param created: The created of this NfsNlmLocksLock.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this NfsNlmLocksLock.  # noqa: E501

        Specifies the system-assigned ID given to the lock. This value is returned when the lock is created with the POST method.  # noqa: E501

        :return: The id of this NfsNlmLocksLock.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NfsNlmLocksLock.

        Specifies the system-assigned ID given to the lock. This value is returned when the lock is created with the POST method.  # noqa: E501

        :param id: The id of this NfsNlmLocksLock.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def lin(self):
        """Gets the lin of this NfsNlmLocksLock.  # noqa: E501

        Specifies the LIN in /ifs that is locked.  # noqa: E501

        :return: The lin of this NfsNlmLocksLock.  # noqa: E501
        :rtype: str
        """
        return self._lin

    @lin.setter
    def lin(self, lin):
        """Sets the lin of this NfsNlmLocksLock.

        Specifies the LIN in /ifs that is locked.  # noqa: E501

        :param lin: The lin of this NfsNlmLocksLock.  # noqa: E501
        :type: str
        """

        self._lin = lin

    @property
    def lock_type(self):
        """Gets the lock_type of this NfsNlmLocksLock.  # noqa: E501

        Specifies the lock type.  # noqa: E501

        :return: The lock_type of this NfsNlmLocksLock.  # noqa: E501
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        """Sets the lock_type of this NfsNlmLocksLock.

        Specifies the lock type.  # noqa: E501

        :param lock_type: The lock_type of this NfsNlmLocksLock.  # noqa: E501
        :type: str
        """

        self._lock_type = lock_type

    @property
    def path(self):
        """Gets the path of this NfsNlmLocksLock.  # noqa: E501

        Specifies the path under /ifs that is locked.  # noqa: E501

        :return: The path of this NfsNlmLocksLock.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NfsNlmLocksLock.

        Specifies the path under /ifs that is locked.  # noqa: E501

        :param path: The path of this NfsNlmLocksLock.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def range(self):
        """Gets the range of this NfsNlmLocksLock.  # noqa: E501

        Specifies the byte range within the locked file.  # noqa: E501

        :return: The range of this NfsNlmLocksLock.  # noqa: E501
        :rtype: list[int]
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this NfsNlmLocksLock.

        Specifies the byte range within the locked file.  # noqa: E501

        :param range: The range of this NfsNlmLocksLock.  # noqa: E501
        :type: list[int]
        """

        self._range = range

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
        if issubclass(NfsNlmLocksLock, dict):
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
        if not isinstance(other, NfsNlmLocksLock):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NfsNlmLocksLock):
            return True

        return self.to_dict() != other.to_dict()
