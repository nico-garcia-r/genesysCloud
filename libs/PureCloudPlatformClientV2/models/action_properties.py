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

class ActionProperties(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ActionProperties - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'webchat_prompt': 'str',
            'webchat_title_text': 'str',
            'webchat_accept_text': 'str',
            'webchat_decline_text': 'str',
            'webchat_survey': 'ActionSurvey'
        }

        self.attribute_map = {
            'webchat_prompt': 'webchatPrompt',
            'webchat_title_text': 'webchatTitleText',
            'webchat_accept_text': 'webchatAcceptText',
            'webchat_decline_text': 'webchatDeclineText',
            'webchat_survey': 'webchatSurvey'
        }

        self._webchat_prompt = None
        self._webchat_title_text = None
        self._webchat_accept_text = None
        self._webchat_decline_text = None
        self._webchat_survey = None

    @property
    def webchat_prompt(self):
        """
        Gets the webchat_prompt of this ActionProperties.
        Prompt message shown to user, used for webchat type action.

        :return: The webchat_prompt of this ActionProperties.
        :rtype: str
        """
        return self._webchat_prompt

    @webchat_prompt.setter
    def webchat_prompt(self, webchat_prompt):
        """
        Sets the webchat_prompt of this ActionProperties.
        Prompt message shown to user, used for webchat type action.

        :param webchat_prompt: The webchat_prompt of this ActionProperties.
        :type: str
        """
        
        self._webchat_prompt = webchat_prompt

    @property
    def webchat_title_text(self):
        """
        Gets the webchat_title_text of this ActionProperties.
        Title shown to the user, used for webchat type action.

        :return: The webchat_title_text of this ActionProperties.
        :rtype: str
        """
        return self._webchat_title_text

    @webchat_title_text.setter
    def webchat_title_text(self, webchat_title_text):
        """
        Sets the webchat_title_text of this ActionProperties.
        Title shown to the user, used for webchat type action.

        :param webchat_title_text: The webchat_title_text of this ActionProperties.
        :type: str
        """
        
        self._webchat_title_text = webchat_title_text

    @property
    def webchat_accept_text(self):
        """
        Gets the webchat_accept_text of this ActionProperties.
        Accept button text shown to user, used for webchat type action.

        :return: The webchat_accept_text of this ActionProperties.
        :rtype: str
        """
        return self._webchat_accept_text

    @webchat_accept_text.setter
    def webchat_accept_text(self, webchat_accept_text):
        """
        Sets the webchat_accept_text of this ActionProperties.
        Accept button text shown to user, used for webchat type action.

        :param webchat_accept_text: The webchat_accept_text of this ActionProperties.
        :type: str
        """
        
        self._webchat_accept_text = webchat_accept_text

    @property
    def webchat_decline_text(self):
        """
        Gets the webchat_decline_text of this ActionProperties.
        Decline button text shown to user, used for webchat type action.

        :return: The webchat_decline_text of this ActionProperties.
        :rtype: str
        """
        return self._webchat_decline_text

    @webchat_decline_text.setter
    def webchat_decline_text(self, webchat_decline_text):
        """
        Sets the webchat_decline_text of this ActionProperties.
        Decline button text shown to user, used for webchat type action.

        :param webchat_decline_text: The webchat_decline_text of this ActionProperties.
        :type: str
        """
        
        self._webchat_decline_text = webchat_decline_text

    @property
    def webchat_survey(self):
        """
        Gets the webchat_survey of this ActionProperties.
        Survey provided to the user, used for webchat type action.

        :return: The webchat_survey of this ActionProperties.
        :rtype: ActionSurvey
        """
        return self._webchat_survey

    @webchat_survey.setter
    def webchat_survey(self, webchat_survey):
        """
        Sets the webchat_survey of this ActionProperties.
        Survey provided to the user, used for webchat type action.

        :param webchat_survey: The webchat_survey of this ActionProperties.
        :type: ActionSurvey
        """
        
        self._webchat_survey = webchat_survey

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

