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


class CloudAccountCredentialProvider(object):
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
        'agency': 'str',
        'certificate': 'str',
        'mission': 'str',
        'proxy': 'str',
        'role': 'str',
        'type': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'agency': 'agency',
        'certificate': 'certificate',
        'mission': 'mission',
        'proxy': 'proxy',
        'role': 'role',
        'type': 'type',
        'uri': 'uri'
    }

    def __init__(self, agency=None, certificate=None, mission=None, proxy=None, role=None, type=None, uri=None, _configuration=None):  # noqa: E501
        """CloudAccountCredentialProvider - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agency = None
        self._certificate = None
        self._mission = None
        self._proxy = None
        self._role = None
        self._type = None
        self._uri = None
        self.discriminator = None

        if agency is not None:
            self.agency = agency
        if certificate is not None:
            self.certificate = certificate
        if mission is not None:
            self.mission = mission
        if proxy is not None:
            self.proxy = proxy
        if role is not None:
            self.role = role
        if type is not None:
            self.type = type
        if uri is not None:
            self.uri = uri

    @property
    def agency(self):
        """Gets the agency of this CloudAccountCredentialProvider.  # noqa: E501

        The agency name used to request credentials from the credential provider  # noqa: E501

        :return: The agency of this CloudAccountCredentialProvider.  # noqa: E501
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this CloudAccountCredentialProvider.

        The agency name used to request credentials from the credential provider  # noqa: E501

        :param agency: The agency of this CloudAccountCredentialProvider.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                agency is not None and len(agency) > 255):
            raise ValueError("Invalid value for `agency`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                agency is not None and len(agency) < 0):
            raise ValueError("Invalid value for `agency`, length must be greater than or equal to `0`")  # noqa: E501

        self._agency = agency

    @property
    def certificate(self):
        """Gets the certificate of this CloudAccountCredentialProvider.  # noqa: E501

        The id or name of a certificate used to connect to the credential provider  # noqa: E501

        :return: The certificate of this CloudAccountCredentialProvider.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CloudAccountCredentialProvider.

        The id or name of a certificate used to connect to the credential provider  # noqa: E501

        :param certificate: The certificate of this CloudAccountCredentialProvider.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                certificate is not None and len(certificate) > 512):
            raise ValueError("Invalid value for `certificate`, length must be less than or equal to `512`")  # noqa: E501
        if (self._configuration.client_side_validation and
                certificate is not None and len(certificate) < 0):
            raise ValueError("Invalid value for `certificate`, length must be greater than or equal to `0`")  # noqa: E501

        self._certificate = certificate

    @property
    def mission(self):
        """Gets the mission of this CloudAccountCredentialProvider.  # noqa: E501

        The mission name used to request credentials from the credential provider  # noqa: E501

        :return: The mission of this CloudAccountCredentialProvider.  # noqa: E501
        :rtype: str
        """
        return self._mission

    @mission.setter
    def mission(self, mission):
        """Sets the mission of this CloudAccountCredentialProvider.

        The mission name used to request credentials from the credential provider  # noqa: E501

        :param mission: The mission of this CloudAccountCredentialProvider.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                mission is not None and len(mission) > 255):
            raise ValueError("Invalid value for `mission`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                mission is not None and len(mission) < 0):
            raise ValueError("Invalid value for `mission`, length must be greater than or equal to `0`")  # noqa: E501

        self._mission = mission

    @property
    def proxy(self):
        """Gets the proxy of this CloudAccountCredentialProvider.  # noqa: E501

        The id or name of a proxy used to connect to the credential provider  # noqa: E501

        :return: The proxy of this CloudAccountCredentialProvider.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CloudAccountCredentialProvider.

        The id or name of a proxy used to connect to the credential provider  # noqa: E501

        :param proxy: The proxy of this CloudAccountCredentialProvider.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                proxy is not None and len(proxy) > 1024):
            raise ValueError("Invalid value for `proxy`, length must be less than or equal to `1024`")  # noqa: E501
        if (self._configuration.client_side_validation and
                proxy is not None and len(proxy) < 0):
            raise ValueError("Invalid value for `proxy`, length must be greater than or equal to `0`")  # noqa: E501

        self._proxy = proxy

    @property
    def role(self):
        """Gets the role of this CloudAccountCredentialProvider.  # noqa: E501

        The role name used to request credentials from the credential provider  # noqa: E501

        :return: The role of this CloudAccountCredentialProvider.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this CloudAccountCredentialProvider.

        The role name used to request credentials from the credential provider  # noqa: E501

        :param role: The role of this CloudAccountCredentialProvider.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                role is not None and len(role) > 255):
            raise ValueError("Invalid value for `role`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                role is not None and len(role) < 0):
            raise ValueError("Invalid value for `role`, length must be greater than or equal to `0`")  # noqa: E501

        self._role = role

    @property
    def type(self):
        """Gets the type of this CloudAccountCredentialProvider.  # noqa: E501

        The type of credential provider  # noqa: E501

        :return: The type of this CloudAccountCredentialProvider.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudAccountCredentialProvider.

        The type of credential provider  # noqa: E501

        :param type: The type of this CloudAccountCredentialProvider.  # noqa: E501
        :type: str
        """
        allowed_values = ["c2s-s3"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def uri(self):
        """Gets the uri of this CloudAccountCredentialProvider.  # noqa: E501

        The URI of the credential provider  # noqa: E501

        :return: The uri of this CloudAccountCredentialProvider.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this CloudAccountCredentialProvider.

        The URI of the credential provider  # noqa: E501

        :param uri: The uri of this CloudAccountCredentialProvider.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                uri is not None and len(uri) > 2048):
            raise ValueError("Invalid value for `uri`, length must be less than or equal to `2048`")  # noqa: E501
        if (self._configuration.client_side_validation and
                uri is not None and len(uri) < 0):
            raise ValueError("Invalid value for `uri`, length must be greater than or equal to `0`")  # noqa: E501

        self._uri = uri

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
        if issubclass(CloudAccountCredentialProvider, dict):
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
        if not isinstance(other, CloudAccountCredentialProvider):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudAccountCredentialProvider):
            return True

        return self.to_dict() != other.to_dict()
