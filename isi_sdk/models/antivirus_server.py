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


class AntivirusServer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AntivirusServer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'enabled': 'bool',
            'url': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'enabled': 'enabled',
            'url': 'url'
        }

        self._description = None
        self._enabled = None
        self._url = None

    @property
    def description(self):
        """
        Gets the description of this AntivirusServer.
        A description for the server.

        :return: The description of this AntivirusServer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AntivirusServer.
        A description for the server.

        :param description: The description of this AntivirusServer.
        :type: str
        """
        
        self._description = description

    @property
    def enabled(self):
        """
        Gets the enabled of this AntivirusServer.
        Whether the server is enabled.

        :return: The enabled of this AntivirusServer.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this AntivirusServer.
        Whether the server is enabled.

        :param enabled: The enabled of this AntivirusServer.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def url(self):
        """
        Gets the url of this AntivirusServer.
        The icap url for the server.  This should have a format of: icap://host.domain:port/path

        :return: The url of this AntivirusServer.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this AntivirusServer.
        The icap url for the server.  This should have a format of: icap://host.domain:port/path

        :param url: The url of this AntivirusServer.
        :type: str
        """
        
        if url is not None and len(url) < 1:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")

        self._url = url

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

