# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class ProvidersFileItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProvidersFileItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'authentication': 'bool',
            'create_home_directory': 'bool',
            'enabled': 'bool',
            'enumerate_groups': 'bool',
            'enumerate_users': 'bool',
            'findable_groups': 'list[str]',
            'findable_users': 'list[str]',
            'group_domain': 'str',
            'group_file': 'str',
            'home_directory_template': 'str',
            'listable_groups': 'list[str]',
            'listable_users': 'list[str]',
            'login_shell': 'str',
            'modifiable_groups': 'list[str]',
            'modifiable_users': 'list[str]',
            'name': 'str',
            'netgroup_file': 'str',
            'normalize_groups': 'bool',
            'normalize_users': 'bool',
            'ntlm_support': 'str',
            'password_file': 'str',
            'provider_domain': 'str',
            'restrict_findable': 'bool',
            'restrict_listable': 'bool',
            'restrict_modifiable': 'bool',
            'unfindable_groups': 'list[str]',
            'unfindable_users': 'list[str]',
            'unlistable_groups': 'list[str]',
            'unlistable_users': 'list[str]',
            'unmodifiable_groups': 'list[str]',
            'unmodifiable_users': 'list[str]',
            'user_domain': 'str'
        }

        self.attribute_map = {
            'authentication': 'authentication',
            'create_home_directory': 'create_home_directory',
            'enabled': 'enabled',
            'enumerate_groups': 'enumerate_groups',
            'enumerate_users': 'enumerate_users',
            'findable_groups': 'findable_groups',
            'findable_users': 'findable_users',
            'group_domain': 'group_domain',
            'group_file': 'group_file',
            'home_directory_template': 'home_directory_template',
            'listable_groups': 'listable_groups',
            'listable_users': 'listable_users',
            'login_shell': 'login_shell',
            'modifiable_groups': 'modifiable_groups',
            'modifiable_users': 'modifiable_users',
            'name': 'name',
            'netgroup_file': 'netgroup_file',
            'normalize_groups': 'normalize_groups',
            'normalize_users': 'normalize_users',
            'ntlm_support': 'ntlm_support',
            'password_file': 'password_file',
            'provider_domain': 'provider_domain',
            'restrict_findable': 'restrict_findable',
            'restrict_listable': 'restrict_listable',
            'restrict_modifiable': 'restrict_modifiable',
            'unfindable_groups': 'unfindable_groups',
            'unfindable_users': 'unfindable_users',
            'unlistable_groups': 'unlistable_groups',
            'unlistable_users': 'unlistable_users',
            'unmodifiable_groups': 'unmodifiable_groups',
            'unmodifiable_users': 'unmodifiable_users',
            'user_domain': 'user_domain'
        }

        self._authentication = None
        self._create_home_directory = None
        self._enabled = None
        self._enumerate_groups = None
        self._enumerate_users = None
        self._findable_groups = None
        self._findable_users = None
        self._group_domain = None
        self._group_file = None
        self._home_directory_template = None
        self._listable_groups = None
        self._listable_users = None
        self._login_shell = None
        self._modifiable_groups = None
        self._modifiable_users = None
        self._name = None
        self._netgroup_file = None
        self._normalize_groups = None
        self._normalize_users = None
        self._ntlm_support = None
        self._password_file = None
        self._provider_domain = None
        self._restrict_findable = None
        self._restrict_listable = None
        self._restrict_modifiable = None
        self._unfindable_groups = None
        self._unfindable_users = None
        self._unlistable_groups = None
        self._unlistable_users = None
        self._unmodifiable_groups = None
        self._unmodifiable_users = None
        self._user_domain = None

    @property
    def authentication(self):
        """
        Gets the authentication of this ProvidersFileItem.
        Enables authentication and identity mapping through the authentication provider.

        :return: The authentication of this ProvidersFileItem.
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """
        Sets the authentication of this ProvidersFileItem.
        Enables authentication and identity mapping through the authentication provider.

        :param authentication: The authentication of this ProvidersFileItem.
        :type: bool
        """
        
        self._authentication = authentication

    @property
    def create_home_directory(self):
        """
        Gets the create_home_directory of this ProvidersFileItem.
        Automatically creates a home directory on the first login.

        :return: The create_home_directory of this ProvidersFileItem.
        :rtype: bool
        """
        return self._create_home_directory

    @create_home_directory.setter
    def create_home_directory(self, create_home_directory):
        """
        Sets the create_home_directory of this ProvidersFileItem.
        Automatically creates a home directory on the first login.

        :param create_home_directory: The create_home_directory of this ProvidersFileItem.
        :type: bool
        """
        
        self._create_home_directory = create_home_directory

    @property
    def enabled(self):
        """
        Gets the enabled of this ProvidersFileItem.
        Enables the file provider.

        :return: The enabled of this ProvidersFileItem.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ProvidersFileItem.
        Enables the file provider.

        :param enabled: The enabled of this ProvidersFileItem.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def enumerate_groups(self):
        """
        Gets the enumerate_groups of this ProvidersFileItem.
        Enables the provider to enumerate groups.

        :return: The enumerate_groups of this ProvidersFileItem.
        :rtype: bool
        """
        return self._enumerate_groups

    @enumerate_groups.setter
    def enumerate_groups(self, enumerate_groups):
        """
        Sets the enumerate_groups of this ProvidersFileItem.
        Enables the provider to enumerate groups.

        :param enumerate_groups: The enumerate_groups of this ProvidersFileItem.
        :type: bool
        """
        
        self._enumerate_groups = enumerate_groups

    @property
    def enumerate_users(self):
        """
        Gets the enumerate_users of this ProvidersFileItem.
        Enables the provider to enumerate users.

        :return: The enumerate_users of this ProvidersFileItem.
        :rtype: bool
        """
        return self._enumerate_users

    @enumerate_users.setter
    def enumerate_users(self, enumerate_users):
        """
        Sets the enumerate_users of this ProvidersFileItem.
        Enables the provider to enumerate users.

        :param enumerate_users: The enumerate_users of this ProvidersFileItem.
        :type: bool
        """
        
        self._enumerate_users = enumerate_users

    @property
    def findable_groups(self):
        """
        Gets the findable_groups of this ProvidersFileItem.
        Specifies the list of groups that can be resolved.

        :return: The findable_groups of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._findable_groups

    @findable_groups.setter
    def findable_groups(self, findable_groups):
        """
        Sets the findable_groups of this ProvidersFileItem.
        Specifies the list of groups that can be resolved.

        :param findable_groups: The findable_groups of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._findable_groups = findable_groups

    @property
    def findable_users(self):
        """
        Gets the findable_users of this ProvidersFileItem.
        Specifies the list of users that can be resolved.

        :return: The findable_users of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._findable_users

    @findable_users.setter
    def findable_users(self, findable_users):
        """
        Sets the findable_users of this ProvidersFileItem.
        Specifies the list of users that can be resolved.

        :param findable_users: The findable_users of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._findable_users = findable_users

    @property
    def group_domain(self):
        """
        Gets the group_domain of this ProvidersFileItem.
        Specifies the domain for this provider through which domains are qualified.

        :return: The group_domain of this ProvidersFileItem.
        :rtype: str
        """
        return self._group_domain

    @group_domain.setter
    def group_domain(self, group_domain):
        """
        Sets the group_domain of this ProvidersFileItem.
        Specifies the domain for this provider through which domains are qualified.

        :param group_domain: The group_domain of this ProvidersFileItem.
        :type: str
        """
        
        self._group_domain = group_domain

    @property
    def group_file(self):
        """
        Gets the group_file of this ProvidersFileItem.
        Specifies the location of the file that contains information about the group.

        :return: The group_file of this ProvidersFileItem.
        :rtype: str
        """
        return self._group_file

    @group_file.setter
    def group_file(self, group_file):
        """
        Sets the group_file of this ProvidersFileItem.
        Specifies the location of the file that contains information about the group.

        :param group_file: The group_file of this ProvidersFileItem.
        :type: str
        """
        
        self._group_file = group_file

    @property
    def home_directory_template(self):
        """
        Gets the home_directory_template of this ProvidersFileItem.
        Specifies the path to the home directory template.

        :return: The home_directory_template of this ProvidersFileItem.
        :rtype: str
        """
        return self._home_directory_template

    @home_directory_template.setter
    def home_directory_template(self, home_directory_template):
        """
        Sets the home_directory_template of this ProvidersFileItem.
        Specifies the path to the home directory template.

        :param home_directory_template: The home_directory_template of this ProvidersFileItem.
        :type: str
        """
        
        self._home_directory_template = home_directory_template

    @property
    def listable_groups(self):
        """
        Gets the listable_groups of this ProvidersFileItem.
        Specifies the groups that can be viewed in the provider.

        :return: The listable_groups of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._listable_groups

    @listable_groups.setter
    def listable_groups(self, listable_groups):
        """
        Sets the listable_groups of this ProvidersFileItem.
        Specifies the groups that can be viewed in the provider.

        :param listable_groups: The listable_groups of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._listable_groups = listable_groups

    @property
    def listable_users(self):
        """
        Gets the listable_users of this ProvidersFileItem.
        Specifies the users that can be viewed in the provider.

        :return: The listable_users of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._listable_users

    @listable_users.setter
    def listable_users(self, listable_users):
        """
        Sets the listable_users of this ProvidersFileItem.
        Specifies the users that can be viewed in the provider.

        :param listable_users: The listable_users of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._listable_users = listable_users

    @property
    def login_shell(self):
        """
        Gets the login_shell of this ProvidersFileItem.
        Specifies the login shell path.

        :return: The login_shell of this ProvidersFileItem.
        :rtype: str
        """
        return self._login_shell

    @login_shell.setter
    def login_shell(self, login_shell):
        """
        Sets the login_shell of this ProvidersFileItem.
        Specifies the login shell path.

        :param login_shell: The login_shell of this ProvidersFileItem.
        :type: str
        """
        
        self._login_shell = login_shell

    @property
    def modifiable_groups(self):
        """
        Gets the modifiable_groups of this ProvidersFileItem.
        Specifies the groups that can be modified in the provider.

        :return: The modifiable_groups of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._modifiable_groups

    @modifiable_groups.setter
    def modifiable_groups(self, modifiable_groups):
        """
        Sets the modifiable_groups of this ProvidersFileItem.
        Specifies the groups that can be modified in the provider.

        :param modifiable_groups: The modifiable_groups of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._modifiable_groups = modifiable_groups

    @property
    def modifiable_users(self):
        """
        Gets the modifiable_users of this ProvidersFileItem.
        Specifies the users that can be modified in the provider.

        :return: The modifiable_users of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._modifiable_users

    @modifiable_users.setter
    def modifiable_users(self, modifiable_users):
        """
        Sets the modifiable_users of this ProvidersFileItem.
        Specifies the users that can be modified in the provider.

        :param modifiable_users: The modifiable_users of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._modifiable_users = modifiable_users

    @property
    def name(self):
        """
        Gets the name of this ProvidersFileItem.
        Specifies the name of the file provider.

        :return: The name of this ProvidersFileItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProvidersFileItem.
        Specifies the name of the file provider.

        :param name: The name of this ProvidersFileItem.
        :type: str
        """
        
        self._name = name

    @property
    def netgroup_file(self):
        """
        Gets the netgroup_file of this ProvidersFileItem.
        Specifies the path to a netgroups replacement file.

        :return: The netgroup_file of this ProvidersFileItem.
        :rtype: str
        """
        return self._netgroup_file

    @netgroup_file.setter
    def netgroup_file(self, netgroup_file):
        """
        Sets the netgroup_file of this ProvidersFileItem.
        Specifies the path to a netgroups replacement file.

        :param netgroup_file: The netgroup_file of this ProvidersFileItem.
        :type: str
        """
        
        self._netgroup_file = netgroup_file

    @property
    def normalize_groups(self):
        """
        Gets the normalize_groups of this ProvidersFileItem.
        Normalizes group names to lowercase before look up.

        :return: The normalize_groups of this ProvidersFileItem.
        :rtype: bool
        """
        return self._normalize_groups

    @normalize_groups.setter
    def normalize_groups(self, normalize_groups):
        """
        Sets the normalize_groups of this ProvidersFileItem.
        Normalizes group names to lowercase before look up.

        :param normalize_groups: The normalize_groups of this ProvidersFileItem.
        :type: bool
        """
        
        self._normalize_groups = normalize_groups

    @property
    def normalize_users(self):
        """
        Gets the normalize_users of this ProvidersFileItem.
        Normalizes user names to lowercase before look up.

        :return: The normalize_users of this ProvidersFileItem.
        :rtype: bool
        """
        return self._normalize_users

    @normalize_users.setter
    def normalize_users(self, normalize_users):
        """
        Sets the normalize_users of this ProvidersFileItem.
        Normalizes user names to lowercase before look up.

        :param normalize_users: The normalize_users of this ProvidersFileItem.
        :type: bool
        """
        
        self._normalize_users = normalize_users

    @property
    def ntlm_support(self):
        """
        Gets the ntlm_support of this ProvidersFileItem.
        Specifies which NTLM versions to support for users with NTLM-compatible credentials.

        :return: The ntlm_support of this ProvidersFileItem.
        :rtype: str
        """
        return self._ntlm_support

    @ntlm_support.setter
    def ntlm_support(self, ntlm_support):
        """
        Sets the ntlm_support of this ProvidersFileItem.
        Specifies which NTLM versions to support for users with NTLM-compatible credentials.

        :param ntlm_support: The ntlm_support of this ProvidersFileItem.
        :type: str
        """
        allowed_values = ["all", "v2only", "none"]
        if ntlm_support is not None and ntlm_support not in allowed_values:
            raise ValueError(
                "Invalid value for `ntlm_support`, must be one of {0}"
                .format(allowed_values)
            )

        self._ntlm_support = ntlm_support

    @property
    def password_file(self):
        """
        Gets the password_file of this ProvidersFileItem.
        Specifies the location of the file containing information about users.

        :return: The password_file of this ProvidersFileItem.
        :rtype: str
        """
        return self._password_file

    @password_file.setter
    def password_file(self, password_file):
        """
        Sets the password_file of this ProvidersFileItem.
        Specifies the location of the file containing information about users.

        :param password_file: The password_file of this ProvidersFileItem.
        :type: str
        """
        
        self._password_file = password_file

    @property
    def provider_domain(self):
        """
        Gets the provider_domain of this ProvidersFileItem.
        Specifies the domain for the provider.

        :return: The provider_domain of this ProvidersFileItem.
        :rtype: str
        """
        return self._provider_domain

    @provider_domain.setter
    def provider_domain(self, provider_domain):
        """
        Sets the provider_domain of this ProvidersFileItem.
        Specifies the domain for the provider.

        :param provider_domain: The provider_domain of this ProvidersFileItem.
        :type: str
        """
        
        self._provider_domain = provider_domain

    @property
    def restrict_findable(self):
        """
        Gets the restrict_findable of this ProvidersFileItem.
        If true, checks the provider for filtered lists of findable and unfindable users and groups.

        :return: The restrict_findable of this ProvidersFileItem.
        :rtype: bool
        """
        return self._restrict_findable

    @restrict_findable.setter
    def restrict_findable(self, restrict_findable):
        """
        Sets the restrict_findable of this ProvidersFileItem.
        If true, checks the provider for filtered lists of findable and unfindable users and groups.

        :param restrict_findable: The restrict_findable of this ProvidersFileItem.
        :type: bool
        """
        
        self._restrict_findable = restrict_findable

    @property
    def restrict_listable(self):
        """
        Gets the restrict_listable of this ProvidersFileItem.
        If true, checks the provider for filtered lists of listable and unlistable users and groups.

        :return: The restrict_listable of this ProvidersFileItem.
        :rtype: bool
        """
        return self._restrict_listable

    @restrict_listable.setter
    def restrict_listable(self, restrict_listable):
        """
        Sets the restrict_listable of this ProvidersFileItem.
        If true, checks the provider for filtered lists of listable and unlistable users and groups.

        :param restrict_listable: The restrict_listable of this ProvidersFileItem.
        :type: bool
        """
        
        self._restrict_listable = restrict_listable

    @property
    def restrict_modifiable(self):
        """
        Gets the restrict_modifiable of this ProvidersFileItem.
        If true, checks the provider for filtered lists of modifiable and unmodifiable users and groups.

        :return: The restrict_modifiable of this ProvidersFileItem.
        :rtype: bool
        """
        return self._restrict_modifiable

    @restrict_modifiable.setter
    def restrict_modifiable(self, restrict_modifiable):
        """
        Sets the restrict_modifiable of this ProvidersFileItem.
        If true, checks the provider for filtered lists of modifiable and unmodifiable users and groups.

        :param restrict_modifiable: The restrict_modifiable of this ProvidersFileItem.
        :type: bool
        """
        
        self._restrict_modifiable = restrict_modifiable

    @property
    def unfindable_groups(self):
        """
        Gets the unfindable_groups of this ProvidersFileItem.
        Specifies groups that cannot be resolved by the provider.

        :return: The unfindable_groups of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._unfindable_groups

    @unfindable_groups.setter
    def unfindable_groups(self, unfindable_groups):
        """
        Sets the unfindable_groups of this ProvidersFileItem.
        Specifies groups that cannot be resolved by the provider.

        :param unfindable_groups: The unfindable_groups of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._unfindable_groups = unfindable_groups

    @property
    def unfindable_users(self):
        """
        Gets the unfindable_users of this ProvidersFileItem.
        Specifies users that cannot be resolved by the provider.

        :return: The unfindable_users of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._unfindable_users

    @unfindable_users.setter
    def unfindable_users(self, unfindable_users):
        """
        Sets the unfindable_users of this ProvidersFileItem.
        Specifies users that cannot be resolved by the provider.

        :param unfindable_users: The unfindable_users of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._unfindable_users = unfindable_users

    @property
    def unlistable_groups(self):
        """
        Gets the unlistable_groups of this ProvidersFileItem.
        Specifies a group that cannot be listed by the provider.

        :return: The unlistable_groups of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._unlistable_groups

    @unlistable_groups.setter
    def unlistable_groups(self, unlistable_groups):
        """
        Sets the unlistable_groups of this ProvidersFileItem.
        Specifies a group that cannot be listed by the provider.

        :param unlistable_groups: The unlistable_groups of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._unlistable_groups = unlistable_groups

    @property
    def unlistable_users(self):
        """
        Gets the unlistable_users of this ProvidersFileItem.
        Specifies a user that cannot be listed by the provider.

        :return: The unlistable_users of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._unlistable_users

    @unlistable_users.setter
    def unlistable_users(self, unlistable_users):
        """
        Sets the unlistable_users of this ProvidersFileItem.
        Specifies a user that cannot be listed by the provider.

        :param unlistable_users: The unlistable_users of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._unlistable_users = unlistable_users

    @property
    def unmodifiable_groups(self):
        """
        Gets the unmodifiable_groups of this ProvidersFileItem.
        Specifies a group that cannot be modified by the provider.

        :return: The unmodifiable_groups of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._unmodifiable_groups

    @unmodifiable_groups.setter
    def unmodifiable_groups(self, unmodifiable_groups):
        """
        Sets the unmodifiable_groups of this ProvidersFileItem.
        Specifies a group that cannot be modified by the provider.

        :param unmodifiable_groups: The unmodifiable_groups of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._unmodifiable_groups = unmodifiable_groups

    @property
    def unmodifiable_users(self):
        """
        Gets the unmodifiable_users of this ProvidersFileItem.
        Specifies a user that cannot be modified by the provider.

        :return: The unmodifiable_users of this ProvidersFileItem.
        :rtype: list[str]
        """
        return self._unmodifiable_users

    @unmodifiable_users.setter
    def unmodifiable_users(self, unmodifiable_users):
        """
        Sets the unmodifiable_users of this ProvidersFileItem.
        Specifies a user that cannot be modified by the provider.

        :param unmodifiable_users: The unmodifiable_users of this ProvidersFileItem.
        :type: list[str]
        """
        
        self._unmodifiable_users = unmodifiable_users

    @property
    def user_domain(self):
        """
        Gets the user_domain of this ProvidersFileItem.
        Specifies the domain for this provider through which users are qualified.

        :return: The user_domain of this ProvidersFileItem.
        :rtype: str
        """
        return self._user_domain

    @user_domain.setter
    def user_domain(self, user_domain):
        """
        Sets the user_domain of this ProvidersFileItem.
        Specifies the domain for this provider through which users are qualified.

        :param user_domain: The user_domain of this ProvidersFileItem.
        :type: str
        """
        
        self._user_domain = user_domain

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

