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


class ProvidersKrb5Krb5Item(object):
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
        'groupnet': 'str',
        'id': 'str',
        'keytab_entries': 'list[ProvidersKrb5IdParamsKeytabEntry]',
        'keytab_file': 'str',
        'manual_keying': 'bool',
        'name': 'str',
        'realm': 'str',
        'recommended_spns': 'list[str]',
        'status': 'str',
        'system': 'bool',
        'user': 'str',
        'zone_name': 'str'
    }

    attribute_map = {
        'groupnet': 'groupnet',
        'id': 'id',
        'keytab_entries': 'keytab_entries',
        'keytab_file': 'keytab_file',
        'manual_keying': 'manual_keying',
        'name': 'name',
        'realm': 'realm',
        'recommended_spns': 'recommended_spns',
        'status': 'status',
        'system': 'system',
        'user': 'user',
        'zone_name': 'zone_name'
    }

    def __init__(self, groupnet=None, id=None, keytab_entries=None, keytab_file=None, manual_keying=None, name=None, realm=None, recommended_spns=None, status=None, system=None, user=None, zone_name=None, _configuration=None):  # noqa: E501
        """ProvidersKrb5Krb5Item - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._groupnet = None
        self._id = None
        self._keytab_entries = None
        self._keytab_file = None
        self._manual_keying = None
        self._name = None
        self._realm = None
        self._recommended_spns = None
        self._status = None
        self._system = None
        self._user = None
        self._zone_name = None
        self.discriminator = None

        if groupnet is not None:
            self.groupnet = groupnet
        if id is not None:
            self.id = id
        if keytab_entries is not None:
            self.keytab_entries = keytab_entries
        if keytab_file is not None:
            self.keytab_file = keytab_file
        if manual_keying is not None:
            self.manual_keying = manual_keying
        if name is not None:
            self.name = name
        if realm is not None:
            self.realm = realm
        if recommended_spns is not None:
            self.recommended_spns = recommended_spns
        if status is not None:
            self.status = status
        if system is not None:
            self.system = system
        if user is not None:
            self.user = user
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def groupnet(self):
        """Gets the groupnet of this ProvidersKrb5Krb5Item.  # noqa: E501

        Groupnet identifier.  # noqa: E501

        :return: The groupnet of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: str
        """
        return self._groupnet

    @groupnet.setter
    def groupnet(self, groupnet):
        """Sets the groupnet of this ProvidersKrb5Krb5Item.

        Groupnet identifier.  # noqa: E501

        :param groupnet: The groupnet of this ProvidersKrb5Krb5Item.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                groupnet is not None and len(groupnet) > 255):
            raise ValueError("Invalid value for `groupnet`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                groupnet is not None and len(groupnet) < 0):
            raise ValueError("Invalid value for `groupnet`, length must be greater than or equal to `0`")  # noqa: E501

        self._groupnet = groupnet

    @property
    def id(self):
        """Gets the id of this ProvidersKrb5Krb5Item.  # noqa: E501

        Specifies the Kerberos provider ID.  # noqa: E501

        :return: The id of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProvidersKrb5Krb5Item.

        Specifies the Kerberos provider ID.  # noqa: E501

        :param id: The id of this ProvidersKrb5Krb5Item.  # noqa: E501
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
    def keytab_entries(self):
        """Gets the keytab_entries of this ProvidersKrb5Krb5Item.  # noqa: E501

        Specifies the key information for the Kerberos SPNs.  # noqa: E501

        :return: The keytab_entries of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: list[ProvidersKrb5IdParamsKeytabEntry]
        """
        return self._keytab_entries

    @keytab_entries.setter
    def keytab_entries(self, keytab_entries):
        """Sets the keytab_entries of this ProvidersKrb5Krb5Item.

        Specifies the key information for the Kerberos SPNs.  # noqa: E501

        :param keytab_entries: The keytab_entries of this ProvidersKrb5Krb5Item.  # noqa: E501
        :type: list[ProvidersKrb5IdParamsKeytabEntry]
        """

        self._keytab_entries = keytab_entries

    @property
    def keytab_file(self):
        """Gets the keytab_file of this ProvidersKrb5Krb5Item.  # noqa: E501

        Specifies the path to a keytab file to import.  # noqa: E501

        :return: The keytab_file of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: str
        """
        return self._keytab_file

    @keytab_file.setter
    def keytab_file(self, keytab_file):
        """Sets the keytab_file of this ProvidersKrb5Krb5Item.

        Specifies the path to a keytab file to import.  # noqa: E501

        :param keytab_file: The keytab_file of this ProvidersKrb5Krb5Item.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                keytab_file is not None and len(keytab_file) > 4096):
            raise ValueError("Invalid value for `keytab_file`, length must be less than or equal to `4096`")  # noqa: E501
        if (self._configuration.client_side_validation and
                keytab_file is not None and len(keytab_file) < 0):
            raise ValueError("Invalid value for `keytab_file`, length must be greater than or equal to `0`")  # noqa: E501

        self._keytab_file = keytab_file

    @property
    def manual_keying(self):
        """Gets the manual_keying of this ProvidersKrb5Krb5Item.  # noqa: E501

        If true, keys are managed manually. If false, keys are managed through kadmin.  # noqa: E501

        :return: The manual_keying of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: bool
        """
        return self._manual_keying

    @manual_keying.setter
    def manual_keying(self, manual_keying):
        """Sets the manual_keying of this ProvidersKrb5Krb5Item.

        If true, keys are managed manually. If false, keys are managed through kadmin.  # noqa: E501

        :param manual_keying: The manual_keying of this ProvidersKrb5Krb5Item.  # noqa: E501
        :type: bool
        """

        self._manual_keying = manual_keying

    @property
    def name(self):
        """Gets the name of this ProvidersKrb5Krb5Item.  # noqa: E501

        Specifies the Kerberos provider name.  # noqa: E501

        :return: The name of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProvidersKrb5Krb5Item.

        Specifies the Kerberos provider name.  # noqa: E501

        :param name: The name of this ProvidersKrb5Krb5Item.  # noqa: E501
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
    def realm(self):
        """Gets the realm of this ProvidersKrb5Krb5Item.  # noqa: E501

        Specifies the name of realm.  # noqa: E501

        :return: The realm of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this ProvidersKrb5Krb5Item.

        Specifies the name of realm.  # noqa: E501

        :param realm: The realm of this ProvidersKrb5Krb5Item.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                realm is not None and len(realm) > 255):
            raise ValueError("Invalid value for `realm`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                realm is not None and len(realm) < 0):
            raise ValueError("Invalid value for `realm`, length must be greater than or equal to `0`")  # noqa: E501

        self._realm = realm

    @property
    def recommended_spns(self):
        """Gets the recommended_spns of this ProvidersKrb5Krb5Item.  # noqa: E501

        Specifies the recommended SPNs.  # noqa: E501

        :return: The recommended_spns of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: list[str]
        """
        return self._recommended_spns

    @recommended_spns.setter
    def recommended_spns(self, recommended_spns):
        """Sets the recommended_spns of this ProvidersKrb5Krb5Item.

        Specifies the recommended SPNs.  # noqa: E501

        :param recommended_spns: The recommended_spns of this ProvidersKrb5Krb5Item.  # noqa: E501
        :type: list[str]
        """

        self._recommended_spns = recommended_spns

    @property
    def status(self):
        """Gets the status of this ProvidersKrb5Krb5Item.  # noqa: E501

        Specifies the status of the provider.  # noqa: E501

        :return: The status of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProvidersKrb5Krb5Item.

        Specifies the status of the provider.  # noqa: E501

        :param status: The status of this ProvidersKrb5Krb5Item.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                status is not None and len(status) > 255):
            raise ValueError("Invalid value for `status`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                status is not None and len(status) < 0):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `0`")  # noqa: E501

        self._status = status

    @property
    def system(self):
        """Gets the system of this ProvidersKrb5Krb5Item.  # noqa: E501

        If true, indicates that this provider instance was created by OneFS and cannot be removed  # noqa: E501

        :return: The system of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this ProvidersKrb5Krb5Item.

        If true, indicates that this provider instance was created by OneFS and cannot be removed  # noqa: E501

        :param system: The system of this ProvidersKrb5Krb5Item.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def user(self):
        """Gets the user of this ProvidersKrb5Krb5Item.  # noqa: E501

        Specifies the name of the user that performs kadmin tasks.  # noqa: E501

        :return: The user of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ProvidersKrb5Krb5Item.

        Specifies the name of the user that performs kadmin tasks.  # noqa: E501

        :param user: The user of this ProvidersKrb5Krb5Item.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                user is not None and len(user) > 255):
            raise ValueError("Invalid value for `user`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                user is not None and len(user) < 0):
            raise ValueError("Invalid value for `user`, length must be greater than or equal to `0`")  # noqa: E501

        self._user = user

    @property
    def zone_name(self):
        """Gets the zone_name of this ProvidersKrb5Krb5Item.  # noqa: E501

        Specifies the name of the access zone in which this provider was created.  # noqa: E501

        :return: The zone_name of this ProvidersKrb5Krb5Item.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this ProvidersKrb5Krb5Item.

        Specifies the name of the access zone in which this provider was created.  # noqa: E501

        :param zone_name: The zone_name of this ProvidersKrb5Krb5Item.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                zone_name is not None and len(zone_name) > 255):
            raise ValueError("Invalid value for `zone_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                zone_name is not None and len(zone_name) < 0):
            raise ValueError("Invalid value for `zone_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._zone_name = zone_name

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
        if issubclass(ProvidersKrb5Krb5Item, dict):
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
        if not isinstance(other, ProvidersKrb5Krb5Item):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProvidersKrb5Krb5Item):
            return True

        return self.to_dict() != other.to_dict()
