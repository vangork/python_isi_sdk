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


class MetadataiqSettingsSettingsProducer(object):
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
        'changelist_job_retries': 'int',
        'changelist_job_tolerable_pause_hours': 'int',
        'changelist_job_tolerable_state_request_failures': 'int',
        'path': 'str',
        'schedule': 'str'
    }

    attribute_map = {
        'changelist_job_retries': 'changelist_job_retries',
        'changelist_job_tolerable_pause_hours': 'changelist_job_tolerable_pause_hours',
        'changelist_job_tolerable_state_request_failures': 'changelist_job_tolerable_state_request_failures',
        'path': 'path',
        'schedule': 'schedule'
    }

    def __init__(self, changelist_job_retries=None, changelist_job_tolerable_pause_hours=None, changelist_job_tolerable_state_request_failures=None, path=None, schedule=None, _configuration=None):  # noqa: E501
        """MetadataiqSettingsSettingsProducer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._changelist_job_retries = None
        self._changelist_job_tolerable_pause_hours = None
        self._changelist_job_tolerable_state_request_failures = None
        self._path = None
        self._schedule = None
        self.discriminator = None

        if changelist_job_retries is not None:
            self.changelist_job_retries = changelist_job_retries
        if changelist_job_tolerable_pause_hours is not None:
            self.changelist_job_tolerable_pause_hours = changelist_job_tolerable_pause_hours
        if changelist_job_tolerable_state_request_failures is not None:
            self.changelist_job_tolerable_state_request_failures = changelist_job_tolerable_state_request_failures
        if path is not None:
            self.path = path
        if schedule is not None:
            self.schedule = schedule

    @property
    def changelist_job_retries(self):
        """Gets the changelist_job_retries of this MetadataiqSettingsSettingsProducer.  # noqa: E501

        Number of additional times, after the first failure, that MetadataIQ retries the ChangelistCreate job on a given pair of snapshots. Default is 2.  # noqa: E501

        :return: The changelist_job_retries of this MetadataiqSettingsSettingsProducer.  # noqa: E501
        :rtype: int
        """
        return self._changelist_job_retries

    @changelist_job_retries.setter
    def changelist_job_retries(self, changelist_job_retries):
        """Sets the changelist_job_retries of this MetadataiqSettingsSettingsProducer.

        Number of additional times, after the first failure, that MetadataIQ retries the ChangelistCreate job on a given pair of snapshots. Default is 2.  # noqa: E501

        :param changelist_job_retries: The changelist_job_retries of this MetadataiqSettingsSettingsProducer.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                changelist_job_retries is not None and changelist_job_retries > 255):  # noqa: E501
            raise ValueError("Invalid value for `changelist_job_retries`, must be a value less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                changelist_job_retries is not None and changelist_job_retries < 0):  # noqa: E501
            raise ValueError("Invalid value for `changelist_job_retries`, must be a value greater than or equal to `0`")  # noqa: E501

        self._changelist_job_retries = changelist_job_retries

    @property
    def changelist_job_tolerable_pause_hours(self):
        """Gets the changelist_job_tolerable_pause_hours of this MetadataiqSettingsSettingsProducer.  # noqa: E501

        Amount of time the Metadataiq system tolerates a MetadataIQ-driven ChangelistCreate job being paused, in hours, before warning. Default is 24.  # noqa: E501

        :return: The changelist_job_tolerable_pause_hours of this MetadataiqSettingsSettingsProducer.  # noqa: E501
        :rtype: int
        """
        return self._changelist_job_tolerable_pause_hours

    @changelist_job_tolerable_pause_hours.setter
    def changelist_job_tolerable_pause_hours(self, changelist_job_tolerable_pause_hours):
        """Sets the changelist_job_tolerable_pause_hours of this MetadataiqSettingsSettingsProducer.

        Amount of time the Metadataiq system tolerates a MetadataIQ-driven ChangelistCreate job being paused, in hours, before warning. Default is 24.  # noqa: E501

        :param changelist_job_tolerable_pause_hours: The changelist_job_tolerable_pause_hours of this MetadataiqSettingsSettingsProducer.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                changelist_job_tolerable_pause_hours is not None and changelist_job_tolerable_pause_hours > 255):  # noqa: E501
            raise ValueError("Invalid value for `changelist_job_tolerable_pause_hours`, must be a value less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                changelist_job_tolerable_pause_hours is not None and changelist_job_tolerable_pause_hours < 0):  # noqa: E501
            raise ValueError("Invalid value for `changelist_job_tolerable_pause_hours`, must be a value greater than or equal to `0`")  # noqa: E501

        self._changelist_job_tolerable_pause_hours = changelist_job_tolerable_pause_hours

    @property
    def changelist_job_tolerable_state_request_failures(self):
        """Gets the changelist_job_tolerable_state_request_failures of this MetadataiqSettingsSettingsProducer.  # noqa: E501

        Number of times the Metadataiq System can fail to get the ChangelistCreate job's status before it gives up. Default is 720.  # noqa: E501

        :return: The changelist_job_tolerable_state_request_failures of this MetadataiqSettingsSettingsProducer.  # noqa: E501
        :rtype: int
        """
        return self._changelist_job_tolerable_state_request_failures

    @changelist_job_tolerable_state_request_failures.setter
    def changelist_job_tolerable_state_request_failures(self, changelist_job_tolerable_state_request_failures):
        """Sets the changelist_job_tolerable_state_request_failures of this MetadataiqSettingsSettingsProducer.

        Number of times the Metadataiq System can fail to get the ChangelistCreate job's status before it gives up. Default is 720.  # noqa: E501

        :param changelist_job_tolerable_state_request_failures: The changelist_job_tolerable_state_request_failures of this MetadataiqSettingsSettingsProducer.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                changelist_job_tolerable_state_request_failures is not None and changelist_job_tolerable_state_request_failures > 65535):  # noqa: E501
            raise ValueError("Invalid value for `changelist_job_tolerable_state_request_failures`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                changelist_job_tolerable_state_request_failures is not None and changelist_job_tolerable_state_request_failures < 0):  # noqa: E501
            raise ValueError("Invalid value for `changelist_job_tolerable_state_request_failures`, must be a value greater than or equal to `0`")  # noqa: E501

        self._changelist_job_tolerable_state_request_failures = changelist_job_tolerable_state_request_failures

    @property
    def path(self):
        """Gets the path of this MetadataiqSettingsSettingsProducer.  # noqa: E501


        :return: The path of this MetadataiqSettingsSettingsProducer.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this MetadataiqSettingsSettingsProducer.


        :param path: The path of this MetadataiqSettingsSettingsProducer.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                path is not None and len(path) > 4096):
            raise ValueError("Invalid value for `path`, length must be less than or equal to `4096`")  # noqa: E501
        if (self._configuration.client_side_validation and
                path is not None and len(path) < 4):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `4`")  # noqa: E501
        if (self._configuration.client_side_validation and
                path is not None and not re.search(r'^\/ifs$|^\/ifs\/', path)):  # noqa: E501
            raise ValueError(r"Invalid value for `path`, must be a follow pattern or equal to `/^\/ifs$|^\/ifs\//`")  # noqa: E501

        self._path = path

    @property
    def schedule(self):
        """Gets the schedule of this MetadataiqSettingsSettingsProducer.  # noqa: E501

        Schedule at which a metadata cycle of analysis and upload occurs. The syntax must be isi-date compatible. Default is ''.  # noqa: E501

        :return: The schedule of this MetadataiqSettingsSettingsProducer.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this MetadataiqSettingsSettingsProducer.

        Schedule at which a metadata cycle of analysis and upload occurs. The syntax must be isi-date compatible. Default is ''.  # noqa: E501

        :param schedule: The schedule of this MetadataiqSettingsSettingsProducer.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                schedule is not None and len(schedule) > 255):
            raise ValueError("Invalid value for `schedule`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                schedule is not None and len(schedule) < 0):
            raise ValueError("Invalid value for `schedule`, length must be greater than or equal to `0`")  # noqa: E501

        self._schedule = schedule

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
        if issubclass(MetadataiqSettingsSettingsProducer, dict):
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
        if not isinstance(other, MetadataiqSettingsSettingsProducer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetadataiqSettingsSettingsProducer):
            return True

        return self.to_dict() != other.to_dict()
