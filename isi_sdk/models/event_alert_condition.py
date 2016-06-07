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


class EventAlertCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EventAlertCondition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'categories': 'list[str]',
            'channel_ids': 'list[int]',
            'condition': 'str',
            'eventgroup_ids': 'list[str]',
            'interval': 'int',
            'limit': 'int',
            'transient': 'int'
        }

        self.attribute_map = {
            'categories': 'categories',
            'channel_ids': 'channel_ids',
            'condition': 'condition',
            'eventgroup_ids': 'eventgroup_ids',
            'interval': 'interval',
            'limit': 'limit',
            'transient': 'transient'
        }

        self._categories = None
        self._channel_ids = None
        self._condition = None
        self._eventgroup_ids = None
        self._interval = None
        self._limit = None
        self._transient = None

    @property
    def categories(self):
        """
        Gets the categories of this EventAlertCondition.
        Event Group categories to be alerted

        :return: The categories of this EventAlertCondition.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this EventAlertCondition.
        Event Group categories to be alerted

        :param categories: The categories of this EventAlertCondition.
        :type: list[str]
        """
        
        self._categories = categories

    @property
    def channel_ids(self):
        """
        Gets the channel_ids of this EventAlertCondition.
        Channels for alert

        :return: The channel_ids of this EventAlertCondition.
        :rtype: list[int]
        """
        return self._channel_ids

    @channel_ids.setter
    def channel_ids(self, channel_ids):
        """
        Sets the channel_ids of this EventAlertCondition.
        Channels for alert

        :param channel_ids: The channel_ids of this EventAlertCondition.
        :type: list[int]
        """
        
        self._channel_ids = channel_ids

    @property
    def condition(self):
        """
        Gets the condition of this EventAlertCondition.
        Trigger condition for alert

        :return: The condition of this EventAlertCondition.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this EventAlertCondition.
        Trigger condition for alert

        :param condition: The condition of this EventAlertCondition.
        :type: str
        """
        allowed_values = ["NEW", "NEW EVENTS", "ONGOING", "SEVERITY INCREASE", "SEVERITY DECREASE", "RESOLVED"]
        if condition is not None and condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition`, must be one of {0}"
                .format(allowed_values)
            )

        self._condition = condition

    @property
    def eventgroup_ids(self):
        """
        Gets the eventgroup_ids of this EventAlertCondition.
        Event Group IDs to be alerted

        :return: The eventgroup_ids of this EventAlertCondition.
        :rtype: list[str]
        """
        return self._eventgroup_ids

    @eventgroup_ids.setter
    def eventgroup_ids(self, eventgroup_ids):
        """
        Sets the eventgroup_ids of this EventAlertCondition.
        Event Group IDs to be alerted

        :param eventgroup_ids: The eventgroup_ids of this EventAlertCondition.
        :type: list[str]
        """
        
        self._eventgroup_ids = eventgroup_ids

    @property
    def interval(self):
        """
        Gets the interval of this EventAlertCondition.
        Required with ONGOING condition only, period in seconds between alerts of ongoing conditions

        :return: The interval of this EventAlertCondition.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this EventAlertCondition.
        Required with ONGOING condition only, period in seconds between alerts of ongoing conditions

        :param interval: The interval of this EventAlertCondition.
        :type: int
        """
        
        self._interval = interval

    @property
    def limit(self):
        """
        Gets the limit of this EventAlertCondition.
        Required with NEW EVENTS condition only, limits the number of alerts sent as events are added

        :return: The limit of this EventAlertCondition.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this EventAlertCondition.
        Required with NEW EVENTS condition only, limits the number of alerts sent as events are added

        :param limit: The limit of this EventAlertCondition.
        :type: int
        """
        
        self._limit = limit

    @property
    def transient(self):
        """
        Gets the transient of this EventAlertCondition.
        Any eventgroup lasting less than this many seconds is deemed transient and will not generate alerts under this condition.

        :return: The transient of this EventAlertCondition.
        :rtype: int
        """
        return self._transient

    @transient.setter
    def transient(self, transient):
        """
        Sets the transient of this EventAlertCondition.
        Any eventgroup lasting less than this many seconds is deemed transient and will not generate alerts under this condition.

        :param transient: The transient of this EventAlertCondition.
        :type: int
        """
        
        self._transient = transient

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

