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

class BuRescheduleResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuRescheduleResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'generation_results': 'ScheduleGenerationResult',
            'generation_results_download_url': 'str',
            'headcount_forecast': 'BuHeadcountForecast',
            'headcount_forecast_download_url': 'str',
            'agent_schedules': 'list[BuRescheduleAgentScheduleResult]'
        }

        self.attribute_map = {
            'generation_results': 'generationResults',
            'generation_results_download_url': 'generationResultsDownloadUrl',
            'headcount_forecast': 'headcountForecast',
            'headcount_forecast_download_url': 'headcountForecastDownloadUrl',
            'agent_schedules': 'agentSchedules'
        }

        self._generation_results = None
        self._generation_results_download_url = None
        self._headcount_forecast = None
        self._headcount_forecast_download_url = None
        self._agent_schedules = None

    @property
    def generation_results(self):
        """
        Gets the generation_results of this BuRescheduleResult.
        The generation results.  Note the result will always be delivered via the downloadUrl; however the schema is included for documentation

        :return: The generation_results of this BuRescheduleResult.
        :rtype: ScheduleGenerationResult
        """
        return self._generation_results

    @generation_results.setter
    def generation_results(self, generation_results):
        """
        Sets the generation_results of this BuRescheduleResult.
        The generation results.  Note the result will always be delivered via the downloadUrl; however the schema is included for documentation

        :param generation_results: The generation_results of this BuRescheduleResult.
        :type: ScheduleGenerationResult
        """
        
        self._generation_results = generation_results

    @property
    def generation_results_download_url(self):
        """
        Gets the generation_results_download_url of this BuRescheduleResult.
        The download URL from which to fetch the generation results for the rescheduling run

        :return: The generation_results_download_url of this BuRescheduleResult.
        :rtype: str
        """
        return self._generation_results_download_url

    @generation_results_download_url.setter
    def generation_results_download_url(self, generation_results_download_url):
        """
        Sets the generation_results_download_url of this BuRescheduleResult.
        The download URL from which to fetch the generation results for the rescheduling run

        :param generation_results_download_url: The generation_results_download_url of this BuRescheduleResult.
        :type: str
        """
        
        self._generation_results_download_url = generation_results_download_url

    @property
    def headcount_forecast(self):
        """
        Gets the headcount_forecast of this BuRescheduleResult.
        The headcount forecast.  Note the result will always be delivered via the downloadUrl; however the schema is included for documentation

        :return: The headcount_forecast of this BuRescheduleResult.
        :rtype: BuHeadcountForecast
        """
        return self._headcount_forecast

    @headcount_forecast.setter
    def headcount_forecast(self, headcount_forecast):
        """
        Sets the headcount_forecast of this BuRescheduleResult.
        The headcount forecast.  Note the result will always be delivered via the downloadUrl; however the schema is included for documentation

        :param headcount_forecast: The headcount_forecast of this BuRescheduleResult.
        :type: BuHeadcountForecast
        """
        
        self._headcount_forecast = headcount_forecast

    @property
    def headcount_forecast_download_url(self):
        """
        Gets the headcount_forecast_download_url of this BuRescheduleResult.
        The download URL from which to fetch the headcount forecast for the rescheduling run

        :return: The headcount_forecast_download_url of this BuRescheduleResult.
        :rtype: str
        """
        return self._headcount_forecast_download_url

    @headcount_forecast_download_url.setter
    def headcount_forecast_download_url(self, headcount_forecast_download_url):
        """
        Sets the headcount_forecast_download_url of this BuRescheduleResult.
        The download URL from which to fetch the headcount forecast for the rescheduling run

        :param headcount_forecast_download_url: The headcount_forecast_download_url of this BuRescheduleResult.
        :type: str
        """
        
        self._headcount_forecast_download_url = headcount_forecast_download_url

    @property
    def agent_schedules(self):
        """
        Gets the agent_schedules of this BuRescheduleResult.
        List of download links for agent schedules produced by the rescheduling run

        :return: The agent_schedules of this BuRescheduleResult.
        :rtype: list[BuRescheduleAgentScheduleResult]
        """
        return self._agent_schedules

    @agent_schedules.setter
    def agent_schedules(self, agent_schedules):
        """
        Sets the agent_schedules of this BuRescheduleResult.
        List of download links for agent schedules produced by the rescheduling run

        :param agent_schedules: The agent_schedules of this BuRescheduleResult.
        :type: list[BuRescheduleAgentScheduleResult]
        """
        
        self._agent_schedules = agent_schedules

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

