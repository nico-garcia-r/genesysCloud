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

class NluFeedbackResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NluFeedbackResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'text': 'str',
            'intents': 'list[IntentFeedback]',
            'version': 'NluDomainVersion',
            'date_created': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'text': 'text',
            'intents': 'intents',
            'version': 'version',
            'date_created': 'dateCreated',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._text = None
        self._intents = None
        self._version = None
        self._date_created = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this NluFeedbackResponse.
        The globally unique identifier for the object.

        :return: The id of this NluFeedbackResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NluFeedbackResponse.
        The globally unique identifier for the object.

        :param id: The id of this NluFeedbackResponse.
        :type: str
        """
        
        self._id = id

    @property
    def text(self):
        """
        Gets the text of this NluFeedbackResponse.
        The feedback text.

        :return: The text of this NluFeedbackResponse.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this NluFeedbackResponse.
        The feedback text.

        :param text: The text of this NluFeedbackResponse.
        :type: str
        """
        
        self._text = text

    @property
    def intents(self):
        """
        Gets the intents of this NluFeedbackResponse.
        Detected intent of the utterance

        :return: The intents of this NluFeedbackResponse.
        :rtype: list[IntentFeedback]
        """
        return self._intents

    @intents.setter
    def intents(self, intents):
        """
        Sets the intents of this NluFeedbackResponse.
        Detected intent of the utterance

        :param intents: The intents of this NluFeedbackResponse.
        :type: list[IntentFeedback]
        """
        
        self._intents = intents

    @property
    def version(self):
        """
        Gets the version of this NluFeedbackResponse.
        The domain version of the feedback.

        :return: The version of this NluFeedbackResponse.
        :rtype: NluDomainVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this NluFeedbackResponse.
        The domain version of the feedback.

        :param version: The version of this NluFeedbackResponse.
        :type: NluDomainVersion
        """
        
        self._version = version

    @property
    def date_created(self):
        """
        Gets the date_created of this NluFeedbackResponse.
        The date when the feedback was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this NluFeedbackResponse.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this NluFeedbackResponse.
        The date when the feedback was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this NluFeedbackResponse.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def self_uri(self):
        """
        Gets the self_uri of this NluFeedbackResponse.
        The URI for this object

        :return: The self_uri of this NluFeedbackResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this NluFeedbackResponse.
        The URI for this object

        :param self_uri: The self_uri of this NluFeedbackResponse.
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

