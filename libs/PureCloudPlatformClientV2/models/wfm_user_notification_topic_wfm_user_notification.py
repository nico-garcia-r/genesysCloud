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

class WfmUserNotificationTopicWfmUserNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmUserNotificationTopicWfmUserNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'mutable_group_id': 'str',
            'timestamp': 'datetime',
            'type': 'str',
            'shift_trade': 'WfmUserNotificationTopicShiftTradeNotification',
            'time_off_request': 'WfmUserNotificationTopicTimeOffRequestNotification',
            'agent_notification': 'bool',
            'other_notification_ids_in_group': 'list[str]',
            'marked_as_read': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'mutable_group_id': 'mutableGroupId',
            'timestamp': 'timestamp',
            'type': 'type',
            'shift_trade': 'shiftTrade',
            'time_off_request': 'timeOffRequest',
            'agent_notification': 'agentNotification',
            'other_notification_ids_in_group': 'otherNotificationIdsInGroup',
            'marked_as_read': 'markedAsRead'
        }

        self._id = None
        self._mutable_group_id = None
        self._timestamp = None
        self._type = None
        self._shift_trade = None
        self._time_off_request = None
        self._agent_notification = None
        self._other_notification_ids_in_group = None
        self._marked_as_read = None

    @property
    def id(self):
        """
        Gets the id of this WfmUserNotificationTopicWfmUserNotification.


        :return: The id of this WfmUserNotificationTopicWfmUserNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WfmUserNotificationTopicWfmUserNotification.


        :param id: The id of this WfmUserNotificationTopicWfmUserNotification.
        :type: str
        """
        
        self._id = id

    @property
    def mutable_group_id(self):
        """
        Gets the mutable_group_id of this WfmUserNotificationTopicWfmUserNotification.


        :return: The mutable_group_id of this WfmUserNotificationTopicWfmUserNotification.
        :rtype: str
        """
        return self._mutable_group_id

    @mutable_group_id.setter
    def mutable_group_id(self, mutable_group_id):
        """
        Sets the mutable_group_id of this WfmUserNotificationTopicWfmUserNotification.


        :param mutable_group_id: The mutable_group_id of this WfmUserNotificationTopicWfmUserNotification.
        :type: str
        """
        
        self._mutable_group_id = mutable_group_id

    @property
    def timestamp(self):
        """
        Gets the timestamp of this WfmUserNotificationTopicWfmUserNotification.


        :return: The timestamp of this WfmUserNotificationTopicWfmUserNotification.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this WfmUserNotificationTopicWfmUserNotification.


        :param timestamp: The timestamp of this WfmUserNotificationTopicWfmUserNotification.
        :type: datetime
        """
        
        self._timestamp = timestamp

    @property
    def type(self):
        """
        Gets the type of this WfmUserNotificationTopicWfmUserNotification.


        :return: The type of this WfmUserNotificationTopicWfmUserNotification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WfmUserNotificationTopicWfmUserNotification.


        :param type: The type of this WfmUserNotificationTopicWfmUserNotification.
        :type: str
        """
        allowed_values = ["ShiftTrade", "TimeOffRequest"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def shift_trade(self):
        """
        Gets the shift_trade of this WfmUserNotificationTopicWfmUserNotification.


        :return: The shift_trade of this WfmUserNotificationTopicWfmUserNotification.
        :rtype: WfmUserNotificationTopicShiftTradeNotification
        """
        return self._shift_trade

    @shift_trade.setter
    def shift_trade(self, shift_trade):
        """
        Sets the shift_trade of this WfmUserNotificationTopicWfmUserNotification.


        :param shift_trade: The shift_trade of this WfmUserNotificationTopicWfmUserNotification.
        :type: WfmUserNotificationTopicShiftTradeNotification
        """
        
        self._shift_trade = shift_trade

    @property
    def time_off_request(self):
        """
        Gets the time_off_request of this WfmUserNotificationTopicWfmUserNotification.


        :return: The time_off_request of this WfmUserNotificationTopicWfmUserNotification.
        :rtype: WfmUserNotificationTopicTimeOffRequestNotification
        """
        return self._time_off_request

    @time_off_request.setter
    def time_off_request(self, time_off_request):
        """
        Sets the time_off_request of this WfmUserNotificationTopicWfmUserNotification.


        :param time_off_request: The time_off_request of this WfmUserNotificationTopicWfmUserNotification.
        :type: WfmUserNotificationTopicTimeOffRequestNotification
        """
        
        self._time_off_request = time_off_request

    @property
    def agent_notification(self):
        """
        Gets the agent_notification of this WfmUserNotificationTopicWfmUserNotification.


        :return: The agent_notification of this WfmUserNotificationTopicWfmUserNotification.
        :rtype: bool
        """
        return self._agent_notification

    @agent_notification.setter
    def agent_notification(self, agent_notification):
        """
        Sets the agent_notification of this WfmUserNotificationTopicWfmUserNotification.


        :param agent_notification: The agent_notification of this WfmUserNotificationTopicWfmUserNotification.
        :type: bool
        """
        
        self._agent_notification = agent_notification

    @property
    def other_notification_ids_in_group(self):
        """
        Gets the other_notification_ids_in_group of this WfmUserNotificationTopicWfmUserNotification.


        :return: The other_notification_ids_in_group of this WfmUserNotificationTopicWfmUserNotification.
        :rtype: list[str]
        """
        return self._other_notification_ids_in_group

    @other_notification_ids_in_group.setter
    def other_notification_ids_in_group(self, other_notification_ids_in_group):
        """
        Sets the other_notification_ids_in_group of this WfmUserNotificationTopicWfmUserNotification.


        :param other_notification_ids_in_group: The other_notification_ids_in_group of this WfmUserNotificationTopicWfmUserNotification.
        :type: list[str]
        """
        
        self._other_notification_ids_in_group = other_notification_ids_in_group

    @property
    def marked_as_read(self):
        """
        Gets the marked_as_read of this WfmUserNotificationTopicWfmUserNotification.


        :return: The marked_as_read of this WfmUserNotificationTopicWfmUserNotification.
        :rtype: bool
        """
        return self._marked_as_read

    @marked_as_read.setter
    def marked_as_read(self, marked_as_read):
        """
        Sets the marked_as_read of this WfmUserNotificationTopicWfmUserNotification.


        :param marked_as_read: The marked_as_read of this WfmUserNotificationTopicWfmUserNotification.
        :type: bool
        """
        
        self._marked_as_read = marked_as_read

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

