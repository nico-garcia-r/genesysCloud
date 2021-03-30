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

class AnalyticsUserDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AnalyticsUserDetail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_id': 'str',
            'primary_presence': 'list[AnalyticsUserPresenceRecord]',
            'routing_status': 'list[AnalyticsRoutingStatusRecord]'
        }

        self.attribute_map = {
            'user_id': 'userId',
            'primary_presence': 'primaryPresence',
            'routing_status': 'routingStatus'
        }

        self._user_id = None
        self._primary_presence = None
        self._routing_status = None

    @property
    def user_id(self):
        """
        Gets the user_id of this AnalyticsUserDetail.
        The identifier for the user

        :return: The user_id of this AnalyticsUserDetail.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AnalyticsUserDetail.
        The identifier for the user

        :param user_id: The user_id of this AnalyticsUserDetail.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def primary_presence(self):
        """
        Gets the primary_presence of this AnalyticsUserDetail.
        The presence records for the user

        :return: The primary_presence of this AnalyticsUserDetail.
        :rtype: list[AnalyticsUserPresenceRecord]
        """
        return self._primary_presence

    @primary_presence.setter
    def primary_presence(self, primary_presence):
        """
        Sets the primary_presence of this AnalyticsUserDetail.
        The presence records for the user

        :param primary_presence: The primary_presence of this AnalyticsUserDetail.
        :type: list[AnalyticsUserPresenceRecord]
        """
        
        self._primary_presence = primary_presence

    @property
    def routing_status(self):
        """
        Gets the routing_status of this AnalyticsUserDetail.
        The ACD routing status records for the user

        :return: The routing_status of this AnalyticsUserDetail.
        :rtype: list[AnalyticsRoutingStatusRecord]
        """
        return self._routing_status

    @routing_status.setter
    def routing_status(self, routing_status):
        """
        Sets the routing_status of this AnalyticsUserDetail.
        The ACD routing status records for the user

        :param routing_status: The routing_status of this AnalyticsUserDetail.
        :type: list[AnalyticsRoutingStatusRecord]
        """
        
        self._routing_status = routing_status

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

