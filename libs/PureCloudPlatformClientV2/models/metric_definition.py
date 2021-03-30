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

class MetricDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MetricDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'unit_type': 'str',
            'short_name': 'str',
            'dividend_metrics': 'list[str]',
            'divisor_metrics': 'list[str]',
            'default_objective': 'DefaultObjective',
            'lock_template_id': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'unit_type': 'unitType',
            'short_name': 'shortName',
            'dividend_metrics': 'dividendMetrics',
            'divisor_metrics': 'divisorMetrics',
            'default_objective': 'defaultObjective',
            'lock_template_id': 'lockTemplateId',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._unit_type = None
        self._short_name = None
        self._dividend_metrics = None
        self._divisor_metrics = None
        self._default_objective = None
        self._lock_template_id = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this MetricDefinition.
        The globally unique identifier for the object.

        :return: The id of this MetricDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MetricDefinition.
        The globally unique identifier for the object.

        :param id: The id of this MetricDefinition.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this MetricDefinition.


        :return: The name of this MetricDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MetricDefinition.


        :param name: The name of this MetricDefinition.
        :type: str
        """
        
        self._name = name

    @property
    def unit_type(self):
        """
        Gets the unit_type of this MetricDefinition.
        The type of associated metric unit

        :return: The unit_type of this MetricDefinition.
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """
        Sets the unit_type of this MetricDefinition.
        The type of associated metric unit

        :param unit_type: The unit_type of this MetricDefinition.
        :type: str
        """
        allowed_values = ["None", "Percent", "Seconds", "Number", "AttendanceStatus", "Unit"]
        if unit_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for unit_type -> " + unit_type)
            self._unit_type = "outdated_sdk_version"
        else:
            self._unit_type = unit_type

    @property
    def short_name(self):
        """
        Gets the short_name of this MetricDefinition.
        An alternate name for this metric definition, often abbreviation

        :return: The short_name of this MetricDefinition.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this MetricDefinition.
        An alternate name for this metric definition, often abbreviation

        :param short_name: The short_name of this MetricDefinition.
        :type: str
        """
        
        self._short_name = short_name

    @property
    def dividend_metrics(self):
        """
        Gets the dividend_metrics of this MetricDefinition.
        Metric names used as dividend

        :return: The dividend_metrics of this MetricDefinition.
        :rtype: list[str]
        """
        return self._dividend_metrics

    @dividend_metrics.setter
    def dividend_metrics(self, dividend_metrics):
        """
        Sets the dividend_metrics of this MetricDefinition.
        Metric names used as dividend

        :param dividend_metrics: The dividend_metrics of this MetricDefinition.
        :type: list[str]
        """
        
        self._dividend_metrics = dividend_metrics

    @property
    def divisor_metrics(self):
        """
        Gets the divisor_metrics of this MetricDefinition.
        Metric names used as divisor

        :return: The divisor_metrics of this MetricDefinition.
        :rtype: list[str]
        """
        return self._divisor_metrics

    @divisor_metrics.setter
    def divisor_metrics(self, divisor_metrics):
        """
        Sets the divisor_metrics of this MetricDefinition.
        Metric names used as divisor

        :param divisor_metrics: The divisor_metrics of this MetricDefinition.
        :type: list[str]
        """
        
        self._divisor_metrics = divisor_metrics

    @property
    def default_objective(self):
        """
        Gets the default_objective of this MetricDefinition.
        A predefined default objective for this metric

        :return: The default_objective of this MetricDefinition.
        :rtype: DefaultObjective
        """
        return self._default_objective

    @default_objective.setter
    def default_objective(self, default_objective):
        """
        Sets the default_objective of this MetricDefinition.
        A predefined default objective for this metric

        :param default_objective: The default_objective of this MetricDefinition.
        :type: DefaultObjective
        """
        
        self._default_objective = default_objective

    @property
    def lock_template_id(self):
        """
        Gets the lock_template_id of this MetricDefinition.
        An optional field to specify if this metric definition is locked to certain template. e.g. punctuality

        :return: The lock_template_id of this MetricDefinition.
        :rtype: str
        """
        return self._lock_template_id

    @lock_template_id.setter
    def lock_template_id(self, lock_template_id):
        """
        Sets the lock_template_id of this MetricDefinition.
        An optional field to specify if this metric definition is locked to certain template. e.g. punctuality

        :param lock_template_id: The lock_template_id of this MetricDefinition.
        :type: str
        """
        
        self._lock_template_id = lock_template_id

    @property
    def self_uri(self):
        """
        Gets the self_uri of this MetricDefinition.
        The URI for this object

        :return: The self_uri of this MetricDefinition.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this MetricDefinition.
        The URI for this object

        :param self_uri: The self_uri of this MetricDefinition.
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

