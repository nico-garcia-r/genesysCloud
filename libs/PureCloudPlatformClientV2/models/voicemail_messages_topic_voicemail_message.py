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

class VoicemailMessagesTopicVoicemailMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VoicemailMessagesTopicVoicemailMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'read': 'bool',
            'audio_recording_duration_seconds': 'int',
            'audio_recording_size_bytes': 'int',
            'created_date': 'datetime',
            'modified_date': 'datetime',
            'caller_address': 'str',
            'caller_name': 'str',
            'action': 'str',
            'note': 'str',
            'deleted': 'bool',
            'modified_by_user_id': 'str',
            'copied_to': 'list[VoicemailMessagesTopicVoicemailCopyRecord]',
            'copied_from': 'VoicemailMessagesTopicVoicemailCopyRecord'
        }

        self.attribute_map = {
            'id': 'id',
            'read': 'read',
            'audio_recording_duration_seconds': 'audioRecordingDurationSeconds',
            'audio_recording_size_bytes': 'audioRecordingSizeBytes',
            'created_date': 'createdDate',
            'modified_date': 'modifiedDate',
            'caller_address': 'callerAddress',
            'caller_name': 'callerName',
            'action': 'action',
            'note': 'note',
            'deleted': 'deleted',
            'modified_by_user_id': 'modifiedByUserId',
            'copied_to': 'copiedTo',
            'copied_from': 'copiedFrom'
        }

        self._id = None
        self._read = None
        self._audio_recording_duration_seconds = None
        self._audio_recording_size_bytes = None
        self._created_date = None
        self._modified_date = None
        self._caller_address = None
        self._caller_name = None
        self._action = None
        self._note = None
        self._deleted = None
        self._modified_by_user_id = None
        self._copied_to = None
        self._copied_from = None

    @property
    def id(self):
        """
        Gets the id of this VoicemailMessagesTopicVoicemailMessage.


        :return: The id of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VoicemailMessagesTopicVoicemailMessage.


        :param id: The id of this VoicemailMessagesTopicVoicemailMessage.
        :type: str
        """
        
        self._id = id

    @property
    def read(self):
        """
        Gets the read of this VoicemailMessagesTopicVoicemailMessage.


        :return: The read of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """
        Sets the read of this VoicemailMessagesTopicVoicemailMessage.


        :param read: The read of this VoicemailMessagesTopicVoicemailMessage.
        :type: bool
        """
        
        self._read = read

    @property
    def audio_recording_duration_seconds(self):
        """
        Gets the audio_recording_duration_seconds of this VoicemailMessagesTopicVoicemailMessage.


        :return: The audio_recording_duration_seconds of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: int
        """
        return self._audio_recording_duration_seconds

    @audio_recording_duration_seconds.setter
    def audio_recording_duration_seconds(self, audio_recording_duration_seconds):
        """
        Sets the audio_recording_duration_seconds of this VoicemailMessagesTopicVoicemailMessage.


        :param audio_recording_duration_seconds: The audio_recording_duration_seconds of this VoicemailMessagesTopicVoicemailMessage.
        :type: int
        """
        
        self._audio_recording_duration_seconds = audio_recording_duration_seconds

    @property
    def audio_recording_size_bytes(self):
        """
        Gets the audio_recording_size_bytes of this VoicemailMessagesTopicVoicemailMessage.


        :return: The audio_recording_size_bytes of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: int
        """
        return self._audio_recording_size_bytes

    @audio_recording_size_bytes.setter
    def audio_recording_size_bytes(self, audio_recording_size_bytes):
        """
        Sets the audio_recording_size_bytes of this VoicemailMessagesTopicVoicemailMessage.


        :param audio_recording_size_bytes: The audio_recording_size_bytes of this VoicemailMessagesTopicVoicemailMessage.
        :type: int
        """
        
        self._audio_recording_size_bytes = audio_recording_size_bytes

    @property
    def created_date(self):
        """
        Gets the created_date of this VoicemailMessagesTopicVoicemailMessage.


        :return: The created_date of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this VoicemailMessagesTopicVoicemailMessage.


        :param created_date: The created_date of this VoicemailMessagesTopicVoicemailMessage.
        :type: datetime
        """
        
        self._created_date = created_date

    @property
    def modified_date(self):
        """
        Gets the modified_date of this VoicemailMessagesTopicVoicemailMessage.


        :return: The modified_date of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this VoicemailMessagesTopicVoicemailMessage.


        :param modified_date: The modified_date of this VoicemailMessagesTopicVoicemailMessage.
        :type: datetime
        """
        
        self._modified_date = modified_date

    @property
    def caller_address(self):
        """
        Gets the caller_address of this VoicemailMessagesTopicVoicemailMessage.


        :return: The caller_address of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: str
        """
        return self._caller_address

    @caller_address.setter
    def caller_address(self, caller_address):
        """
        Sets the caller_address of this VoicemailMessagesTopicVoicemailMessage.


        :param caller_address: The caller_address of this VoicemailMessagesTopicVoicemailMessage.
        :type: str
        """
        
        self._caller_address = caller_address

    @property
    def caller_name(self):
        """
        Gets the caller_name of this VoicemailMessagesTopicVoicemailMessage.


        :return: The caller_name of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: str
        """
        return self._caller_name

    @caller_name.setter
    def caller_name(self, caller_name):
        """
        Sets the caller_name of this VoicemailMessagesTopicVoicemailMessage.


        :param caller_name: The caller_name of this VoicemailMessagesTopicVoicemailMessage.
        :type: str
        """
        
        self._caller_name = caller_name

    @property
    def action(self):
        """
        Gets the action of this VoicemailMessagesTopicVoicemailMessage.


        :return: The action of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this VoicemailMessagesTopicVoicemailMessage.


        :param action: The action of this VoicemailMessagesTopicVoicemailMessage.
        :type: str
        """
        
        self._action = action

    @property
    def note(self):
        """
        Gets the note of this VoicemailMessagesTopicVoicemailMessage.


        :return: The note of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this VoicemailMessagesTopicVoicemailMessage.


        :param note: The note of this VoicemailMessagesTopicVoicemailMessage.
        :type: str
        """
        
        self._note = note

    @property
    def deleted(self):
        """
        Gets the deleted of this VoicemailMessagesTopicVoicemailMessage.


        :return: The deleted of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this VoicemailMessagesTopicVoicemailMessage.


        :param deleted: The deleted of this VoicemailMessagesTopicVoicemailMessage.
        :type: bool
        """
        
        self._deleted = deleted

    @property
    def modified_by_user_id(self):
        """
        Gets the modified_by_user_id of this VoicemailMessagesTopicVoicemailMessage.


        :return: The modified_by_user_id of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: str
        """
        return self._modified_by_user_id

    @modified_by_user_id.setter
    def modified_by_user_id(self, modified_by_user_id):
        """
        Sets the modified_by_user_id of this VoicemailMessagesTopicVoicemailMessage.


        :param modified_by_user_id: The modified_by_user_id of this VoicemailMessagesTopicVoicemailMessage.
        :type: str
        """
        
        self._modified_by_user_id = modified_by_user_id

    @property
    def copied_to(self):
        """
        Gets the copied_to of this VoicemailMessagesTopicVoicemailMessage.


        :return: The copied_to of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: list[VoicemailMessagesTopicVoicemailCopyRecord]
        """
        return self._copied_to

    @copied_to.setter
    def copied_to(self, copied_to):
        """
        Sets the copied_to of this VoicemailMessagesTopicVoicemailMessage.


        :param copied_to: The copied_to of this VoicemailMessagesTopicVoicemailMessage.
        :type: list[VoicemailMessagesTopicVoicemailCopyRecord]
        """
        
        self._copied_to = copied_to

    @property
    def copied_from(self):
        """
        Gets the copied_from of this VoicemailMessagesTopicVoicemailMessage.


        :return: The copied_from of this VoicemailMessagesTopicVoicemailMessage.
        :rtype: VoicemailMessagesTopicVoicemailCopyRecord
        """
        return self._copied_from

    @copied_from.setter
    def copied_from(self, copied_from):
        """
        Sets the copied_from of this VoicemailMessagesTopicVoicemailMessage.


        :param copied_from: The copied_from of this VoicemailMessagesTopicVoicemailMessage.
        :type: VoicemailMessagesTopicVoicemailCopyRecord
        """
        
        self._copied_from = copied_from

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

