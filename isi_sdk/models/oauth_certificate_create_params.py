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


class OauthCertificateCreateParams(object):
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
        'certificate': 'str',
        'certificate_format': 'str',
        'passphrase': 'str',
        'private_key': 'str',
        'scope': 'str',
        'service': 'str',
        'type': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'certificate_format': 'certificate_format',
        'passphrase': 'passphrase',
        'private_key': 'private_key',
        'scope': 'scope',
        'service': 'service',
        'type': 'type'
    }

    def __init__(self, certificate=None, certificate_format=None, passphrase=None, private_key=None, scope=None, service=None, type=None, _configuration=None):  # noqa: E501
        """OauthCertificateCreateParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._certificate = None
        self._certificate_format = None
        self._passphrase = None
        self._private_key = None
        self._scope = None
        self._service = None
        self._type = None
        self.discriminator = None

        self.certificate = certificate
        self.certificate_format = certificate_format
        if passphrase is not None:
            self.passphrase = passphrase
        if private_key is not None:
            self.private_key = private_key
        if scope is not None:
            self.scope = scope
        self.service = service
        self.type = type

    @property
    def certificate(self):
        """Gets the certificate of this OauthCertificateCreateParams.  # noqa: E501

        The certificate content encoded as PEM string (including header, footer and line break).  # noqa: E501

        :return: The certificate of this OauthCertificateCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this OauthCertificateCreateParams.

        The certificate content encoded as PEM string (including header, footer and line break).  # noqa: E501

        :param certificate: The certificate of this OauthCertificateCreateParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and certificate is None:
            raise ValueError("Invalid value for `certificate`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                certificate is not None and len(certificate) > 8192):
            raise ValueError("Invalid value for `certificate`, length must be less than or equal to `8192`")  # noqa: E501
        if (self._configuration.client_side_validation and
                certificate is not None and len(certificate) < 1):
            raise ValueError("Invalid value for `certificate`, length must be greater than or equal to `1`")  # noqa: E501

        self._certificate = certificate

    @property
    def certificate_format(self):
        """Gets the certificate_format of this OauthCertificateCreateParams.  # noqa: E501

        The encoding format of the certificate string.  # noqa: E501

        :return: The certificate_format of this OauthCertificateCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._certificate_format

    @certificate_format.setter
    def certificate_format(self, certificate_format):
        """Sets the certificate_format of this OauthCertificateCreateParams.

        The encoding format of the certificate string.  # noqa: E501

        :param certificate_format: The certificate_format of this OauthCertificateCreateParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and certificate_format is None:
            raise ValueError("Invalid value for `certificate_format`, must not be `None`")  # noqa: E501
        allowed_values = ["PEM", "PKCS7"]  # noqa: E501
        if (self._configuration.client_side_validation and
                certificate_format not in allowed_values):
            raise ValueError(
                "Invalid value for `certificate_format` ({0}), must be one of {1}"  # noqa: E501
                .format(certificate_format, allowed_values)
            )

        self._certificate_format = certificate_format

    @property
    def passphrase(self):
        """Gets the passphrase of this OauthCertificateCreateParams.  # noqa: E501

        Passphrase used to encrypt private key.  # noqa: E501

        :return: The passphrase of this OauthCertificateCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """Sets the passphrase of this OauthCertificateCreateParams.

        Passphrase used to encrypt private key.  # noqa: E501

        :param passphrase: The passphrase of this OauthCertificateCreateParams.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                passphrase is not None and len(passphrase) > 256):
            raise ValueError("Invalid value for `passphrase`, length must be less than or equal to `256`")  # noqa: E501
        if (self._configuration.client_side_validation and
                passphrase is not None and len(passphrase) < 1):
            raise ValueError("Invalid value for `passphrase`, length must be greater than or equal to `1`")  # noqa: E501

        self._passphrase = passphrase

    @property
    def private_key(self):
        """Gets the private_key of this OauthCertificateCreateParams.  # noqa: E501

        PEM encoded (including header, footer and line break) private key following encrypted PKCS8.  # noqa: E501

        :return: The private_key of this OauthCertificateCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this OauthCertificateCreateParams.

        PEM encoded (including header, footer and line break) private key following encrypted PKCS8.  # noqa: E501

        :param private_key: The private_key of this OauthCertificateCreateParams.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                private_key is not None and len(private_key) > 8192):
            raise ValueError("Invalid value for `private_key`, length must be less than or equal to `8192`")  # noqa: E501
        if (self._configuration.client_side_validation and
                private_key is not None and len(private_key) < 1):
            raise ValueError("Invalid value for `private_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._private_key = private_key

    @property
    def scope(self):
        """Gets the scope of this OauthCertificateCreateParams.  # noqa: E501

        Scope narrows the application of a certificate to a specific instance of a service.  # noqa: E501

        :return: The scope of this OauthCertificateCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OauthCertificateCreateParams.

        Scope narrows the application of a certificate to a specific instance of a service.  # noqa: E501

        :param scope: The scope of this OauthCertificateCreateParams.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                scope is not None and len(scope) > 255):
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                scope is not None and len(scope) < 1):
            raise ValueError("Invalid value for `scope`, length must be greater than or equal to `1`")  # noqa: E501

        self._scope = scope

    @property
    def service(self):
        """Gets the service of this OauthCertificateCreateParams.  # noqa: E501

        The kind of the service for which the certificate is used.  # noqa: E501

        :return: The service of this OauthCertificateCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this OauthCertificateCreateParams.

        The kind of the service for which the certificate is used.  # noqa: E501

        :param service: The service of this OauthCertificateCreateParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501
        allowed_values = ["ALL", "MANAGEMENT_HTTPS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                service not in allowed_values):
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def type(self):
        """Gets the type of this OauthCertificateCreateParams.  # noqa: E501

        Whether the certificate is used as client or server certificate, and whether it is a CA certificate.  # noqa: E501

        :return: The type of this OauthCertificateCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OauthCertificateCreateParams.

        Whether the certificate is used as client or server certificate, and whether it is a CA certificate.  # noqa: E501

        :param type: The type of this OauthCertificateCreateParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["SERVER", "CLIENT", "CA", "CRYPTOGRAPHY"]  # noqa: E501
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
        if issubclass(OauthCertificateCreateParams, dict):
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
        if not isinstance(other, OauthCertificateCreateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OauthCertificateCreateParams):
            return True

        return self.to_dict() != other.to_dict()
