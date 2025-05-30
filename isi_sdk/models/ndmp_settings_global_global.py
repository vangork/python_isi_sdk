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


class NdmpSettingsGlobalGlobal(object):
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
        'bre_max_num_contexts': 'int',
        'dma': 'str',
        'enable_redirector': 'bool',
        'enable_throttler': 'bool',
        'msb_context_retention_duration': 'int',
        'msr_context_retention_duration': 'int',
        'port': 'int',
        'service': 'bool',
        'stub_file_open_timeout': 'int',
        'throttler_cpu_threshold': 'int',
        'vmem_size': 'int'
    }

    attribute_map = {
        'bre_max_num_contexts': 'bre_max_num_contexts',
        'dma': 'dma',
        'enable_redirector': 'enable_redirector',
        'enable_throttler': 'enable_throttler',
        'msb_context_retention_duration': 'msb_context_retention_duration',
        'msr_context_retention_duration': 'msr_context_retention_duration',
        'port': 'port',
        'service': 'service',
        'stub_file_open_timeout': 'stub_file_open_timeout',
        'throttler_cpu_threshold': 'throttler_cpu_threshold',
        'vmem_size': 'vmem_size'
    }

    def __init__(self, bre_max_num_contexts=None, dma=None, enable_redirector=None, enable_throttler=None, msb_context_retention_duration=None, msr_context_retention_duration=None, port=None, service=None, stub_file_open_timeout=None, throttler_cpu_threshold=None, vmem_size=None, _configuration=None):  # noqa: E501
        """NdmpSettingsGlobalGlobal - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bre_max_num_contexts = None
        self._dma = None
        self._enable_redirector = None
        self._enable_throttler = None
        self._msb_context_retention_duration = None
        self._msr_context_retention_duration = None
        self._port = None
        self._service = None
        self._stub_file_open_timeout = None
        self._throttler_cpu_threshold = None
        self._vmem_size = None
        self.discriminator = None

        if bre_max_num_contexts is not None:
            self.bre_max_num_contexts = bre_max_num_contexts
        if dma is not None:
            self.dma = dma
        if enable_redirector is not None:
            self.enable_redirector = enable_redirector
        if enable_throttler is not None:
            self.enable_throttler = enable_throttler
        if msb_context_retention_duration is not None:
            self.msb_context_retention_duration = msb_context_retention_duration
        if msr_context_retention_duration is not None:
            self.msr_context_retention_duration = msr_context_retention_duration
        if port is not None:
            self.port = port
        if service is not None:
            self.service = service
        if stub_file_open_timeout is not None:
            self.stub_file_open_timeout = stub_file_open_timeout
        if throttler_cpu_threshold is not None:
            self.throttler_cpu_threshold = throttler_cpu_threshold
        if vmem_size is not None:
            self.vmem_size = vmem_size

    @property
    def bre_max_num_contexts(self):
        """Gets the bre_max_num_contexts of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Maximum number of BRE contexts.  # noqa: E501

        :return: The bre_max_num_contexts of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._bre_max_num_contexts

    @bre_max_num_contexts.setter
    def bre_max_num_contexts(self, bre_max_num_contexts):
        """Sets the bre_max_num_contexts of this NdmpSettingsGlobalGlobal.

        Maximum number of BRE contexts.  # noqa: E501

        :param bre_max_num_contexts: The bre_max_num_contexts of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                bre_max_num_contexts is not None and bre_max_num_contexts > 1024):  # noqa: E501
            raise ValueError("Invalid value for `bre_max_num_contexts`, must be a value less than or equal to `1024`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bre_max_num_contexts is not None and bre_max_num_contexts < 0):  # noqa: E501
            raise ValueError("Invalid value for `bre_max_num_contexts`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bre_max_num_contexts = bre_max_num_contexts

    @property
    def dma(self):
        """Gets the dma of this NdmpSettingsGlobalGlobal.  # noqa: E501

        A unique identifier for the dma vendor.  # noqa: E501

        :return: The dma of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: str
        """
        return self._dma

    @dma.setter
    def dma(self, dma):
        """Sets the dma of this NdmpSettingsGlobalGlobal.

        A unique identifier for the dma vendor.  # noqa: E501

        :param dma: The dma of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: str
        """
        allowed_values = ["generic", "atempo", "bakbone", "commvault", "emc", "veritas", "tivoli", "veritas-netbackup", "veritas-backupexec"]  # noqa: E501
        if (self._configuration.client_side_validation and
                dma not in allowed_values):
            raise ValueError(
                "Invalid value for `dma` ({0}), must be one of {1}"  # noqa: E501
                .format(dma, allowed_values)
            )

        self._dma = dma

    @property
    def enable_redirector(self):
        """Gets the enable_redirector of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Enable/Disable NDMP Redirector feature to distribute NDMP backup and restore operations among multiple nodes.  # noqa: E501

        :return: The enable_redirector of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: bool
        """
        return self._enable_redirector

    @enable_redirector.setter
    def enable_redirector(self, enable_redirector):
        """Sets the enable_redirector of this NdmpSettingsGlobalGlobal.

        Enable/Disable NDMP Redirector feature to distribute NDMP backup and restore operations among multiple nodes.  # noqa: E501

        :param enable_redirector: The enable_redirector of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: bool
        """

        self._enable_redirector = enable_redirector

    @property
    def enable_throttler(self):
        """Gets the enable_throttler of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Enable/Disable NDMP throttler feature to limit CPU usage for NDMP backup or restore operations on each node.  # noqa: E501

        :return: The enable_throttler of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: bool
        """
        return self._enable_throttler

    @enable_throttler.setter
    def enable_throttler(self, enable_throttler):
        """Sets the enable_throttler of this NdmpSettingsGlobalGlobal.

        Enable/Disable NDMP throttler feature to limit CPU usage for NDMP backup or restore operations on each node.  # noqa: E501

        :param enable_throttler: The enable_throttler of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: bool
        """

        self._enable_throttler = enable_throttler

    @property
    def msb_context_retention_duration(self):
        """Gets the msb_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Multi-Stream Backup context retention duration, expressed in seconds.  # noqa: E501

        :return: The msb_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._msb_context_retention_duration

    @msb_context_retention_duration.setter
    def msb_context_retention_duration(self, msb_context_retention_duration):
        """Sets the msb_context_retention_duration of this NdmpSettingsGlobalGlobal.

        Multi-Stream Backup context retention duration, expressed in seconds.  # noqa: E501

        :param msb_context_retention_duration: The msb_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                msb_context_retention_duration is not None and msb_context_retention_duration < 0):  # noqa: E501
            raise ValueError("Invalid value for `msb_context_retention_duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._msb_context_retention_duration = msb_context_retention_duration

    @property
    def msr_context_retention_duration(self):
        """Gets the msr_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Multi-Stream Restore context retention duration, expressed in seconds.  # noqa: E501

        :return: The msr_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._msr_context_retention_duration

    @msr_context_retention_duration.setter
    def msr_context_retention_duration(self, msr_context_retention_duration):
        """Sets the msr_context_retention_duration of this NdmpSettingsGlobalGlobal.

        Multi-Stream Restore context retention duration, expressed in seconds.  # noqa: E501

        :param msr_context_retention_duration: The msr_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                msr_context_retention_duration is not None and msr_context_retention_duration < 0):  # noqa: E501
            raise ValueError("Invalid value for `msr_context_retention_duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._msr_context_retention_duration = msr_context_retention_duration

    @property
    def port(self):
        """Gets the port of this NdmpSettingsGlobalGlobal.  # noqa: E501

        The port to listen on.  # noqa: E501

        :return: The port of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NdmpSettingsGlobalGlobal.

        The port to listen on.  # noqa: E501

        :param port: The port of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                port is not None and port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port is not None and port < 1024):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1024`")  # noqa: E501

        self._port = port

    @property
    def service(self):
        """Gets the service of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Property to enable/disable the NDMP service.  # noqa: E501

        :return: The service of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this NdmpSettingsGlobalGlobal.

        Property to enable/disable the NDMP service.  # noqa: E501

        :param service: The service of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: bool
        """

        self._service = service

    @property
    def stub_file_open_timeout(self):
        """Gets the stub_file_open_timeout of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Stub file open timeout during a backup or restore, expressed in seconds.  # noqa: E501

        :return: The stub_file_open_timeout of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._stub_file_open_timeout

    @stub_file_open_timeout.setter
    def stub_file_open_timeout(self, stub_file_open_timeout):
        """Sets the stub_file_open_timeout of this NdmpSettingsGlobalGlobal.

        Stub file open timeout during a backup or restore, expressed in seconds.  # noqa: E501

        :param stub_file_open_timeout: The stub_file_open_timeout of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                stub_file_open_timeout is not None and stub_file_open_timeout > 1200):  # noqa: E501
            raise ValueError("Invalid value for `stub_file_open_timeout`, must be a value less than or equal to `1200`")  # noqa: E501
        if (self._configuration.client_side_validation and
                stub_file_open_timeout is not None and stub_file_open_timeout < 0):  # noqa: E501
            raise ValueError("Invalid value for `stub_file_open_timeout`, must be a value greater than or equal to `0`")  # noqa: E501

        self._stub_file_open_timeout = stub_file_open_timeout

    @property
    def throttler_cpu_threshold(self):
        """Gets the throttler_cpu_threshold of this NdmpSettingsGlobalGlobal.  # noqa: E501

        NDMP Throttler CPU threshold in percentage.  # noqa: E501

        :return: The throttler_cpu_threshold of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._throttler_cpu_threshold

    @throttler_cpu_threshold.setter
    def throttler_cpu_threshold(self, throttler_cpu_threshold):
        """Sets the throttler_cpu_threshold of this NdmpSettingsGlobalGlobal.

        NDMP Throttler CPU threshold in percentage.  # noqa: E501

        :param throttler_cpu_threshold: The throttler_cpu_threshold of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                throttler_cpu_threshold is not None and throttler_cpu_threshold > 100):  # noqa: E501
            raise ValueError("Invalid value for `throttler_cpu_threshold`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                throttler_cpu_threshold is not None and throttler_cpu_threshold < 1):  # noqa: E501
            raise ValueError("Invalid value for `throttler_cpu_threshold`, must be a value greater than or equal to `1`")  # noqa: E501

        self._throttler_cpu_threshold = throttler_cpu_threshold

    @property
    def vmem_size(self):
        """Gets the vmem_size of this NdmpSettingsGlobalGlobal.  # noqa: E501

        NDMP Vmem size in mebibytes.  # noqa: E501

        :return: The vmem_size of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._vmem_size

    @vmem_size.setter
    def vmem_size(self, vmem_size):
        """Sets the vmem_size of this NdmpSettingsGlobalGlobal.

        NDMP Vmem size in mebibytes.  # noqa: E501

        :param vmem_size: The vmem_size of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                vmem_size is not None and vmem_size > 8192):  # noqa: E501
            raise ValueError("Invalid value for `vmem_size`, must be a value less than or equal to `8192`")  # noqa: E501
        if (self._configuration.client_side_validation and
                vmem_size is not None and vmem_size < 512):  # noqa: E501
            raise ValueError("Invalid value for `vmem_size`, must be a value greater than or equal to `512`")  # noqa: E501

        self._vmem_size = vmem_size

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
        if issubclass(NdmpSettingsGlobalGlobal, dict):
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
        if not isinstance(other, NdmpSettingsGlobalGlobal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NdmpSettingsGlobalGlobal):
            return True

        return self.to_dict() != other.to_dict()
