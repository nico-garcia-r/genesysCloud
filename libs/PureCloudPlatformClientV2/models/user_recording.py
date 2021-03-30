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

class UserRecording(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserRecording - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'content_uri': 'str',
            'workspace': 'DomainEntityRef',
            'created_by': 'DomainEntityRef',
            'conversation': 'Conversation',
            'content_length': 'int',
            'duration_milliseconds': 'int',
            'thumbnails': 'list[DocumentThumbnail]',
            'read': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'content_uri': 'contentUri',
            'workspace': 'workspace',
            'created_by': 'createdBy',
            'conversation': 'conversation',
            'content_length': 'contentLength',
            'duration_milliseconds': 'durationMilliseconds',
            'thumbnails': 'thumbnails',
            'read': 'read',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._content_uri = None
        self._workspace = None
        self._created_by = None
        self._conversation = None
        self._content_length = None
        self._duration_milliseconds = None
        self._thumbnails = None
        self._read = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this UserRecording.
        The globally unique identifier for the object.

        :return: The id of this UserRecording.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserRecording.
        The globally unique identifier for the object.

        :param id: The id of this UserRecording.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this UserRecording.


        :return: The name of this UserRecording.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserRecording.


        :param name: The name of this UserRecording.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this UserRecording.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this UserRecording.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this UserRecording.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this UserRecording.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this UserRecording.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this UserRecording.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this UserRecording.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this UserRecording.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def content_uri(self):
        """
        Gets the content_uri of this UserRecording.


        :return: The content_uri of this UserRecording.
        :rtype: str
        """
        return self._content_uri

    @content_uri.setter
    def content_uri(self, content_uri):
        """
        Sets the content_uri of this UserRecording.


        :param content_uri: The content_uri of this UserRecording.
        :type: str
        """
        
        self._content_uri = content_uri

    @property
    def workspace(self):
        """
        Gets the workspace of this UserRecording.


        :return: The workspace of this UserRecording.
        :rtype: DomainEntityRef
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """
        Sets the workspace of this UserRecording.


        :param workspace: The workspace of this UserRecording.
        :type: DomainEntityRef
        """
        
        self._workspace = workspace

    @property
    def created_by(self):
        """
        Gets the created_by of this UserRecording.


        :return: The created_by of this UserRecording.
        :rtype: DomainEntityRef
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this UserRecording.


        :param created_by: The created_by of this UserRecording.
        :type: DomainEntityRef
        """
        
        self._created_by = created_by

    @property
    def conversation(self):
        """
        Gets the conversation of this UserRecording.


        :return: The conversation of this UserRecording.
        :rtype: Conversation
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """
        Sets the conversation of this UserRecording.


        :param conversation: The conversation of this UserRecording.
        :type: Conversation
        """
        
        self._conversation = conversation

    @property
    def content_length(self):
        """
        Gets the content_length of this UserRecording.


        :return: The content_length of this UserRecording.
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """
        Sets the content_length of this UserRecording.


        :param content_length: The content_length of this UserRecording.
        :type: int
        """
        
        self._content_length = content_length

    @property
    def duration_milliseconds(self):
        """
        Gets the duration_milliseconds of this UserRecording.


        :return: The duration_milliseconds of this UserRecording.
        :rtype: int
        """
        return self._duration_milliseconds

    @duration_milliseconds.setter
    def duration_milliseconds(self, duration_milliseconds):
        """
        Sets the duration_milliseconds of this UserRecording.


        :param duration_milliseconds: The duration_milliseconds of this UserRecording.
        :type: int
        """
        
        self._duration_milliseconds = duration_milliseconds

    @property
    def thumbnails(self):
        """
        Gets the thumbnails of this UserRecording.


        :return: The thumbnails of this UserRecording.
        :rtype: list[DocumentThumbnail]
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """
        Sets the thumbnails of this UserRecording.


        :param thumbnails: The thumbnails of this UserRecording.
        :type: list[DocumentThumbnail]
        """
        
        self._thumbnails = thumbnails

    @property
    def read(self):
        """
        Gets the read of this UserRecording.


        :return: The read of this UserRecording.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """
        Sets the read of this UserRecording.


        :param read: The read of this UserRecording.
        :type: bool
        """
        
        self._read = read

    @property
    def self_uri(self):
        """
        Gets the self_uri of this UserRecording.
        The URI for this object

        :return: The self_uri of this UserRecording.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this UserRecording.
        The URI for this object

        :param self_uri: The self_uri of this UserRecording.
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

