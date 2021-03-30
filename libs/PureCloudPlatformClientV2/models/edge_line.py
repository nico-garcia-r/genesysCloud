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

class EdgeLine(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EdgeLine - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'version': 'int',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'modified_by': 'str',
            'created_by': 'str',
            'state': 'str',
            'modified_by_app': 'str',
            'created_by_app': 'str',
            'schema': 'DomainEntityRef',
            'properties': 'dict(str, object)',
            'edge': 'Edge',
            'edge_group': 'EdgeGroup',
            'line_type': 'str',
            'endpoint': 'Endpoint',
            'ip_address': 'str',
            'logical_interface_id': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'version': 'version',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'modified_by': 'modifiedBy',
            'created_by': 'createdBy',
            'state': 'state',
            'modified_by_app': 'modifiedByApp',
            'created_by_app': 'createdByApp',
            'schema': 'schema',
            'properties': 'properties',
            'edge': 'edge',
            'edge_group': 'edgeGroup',
            'line_type': 'lineType',
            'endpoint': 'endpoint',
            'ip_address': 'ipAddress',
            'logical_interface_id': 'logicalInterfaceId',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._version = None
        self._date_created = None
        self._date_modified = None
        self._modified_by = None
        self._created_by = None
        self._state = None
        self._modified_by_app = None
        self._created_by_app = None
        self._schema = None
        self._properties = None
        self._edge = None
        self._edge_group = None
        self._line_type = None
        self._endpoint = None
        self._ip_address = None
        self._logical_interface_id = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this EdgeLine.
        The globally unique identifier for the object.

        :return: The id of this EdgeLine.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EdgeLine.
        The globally unique identifier for the object.

        :param id: The id of this EdgeLine.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this EdgeLine.
        The name of the entity.

        :return: The name of this EdgeLine.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EdgeLine.
        The name of the entity.

        :param name: The name of this EdgeLine.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this EdgeLine.
        The resource's description.

        :return: The description of this EdgeLine.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EdgeLine.
        The resource's description.

        :param description: The description of this EdgeLine.
        :type: str
        """
        
        self._description = description

    @property
    def version(self):
        """
        Gets the version of this EdgeLine.
        The current version of the resource.

        :return: The version of this EdgeLine.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this EdgeLine.
        The current version of the resource.

        :param version: The version of this EdgeLine.
        :type: int
        """
        
        self._version = version

    @property
    def date_created(self):
        """
        Gets the date_created of this EdgeLine.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this EdgeLine.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this EdgeLine.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this EdgeLine.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this EdgeLine.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this EdgeLine.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this EdgeLine.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this EdgeLine.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def modified_by(self):
        """
        Gets the modified_by of this EdgeLine.
        The ID of the user that last modified the resource.

        :return: The modified_by of this EdgeLine.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this EdgeLine.
        The ID of the user that last modified the resource.

        :param modified_by: The modified_by of this EdgeLine.
        :type: str
        """
        
        self._modified_by = modified_by

    @property
    def created_by(self):
        """
        Gets the created_by of this EdgeLine.
        The ID of the user that created the resource.

        :return: The created_by of this EdgeLine.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this EdgeLine.
        The ID of the user that created the resource.

        :param created_by: The created_by of this EdgeLine.
        :type: str
        """
        
        self._created_by = created_by

    @property
    def state(self):
        """
        Gets the state of this EdgeLine.
        Indicates if the resource is active, inactive, or deleted.

        :return: The state of this EdgeLine.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this EdgeLine.
        Indicates if the resource is active, inactive, or deleted.

        :param state: The state of this EdgeLine.
        :type: str
        """
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def modified_by_app(self):
        """
        Gets the modified_by_app of this EdgeLine.
        The application that last modified the resource.

        :return: The modified_by_app of this EdgeLine.
        :rtype: str
        """
        return self._modified_by_app

    @modified_by_app.setter
    def modified_by_app(self, modified_by_app):
        """
        Sets the modified_by_app of this EdgeLine.
        The application that last modified the resource.

        :param modified_by_app: The modified_by_app of this EdgeLine.
        :type: str
        """
        
        self._modified_by_app = modified_by_app

    @property
    def created_by_app(self):
        """
        Gets the created_by_app of this EdgeLine.
        The application that created the resource.

        :return: The created_by_app of this EdgeLine.
        :rtype: str
        """
        return self._created_by_app

    @created_by_app.setter
    def created_by_app(self, created_by_app):
        """
        Sets the created_by_app of this EdgeLine.
        The application that created the resource.

        :param created_by_app: The created_by_app of this EdgeLine.
        :type: str
        """
        
        self._created_by_app = created_by_app

    @property
    def schema(self):
        """
        Gets the schema of this EdgeLine.


        :return: The schema of this EdgeLine.
        :rtype: DomainEntityRef
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this EdgeLine.


        :param schema: The schema of this EdgeLine.
        :type: DomainEntityRef
        """
        
        self._schema = schema

    @property
    def properties(self):
        """
        Gets the properties of this EdgeLine.


        :return: The properties of this EdgeLine.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this EdgeLine.


        :param properties: The properties of this EdgeLine.
        :type: dict(str, object)
        """
        
        self._properties = properties

    @property
    def edge(self):
        """
        Gets the edge of this EdgeLine.


        :return: The edge of this EdgeLine.
        :rtype: Edge
        """
        return self._edge

    @edge.setter
    def edge(self, edge):
        """
        Sets the edge of this EdgeLine.


        :param edge: The edge of this EdgeLine.
        :type: Edge
        """
        
        self._edge = edge

    @property
    def edge_group(self):
        """
        Gets the edge_group of this EdgeLine.


        :return: The edge_group of this EdgeLine.
        :rtype: EdgeGroup
        """
        return self._edge_group

    @edge_group.setter
    def edge_group(self, edge_group):
        """
        Sets the edge_group of this EdgeLine.


        :param edge_group: The edge_group of this EdgeLine.
        :type: EdgeGroup
        """
        
        self._edge_group = edge_group

    @property
    def line_type(self):
        """
        Gets the line_type of this EdgeLine.


        :return: The line_type of this EdgeLine.
        :rtype: str
        """
        return self._line_type

    @line_type.setter
    def line_type(self, line_type):
        """
        Sets the line_type of this EdgeLine.


        :param line_type: The line_type of this EdgeLine.
        :type: str
        """
        allowed_values = ["TIE", "NETWORK", "TRUNK", "STATION"]
        if line_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for line_type -> " + line_type)
            self._line_type = "outdated_sdk_version"
        else:
            self._line_type = line_type

    @property
    def endpoint(self):
        """
        Gets the endpoint of this EdgeLine.


        :return: The endpoint of this EdgeLine.
        :rtype: Endpoint
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this EdgeLine.


        :param endpoint: The endpoint of this EdgeLine.
        :type: Endpoint
        """
        
        self._endpoint = endpoint

    @property
    def ip_address(self):
        """
        Gets the ip_address of this EdgeLine.


        :return: The ip_address of this EdgeLine.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this EdgeLine.


        :param ip_address: The ip_address of this EdgeLine.
        :type: str
        """
        
        self._ip_address = ip_address

    @property
    def logical_interface_id(self):
        """
        Gets the logical_interface_id of this EdgeLine.


        :return: The logical_interface_id of this EdgeLine.
        :rtype: str
        """
        return self._logical_interface_id

    @logical_interface_id.setter
    def logical_interface_id(self, logical_interface_id):
        """
        Sets the logical_interface_id of this EdgeLine.


        :param logical_interface_id: The logical_interface_id of this EdgeLine.
        :type: str
        """
        
        self._logical_interface_id = logical_interface_id

    @property
    def self_uri(self):
        """
        Gets the self_uri of this EdgeLine.
        The URI for this object

        :return: The self_uri of this EdgeLine.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this EdgeLine.
        The URI for this object

        :param self_uri: The self_uri of this EdgeLine.
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

