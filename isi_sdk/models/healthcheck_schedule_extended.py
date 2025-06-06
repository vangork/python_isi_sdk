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


class HealthcheckScheduleExtended(object):
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
        'base': 'str',
        'checklist': 'list[str]',
        'id': 'str',
        'name': 'str',
        'next_run': 'str',
        'schedule': 'str'
    }

    attribute_map = {
        'base': 'base',
        'checklist': 'checklist',
        'id': 'id',
        'name': 'name',
        'next_run': 'next_run',
        'schedule': 'schedule'
    }

    def __init__(self, base=None, checklist=None, id=None, name=None, next_run=None, schedule=None, _configuration=None):  # noqa: E501
        """HealthcheckScheduleExtended - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base = None
        self._checklist = None
        self._id = None
        self._name = None
        self._next_run = None
        self._schedule = None
        self.discriminator = None

        if base is not None:
            self.base = base
        if checklist is not None:
            self.checklist = checklist
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if next_run is not None:
            self.next_run = next_run
        if schedule is not None:
            self.schedule = schedule

    @property
    def base(self):
        """Gets the base of this HealthcheckScheduleExtended.  # noqa: E501

        Seconds from Epoch when schedule was created.  # noqa: E501

        :return: The base of this HealthcheckScheduleExtended.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this HealthcheckScheduleExtended.

        Seconds from Epoch when schedule was created.  # noqa: E501

        :param base: The base of this HealthcheckScheduleExtended.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                base is not None and len(base) > 255):
            raise ValueError("Invalid value for `base`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                base is not None and len(base) < 0):
            raise ValueError("Invalid value for `base`, length must be greater than or equal to `0`")  # noqa: E501

        self._base = base

    @property
    def checklist(self):
        """Gets the checklist of this HealthcheckScheduleExtended.  # noqa: E501

        Checklists or Items for scheduling.  # noqa: E501

        :return: The checklist of this HealthcheckScheduleExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._checklist

    @checklist.setter
    def checklist(self, checklist):
        """Sets the checklist of this HealthcheckScheduleExtended.

        Checklists or Items for scheduling.  # noqa: E501

        :param checklist: The checklist of this HealthcheckScheduleExtended.  # noqa: E501
        :type: list[str]
        """

        self._checklist = checklist

    @property
    def id(self):
        """Gets the id of this HealthcheckScheduleExtended.  # noqa: E501

        The ID of the newly created schedule.  # noqa: E501

        :return: The id of this HealthcheckScheduleExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthcheckScheduleExtended.

        The ID of the newly created schedule.  # noqa: E501

        :param id: The id of this HealthcheckScheduleExtended.  # noqa: E501
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
    def name(self):
        """Gets the name of this HealthcheckScheduleExtended.  # noqa: E501

        The schedule name.  # noqa: E501

        :return: The name of this HealthcheckScheduleExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthcheckScheduleExtended.

        The schedule name.  # noqa: E501

        :param name: The name of this HealthcheckScheduleExtended.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def next_run(self):
        """Gets the next_run of this HealthcheckScheduleExtended.  # noqa: E501

        Seconds from Epoch when next evaluation will run.  # noqa: E501

        :return: The next_run of this HealthcheckScheduleExtended.  # noqa: E501
        :rtype: str
        """
        return self._next_run

    @next_run.setter
    def next_run(self, next_run):
        """Sets the next_run of this HealthcheckScheduleExtended.

        Seconds from Epoch when next evaluation will run.  # noqa: E501

        :param next_run: The next_run of this HealthcheckScheduleExtended.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                next_run is not None and len(next_run) > 255):
            raise ValueError("Invalid value for `next_run`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                next_run is not None and len(next_run) < 0):
            raise ValueError("Invalid value for `next_run`, length must be greater than or equal to `0`")  # noqa: E501

        self._next_run = next_run

    @property
    def schedule(self):
        """Gets the schedule of this HealthcheckScheduleExtended.  # noqa: E501

        The isi-schedule compatible natural language description of the schedule.  # noqa: E501

        :return: The schedule of this HealthcheckScheduleExtended.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this HealthcheckScheduleExtended.

        The isi-schedule compatible natural language description of the schedule.  # noqa: E501

        :param schedule: The schedule of this HealthcheckScheduleExtended.  # noqa: E501
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
        if issubclass(HealthcheckScheduleExtended, dict):
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
        if not isinstance(other, HealthcheckScheduleExtended):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HealthcheckScheduleExtended):
            return True

        return self.to_dict() != other.to_dict()
