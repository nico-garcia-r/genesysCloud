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

class PresenceEventUserPresence(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PresenceEventUserPresence - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'source': 'str',
            'presence_definition': 'PresenceEventOrganizationPresence',
            'primary': 'bool',
            'message': 'str',
            'modified_date': 'datetime'
        }

        self.attribute_map = {
            'source': 'source',
            'presence_definition': 'presenceDefinition',
            'primary': 'primary',
            'message': 'message',
            'modified_date': 'modifiedDate'
        }

        self._source = None
        self._presence_definition = None
        self._primary = None
        self._message = None
        self._modified_date = None

    @property
    def source(self):
        """
        Gets the source of this PresenceEventUserPresence.


        :return: The source of this PresenceEventUserPresence.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this PresenceEventUserPresence.


        :param source: The source of this PresenceEventUserPresence.
        :type: str
        """
        
        self._source = source

    @property
    def presence_definition(self):
        """
        Gets the presence_definition of this PresenceEventUserPresence.


        :return: The presence_definition of this PresenceEventUserPresence.
        :rtype: PresenceEventOrganizationPresence
        """
        return self._presence_definition

    @presence_definition.setter
    def presence_definition(self, presence_definition):
        """
        Sets the presence_definition of this PresenceEventUserPresence.


        :param presence_definition: The presence_definition of this PresenceEventUserPresence.
        :type: PresenceEventOrganizationPresence
        """
        
        self._presence_definition = presence_definition

    @property
    def primary(self):
        """
        Gets the primary of this PresenceEventUserPresence.


        :return: The primary of this PresenceEventUserPresence.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """
        Sets the primary of this PresenceEventUserPresence.


        :param primary: The primary of this PresenceEventUserPresence.
        :type: bool
        """
        
        self._primary = primary

    @property
    def message(self):
        """
        Gets the message of this PresenceEventUserPresence.


        :return: The message of this PresenceEventUserPresence.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this PresenceEventUserPresence.


        :param message: The message of this PresenceEventUserPresence.
        :type: str
        """
        
        self._message = message

    @property
    def modified_date(self):
        """
        Gets the modified_date of this PresenceEventUserPresence.


        :return: The modified_date of this PresenceEventUserPresence.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this PresenceEventUserPresence.


        :param modified_date: The modified_date of this PresenceEventUserPresence.
        :type: datetime
        """
        
        self._modified_date = modified_date

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

