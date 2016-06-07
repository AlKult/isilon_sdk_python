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


class NetworkGroupnetCreateParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NetworkGroupnetCreateParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'dns_cache_enabled': 'bool',
            'dns_options': 'list[str]',
            'dns_search': 'list[str]',
            'dns_servers': 'list[str]',
            'name': 'str',
            'server_side_dns_search': 'bool'
        }

        self.attribute_map = {
            'description': 'description',
            'dns_cache_enabled': 'dns_cache_enabled',
            'dns_options': 'dns_options',
            'dns_search': 'dns_search',
            'dns_servers': 'dns_servers',
            'name': 'name',
            'server_side_dns_search': 'server_side_dns_search'
        }

        self._description = None
        self._dns_cache_enabled = None
        self._dns_options = None
        self._dns_search = None
        self._dns_servers = None
        self._name = None
        self._server_side_dns_search = None

    @property
    def description(self):
        """
        Gets the description of this NetworkGroupnetCreateParams.
        A description of the groupnet.

        :return: The description of this NetworkGroupnetCreateParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this NetworkGroupnetCreateParams.
        A description of the groupnet.

        :param description: The description of this NetworkGroupnetCreateParams.
        :type: str
        """
        
        if description is not None and len(description) > 128: 
            raise ValueError("Invalid value for `description`, length must be less than `128`")

        self._description = description

    @property
    def dns_cache_enabled(self):
        """
        Gets the dns_cache_enabled of this NetworkGroupnetCreateParams.
        DNS caching is enabled or disabled.

        :return: The dns_cache_enabled of this NetworkGroupnetCreateParams.
        :rtype: bool
        """
        return self._dns_cache_enabled

    @dns_cache_enabled.setter
    def dns_cache_enabled(self, dns_cache_enabled):
        """
        Sets the dns_cache_enabled of this NetworkGroupnetCreateParams.
        DNS caching is enabled or disabled.

        :param dns_cache_enabled: The dns_cache_enabled of this NetworkGroupnetCreateParams.
        :type: bool
        """
        
        self._dns_cache_enabled = dns_cache_enabled

    @property
    def dns_options(self):
        """
        Gets the dns_options of this NetworkGroupnetCreateParams.
        List of DNS resolver options.

        :return: The dns_options of this NetworkGroupnetCreateParams.
        :rtype: list[str]
        """
        return self._dns_options

    @dns_options.setter
    def dns_options(self, dns_options):
        """
        Sets the dns_options of this NetworkGroupnetCreateParams.
        List of DNS resolver options.

        :param dns_options: The dns_options of this NetworkGroupnetCreateParams.
        :type: list[str]
        """
        
        self._dns_options = dns_options

    @property
    def dns_search(self):
        """
        Gets the dns_search of this NetworkGroupnetCreateParams.
        List of DNS search suffixes.

        :return: The dns_search of this NetworkGroupnetCreateParams.
        :rtype: list[str]
        """
        return self._dns_search

    @dns_search.setter
    def dns_search(self, dns_search):
        """
        Sets the dns_search of this NetworkGroupnetCreateParams.
        List of DNS search suffixes.

        :param dns_search: The dns_search of this NetworkGroupnetCreateParams.
        :type: list[str]
        """
        
        self._dns_search = dns_search

    @property
    def dns_servers(self):
        """
        Gets the dns_servers of this NetworkGroupnetCreateParams.
        List of Domain Name Server IP addresses.

        :return: The dns_servers of this NetworkGroupnetCreateParams.
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """
        Sets the dns_servers of this NetworkGroupnetCreateParams.
        List of Domain Name Server IP addresses.

        :param dns_servers: The dns_servers of this NetworkGroupnetCreateParams.
        :type: list[str]
        """
        
        self._dns_servers = dns_servers

    @property
    def name(self):
        """
        Gets the name of this NetworkGroupnetCreateParams.
        The name of the groupnet.

        :return: The name of this NetworkGroupnetCreateParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NetworkGroupnetCreateParams.
        The name of the groupnet.

        :param name: The name of this NetworkGroupnetCreateParams.
        :type: str
        """
        
        if name is not None and len(name) > 32: 
            raise ValueError("Invalid value for `name`, length must be less than `32`")

        self._name = name

    @property
    def server_side_dns_search(self):
        """
        Gets the server_side_dns_search of this NetworkGroupnetCreateParams.
        Enable or disable appending nodes DNS search  list to client DNS inquiries directed at SmartConnect service IP.

        :return: The server_side_dns_search of this NetworkGroupnetCreateParams.
        :rtype: bool
        """
        return self._server_side_dns_search

    @server_side_dns_search.setter
    def server_side_dns_search(self, server_side_dns_search):
        """
        Sets the server_side_dns_search of this NetworkGroupnetCreateParams.
        Enable or disable appending nodes DNS search  list to client DNS inquiries directed at SmartConnect service IP.

        :param server_side_dns_search: The server_side_dns_search of this NetworkGroupnetCreateParams.
        :type: bool
        """
        
        self._server_side_dns_search = server_side_dns_search

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

