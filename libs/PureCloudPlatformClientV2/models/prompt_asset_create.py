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

class PromptAssetCreate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PromptAssetCreate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'prompt_id': 'str',
            'language': 'str',
            'media_uri': 'str',
            'tts_string': 'str',
            'text': 'str',
            'upload_status': 'str',
            'upload_uri': 'str',
            'language_default': 'bool',
            'tags': 'dict(str, list[str])',
            'duration_seconds': 'float',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'prompt_id': 'promptId',
            'language': 'language',
            'media_uri': 'mediaUri',
            'tts_string': 'ttsString',
            'text': 'text',
            'upload_status': 'uploadStatus',
            'upload_uri': 'uploadUri',
            'language_default': 'languageDefault',
            'tags': 'tags',
            'duration_seconds': 'durationSeconds',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._prompt_id = None
        self._language = None
        self._media_uri = None
        self._tts_string = None
        self._text = None
        self._upload_status = None
        self._upload_uri = None
        self._language_default = None
        self._tags = None
        self._duration_seconds = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this PromptAssetCreate.
        The globally unique identifier for the object.

        :return: The id of this PromptAssetCreate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PromptAssetCreate.
        The globally unique identifier for the object.

        :param id: The id of this PromptAssetCreate.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PromptAssetCreate.


        :return: The name of this PromptAssetCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PromptAssetCreate.


        :param name: The name of this PromptAssetCreate.
        :type: str
        """
        
        self._name = name

    @property
    def prompt_id(self):
        """
        Gets the prompt_id of this PromptAssetCreate.
        Associated prompt ID

        :return: The prompt_id of this PromptAssetCreate.
        :rtype: str
        """
        return self._prompt_id

    @prompt_id.setter
    def prompt_id(self, prompt_id):
        """
        Sets the prompt_id of this PromptAssetCreate.
        Associated prompt ID

        :param prompt_id: The prompt_id of this PromptAssetCreate.
        :type: str
        """
        
        self._prompt_id = prompt_id

    @property
    def language(self):
        """
        Gets the language of this PromptAssetCreate.
        The prompt language.

        :return: The language of this PromptAssetCreate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this PromptAssetCreate.
        The prompt language.

        :param language: The language of this PromptAssetCreate.
        :type: str
        """
        
        self._language = language

    @property
    def media_uri(self):
        """
        Gets the media_uri of this PromptAssetCreate.
        URI of the resource audio

        :return: The media_uri of this PromptAssetCreate.
        :rtype: str
        """
        return self._media_uri

    @media_uri.setter
    def media_uri(self, media_uri):
        """
        Sets the media_uri of this PromptAssetCreate.
        URI of the resource audio

        :param media_uri: The media_uri of this PromptAssetCreate.
        :type: str
        """
        
        self._media_uri = media_uri

    @property
    def tts_string(self):
        """
        Gets the tts_string of this PromptAssetCreate.
        Text to speech of the resource

        :return: The tts_string of this PromptAssetCreate.
        :rtype: str
        """
        return self._tts_string

    @tts_string.setter
    def tts_string(self, tts_string):
        """
        Sets the tts_string of this PromptAssetCreate.
        Text to speech of the resource

        :param tts_string: The tts_string of this PromptAssetCreate.
        :type: str
        """
        
        self._tts_string = tts_string

    @property
    def text(self):
        """
        Gets the text of this PromptAssetCreate.
        Text of the resource

        :return: The text of this PromptAssetCreate.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this PromptAssetCreate.
        Text of the resource

        :param text: The text of this PromptAssetCreate.
        :type: str
        """
        
        self._text = text

    @property
    def upload_status(self):
        """
        Gets the upload_status of this PromptAssetCreate.
        Audio upload status

        :return: The upload_status of this PromptAssetCreate.
        :rtype: str
        """
        return self._upload_status

    @upload_status.setter
    def upload_status(self, upload_status):
        """
        Sets the upload_status of this PromptAssetCreate.
        Audio upload status

        :param upload_status: The upload_status of this PromptAssetCreate.
        :type: str
        """
        allowed_values = ["created", "uploaded", "transcoded", "transcodeFailed"]
        if upload_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for upload_status -> " + upload_status)
            self._upload_status = "outdated_sdk_version"
        else:
            self._upload_status = upload_status

    @property
    def upload_uri(self):
        """
        Gets the upload_uri of this PromptAssetCreate.
        Upload URI for the resource audio

        :return: The upload_uri of this PromptAssetCreate.
        :rtype: str
        """
        return self._upload_uri

    @upload_uri.setter
    def upload_uri(self, upload_uri):
        """
        Sets the upload_uri of this PromptAssetCreate.
        Upload URI for the resource audio

        :param upload_uri: The upload_uri of this PromptAssetCreate.
        :type: str
        """
        
        self._upload_uri = upload_uri

    @property
    def language_default(self):
        """
        Gets the language_default of this PromptAssetCreate.
        Whether or not this resource locale is the default for the language

        :return: The language_default of this PromptAssetCreate.
        :rtype: bool
        """
        return self._language_default

    @language_default.setter
    def language_default(self, language_default):
        """
        Sets the language_default of this PromptAssetCreate.
        Whether or not this resource locale is the default for the language

        :param language_default: The language_default of this PromptAssetCreate.
        :type: bool
        """
        
        self._language_default = language_default

    @property
    def tags(self):
        """
        Gets the tags of this PromptAssetCreate.


        :return: The tags of this PromptAssetCreate.
        :rtype: dict(str, list[str])
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this PromptAssetCreate.


        :param tags: The tags of this PromptAssetCreate.
        :type: dict(str, list[str])
        """
        
        self._tags = tags

    @property
    def duration_seconds(self):
        """
        Gets the duration_seconds of this PromptAssetCreate.


        :return: The duration_seconds of this PromptAssetCreate.
        :rtype: float
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        """
        Sets the duration_seconds of this PromptAssetCreate.


        :param duration_seconds: The duration_seconds of this PromptAssetCreate.
        :type: float
        """
        
        self._duration_seconds = duration_seconds

    @property
    def self_uri(self):
        """
        Gets the self_uri of this PromptAssetCreate.
        The URI for this object

        :return: The self_uri of this PromptAssetCreate.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this PromptAssetCreate.
        The URI for this object

        :param self_uri: The self_uri of this PromptAssetCreate.
        :type: str
        """
        
        self._self_uri = self_uri

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

