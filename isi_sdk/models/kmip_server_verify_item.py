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


class KmipServerVerifyItem(object):
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
        'ca_cert_path': 'str',
        'client_cert_password': 'str',
        'client_cert_path': 'str',
        'connection_timeout': 'int',
        'host': 'str',
        'minimum_tls_version': 'str',
        'port': 'int',
        'retry_timeout': 'int',
        'tls_ciphers': 'str'
    }

    attribute_map = {
        'ca_cert_path': 'ca_cert_path',
        'client_cert_password': 'client_cert_password',
        'client_cert_path': 'client_cert_path',
        'connection_timeout': 'connection_timeout',
        'host': 'host',
        'minimum_tls_version': 'minimum_tls_version',
        'port': 'port',
        'retry_timeout': 'retry_timeout',
        'tls_ciphers': 'tls_ciphers'
    }

    def __init__(self, ca_cert_path=None, client_cert_password=None, client_cert_path=None, connection_timeout=None, host=None, minimum_tls_version=None, port=None, retry_timeout=None, tls_ciphers=None, _configuration=None):  # noqa: E501
        """KmipServerVerifyItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ca_cert_path = None
        self._client_cert_password = None
        self._client_cert_path = None
        self._connection_timeout = None
        self._host = None
        self._minimum_tls_version = None
        self._port = None
        self._retry_timeout = None
        self._tls_ciphers = None
        self.discriminator = None

        self.ca_cert_path = ca_cert_path
        if client_cert_password is not None:
            self.client_cert_password = client_cert_password
        self.client_cert_path = client_cert_path
        if connection_timeout is not None:
            self.connection_timeout = connection_timeout
        self.host = host
        if minimum_tls_version is not None:
            self.minimum_tls_version = minimum_tls_version
        if port is not None:
            self.port = port
        if retry_timeout is not None:
            self.retry_timeout = retry_timeout
        if tls_ciphers is not None:
            self.tls_ciphers = tls_ciphers

    @property
    def ca_cert_path(self):
        """Gets the ca_cert_path of this KmipServerVerifyItem.  # noqa: E501

        Certification Authority (CA) certificate, used for TLS Mutual Authentication with the KMIP Server.  # noqa: E501

        :return: The ca_cert_path of this KmipServerVerifyItem.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert_path

    @ca_cert_path.setter
    def ca_cert_path(self, ca_cert_path):
        """Sets the ca_cert_path of this KmipServerVerifyItem.

        Certification Authority (CA) certificate, used for TLS Mutual Authentication with the KMIP Server.  # noqa: E501

        :param ca_cert_path: The ca_cert_path of this KmipServerVerifyItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ca_cert_path is None:
            raise ValueError("Invalid value for `ca_cert_path`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                ca_cert_path is not None and len(ca_cert_path) > 4096):
            raise ValueError("Invalid value for `ca_cert_path`, length must be less than or equal to `4096`")  # noqa: E501
        if (self._configuration.client_side_validation and
                ca_cert_path is not None and len(ca_cert_path) < 1):
            raise ValueError("Invalid value for `ca_cert_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._ca_cert_path = ca_cert_path

    @property
    def client_cert_password(self):
        """Gets the client_cert_password of this KmipServerVerifyItem.  # noqa: E501

        Cluster identity private key password.  # noqa: E501

        :return: The client_cert_password of this KmipServerVerifyItem.  # noqa: E501
        :rtype: str
        """
        return self._client_cert_password

    @client_cert_password.setter
    def client_cert_password(self, client_cert_password):
        """Sets the client_cert_password of this KmipServerVerifyItem.

        Cluster identity private key password.  # noqa: E501

        :param client_cert_password: The client_cert_password of this KmipServerVerifyItem.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                client_cert_password is not None and len(client_cert_password) > 255):
            raise ValueError("Invalid value for `client_cert_password`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                client_cert_password is not None and len(client_cert_password) < 1):
            raise ValueError("Invalid value for `client_cert_password`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_cert_password = client_cert_password

    @property
    def client_cert_path(self):
        """Gets the client_cert_path of this KmipServerVerifyItem.  # noqa: E501

        Cluster identity certificate and private key used for TLS Mutual Authentication with the KMIP Server.  # noqa: E501

        :return: The client_cert_path of this KmipServerVerifyItem.  # noqa: E501
        :rtype: str
        """
        return self._client_cert_path

    @client_cert_path.setter
    def client_cert_path(self, client_cert_path):
        """Sets the client_cert_path of this KmipServerVerifyItem.

        Cluster identity certificate and private key used for TLS Mutual Authentication with the KMIP Server.  # noqa: E501

        :param client_cert_path: The client_cert_path of this KmipServerVerifyItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and client_cert_path is None:
            raise ValueError("Invalid value for `client_cert_path`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                client_cert_path is not None and len(client_cert_path) > 4096):
            raise ValueError("Invalid value for `client_cert_path`, length must be less than or equal to `4096`")  # noqa: E501
        if (self._configuration.client_side_validation and
                client_cert_path is not None and len(client_cert_path) < 1):
            raise ValueError("Invalid value for `client_cert_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_cert_path = client_cert_path

    @property
    def connection_timeout(self):
        """Gets the connection_timeout of this KmipServerVerifyItem.  # noqa: E501

        KMIP RPC connection timeout in seconds.  # noqa: E501

        :return: The connection_timeout of this KmipServerVerifyItem.  # noqa: E501
        :rtype: int
        """
        return self._connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, connection_timeout):
        """Sets the connection_timeout of this KmipServerVerifyItem.

        KMIP RPC connection timeout in seconds.  # noqa: E501

        :param connection_timeout: The connection_timeout of this KmipServerVerifyItem.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                connection_timeout is not None and connection_timeout > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `connection_timeout`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                connection_timeout is not None and connection_timeout < 0):  # noqa: E501
            raise ValueError("Invalid value for `connection_timeout`, must be a value greater than or equal to `0`")  # noqa: E501

        self._connection_timeout = connection_timeout

    @property
    def host(self):
        """Gets the host of this KmipServerVerifyItem.  # noqa: E501

        KMIP server hostname.  # noqa: E501

        :return: The host of this KmipServerVerifyItem.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this KmipServerVerifyItem.

        KMIP server hostname.  # noqa: E501

        :param host: The host of this KmipServerVerifyItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                host is not None and len(host) > 256):
            raise ValueError("Invalid value for `host`, length must be less than or equal to `256`")  # noqa: E501
        if (self._configuration.client_side_validation and
                host is not None and len(host) < 1):
            raise ValueError("Invalid value for `host`, length must be greater than or equal to `1`")  # noqa: E501

        self._host = host

    @property
    def minimum_tls_version(self):
        """Gets the minimum_tls_version of this KmipServerVerifyItem.  # noqa: E501

        Denotes the minimum TLS version supported by the KTP. Default value is set to '1.2'. Supported versions: '1.1', '1.2' and '1.3'.  # noqa: E501

        :return: The minimum_tls_version of this KmipServerVerifyItem.  # noqa: E501
        :rtype: str
        """
        return self._minimum_tls_version

    @minimum_tls_version.setter
    def minimum_tls_version(self, minimum_tls_version):
        """Sets the minimum_tls_version of this KmipServerVerifyItem.

        Denotes the minimum TLS version supported by the KTP. Default value is set to '1.2'. Supported versions: '1.1', '1.2' and '1.3'.  # noqa: E501

        :param minimum_tls_version: The minimum_tls_version of this KmipServerVerifyItem.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                minimum_tls_version is not None and len(minimum_tls_version) > 3):
            raise ValueError("Invalid value for `minimum_tls_version`, length must be less than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                minimum_tls_version is not None and len(minimum_tls_version) < 3):
            raise ValueError("Invalid value for `minimum_tls_version`, length must be greater than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                minimum_tls_version is not None and not re.search(r'^[0-9]{1}[.][0-9]{1}$', minimum_tls_version)):  # noqa: E501
            raise ValueError(r"Invalid value for `minimum_tls_version`, must be a follow pattern or equal to `/^[0-9]{1}[.][0-9]{1}$/`")  # noqa: E501

        self._minimum_tls_version = minimum_tls_version

    @property
    def port(self):
        """Gets the port of this KmipServerVerifyItem.  # noqa: E501

        KMIP server port.  # noqa: E501

        :return: The port of this KmipServerVerifyItem.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this KmipServerVerifyItem.

        KMIP server port.  # noqa: E501

        :param port: The port of this KmipServerVerifyItem.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                port is not None and port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port is not None and port < 1):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._port = port

    @property
    def retry_timeout(self):
        """Gets the retry_timeout of this KmipServerVerifyItem.  # noqa: E501

        KMIP RPC retry timeout in milliseconds.  # noqa: E501

        :return: The retry_timeout of this KmipServerVerifyItem.  # noqa: E501
        :rtype: int
        """
        return self._retry_timeout

    @retry_timeout.setter
    def retry_timeout(self, retry_timeout):
        """Sets the retry_timeout of this KmipServerVerifyItem.

        KMIP RPC retry timeout in milliseconds.  # noqa: E501

        :param retry_timeout: The retry_timeout of this KmipServerVerifyItem.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                retry_timeout is not None and retry_timeout > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `retry_timeout`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                retry_timeout is not None and retry_timeout < 0):  # noqa: E501
            raise ValueError("Invalid value for `retry_timeout`, must be a value greater than or equal to `0`")  # noqa: E501

        self._retry_timeout = retry_timeout

    @property
    def tls_ciphers(self):
        """Gets the tls_ciphers of this KmipServerVerifyItem.  # noqa: E501

        TLS cipher suite to use for communication with the KMIP server.  # noqa: E501

        :return: The tls_ciphers of this KmipServerVerifyItem.  # noqa: E501
        :rtype: str
        """
        return self._tls_ciphers

    @tls_ciphers.setter
    def tls_ciphers(self, tls_ciphers):
        """Sets the tls_ciphers of this KmipServerVerifyItem.

        TLS cipher suite to use for communication with the KMIP server.  # noqa: E501

        :param tls_ciphers: The tls_ciphers of this KmipServerVerifyItem.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                tls_ciphers is not None and len(tls_ciphers) > 8192):
            raise ValueError("Invalid value for `tls_ciphers`, length must be less than or equal to `8192`")  # noqa: E501
        if (self._configuration.client_side_validation and
                tls_ciphers is not None and len(tls_ciphers) < 0):
            raise ValueError("Invalid value for `tls_ciphers`, length must be greater than or equal to `0`")  # noqa: E501

        self._tls_ciphers = tls_ciphers

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
        if issubclass(KmipServerVerifyItem, dict):
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
        if not isinstance(other, KmipServerVerifyItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KmipServerVerifyItem):
            return True

        return self.to_dict() != other.to_dict()
