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


class StoragepoolNodetype(object):
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
        'id': 'int',
        'manual': 'bool',
        'nodes': 'list[int]',
        'product_name': 'str',
        'sjm_capable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'manual': 'manual',
        'nodes': 'nodes',
        'product_name': 'product_name',
        'sjm_capable': 'sjm_capable'
    }

    def __init__(self, id=None, manual=None, nodes=None, product_name=None, sjm_capable=None, _configuration=None):  # noqa: E501
        """StoragepoolNodetype - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._manual = None
        self._nodes = None
        self._product_name = None
        self._sjm_capable = None
        self.discriminator = None

        self.id = id
        self.manual = manual
        self.nodes = nodes
        self.product_name = product_name
        self.sjm_capable = sjm_capable

    @property
    def id(self):
        """Gets the id of this StoragepoolNodetype.  # noqa: E501

        The system ID given to the nodetype.  # noqa: E501

        :return: The id of this StoragepoolNodetype.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoragepoolNodetype.

        The system ID given to the nodetype.  # noqa: E501

        :param id: The id of this StoragepoolNodetype.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and id < 1):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def manual(self):
        """Gets the manual of this StoragepoolNodetype.  # noqa: E501

        Whether or not the nodetype is in a manually managed node pool.  # noqa: E501

        :return: The manual of this StoragepoolNodetype.  # noqa: E501
        :rtype: bool
        """
        return self._manual

    @manual.setter
    def manual(self, manual):
        """Sets the manual of this StoragepoolNodetype.

        Whether or not the nodetype is in a manually managed node pool.  # noqa: E501

        :param manual: The manual of this StoragepoolNodetype.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and manual is None:
            raise ValueError("Invalid value for `manual`, must not be `None`")  # noqa: E501

        self._manual = manual

    @property
    def nodes(self):
        """Gets the nodes of this StoragepoolNodetype.  # noqa: E501

        The nodes that are part of this nodetype.  # noqa: E501

        :return: The nodes of this StoragepoolNodetype.  # noqa: E501
        :rtype: list[int]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this StoragepoolNodetype.

        The nodes that are part of this nodetype.  # noqa: E501

        :param nodes: The nodes of this StoragepoolNodetype.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        self._nodes = nodes

    @property
    def product_name(self):
        """Gets the product_name of this StoragepoolNodetype.  # noqa: E501

        The product name of the node type.  # noqa: E501

        :return: The product_name of this StoragepoolNodetype.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this StoragepoolNodetype.

        The product name of the node type.  # noqa: E501

        :param product_name: The product_name of this StoragepoolNodetype.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_name is None:
            raise ValueError("Invalid value for `product_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                product_name is not None and len(product_name) > 255):
            raise ValueError("Invalid value for `product_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                product_name is not None and len(product_name) < 1):
            raise ValueError("Invalid value for `product_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._product_name = product_name

    @property
    def sjm_capable(self):
        """Gets the sjm_capable of this StoragepoolNodetype.  # noqa: E501

        Whether SJM is supported by this nodetype  # noqa: E501

        :return: The sjm_capable of this StoragepoolNodetype.  # noqa: E501
        :rtype: bool
        """
        return self._sjm_capable

    @sjm_capable.setter
    def sjm_capable(self, sjm_capable):
        """Sets the sjm_capable of this StoragepoolNodetype.

        Whether SJM is supported by this nodetype  # noqa: E501

        :param sjm_capable: The sjm_capable of this StoragepoolNodetype.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and sjm_capable is None:
            raise ValueError("Invalid value for `sjm_capable`, must not be `None`")  # noqa: E501

        self._sjm_capable = sjm_capable

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
        if issubclass(StoragepoolNodetype, dict):
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
        if not isinstance(other, StoragepoolNodetype):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StoragepoolNodetype):
            return True

        return self.to_dict() != other.to_dict()
