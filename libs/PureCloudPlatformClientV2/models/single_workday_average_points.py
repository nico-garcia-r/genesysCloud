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

class SingleWorkdayAveragePoints(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SingleWorkdayAveragePoints - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'date_workday': 'date',
            'division': 'Division',
            'average_points': 'float'
        }

        self.attribute_map = {
            'date_workday': 'dateWorkday',
            'division': 'division',
            'average_points': 'averagePoints'
        }

        self._date_workday = None
        self._division = None
        self._average_points = None

    @property
    def date_workday(self):
        """
        Gets the date_workday of this SingleWorkdayAveragePoints.
        Queried target workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The date_workday of this SingleWorkdayAveragePoints.
        :rtype: date
        """
        return self._date_workday

    @date_workday.setter
    def date_workday(self, date_workday):
        """
        Sets the date_workday of this SingleWorkdayAveragePoints.
        Queried target workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param date_workday: The date_workday of this SingleWorkdayAveragePoints.
        :type: date
        """
        
        self._date_workday = date_workday

    @property
    def division(self):
        """
        Gets the division of this SingleWorkdayAveragePoints.
        The targeted division for the average points

        :return: The division of this SingleWorkdayAveragePoints.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division):
        """
        Sets the division of this SingleWorkdayAveragePoints.
        The targeted division for the average points

        :param division: The division of this SingleWorkdayAveragePoints.
        :type: Division
        """
        
        self._division = division

    @property
    def average_points(self):
        """
        Gets the average_points of this SingleWorkdayAveragePoints.
        The average points per agent earned within the division

        :return: The average_points of this SingleWorkdayAveragePoints.
        :rtype: float
        """
        return self._average_points

    @average_points.setter
    def average_points(self, average_points):
        """
        Sets the average_points of this SingleWorkdayAveragePoints.
        The average points per agent earned within the division

        :param average_points: The average_points of this SingleWorkdayAveragePoints.
        :type: float
        """
        
        self._average_points = average_points

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

