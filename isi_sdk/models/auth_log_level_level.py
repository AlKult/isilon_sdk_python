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


class AuthLogLevelLevel(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuthLogLevelLevel - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'lsass_level': 'str',
            'netlogon_level': 'str'
        }

        self.attribute_map = {
            'lsass_level': 'lsass-level',
            'netlogon_level': 'netlogon-level'
        }

        self._lsass_level = None
        self._netlogon_level = None

    @property
    def lsass_level(self):
        """
        Gets the lsass_level of this AuthLogLevelLevel.
        Valid auth logging levels

        :return: The lsass_level of this AuthLogLevelLevel.
        :rtype: str
        """
        return self._lsass_level

    @lsass_level.setter
    def lsass_level(self, lsass_level):
        """
        Sets the lsass_level of this AuthLogLevelLevel.
        Valid auth logging levels

        :param lsass_level: The lsass_level of this AuthLogLevelLevel.
        :type: str
        """
        allowed_values = ["always", "error", "warning", "info", "verbose", "debug", "trace"]
        if lsass_level is not None and lsass_level not in allowed_values:
            raise ValueError(
                "Invalid value for `lsass_level`, must be one of {0}"
                .format(allowed_values)
            )

        self._lsass_level = lsass_level

    @property
    def netlogon_level(self):
        """
        Gets the netlogon_level of this AuthLogLevelLevel.
        Valid auth logging levels

        :return: The netlogon_level of this AuthLogLevelLevel.
        :rtype: str
        """
        return self._netlogon_level

    @netlogon_level.setter
    def netlogon_level(self, netlogon_level):
        """
        Sets the netlogon_level of this AuthLogLevelLevel.
        Valid auth logging levels

        :param netlogon_level: The netlogon_level of this AuthLogLevelLevel.
        :type: str
        """
        allowed_values = ["always", "error", "warning", "info", "verbose", "debug", "trace"]
        if netlogon_level is not None and netlogon_level not in allowed_values:
            raise ValueError(
                "Invalid value for `netlogon_level`, must be one of {0}"
                .format(allowed_values)
            )

        self._netlogon_level = netlogon_level

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

