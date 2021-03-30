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

class RecordingArchiveRestoreTopicMediaResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RecordingArchiveRestoreTopicMediaResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'channel_id': 'str',
            'wave_uri': 'str',
            'media_uri': 'str',
            'waveform_data': 'list[float]'
        }

        self.attribute_map = {
            'channel_id': 'channelId',
            'wave_uri': 'waveUri',
            'media_uri': 'mediaUri',
            'waveform_data': 'waveformData'
        }

        self._channel_id = None
        self._wave_uri = None
        self._media_uri = None
        self._waveform_data = None

    @property
    def channel_id(self):
        """
        Gets the channel_id of this RecordingArchiveRestoreTopicMediaResult.


        :return: The channel_id of this RecordingArchiveRestoreTopicMediaResult.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """
        Sets the channel_id of this RecordingArchiveRestoreTopicMediaResult.


        :param channel_id: The channel_id of this RecordingArchiveRestoreTopicMediaResult.
        :type: str
        """
        
        self._channel_id = channel_id

    @property
    def wave_uri(self):
        """
        Gets the wave_uri of this RecordingArchiveRestoreTopicMediaResult.


        :return: The wave_uri of this RecordingArchiveRestoreTopicMediaResult.
        :rtype: str
        """
        return self._wave_uri

    @wave_uri.setter
    def wave_uri(self, wave_uri):
        """
        Sets the wave_uri of this RecordingArchiveRestoreTopicMediaResult.


        :param wave_uri: The wave_uri of this RecordingArchiveRestoreTopicMediaResult.
        :type: str
        """
        
        self._wave_uri = wave_uri

    @property
    def media_uri(self):
        """
        Gets the media_uri of this RecordingArchiveRestoreTopicMediaResult.


        :return: The media_uri of this RecordingArchiveRestoreTopicMediaResult.
        :rtype: str
        """
        return self._media_uri

    @media_uri.setter
    def media_uri(self, media_uri):
        """
        Sets the media_uri of this RecordingArchiveRestoreTopicMediaResult.


        :param media_uri: The media_uri of this RecordingArchiveRestoreTopicMediaResult.
        :type: str
        """
        
        self._media_uri = media_uri

    @property
    def waveform_data(self):
        """
        Gets the waveform_data of this RecordingArchiveRestoreTopicMediaResult.


        :return: The waveform_data of this RecordingArchiveRestoreTopicMediaResult.
        :rtype: list[float]
        """
        return self._waveform_data

    @waveform_data.setter
    def waveform_data(self, waveform_data):
        """
        Sets the waveform_data of this RecordingArchiveRestoreTopicMediaResult.


        :param waveform_data: The waveform_data of this RecordingArchiveRestoreTopicMediaResult.
        :type: list[float]
        """
        
        self._waveform_data = waveform_data

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

