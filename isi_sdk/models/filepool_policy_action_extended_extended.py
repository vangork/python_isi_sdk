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


class FilepoolPolicyActionExtendedExtended(object):
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
        'action_param': 'str',
        'action_type': 'str'
    }

    attribute_map = {
        'action_param': 'action_param',
        'action_type': 'action_type'
    }

    def __init__(self, action_param=None, action_type=None, _configuration=None):  # noqa: E501
        """FilepoolPolicyActionExtendedExtended - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action_param = None
        self._action_type = None
        self.discriminator = None

        if action_param is not None:
            self.action_param = action_param
        self.action_type = action_type

    @property
    def action_param(self):
        """Gets the action_param of this FilepoolPolicyActionExtendedExtended.  # noqa: E501

        Varies according to action_type:  - set_requested_protection: (default | +1 | +1n | +2:1 | +2d:1n | +2 | +2n | +3:1 | +3d:1n | +3d:1n1d | +3 | +3n | +4 | +4n | +4:1 | +4d:1n | +4:2 | +4d:2n | 2x | 3x | 4x | 5x | 6x | 7x | 8x).  - set_data_access_pattern: (random | concurrency | streaming).  - enable_coalescer <boolean>  - apply_data_storage_policy or apply_snapshot_storage_policy <object(dictionary)>:  -- storagepool <string>      Name of a storage pool or 'anywhere'.  -- ssd_strategy (metadata | metadata-write | data | avoid).      SSD strategy of diskpool policy action. 'metadata' stores a single metadata mirror on SSD; 'metadata-write' stores all metadata on SSD; 'data' stores all metadata and data on SSD and 'avoid' stores no data or metadata on SSD.   - set_cloudpool_policy <object (dictionary)>:  -- archive_parameters <object (dictionary)>:  --- pool <string>       Move to the cloud pool with the given ID.   --- compression <boolean>       Compress data moved to the cloud.   --- encryption <boolean>       Encrypt data moved to the cloud.   --- data_retention <duration>       The minimum number of seconds archived data will be retained in the cloud after deletion.   --- incremental_backup_retention <duration>       (Used with SyncIQ and NDMP backups.)  The minimum number of seconds cloud files will be retained after the creation of a SyncIQ backup or an incremental NDMP backup.   --- full_backup_retention <duration>       (Used with NDMP backups only.  Not applicable to SyncIQ.) The minimum number of seconds cloud files will be retained after the creation of a full NDMP backup.   --- writeback_frequency <duration>       The minimum number of seconds to wait before updating cloud data with local changes.   --- archive_snapshot_files <boolean>       Also include snapshots file when uploading to the cloud.  --- cache <object dictionary>:   ---- type <string>       Accessibility of archived files (one of \"cached\" or \"no-cache\").  ---- read_ahead <string>       Cache read ahead strategy for cloud files (one of partial, full).  ---- expiration <duration>      Duration of time in seconds until the cache expires.  - enable_packing <boolean> (only supported in version 4 and above)  - null parameter for action_param is use to clear the policy (POST).  <duration> Duration expressed as <integer>[YMWDHms].  # noqa: E501

        :return: The action_param of this FilepoolPolicyActionExtendedExtended.  # noqa: E501
        :rtype: str
        """
        return self._action_param

    @action_param.setter
    def action_param(self, action_param):
        """Sets the action_param of this FilepoolPolicyActionExtendedExtended.

        Varies according to action_type:  - set_requested_protection: (default | +1 | +1n | +2:1 | +2d:1n | +2 | +2n | +3:1 | +3d:1n | +3d:1n1d | +3 | +3n | +4 | +4n | +4:1 | +4d:1n | +4:2 | +4d:2n | 2x | 3x | 4x | 5x | 6x | 7x | 8x).  - set_data_access_pattern: (random | concurrency | streaming).  - enable_coalescer <boolean>  - apply_data_storage_policy or apply_snapshot_storage_policy <object(dictionary)>:  -- storagepool <string>      Name of a storage pool or 'anywhere'.  -- ssd_strategy (metadata | metadata-write | data | avoid).      SSD strategy of diskpool policy action. 'metadata' stores a single metadata mirror on SSD; 'metadata-write' stores all metadata on SSD; 'data' stores all metadata and data on SSD and 'avoid' stores no data or metadata on SSD.   - set_cloudpool_policy <object (dictionary)>:  -- archive_parameters <object (dictionary)>:  --- pool <string>       Move to the cloud pool with the given ID.   --- compression <boolean>       Compress data moved to the cloud.   --- encryption <boolean>       Encrypt data moved to the cloud.   --- data_retention <duration>       The minimum number of seconds archived data will be retained in the cloud after deletion.   --- incremental_backup_retention <duration>       (Used with SyncIQ and NDMP backups.)  The minimum number of seconds cloud files will be retained after the creation of a SyncIQ backup or an incremental NDMP backup.   --- full_backup_retention <duration>       (Used with NDMP backups only.  Not applicable to SyncIQ.) The minimum number of seconds cloud files will be retained after the creation of a full NDMP backup.   --- writeback_frequency <duration>       The minimum number of seconds to wait before updating cloud data with local changes.   --- archive_snapshot_files <boolean>       Also include snapshots file when uploading to the cloud.  --- cache <object dictionary>:   ---- type <string>       Accessibility of archived files (one of \"cached\" or \"no-cache\").  ---- read_ahead <string>       Cache read ahead strategy for cloud files (one of partial, full).  ---- expiration <duration>      Duration of time in seconds until the cache expires.  - enable_packing <boolean> (only supported in version 4 and above)  - null parameter for action_param is use to clear the policy (POST).  <duration> Duration expressed as <integer>[YMWDHms].  # noqa: E501

        :param action_param: The action_param of this FilepoolPolicyActionExtendedExtended.  # noqa: E501
        :type: str
        """

        self._action_param = action_param

    @property
    def action_type(self):
        """Gets the action_type of this FilepoolPolicyActionExtendedExtended.  # noqa: E501


        :return: The action_type of this FilepoolPolicyActionExtendedExtended.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this FilepoolPolicyActionExtendedExtended.


        :param action_type: The action_type of this FilepoolPolicyActionExtendedExtended.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and action_type is None:
            raise ValueError("Invalid value for `action_type`, must not be `None`")  # noqa: E501
        allowed_values = ["set_requested_protection", "set_data_access_pattern", "enable_coalescer", "apply_data_storage_policy", "apply_snapshot_storage_policy", "set_cloudpool_policy", "enable_packing"]  # noqa: E501
        if (self._configuration.client_side_validation and
                action_type not in allowed_values):
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

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
        if issubclass(FilepoolPolicyActionExtendedExtended, dict):
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
        if not isinstance(other, FilepoolPolicyActionExtendedExtended):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilepoolPolicyActionExtendedExtended):
            return True

        return self.to_dict() != other.to_dict()
