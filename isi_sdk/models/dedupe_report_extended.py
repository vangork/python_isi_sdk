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


class DedupeReportExtended(object):
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
        'dedupe_percent': 'str',
        'elapsed_time': 'int',
        'id': 'int',
        'job_id': 'int',
        'job_type': 'str',
        'reports': 'list[DedupeReport]'
    }

    attribute_map = {
        'dedupe_percent': 'dedupe_percent',
        'elapsed_time': 'elapsed_time',
        'id': 'id',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'reports': 'reports'
    }

    def __init__(self, dedupe_percent=None, elapsed_time=None, id=None, job_id=None, job_type=None, reports=None, _configuration=None):  # noqa: E501
        """DedupeReportExtended - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dedupe_percent = None
        self._elapsed_time = None
        self._id = None
        self._job_id = None
        self._job_type = None
        self._reports = None
        self.discriminator = None

        if dedupe_percent is not None:
            self.dedupe_percent = dedupe_percent
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if id is not None:
            self.id = id
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if reports is not None:
            self.reports = reports

    @property
    def dedupe_percent(self):
        """Gets the dedupe_percent of this DedupeReportExtended.  # noqa: E501

        The amount of space the directory trees under this job's paths now take up, compared to what they would take up if not deduplicated (0 ~ 100).  # noqa: E501

        :return: The dedupe_percent of this DedupeReportExtended.  # noqa: E501
        :rtype: str
        """
        return self._dedupe_percent

    @dedupe_percent.setter
    def dedupe_percent(self, dedupe_percent):
        """Sets the dedupe_percent of this DedupeReportExtended.

        The amount of space the directory trees under this job's paths now take up, compared to what they would take up if not deduplicated (0 ~ 100).  # noqa: E501

        :param dedupe_percent: The dedupe_percent of this DedupeReportExtended.  # noqa: E501
        :type: str
        """

        self._dedupe_percent = dedupe_percent

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this DedupeReportExtended.  # noqa: E501

        The amount of time in seconds it took to run this job.  # noqa: E501

        :return: The elapsed_time of this DedupeReportExtended.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this DedupeReportExtended.

        The amount of time in seconds it took to run this job.  # noqa: E501

        :param elapsed_time: The elapsed_time of this DedupeReportExtended.  # noqa: E501
        :type: int
        """

        self._elapsed_time = elapsed_time

    @property
    def id(self):
        """Gets the id of this DedupeReportExtended.  # noqa: E501

        An unique identifier for this report.  # noqa: E501

        :return: The id of this DedupeReportExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DedupeReportExtended.

        An unique identifier for this report.  # noqa: E501

        :param id: The id of this DedupeReportExtended.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def job_id(self):
        """Gets the job_id of this DedupeReportExtended.  # noqa: E501

        The job id this report refers to.  # noqa: E501

        :return: The job_id of this DedupeReportExtended.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DedupeReportExtended.

        The job id this report refers to.  # noqa: E501

        :param job_id: The job_id of this DedupeReportExtended.  # noqa: E501
        :type: int
        """

        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this DedupeReportExtended.  # noqa: E501

        The type of dedupe job this report refers to.  # noqa: E501

        :return: The job_type of this DedupeReportExtended.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this DedupeReportExtended.

        The type of dedupe job this report refers to.  # noqa: E501

        :param job_type: The job_type of this DedupeReportExtended.  # noqa: E501
        :type: str
        """

        self._job_type = job_type

    @property
    def reports(self):
        """Gets the reports of this DedupeReportExtended.  # noqa: E501

        A list of report entries for this dedupe job.  # noqa: E501

        :return: The reports of this DedupeReportExtended.  # noqa: E501
        :rtype: list[DedupeReport]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this DedupeReportExtended.

        A list of report entries for this dedupe job.  # noqa: E501

        :param reports: The reports of this DedupeReportExtended.  # noqa: E501
        :type: list[DedupeReport]
        """

        self._reports = reports

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
        if issubclass(DedupeReportExtended, dict):
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
        if not isinstance(other, DedupeReportExtended):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DedupeReportExtended):
            return True

        return self.to_dict() != other.to_dict()
