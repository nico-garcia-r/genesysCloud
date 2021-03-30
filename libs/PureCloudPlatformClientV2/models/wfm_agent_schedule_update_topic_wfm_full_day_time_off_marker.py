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

class WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'time_off_request_id': 'str',
            'management_unit_date': 'str',
            'activity_code_id': 'str',
            'is_paid': 'bool',
            'length_in_minutes': 'int',
            'description': 'str',
            'paid': 'bool'
        }

        self.attribute_map = {
            'time_off_request_id': 'timeOffRequestId',
            'management_unit_date': 'managementUnitDate',
            'activity_code_id': 'activityCodeId',
            'is_paid': 'isPaid',
            'length_in_minutes': 'lengthInMinutes',
            'description': 'description',
            'paid': 'paid'
        }

        self._time_off_request_id = None
        self._management_unit_date = None
        self._activity_code_id = None
        self._is_paid = None
        self._length_in_minutes = None
        self._description = None
        self._paid = None

    @property
    def time_off_request_id(self):
        """
        Gets the time_off_request_id of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :return: The time_off_request_id of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :rtype: str
        """
        return self._time_off_request_id

    @time_off_request_id.setter
    def time_off_request_id(self, time_off_request_id):
        """
        Sets the time_off_request_id of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :param time_off_request_id: The time_off_request_id of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :type: str
        """
        
        self._time_off_request_id = time_off_request_id

    @property
    def management_unit_date(self):
        """
        Gets the management_unit_date of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :return: The management_unit_date of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :rtype: str
        """
        return self._management_unit_date

    @management_unit_date.setter
    def management_unit_date(self, management_unit_date):
        """
        Sets the management_unit_date of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :param management_unit_date: The management_unit_date of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :type: str
        """
        
        self._management_unit_date = management_unit_date

    @property
    def activity_code_id(self):
        """
        Gets the activity_code_id of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :return: The activity_code_id of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :rtype: str
        """
        return self._activity_code_id

    @activity_code_id.setter
    def activity_code_id(self, activity_code_id):
        """
        Sets the activity_code_id of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :param activity_code_id: The activity_code_id of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :type: str
        """
        
        self._activity_code_id = activity_code_id

    @property
    def is_paid(self):
        """
        Gets the is_paid of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :return: The is_paid of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :rtype: bool
        """
        return self._is_paid

    @is_paid.setter
    def is_paid(self, is_paid):
        """
        Sets the is_paid of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :param is_paid: The is_paid of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :type: bool
        """
        
        self._is_paid = is_paid

    @property
    def length_in_minutes(self):
        """
        Gets the length_in_minutes of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :return: The length_in_minutes of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :rtype: int
        """
        return self._length_in_minutes

    @length_in_minutes.setter
    def length_in_minutes(self, length_in_minutes):
        """
        Sets the length_in_minutes of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :param length_in_minutes: The length_in_minutes of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :type: int
        """
        
        self._length_in_minutes = length_in_minutes

    @property
    def description(self):
        """
        Gets the description of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :return: The description of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :param description: The description of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :type: str
        """
        
        self._description = description

    @property
    def paid(self):
        """
        Gets the paid of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :return: The paid of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :rtype: bool
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """
        Sets the paid of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.


        :param paid: The paid of this WfmAgentScheduleUpdateTopicWfmFullDayTimeOffMarker.
        :type: bool
        """
        
        self._paid = paid

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

