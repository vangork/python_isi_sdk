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


class ProvidersSamlServicesIdpsIdp(object):
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
        'entity_id': 'str',
        'id': 'str',
        'login': 'ProvidersSamlServicesIdpLogin',
        'logout': 'ProvidersSamlServicesIdpLogout',
        'metadata_location': 'str',
        'signing_certificate': 'CreateProvidersSamlServicesCertExtractItemResponseCertificateInfo',
        'type': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'id': 'id',
        'login': 'login',
        'logout': 'logout',
        'metadata_location': 'metadata_location',
        'signing_certificate': 'signing_certificate',
        'type': 'type'
    }

    def __init__(self, entity_id=None, id=None, login=None, logout=None, metadata_location=None, signing_certificate=None, type=None, _configuration=None):  # noqa: E501
        """ProvidersSamlServicesIdpsIdp - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._entity_id = None
        self._id = None
        self._login = None
        self._logout = None
        self._metadata_location = None
        self._signing_certificate = None
        self._type = None
        self.discriminator = None

        if entity_id is not None:
            self.entity_id = entity_id
        if id is not None:
            self.id = id
        if login is not None:
            self.login = login
        if logout is not None:
            self.logout = logout
        if metadata_location is not None:
            self.metadata_location = metadata_location
        if signing_certificate is not None:
            self.signing_certificate = signing_certificate
        if type is not None:
            self.type = type

    @property
    def entity_id(self):
        """Gets the entity_id of this ProvidersSamlServicesIdpsIdp.  # noqa: E501

        Unique identifier of the IDP.  # noqa: E501

        :return: The entity_id of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this ProvidersSamlServicesIdpsIdp.

        Unique identifier of the IDP.  # noqa: E501

        :param entity_id: The entity_id of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                entity_id is not None and len(entity_id) > 1024):
            raise ValueError("Invalid value for `entity_id`, length must be less than or equal to `1024`")  # noqa: E501
        if (self._configuration.client_side_validation and
                entity_id is not None and len(entity_id) < 0):
            raise ValueError("Invalid value for `entity_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def id(self):
        """Gets the id of this ProvidersSamlServicesIdpsIdp.  # noqa: E501

        Unique identifier of a SAML service resource.  # noqa: E501

        :return: The id of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProvidersSamlServicesIdpsIdp.

        Unique identifier of a SAML service resource.  # noqa: E501

        :param id: The id of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
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
    def login(self):
        """Gets the login of this ProvidersSamlServicesIdpsIdp.  # noqa: E501

        Login endpoint of the IDP. This specifies the method and location PowerScale will use to send AuthnRequest messages to the IDP.  # noqa: E501

        :return: The login of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :rtype: ProvidersSamlServicesIdpLogin
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this ProvidersSamlServicesIdpsIdp.

        Login endpoint of the IDP. This specifies the method and location PowerScale will use to send AuthnRequest messages to the IDP.  # noqa: E501

        :param login: The login of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :type: ProvidersSamlServicesIdpLogin
        """

        self._login = login

    @property
    def logout(self):
        """Gets the logout of this ProvidersSamlServicesIdpsIdp.  # noqa: E501

          # noqa: E501

        :return: The logout of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :rtype: ProvidersSamlServicesIdpLogout
        """
        return self._logout

    @logout.setter
    def logout(self, logout):
        """Sets the logout of this ProvidersSamlServicesIdpsIdp.

          # noqa: E501

        :param logout: The logout of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :type: ProvidersSamlServicesIdpLogout
        """

        self._logout = logout

    @property
    def metadata_location(self):
        """Gets the metadata_location of this ProvidersSamlServicesIdpsIdp.  # noqa: E501

        Metadata location of the SAML provider.  # noqa: E501

        :return: The metadata_location of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :rtype: str
        """
        return self._metadata_location

    @metadata_location.setter
    def metadata_location(self, metadata_location):
        """Sets the metadata_location of this ProvidersSamlServicesIdpsIdp.

        Metadata location of the SAML provider.  # noqa: E501

        :param metadata_location: The metadata_location of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                metadata_location is not None and len(metadata_location) > 2048):
            raise ValueError("Invalid value for `metadata_location`, length must be less than or equal to `2048`")  # noqa: E501
        if (self._configuration.client_side_validation and
                metadata_location is not None and len(metadata_location) < 0):
            raise ValueError("Invalid value for `metadata_location`, length must be greater than or equal to `0`")  # noqa: E501

        self._metadata_location = metadata_location

    @property
    def signing_certificate(self):
        """Gets the signing_certificate of this ProvidersSamlServicesIdpsIdp.  # noqa: E501

        Certificate with information about it.  # noqa: E501

        :return: The signing_certificate of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :rtype: CreateProvidersSamlServicesCertExtractItemResponseCertificateInfo
        """
        return self._signing_certificate

    @signing_certificate.setter
    def signing_certificate(self, signing_certificate):
        """Sets the signing_certificate of this ProvidersSamlServicesIdpsIdp.

        Certificate with information about it.  # noqa: E501

        :param signing_certificate: The signing_certificate of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :type: CreateProvidersSamlServicesCertExtractItemResponseCertificateInfo
        """

        self._signing_certificate = signing_certificate

    @property
    def type(self):
        """Gets the type of this ProvidersSamlServicesIdpsIdp.  # noqa: E501

        How the IDP was configured and how it can be updated. When set to \"metadata\" metadata XML was used to configure the IDP and can be used to update it. When set to \"manual\" the IDP was manually configured and can be manually updated.  # noqa: E501

        :return: The type of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProvidersSamlServicesIdpsIdp.

        How the IDP was configured and how it can be updated. When set to \"metadata\" metadata XML was used to configure the IDP and can be used to update it. When set to \"manual\" the IDP was manually configured and can be manually updated.  # noqa: E501

        :param type: The type of this ProvidersSamlServicesIdpsIdp.  # noqa: E501
        :type: str
        """
        allowed_values = ["metadata", "manual"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ProvidersSamlServicesIdpsIdp, dict):
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
        if not isinstance(other, ProvidersSamlServicesIdpsIdp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProvidersSamlServicesIdpsIdp):
            return True

        return self.to_dict() != other.to_dict()
