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


class DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics(object):
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
        '_0_k_8_k_files_xferred': 'int',
        '_100_m_10_g_files_xferred': 'int',
        '_1_m_100_m_files_xferred': 'int',
        '_8_k_1_m_files_xferred': 'int',
        'ads_xferred': 'int',
        'block_files_xferred': 'int',
        'bytes_xferred': 'int',
        'char_files_xferred': 'int',
        'dirs_xferred': 'int',
        'fifo_files_xferred': 'int',
        'files_xferred': 'int',
        'hardlinks_xferred': 'int',
        'huge_files_xferred': 'int',
        'sock_files_xferred': 'int',
        'softlinks_xferred': 'int',
        'source_base_dataset_id': 'int',
        'target_dataset_id': 'int',
        'total_size_xferred': 'int'
    }

    attribute_map = {
        '_0_k_8_k_files_xferred': '0K_8K_files_xferred',
        '_100_m_10_g_files_xferred': '100M_10G_files_xferred',
        '_1_m_100_m_files_xferred': '1M_100M_files_xferred',
        '_8_k_1_m_files_xferred': '8K_1M_files_xferred',
        'ads_xferred': 'ads_xferred',
        'block_files_xferred': 'block_files_xferred',
        'bytes_xferred': 'bytes_xferred',
        'char_files_xferred': 'char_files_xferred',
        'dirs_xferred': 'dirs_xferred',
        'fifo_files_xferred': 'fifo_files_xferred',
        'files_xferred': 'files_xferred',
        'hardlinks_xferred': 'hardlinks_xferred',
        'huge_files_xferred': 'huge_files_xferred',
        'sock_files_xferred': 'sock_files_xferred',
        'softlinks_xferred': 'softlinks_xferred',
        'source_base_dataset_id': 'source_base_dataset_id',
        'target_dataset_id': 'target_dataset_id',
        'total_size_xferred': 'total_size_xferred'
    }

    def __init__(self, _0_k_8_k_files_xferred=None, _100_m_10_g_files_xferred=None, _1_m_100_m_files_xferred=None, _8_k_1_m_files_xferred=None, ads_xferred=None, block_files_xferred=None, bytes_xferred=None, char_files_xferred=None, dirs_xferred=None, fifo_files_xferred=None, files_xferred=None, hardlinks_xferred=None, huge_files_xferred=None, sock_files_xferred=None, softlinks_xferred=None, source_base_dataset_id=None, target_dataset_id=None, total_size_xferred=None, _configuration=None):  # noqa: E501
        """DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__0_k_8_k_files_xferred = None
        self.__100_m_10_g_files_xferred = None
        self.__1_m_100_m_files_xferred = None
        self.__8_k_1_m_files_xferred = None
        self._ads_xferred = None
        self._block_files_xferred = None
        self._bytes_xferred = None
        self._char_files_xferred = None
        self._dirs_xferred = None
        self._fifo_files_xferred = None
        self._files_xferred = None
        self._hardlinks_xferred = None
        self._huge_files_xferred = None
        self._sock_files_xferred = None
        self._softlinks_xferred = None
        self._source_base_dataset_id = None
        self._target_dataset_id = None
        self._total_size_xferred = None
        self.discriminator = None

        if _0_k_8_k_files_xferred is not None:
            self._0_k_8_k_files_xferred = _0_k_8_k_files_xferred
        if _100_m_10_g_files_xferred is not None:
            self._100_m_10_g_files_xferred = _100_m_10_g_files_xferred
        if _1_m_100_m_files_xferred is not None:
            self._1_m_100_m_files_xferred = _1_m_100_m_files_xferred
        if _8_k_1_m_files_xferred is not None:
            self._8_k_1_m_files_xferred = _8_k_1_m_files_xferred
        if ads_xferred is not None:
            self.ads_xferred = ads_xferred
        if block_files_xferred is not None:
            self.block_files_xferred = block_files_xferred
        if bytes_xferred is not None:
            self.bytes_xferred = bytes_xferred
        if char_files_xferred is not None:
            self.char_files_xferred = char_files_xferred
        if dirs_xferred is not None:
            self.dirs_xferred = dirs_xferred
        if fifo_files_xferred is not None:
            self.fifo_files_xferred = fifo_files_xferred
        if files_xferred is not None:
            self.files_xferred = files_xferred
        if hardlinks_xferred is not None:
            self.hardlinks_xferred = hardlinks_xferred
        if huge_files_xferred is not None:
            self.huge_files_xferred = huge_files_xferred
        if sock_files_xferred is not None:
            self.sock_files_xferred = sock_files_xferred
        if softlinks_xferred is not None:
            self.softlinks_xferred = softlinks_xferred
        if source_base_dataset_id is not None:
            self.source_base_dataset_id = source_base_dataset_id
        if target_dataset_id is not None:
            self.target_dataset_id = target_dataset_id
        if total_size_xferred is not None:
            self.total_size_xferred = total_size_xferred

    @property
    def _0_k_8_k_files_xferred(self):
        """Gets the _0_k_8_k_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of files that were <= 8K in size.  # noqa: E501

        :return: The _0_k_8_k_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self.__0_k_8_k_files_xferred

    @_0_k_8_k_files_xferred.setter
    def _0_k_8_k_files_xferred(self, _0_k_8_k_files_xferred):
        """Sets the _0_k_8_k_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of files that were <= 8K in size.  # noqa: E501

        :param _0_k_8_k_files_xferred: The _0_k_8_k_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                _0_k_8_k_files_xferred is not None and _0_k_8_k_files_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `_0_k_8_k_files_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                _0_k_8_k_files_xferred is not None and _0_k_8_k_files_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `_0_k_8_k_files_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self.__0_k_8_k_files_xferred = _0_k_8_k_files_xferred

    @property
    def _100_m_10_g_files_xferred(self):
        """Gets the _100_m_10_g_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of files that were greater than 100MB and  <= 10GB in size.  # noqa: E501

        :return: The _100_m_10_g_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self.__100_m_10_g_files_xferred

    @_100_m_10_g_files_xferred.setter
    def _100_m_10_g_files_xferred(self, _100_m_10_g_files_xferred):
        """Sets the _100_m_10_g_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of files that were greater than 100MB and  <= 10GB in size.  # noqa: E501

        :param _100_m_10_g_files_xferred: The _100_m_10_g_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                _100_m_10_g_files_xferred is not None and _100_m_10_g_files_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `_100_m_10_g_files_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                _100_m_10_g_files_xferred is not None and _100_m_10_g_files_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `_100_m_10_g_files_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self.__100_m_10_g_files_xferred = _100_m_10_g_files_xferred

    @property
    def _1_m_100_m_files_xferred(self):
        """Gets the _1_m_100_m_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of files that were greater than 1MB and <= 100MB in size.  # noqa: E501

        :return: The _1_m_100_m_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self.__1_m_100_m_files_xferred

    @_1_m_100_m_files_xferred.setter
    def _1_m_100_m_files_xferred(self, _1_m_100_m_files_xferred):
        """Sets the _1_m_100_m_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of files that were greater than 1MB and <= 100MB in size.  # noqa: E501

        :param _1_m_100_m_files_xferred: The _1_m_100_m_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                _1_m_100_m_files_xferred is not None and _1_m_100_m_files_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `_1_m_100_m_files_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                _1_m_100_m_files_xferred is not None and _1_m_100_m_files_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `_1_m_100_m_files_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self.__1_m_100_m_files_xferred = _1_m_100_m_files_xferred

    @property
    def _8_k_1_m_files_xferred(self):
        """Gets the _8_k_1_m_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of files that were greater than 8K and <= 1MB in size.  # noqa: E501

        :return: The _8_k_1_m_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self.__8_k_1_m_files_xferred

    @_8_k_1_m_files_xferred.setter
    def _8_k_1_m_files_xferred(self, _8_k_1_m_files_xferred):
        """Sets the _8_k_1_m_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of files that were greater than 8K and <= 1MB in size.  # noqa: E501

        :param _8_k_1_m_files_xferred: The _8_k_1_m_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                _8_k_1_m_files_xferred is not None and _8_k_1_m_files_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `_8_k_1_m_files_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                _8_k_1_m_files_xferred is not None and _8_k_1_m_files_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `_8_k_1_m_files_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self.__8_k_1_m_files_xferred = _8_k_1_m_files_xferred

    @property
    def ads_xferred(self):
        """Gets the ads_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of alternate data streams transferred.  # noqa: E501

        :return: The ads_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._ads_xferred

    @ads_xferred.setter
    def ads_xferred(self, ads_xferred):
        """Sets the ads_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of alternate data streams transferred.  # noqa: E501

        :param ads_xferred: The ads_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                ads_xferred is not None and ads_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `ads_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                ads_xferred is not None and ads_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `ads_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ads_xferred = ads_xferred

    @property
    def block_files_xferred(self):
        """Gets the block_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of block files transferred.  # noqa: E501

        :return: The block_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._block_files_xferred

    @block_files_xferred.setter
    def block_files_xferred(self, block_files_xferred):
        """Sets the block_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of block files transferred.  # noqa: E501

        :param block_files_xferred: The block_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                block_files_xferred is not None and block_files_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `block_files_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                block_files_xferred is not None and block_files_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `block_files_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._block_files_xferred = block_files_xferred

    @property
    def bytes_xferred(self):
        """Gets the bytes_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of file bytes transferred.  # noqa: E501

        :return: The bytes_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._bytes_xferred

    @bytes_xferred.setter
    def bytes_xferred(self, bytes_xferred):
        """Sets the bytes_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of file bytes transferred.  # noqa: E501

        :param bytes_xferred: The bytes_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                bytes_xferred is not None and bytes_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `bytes_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bytes_xferred is not None and bytes_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `bytes_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bytes_xferred = bytes_xferred

    @property
    def char_files_xferred(self):
        """Gets the char_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of char files transferred.  # noqa: E501

        :return: The char_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._char_files_xferred

    @char_files_xferred.setter
    def char_files_xferred(self, char_files_xferred):
        """Sets the char_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of char files transferred.  # noqa: E501

        :param char_files_xferred: The char_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                char_files_xferred is not None and char_files_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `char_files_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                char_files_xferred is not None and char_files_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `char_files_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._char_files_xferred = char_files_xferred

    @property
    def dirs_xferred(self):
        """Gets the dirs_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of directories transferred.  # noqa: E501

        :return: The dirs_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._dirs_xferred

    @dirs_xferred.setter
    def dirs_xferred(self, dirs_xferred):
        """Sets the dirs_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of directories transferred.  # noqa: E501

        :param dirs_xferred: The dirs_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                dirs_xferred is not None and dirs_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `dirs_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                dirs_xferred is not None and dirs_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `dirs_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._dirs_xferred = dirs_xferred

    @property
    def fifo_files_xferred(self):
        """Gets the fifo_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of FIFO files transferred.  # noqa: E501

        :return: The fifo_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._fifo_files_xferred

    @fifo_files_xferred.setter
    def fifo_files_xferred(self, fifo_files_xferred):
        """Sets the fifo_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of FIFO files transferred.  # noqa: E501

        :param fifo_files_xferred: The fifo_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                fifo_files_xferred is not None and fifo_files_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `fifo_files_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                fifo_files_xferred is not None and fifo_files_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `fifo_files_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._fifo_files_xferred = fifo_files_xferred

    @property
    def files_xferred(self):
        """Gets the files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of files transferred.  # noqa: E501

        :return: The files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._files_xferred

    @files_xferred.setter
    def files_xferred(self, files_xferred):
        """Sets the files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of files transferred.  # noqa: E501

        :param files_xferred: The files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                files_xferred is not None and files_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `files_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                files_xferred is not None and files_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `files_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._files_xferred = files_xferred

    @property
    def hardlinks_xferred(self):
        """Gets the hardlinks_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of hardlinks transferred.  # noqa: E501

        :return: The hardlinks_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._hardlinks_xferred

    @hardlinks_xferred.setter
    def hardlinks_xferred(self, hardlinks_xferred):
        """Sets the hardlinks_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of hardlinks transferred.  # noqa: E501

        :param hardlinks_xferred: The hardlinks_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                hardlinks_xferred is not None and hardlinks_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `hardlinks_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                hardlinks_xferred is not None and hardlinks_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `hardlinks_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._hardlinks_xferred = hardlinks_xferred

    @property
    def huge_files_xferred(self):
        """Gets the huge_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of files that were greater than 10GB in size.  # noqa: E501

        :return: The huge_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._huge_files_xferred

    @huge_files_xferred.setter
    def huge_files_xferred(self, huge_files_xferred):
        """Sets the huge_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of files that were greater than 10GB in size.  # noqa: E501

        :param huge_files_xferred: The huge_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                huge_files_xferred is not None and huge_files_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `huge_files_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                huge_files_xferred is not None and huge_files_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `huge_files_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._huge_files_xferred = huge_files_xferred

    @property
    def sock_files_xferred(self):
        """Gets the sock_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of socket files transferred.  # noqa: E501

        :return: The sock_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._sock_files_xferred

    @sock_files_xferred.setter
    def sock_files_xferred(self, sock_files_xferred):
        """Sets the sock_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of socket files transferred.  # noqa: E501

        :param sock_files_xferred: The sock_files_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                sock_files_xferred is not None and sock_files_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `sock_files_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                sock_files_xferred is not None and sock_files_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `sock_files_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sock_files_xferred = sock_files_xferred

    @property
    def softlinks_xferred(self):
        """Gets the softlinks_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total number of softlinks transferred.  # noqa: E501

        :return: The softlinks_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._softlinks_xferred

    @softlinks_xferred.setter
    def softlinks_xferred(self, softlinks_xferred):
        """Sets the softlinks_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total number of softlinks transferred.  # noqa: E501

        :param softlinks_xferred: The softlinks_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                softlinks_xferred is not None and softlinks_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `softlinks_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                softlinks_xferred is not None and softlinks_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `softlinks_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._softlinks_xferred = softlinks_xferred

    @property
    def source_base_dataset_id(self):
        """Gets the source_base_dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Source Base Dataset ID.  # noqa: E501

        :return: The source_base_dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._source_base_dataset_id

    @source_base_dataset_id.setter
    def source_base_dataset_id(self, source_base_dataset_id):
        """Sets the source_base_dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Source Base Dataset ID.  # noqa: E501

        :param source_base_dataset_id: The source_base_dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                source_base_dataset_id is not None and source_base_dataset_id > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `source_base_dataset_id`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                source_base_dataset_id is not None and source_base_dataset_id < 0):  # noqa: E501
            raise ValueError("Invalid value for `source_base_dataset_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._source_base_dataset_id = source_base_dataset_id

    @property
    def target_dataset_id(self):
        """Gets the target_dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Target Dataset ID.  # noqa: E501

        :return: The target_dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._target_dataset_id

    @target_dataset_id.setter
    def target_dataset_id(self, target_dataset_id):
        """Sets the target_dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Target Dataset ID.  # noqa: E501

        :param target_dataset_id: The target_dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                target_dataset_id is not None and target_dataset_id > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `target_dataset_id`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                target_dataset_id is not None and target_dataset_id < 0):  # noqa: E501
            raise ValueError("Invalid value for `target_dataset_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._target_dataset_id = target_dataset_id

    @property
    def total_size_xferred(self):
        """Gets the total_size_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501

        Total size of files transferred.  # noqa: E501

        :return: The total_size_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :rtype: int
        """
        return self._total_size_xferred

    @total_size_xferred.setter
    def total_size_xferred(self, total_size_xferred):
        """Sets the total_size_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.

        Total size of files transferred.  # noqa: E501

        :param total_size_xferred: The total_size_xferred of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                total_size_xferred is not None and total_size_xferred > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `total_size_xferred`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self._configuration.client_side_validation and
                total_size_xferred is not None and total_size_xferred < 0):  # noqa: E501
            raise ValueError("Invalid value for `total_size_xferred`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_size_xferred = total_size_xferred

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
        if issubclass(DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics, dict):
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
        if not isinstance(other, DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics):
            return True

        return self.to_dict() != other.to_dict()
