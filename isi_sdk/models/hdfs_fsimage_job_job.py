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


class HdfsFsimageJobJob(object):
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
        'reason': 'str',
        'state': 'str',
        'time_started': 'int',
        'txid': 'int'
    }

    attribute_map = {
        'reason': 'reason',
        'state': 'state',
        'time_started': 'time_started',
        'txid': 'txid'
    }

    def __init__(self, reason=None, state=None, time_started=None, txid=None, _configuration=None):  # noqa: E501
        """HdfsFsimageJobJob - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._reason = None
        self._state = None
        self._time_started = None
        self._txid = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        if state is not None:
            self.state = state
        if time_started is not None:
            self.time_started = time_started
        if txid is not None:
            self.txid = txid

    @property
    def reason(self):
        """Gets the reason of this HdfsFsimageJobJob.  # noqa: E501

        Further details about the state of the job.  # noqa: E501

        :return: The reason of this HdfsFsimageJobJob.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this HdfsFsimageJobJob.

        Further details about the state of the job.  # noqa: E501

        :param reason: The reason of this HdfsFsimageJobJob.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def state(self):
        """Gets the state of this HdfsFsimageJobJob.  # noqa: E501

        State of the job.  # noqa: E501

        :return: The state of this HdfsFsimageJobJob.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this HdfsFsimageJobJob.

        State of the job.  # noqa: E501

        :param state: The state of this HdfsFsimageJobJob.  # noqa: E501
        :type: str
        """
        allowed_values = ["INPROGRESS", "IDLE", "FAILED", "DISABLED", "NONE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def time_started(self):
        """Gets the time_started of this HdfsFsimageJobJob.  # noqa: E501

        The date and time job was started as a UNIX epoch. If null, started is not relevant to the state.  # noqa: E501

        :return: The time_started of this HdfsFsimageJobJob.  # noqa: E501
        :rtype: int
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """Sets the time_started of this HdfsFsimageJobJob.

        The date and time job was started as a UNIX epoch. If null, started is not relevant to the state.  # noqa: E501

        :param time_started: The time_started of this HdfsFsimageJobJob.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                time_started is not None and time_started > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `time_started`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                time_started is not None and time_started < 0):  # noqa: E501
            raise ValueError("Invalid value for `time_started`, must be a value greater than or equal to `0`")  # noqa: E501

        self._time_started = time_started

    @property
    def txid(self):
        """Gets the txid of this HdfsFsimageJobJob.  # noqa: E501

        The transaction id of the FSImage. If null, txid is not relevant to the state.  # noqa: E501

        :return: The txid of this HdfsFsimageJobJob.  # noqa: E501
        :rtype: int
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this HdfsFsimageJobJob.

        The transaction id of the FSImage. If null, txid is not relevant to the state.  # noqa: E501

        :param txid: The txid of this HdfsFsimageJobJob.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                txid is not None and txid > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `txid`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                txid is not None and txid < 0):  # noqa: E501
            raise ValueError("Invalid value for `txid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._txid = txid

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
        if issubclass(HdfsFsimageJobJob, dict):
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
        if not isinstance(other, HdfsFsimageJobJob):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HdfsFsimageJobJob):
            return True

        return self.to_dict() != other.to_dict()
