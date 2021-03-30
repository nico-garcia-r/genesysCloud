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
import json

from ..utils import sanitize_for_serialization

class AnalyticsUserPresenceRecord(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AnalyticsUserPresenceRecord - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_time': 'datetime',
            'end_time': 'datetime',
            'system_presence': 'str',
            'organization_presence_id': 'str'
        }

        self.attribute_map = {
            'start_time': 'startTime',
            'end_time': 'endTime',
            'system_presence': 'systemPresence',
            'organization_presence_id': 'organizationPresenceId'
        }

        self._start_time = None
        self._end_time = None
        self._system_presence = None
        self._organization_presence_id = None

    @property
    def start_time(self):
        """
        Gets the start_time of this AnalyticsUserPresenceRecord.
        The start time of the record. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_time of this AnalyticsUserPresenceRecord.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this AnalyticsUserPresenceRecord.
        The start time of the record. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_time: The start_time of this AnalyticsUserPresenceRecord.
        :type: datetime
        """
        
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this AnalyticsUserPresenceRecord.
        The end time of the record. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The end_time of this AnalyticsUserPresenceRecord.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this AnalyticsUserPresenceRecord.
        The end time of the record. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param end_time: The end_time of this AnalyticsUserPresenceRecord.
        :type: datetime
        """
        
        self._end_time = end_time

    @property
    def system_presence(self):
        """
        Gets the system_presence of this AnalyticsUserPresenceRecord.
        The user's system presence

        :return: The system_presence of this AnalyticsUserPresenceRecord.
        :rtype: str
        """
        return self._system_presence

    @system_presence.setter
    def system_presence(self, system_presence):
        """
        Sets the system_presence of this AnalyticsUserPresenceRecord.
        The user's system presence

        :param system_presence: The system_presence of this AnalyticsUserPresenceRecord.
        :type: str
        """
        allowed_values = ["AVAILABLE", "AWAY", "BUSY", "OFFLINE", "IDLE", "ON_QUEUE", "MEAL", "TRAINING", "MEETING", "BREAK"]
        if system_presence.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for system_presence -> " + system_presence)
            self._system_presence = "outdated_sdk_version"
        else:
            self._system_presence = system_presence

    @property
    def organization_presence_id(self):
        """
        Gets the organization_presence_id of this AnalyticsUserPresenceRecord.
        The identifier for the user's organization presence

        :return: The organization_presence_id of this AnalyticsUserPresenceRecord.
        :rtype: str
        """
        return self._organization_presence_id

    @organization_presence_id.setter
    def organization_presence_id(self, organization_presence_id):
        """
        Sets the organization_presence_id of this AnalyticsUserPresenceRecord.
        The identifier for the user's organization presence

        :param organization_presence_id: The organization_presence_id of this AnalyticsUserPresenceRecord.
        :type: str
        """
        
        self._organization_presence_id = organization_presence_id

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

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

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

