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

class PatchActionMapScheduleGroups(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PatchActionMapScheduleGroups - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action_map_schedule_group': 'ActionMapScheduleGroup',
            'emergency_action_map_schedule_group': 'ActionMapScheduleGroup'
        }

        self.attribute_map = {
            'action_map_schedule_group': 'actionMapScheduleGroup',
            'emergency_action_map_schedule_group': 'emergencyActionMapScheduleGroup'
        }

        self._action_map_schedule_group = None
        self._emergency_action_map_schedule_group = None

    @property
    def action_map_schedule_group(self):
        """
        Gets the action_map_schedule_group of this PatchActionMapScheduleGroups.
        The actions map's associated schedule group.

        :return: The action_map_schedule_group of this PatchActionMapScheduleGroups.
        :rtype: ActionMapScheduleGroup
        """
        return self._action_map_schedule_group

    @action_map_schedule_group.setter
    def action_map_schedule_group(self, action_map_schedule_group):
        """
        Sets the action_map_schedule_group of this PatchActionMapScheduleGroups.
        The actions map's associated schedule group.

        :param action_map_schedule_group: The action_map_schedule_group of this PatchActionMapScheduleGroups.
        :type: ActionMapScheduleGroup
        """
        
        self._action_map_schedule_group = action_map_schedule_group

    @property
    def emergency_action_map_schedule_group(self):
        """
        Gets the emergency_action_map_schedule_group of this PatchActionMapScheduleGroups.
        The action map's associated emergency schedule group.

        :return: The emergency_action_map_schedule_group of this PatchActionMapScheduleGroups.
        :rtype: ActionMapScheduleGroup
        """
        return self._emergency_action_map_schedule_group

    @emergency_action_map_schedule_group.setter
    def emergency_action_map_schedule_group(self, emergency_action_map_schedule_group):
        """
        Sets the emergency_action_map_schedule_group of this PatchActionMapScheduleGroups.
        The action map's associated emergency schedule group.

        :param emergency_action_map_schedule_group: The emergency_action_map_schedule_group of this PatchActionMapScheduleGroups.
        :type: ActionMapScheduleGroup
        """
        
        self._emergency_action_map_schedule_group = emergency_action_map_schedule_group

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

