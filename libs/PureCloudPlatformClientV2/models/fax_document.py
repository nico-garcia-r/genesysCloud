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

class FaxDocument(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FaxDocument - a model defined in Swagger

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
            'content_type': 'str',
            'content_length': 'int',
            'filename': 'str',
            'read': 'bool',
            'page_count': 'int',
            'caller_address': 'str',
            'receiver_address': 'str',
            'thumbnails': 'list[DocumentThumbnail]',
            'sharing_uri': 'str',
            'download_sharing_uri': 'str',
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
            'content_type': 'contentType',
            'content_length': 'contentLength',
            'filename': 'filename',
            'read': 'read',
            'page_count': 'pageCount',
            'caller_address': 'callerAddress',
            'receiver_address': 'receiverAddress',
            'thumbnails': 'thumbnails',
            'sharing_uri': 'sharingUri',
            'download_sharing_uri': 'downloadSharingUri',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._content_uri = None
        self._workspace = None
        self._created_by = None
        self._content_type = None
        self._content_length = None
        self._filename = None
        self._read = None
        self._page_count = None
        self._caller_address = None
        self._receiver_address = None
        self._thumbnails = None
        self._sharing_uri = None
        self._download_sharing_uri = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this FaxDocument.
        The globally unique identifier for the object.

        :return: The id of this FaxDocument.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FaxDocument.
        The globally unique identifier for the object.

        :param id: The id of this FaxDocument.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FaxDocument.


        :return: The name of this FaxDocument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FaxDocument.


        :param name: The name of this FaxDocument.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this FaxDocument.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this FaxDocument.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this FaxDocument.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this FaxDocument.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this FaxDocument.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this FaxDocument.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this FaxDocument.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this FaxDocument.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def content_uri(self):
        """
        Gets the content_uri of this FaxDocument.


        :return: The content_uri of this FaxDocument.
        :rtype: str
        """
        return self._content_uri

    @content_uri.setter
    def content_uri(self, content_uri):
        """
        Sets the content_uri of this FaxDocument.


        :param content_uri: The content_uri of this FaxDocument.
        :type: str
        """
        
        self._content_uri = content_uri

    @property
    def workspace(self):
        """
        Gets the workspace of this FaxDocument.


        :return: The workspace of this FaxDocument.
        :rtype: DomainEntityRef
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """
        Sets the workspace of this FaxDocument.


        :param workspace: The workspace of this FaxDocument.
        :type: DomainEntityRef
        """
        
        self._workspace = workspace

    @property
    def created_by(self):
        """
        Gets the created_by of this FaxDocument.


        :return: The created_by of this FaxDocument.
        :rtype: DomainEntityRef
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this FaxDocument.


        :param created_by: The created_by of this FaxDocument.
        :type: DomainEntityRef
        """
        
        self._created_by = created_by

    @property
    def content_type(self):
        """
        Gets the content_type of this FaxDocument.


        :return: The content_type of this FaxDocument.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this FaxDocument.


        :param content_type: The content_type of this FaxDocument.
        :type: str
        """
        
        self._content_type = content_type

    @property
    def content_length(self):
        """
        Gets the content_length of this FaxDocument.


        :return: The content_length of this FaxDocument.
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """
        Sets the content_length of this FaxDocument.


        :param content_length: The content_length of this FaxDocument.
        :type: int
        """
        
        self._content_length = content_length

    @property
    def filename(self):
        """
        Gets the filename of this FaxDocument.


        :return: The filename of this FaxDocument.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this FaxDocument.


        :param filename: The filename of this FaxDocument.
        :type: str
        """
        
        self._filename = filename

    @property
    def read(self):
        """
        Gets the read of this FaxDocument.


        :return: The read of this FaxDocument.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """
        Sets the read of this FaxDocument.


        :param read: The read of this FaxDocument.
        :type: bool
        """
        
        self._read = read

    @property
    def page_count(self):
        """
        Gets the page_count of this FaxDocument.


        :return: The page_count of this FaxDocument.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this FaxDocument.


        :param page_count: The page_count of this FaxDocument.
        :type: int
        """
        
        self._page_count = page_count

    @property
    def caller_address(self):
        """
        Gets the caller_address of this FaxDocument.


        :return: The caller_address of this FaxDocument.
        :rtype: str
        """
        return self._caller_address

    @caller_address.setter
    def caller_address(self, caller_address):
        """
        Sets the caller_address of this FaxDocument.


        :param caller_address: The caller_address of this FaxDocument.
        :type: str
        """
        
        self._caller_address = caller_address

    @property
    def receiver_address(self):
        """
        Gets the receiver_address of this FaxDocument.


        :return: The receiver_address of this FaxDocument.
        :rtype: str
        """
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, receiver_address):
        """
        Sets the receiver_address of this FaxDocument.


        :param receiver_address: The receiver_address of this FaxDocument.
        :type: str
        """
        
        self._receiver_address = receiver_address

    @property
    def thumbnails(self):
        """
        Gets the thumbnails of this FaxDocument.


        :return: The thumbnails of this FaxDocument.
        :rtype: list[DocumentThumbnail]
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """
        Sets the thumbnails of this FaxDocument.


        :param thumbnails: The thumbnails of this FaxDocument.
        :type: list[DocumentThumbnail]
        """
        
        self._thumbnails = thumbnails

    @property
    def sharing_uri(self):
        """
        Gets the sharing_uri of this FaxDocument.


        :return: The sharing_uri of this FaxDocument.
        :rtype: str
        """
        return self._sharing_uri

    @sharing_uri.setter
    def sharing_uri(self, sharing_uri):
        """
        Sets the sharing_uri of this FaxDocument.


        :param sharing_uri: The sharing_uri of this FaxDocument.
        :type: str
        """
        
        self._sharing_uri = sharing_uri

    @property
    def download_sharing_uri(self):
        """
        Gets the download_sharing_uri of this FaxDocument.


        :return: The download_sharing_uri of this FaxDocument.
        :rtype: str
        """
        return self._download_sharing_uri

    @download_sharing_uri.setter
    def download_sharing_uri(self, download_sharing_uri):
        """
        Sets the download_sharing_uri of this FaxDocument.


        :param download_sharing_uri: The download_sharing_uri of this FaxDocument.
        :type: str
        """
        
        self._download_sharing_uri = download_sharing_uri

    @property
    def self_uri(self):
        """
        Gets the self_uri of this FaxDocument.
        The URI for this object

        :return: The self_uri of this FaxDocument.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this FaxDocument.
        The URI for this object

        :param self_uri: The self_uri of this FaxDocument.
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

