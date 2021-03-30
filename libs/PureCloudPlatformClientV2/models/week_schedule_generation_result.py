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

class WeekScheduleGenerationResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WeekScheduleGenerationResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'failed': 'bool',
            'run_id': 'str',
            'agent_warnings': 'list[ScheduleGenerationWarning]',
            'agent_warning_count': 'int'
        }

        self.attribute_map = {
            'failed': 'failed',
            'run_id': 'runId',
            'agent_warnings': 'agentWarnings',
            'agent_warning_count': 'agentWarningCount'
        }

        self._failed = None
        self._run_id = None
        self._agent_warnings = None
        self._agent_warning_count = None

    @property
    def failed(self):
        """
        Gets the failed of this WeekScheduleGenerationResult.
        Whether the schedule generation failed

        :return: The failed of this WeekScheduleGenerationResult.
        :rtype: bool
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """
        Sets the failed of this WeekScheduleGenerationResult.
        Whether the schedule generation failed

        :param failed: The failed of this WeekScheduleGenerationResult.
        :type: bool
        """
        
        self._failed = failed

    @property
    def run_id(self):
        """
        Gets the run_id of this WeekScheduleGenerationResult.
        ID of the schedule run

        :return: The run_id of this WeekScheduleGenerationResult.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """
        Sets the run_id of this WeekScheduleGenerationResult.
        ID of the schedule run

        :param run_id: The run_id of this WeekScheduleGenerationResult.
        :type: str
        """
        
        self._run_id = run_id

    @property
    def agent_warnings(self):
        """
        Gets the agent_warnings of this WeekScheduleGenerationResult.
        Warning messages from the schedule run. This will be available only when requesting information for a single week schedule

        :return: The agent_warnings of this WeekScheduleGenerationResult.
        :rtype: list[ScheduleGenerationWarning]
        """
        return self._agent_warnings

    @agent_warnings.setter
    def agent_warnings(self, agent_warnings):
        """
        Sets the agent_warnings of this WeekScheduleGenerationResult.
        Warning messages from the schedule run. This will be available only when requesting information for a single week schedule

        :param agent_warnings: The agent_warnings of this WeekScheduleGenerationResult.
        :type: list[ScheduleGenerationWarning]
        """
        
        self._agent_warnings = agent_warnings

    @property
    def agent_warning_count(self):
        """
        Gets the agent_warning_count of this WeekScheduleGenerationResult.
        Count of warning messages from the schedule run. This will be available only when requesting multiple week schedules

        :return: The agent_warning_count of this WeekScheduleGenerationResult.
        :rtype: int
        """
        return self._agent_warning_count

    @agent_warning_count.setter
    def agent_warning_count(self, agent_warning_count):
        """
        Sets the agent_warning_count of this WeekScheduleGenerationResult.
        Count of warning messages from the schedule run. This will be available only when requesting multiple week schedules

        :param agent_warning_count: The agent_warning_count of this WeekScheduleGenerationResult.
        :type: int
        """
        
        self._agent_warning_count = agent_warning_count

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

