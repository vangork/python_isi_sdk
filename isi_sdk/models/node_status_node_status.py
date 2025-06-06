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


class NodeStatusNodeStatus(object):
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
        'av_vendor': 'str',
        'blocking_events': 'list[str]',
        'cee_version': 'str',
        'dtd_version': 'str',
        'server_status': 'list[NodeStatusNodeStatusServerStatusItem]',
        'signature_timestamp': 'str',
        'system_stats': 'NodeStatusNodeStatusSystemStats',
        'system_status': 'str'
    }

    attribute_map = {
        'av_vendor': 'av_vendor',
        'blocking_events': 'blocking_events',
        'cee_version': 'cee_version',
        'dtd_version': 'dtd_version',
        'server_status': 'server_status',
        'signature_timestamp': 'signature_timestamp',
        'system_stats': 'system_stats',
        'system_status': 'system_status'
    }

    def __init__(self, av_vendor=None, blocking_events=None, cee_version=None, dtd_version=None, server_status=None, signature_timestamp=None, system_stats=None, system_status=None, _configuration=None):  # noqa: E501
        """NodeStatusNodeStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._av_vendor = None
        self._blocking_events = None
        self._cee_version = None
        self._dtd_version = None
        self._server_status = None
        self._signature_timestamp = None
        self._system_stats = None
        self._system_status = None
        self.discriminator = None

        if av_vendor is not None:
            self.av_vendor = av_vendor
        if blocking_events is not None:
            self.blocking_events = blocking_events
        if cee_version is not None:
            self.cee_version = cee_version
        if dtd_version is not None:
            self.dtd_version = dtd_version
        if server_status is not None:
            self.server_status = server_status
        if signature_timestamp is not None:
            self.signature_timestamp = signature_timestamp
        if system_stats is not None:
            self.system_stats = system_stats
        if system_status is not None:
            self.system_status = system_status

    @property
    def av_vendor(self):
        """Gets the av_vendor of this NodeStatusNodeStatus.  # noqa: E501

        Name of antivirus engine for scanning files.  # noqa: E501

        :return: The av_vendor of this NodeStatusNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._av_vendor

    @av_vendor.setter
    def av_vendor(self, av_vendor):
        """Sets the av_vendor of this NodeStatusNodeStatus.

        Name of antivirus engine for scanning files.  # noqa: E501

        :param av_vendor: The av_vendor of this NodeStatusNodeStatus.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                av_vendor is not None and len(av_vendor) > 255):
            raise ValueError("Invalid value for `av_vendor`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                av_vendor is not None and len(av_vendor) < 1):
            raise ValueError("Invalid value for `av_vendor`, length must be greater than or equal to `1`")  # noqa: E501

        self._av_vendor = av_vendor

    @property
    def blocking_events(self):
        """Gets the blocking_events of this NodeStatusNodeStatus.  # noqa: E501

        List of blocking event strings if CAVA is FAULTED  # noqa: E501

        :return: The blocking_events of this NodeStatusNodeStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._blocking_events

    @blocking_events.setter
    def blocking_events(self, blocking_events):
        """Sets the blocking_events of this NodeStatusNodeStatus.

        List of blocking event strings if CAVA is FAULTED  # noqa: E501

        :param blocking_events: The blocking_events of this NodeStatusNodeStatus.  # noqa: E501
        :type: list[str]
        """

        self._blocking_events = blocking_events

    @property
    def cee_version(self):
        """Gets the cee_version of this NodeStatusNodeStatus.  # noqa: E501

        Remote CEE software version string.  # noqa: E501

        :return: The cee_version of this NodeStatusNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._cee_version

    @cee_version.setter
    def cee_version(self, cee_version):
        """Sets the cee_version of this NodeStatusNodeStatus.

        Remote CEE software version string.  # noqa: E501

        :param cee_version: The cee_version of this NodeStatusNodeStatus.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cee_version is not None and len(cee_version) > 255):
            raise ValueError("Invalid value for `cee_version`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                cee_version is not None and len(cee_version) < 1):
            raise ValueError("Invalid value for `cee_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._cee_version = cee_version

    @property
    def dtd_version(self):
        """Gets the dtd_version of this NodeStatusNodeStatus.  # noqa: E501

        Document type definition version for message exchanges.  # noqa: E501

        :return: The dtd_version of this NodeStatusNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._dtd_version

    @dtd_version.setter
    def dtd_version(self, dtd_version):
        """Sets the dtd_version of this NodeStatusNodeStatus.

        Document type definition version for message exchanges.  # noqa: E501

        :param dtd_version: The dtd_version of this NodeStatusNodeStatus.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                dtd_version is not None and len(dtd_version) > 255):
            raise ValueError("Invalid value for `dtd_version`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                dtd_version is not None and len(dtd_version) < 1):
            raise ValueError("Invalid value for `dtd_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._dtd_version = dtd_version

    @property
    def server_status(self):
        """Gets the server_status of this NodeStatusNodeStatus.  # noqa: E501

        Specifies the list of CAVA servers along with their status.  # noqa: E501

        :return: The server_status of this NodeStatusNodeStatus.  # noqa: E501
        :rtype: list[NodeStatusNodeStatusServerStatusItem]
        """
        return self._server_status

    @server_status.setter
    def server_status(self, server_status):
        """Sets the server_status of this NodeStatusNodeStatus.

        Specifies the list of CAVA servers along with their status.  # noqa: E501

        :param server_status: The server_status of this NodeStatusNodeStatus.  # noqa: E501
        :type: list[NodeStatusNodeStatusServerStatusItem]
        """

        self._server_status = server_status

    @property
    def signature_timestamp(self):
        """Gets the signature_timestamp of this NodeStatusNodeStatus.  # noqa: E501

        Timestamp of the last antivirus signature update.  # noqa: E501

        :return: The signature_timestamp of this NodeStatusNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._signature_timestamp

    @signature_timestamp.setter
    def signature_timestamp(self, signature_timestamp):
        """Sets the signature_timestamp of this NodeStatusNodeStatus.

        Timestamp of the last antivirus signature update.  # noqa: E501

        :param signature_timestamp: The signature_timestamp of this NodeStatusNodeStatus.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                signature_timestamp is not None and len(signature_timestamp) > 255):
            raise ValueError("Invalid value for `signature_timestamp`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                signature_timestamp is not None and len(signature_timestamp) < 1):
            raise ValueError("Invalid value for `signature_timestamp`, length must be greater than or equal to `1`")  # noqa: E501

        self._signature_timestamp = signature_timestamp

    @property
    def system_stats(self):
        """Gets the system_stats of this NodeStatusNodeStatus.  # noqa: E501

        Specifies properties for CAVA system statistics.  # noqa: E501

        :return: The system_stats of this NodeStatusNodeStatus.  # noqa: E501
        :rtype: NodeStatusNodeStatusSystemStats
        """
        return self._system_stats

    @system_stats.setter
    def system_stats(self, system_stats):
        """Sets the system_stats of this NodeStatusNodeStatus.

        Specifies properties for CAVA system statistics.  # noqa: E501

        :param system_stats: The system_stats of this NodeStatusNodeStatus.  # noqa: E501
        :type: NodeStatusNodeStatusSystemStats
        """

        self._system_stats = system_stats

    @property
    def system_status(self):
        """Gets the system_status of this NodeStatusNodeStatus.  # noqa: E501

        Status of the CAVA antivirus system.  # noqa: E501

        :return: The system_status of this NodeStatusNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._system_status

    @system_status.setter
    def system_status(self, system_status):
        """Sets the system_status of this NodeStatusNodeStatus.

        Status of the CAVA antivirus system.  # noqa: E501

        :param system_status: The system_status of this NodeStatusNodeStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["DISABLED", "RUNNING", "FAULTED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                system_status not in allowed_values):
            raise ValueError(
                "Invalid value for `system_status` ({0}), must be one of {1}"  # noqa: E501
                .format(system_status, allowed_values)
            )

        self._system_status = system_status

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
        if issubclass(NodeStatusNodeStatus, dict):
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
        if not isinstance(other, NodeStatusNodeStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeStatusNodeStatus):
            return True

        return self.to_dict() != other.to_dict()
