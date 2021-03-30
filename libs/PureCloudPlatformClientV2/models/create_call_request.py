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

class CreateCallRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateCallRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phone_number': 'str',
            'caller_id': 'str',
            'caller_id_name': 'str',
            'call_from_queue_id': 'str',
            'call_queue_id': 'str',
            'call_user_id': 'str',
            'priority': 'int',
            'language_id': 'str',
            'routing_skills_ids': 'list[str]',
            'conversation_ids': 'list[str]',
            'participants': 'list[Destination]',
            'uui_data': 'str'
        }

        self.attribute_map = {
            'phone_number': 'phoneNumber',
            'caller_id': 'callerId',
            'caller_id_name': 'callerIdName',
            'call_from_queue_id': 'callFromQueueId',
            'call_queue_id': 'callQueueId',
            'call_user_id': 'callUserId',
            'priority': 'priority',
            'language_id': 'languageId',
            'routing_skills_ids': 'routingSkillsIds',
            'conversation_ids': 'conversationIds',
            'participants': 'participants',
            'uui_data': 'uuiData'
        }

        self._phone_number = None
        self._caller_id = None
        self._caller_id_name = None
        self._call_from_queue_id = None
        self._call_queue_id = None
        self._call_user_id = None
        self._priority = None
        self._language_id = None
        self._routing_skills_ids = None
        self._conversation_ids = None
        self._participants = None
        self._uui_data = None

    @property
    def phone_number(self):
        """
        Gets the phone_number of this CreateCallRequest.
        The phone number to dial.

        :return: The phone_number of this CreateCallRequest.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this CreateCallRequest.
        The phone number to dial.

        :param phone_number: The phone_number of this CreateCallRequest.
        :type: str
        """
        
        self._phone_number = phone_number

    @property
    def caller_id(self):
        """
        Gets the caller_id of this CreateCallRequest.
        The caller id phone number for this outbound call.

        :return: The caller_id of this CreateCallRequest.
        :rtype: str
        """
        return self._caller_id

    @caller_id.setter
    def caller_id(self, caller_id):
        """
        Sets the caller_id of this CreateCallRequest.
        The caller id phone number for this outbound call.

        :param caller_id: The caller_id of this CreateCallRequest.
        :type: str
        """
        
        self._caller_id = caller_id

    @property
    def caller_id_name(self):
        """
        Gets the caller_id_name of this CreateCallRequest.
        The caller id name for this outbound call.

        :return: The caller_id_name of this CreateCallRequest.
        :rtype: str
        """
        return self._caller_id_name

    @caller_id_name.setter
    def caller_id_name(self, caller_id_name):
        """
        Sets the caller_id_name of this CreateCallRequest.
        The caller id name for this outbound call.

        :param caller_id_name: The caller_id_name of this CreateCallRequest.
        :type: str
        """
        
        self._caller_id_name = caller_id_name

    @property
    def call_from_queue_id(self):
        """
        Gets the call_from_queue_id of this CreateCallRequest.
        The queue ID to call on behalf of.

        :return: The call_from_queue_id of this CreateCallRequest.
        :rtype: str
        """
        return self._call_from_queue_id

    @call_from_queue_id.setter
    def call_from_queue_id(self, call_from_queue_id):
        """
        Sets the call_from_queue_id of this CreateCallRequest.
        The queue ID to call on behalf of.

        :param call_from_queue_id: The call_from_queue_id of this CreateCallRequest.
        :type: str
        """
        
        self._call_from_queue_id = call_from_queue_id

    @property
    def call_queue_id(self):
        """
        Gets the call_queue_id of this CreateCallRequest.
        The queue ID to call.

        :return: The call_queue_id of this CreateCallRequest.
        :rtype: str
        """
        return self._call_queue_id

    @call_queue_id.setter
    def call_queue_id(self, call_queue_id):
        """
        Sets the call_queue_id of this CreateCallRequest.
        The queue ID to call.

        :param call_queue_id: The call_queue_id of this CreateCallRequest.
        :type: str
        """
        
        self._call_queue_id = call_queue_id

    @property
    def call_user_id(self):
        """
        Gets the call_user_id of this CreateCallRequest.
        The user ID to call.

        :return: The call_user_id of this CreateCallRequest.
        :rtype: str
        """
        return self._call_user_id

    @call_user_id.setter
    def call_user_id(self, call_user_id):
        """
        Sets the call_user_id of this CreateCallRequest.
        The user ID to call.

        :param call_user_id: The call_user_id of this CreateCallRequest.
        :type: str
        """
        
        self._call_user_id = call_user_id

    @property
    def priority(self):
        """
        Gets the priority of this CreateCallRequest.
        The priority to assign to this call (if calling a queue).

        :return: The priority of this CreateCallRequest.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this CreateCallRequest.
        The priority to assign to this call (if calling a queue).

        :param priority: The priority of this CreateCallRequest.
        :type: int
        """
        
        self._priority = priority

    @property
    def language_id(self):
        """
        Gets the language_id of this CreateCallRequest.
        The language skill ID to use for routing this call (if calling a queue).

        :return: The language_id of this CreateCallRequest.
        :rtype: str
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        """
        Sets the language_id of this CreateCallRequest.
        The language skill ID to use for routing this call (if calling a queue).

        :param language_id: The language_id of this CreateCallRequest.
        :type: str
        """
        
        self._language_id = language_id

    @property
    def routing_skills_ids(self):
        """
        Gets the routing_skills_ids of this CreateCallRequest.
        The skill ID's to use for routing this call (if calling a queue).

        :return: The routing_skills_ids of this CreateCallRequest.
        :rtype: list[str]
        """
        return self._routing_skills_ids

    @routing_skills_ids.setter
    def routing_skills_ids(self, routing_skills_ids):
        """
        Sets the routing_skills_ids of this CreateCallRequest.
        The skill ID's to use for routing this call (if calling a queue).

        :param routing_skills_ids: The routing_skills_ids of this CreateCallRequest.
        :type: list[str]
        """
        
        self._routing_skills_ids = routing_skills_ids

    @property
    def conversation_ids(self):
        """
        Gets the conversation_ids of this CreateCallRequest.
        The list of existing call conversations to merge into a new ad-hoc conference.

        :return: The conversation_ids of this CreateCallRequest.
        :rtype: list[str]
        """
        return self._conversation_ids

    @conversation_ids.setter
    def conversation_ids(self, conversation_ids):
        """
        Sets the conversation_ids of this CreateCallRequest.
        The list of existing call conversations to merge into a new ad-hoc conference.

        :param conversation_ids: The conversation_ids of this CreateCallRequest.
        :type: list[str]
        """
        
        self._conversation_ids = conversation_ids

    @property
    def participants(self):
        """
        Gets the participants of this CreateCallRequest.
        The list of participants to call to create a new ad-hoc conference.

        :return: The participants of this CreateCallRequest.
        :rtype: list[Destination]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """
        Sets the participants of this CreateCallRequest.
        The list of participants to call to create a new ad-hoc conference.

        :param participants: The participants of this CreateCallRequest.
        :type: list[Destination]
        """
        
        self._participants = participants

    @property
    def uui_data(self):
        """
        Gets the uui_data of this CreateCallRequest.
        User to User Information (UUI) data managed by SIP session application.

        :return: The uui_data of this CreateCallRequest.
        :rtype: str
        """
        return self._uui_data

    @uui_data.setter
    def uui_data(self, uui_data):
        """
        Sets the uui_data of this CreateCallRequest.
        User to User Information (UUI) data managed by SIP session application.

        :param uui_data: The uui_data of this CreateCallRequest.
        :type: str
        """
        
        self._uui_data = uui_data

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

