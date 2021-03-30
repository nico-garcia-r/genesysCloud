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

class BuForecastGenerationPlanningGroupResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuForecastGenerationPlanningGroupResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'planning_group_id': 'str',
            'metric_results': 'list[BuForecastTimeSeriesResult]'
        }

        self.attribute_map = {
            'planning_group_id': 'planningGroupId',
            'metric_results': 'metricResults'
        }

        self._planning_group_id = None
        self._metric_results = None

    @property
    def planning_group_id(self):
        """
        Gets the planning_group_id of this BuForecastGenerationPlanningGroupResult.
        The ID of the planning group

        :return: The planning_group_id of this BuForecastGenerationPlanningGroupResult.
        :rtype: str
        """
        return self._planning_group_id

    @planning_group_id.setter
    def planning_group_id(self, planning_group_id):
        """
        Sets the planning_group_id of this BuForecastGenerationPlanningGroupResult.
        The ID of the planning group

        :param planning_group_id: The planning_group_id of this BuForecastGenerationPlanningGroupResult.
        :type: str
        """
        
        self._planning_group_id = planning_group_id

    @property
    def metric_results(self):
        """
        Gets the metric_results of this BuForecastGenerationPlanningGroupResult.
        The generation results for the associated planning group

        :return: The metric_results of this BuForecastGenerationPlanningGroupResult.
        :rtype: list[BuForecastTimeSeriesResult]
        """
        return self._metric_results

    @metric_results.setter
    def metric_results(self, metric_results):
        """
        Sets the metric_results of this BuForecastGenerationPlanningGroupResult.
        The generation results for the associated planning group

        :param metric_results: The metric_results of this BuForecastGenerationPlanningGroupResult.
        :type: list[BuForecastTimeSeriesResult]
        """
        
        self._metric_results = metric_results

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

