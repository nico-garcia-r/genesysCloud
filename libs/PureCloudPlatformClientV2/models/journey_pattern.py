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

class JourneyPattern(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JourneyPattern - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'criteria': 'list[Criteria]',
            'count': 'int',
            'stream_type': 'str',
            'session_type': 'str',
            'event_name': 'str'
        }

        self.attribute_map = {
            'criteria': 'criteria',
            'count': 'count',
            'stream_type': 'streamType',
            'session_type': 'sessionType',
            'event_name': 'eventName'
        }

        self._criteria = None
        self._count = None
        self._stream_type = None
        self._session_type = None
        self._event_name = None

    @property
    def criteria(self):
        """
        Gets the criteria of this JourneyPattern.
        A list of one or more criteria to satisfy.

        :return: The criteria of this JourneyPattern.
        :rtype: list[Criteria]
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """
        Sets the criteria of this JourneyPattern.
        A list of one or more criteria to satisfy.

        :param criteria: The criteria of this JourneyPattern.
        :type: list[Criteria]
        """
        
        self._criteria = criteria

    @property
    def count(self):
        """
        Gets the count of this JourneyPattern.
        The number of times the pattern must match.

        :return: The count of this JourneyPattern.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this JourneyPattern.
        The number of times the pattern must match.

        :param count: The count of this JourneyPattern.
        :type: int
        """
        
        self._count = count

    @property
    def stream_type(self):
        """
        Gets the stream_type of this JourneyPattern.
        The stream type for which this pattern can be matched on.

        :return: The stream_type of this JourneyPattern.
        :rtype: str
        """
        return self._stream_type

    @stream_type.setter
    def stream_type(self, stream_type):
        """
        Sets the stream_type of this JourneyPattern.
        The stream type for which this pattern can be matched on.

        :param stream_type: The stream_type of this JourneyPattern.
        :type: str
        """
        allowed_values = ["Web", "Custom", "Conversation"]
        if stream_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for stream_type -> " + stream_type)
            self._stream_type = "outdated_sdk_version"
        else:
            self._stream_type = stream_type

    @property
    def session_type(self):
        """
        Gets the session_type of this JourneyPattern.
        The session type for which this pattern can be matched on.

        :return: The session_type of this JourneyPattern.
        :rtype: str
        """
        return self._session_type

    @session_type.setter
    def session_type(self, session_type):
        """
        Sets the session_type of this JourneyPattern.
        The session type for which this pattern can be matched on.

        :param session_type: The session_type of this JourneyPattern.
        :type: str
        """
        
        self._session_type = session_type

    @property
    def event_name(self):
        """
        Gets the event_name of this JourneyPattern.
        The name of the event for which this pattern can be matched on.

        :return: The event_name of this JourneyPattern.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this JourneyPattern.
        The name of the event for which this pattern can be matched on.

        :param event_name: The event_name of this JourneyPattern.
        :type: str
        """
        
        self._event_name = event_name

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

