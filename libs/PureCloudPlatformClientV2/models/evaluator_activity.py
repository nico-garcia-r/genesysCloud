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

class EvaluatorActivity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EvaluatorActivity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'evaluator': 'User',
            'num_evaluations_assigned': 'int',
            'num_evaluations_started': 'int',
            'num_evaluations_completed': 'int',
            'num_calibrations_assigned': 'int',
            'num_calibrations_started': 'int',
            'num_calibrations_completed': 'int',
            'num_evaluations_without_view_permission': 'int',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'evaluator': 'evaluator',
            'num_evaluations_assigned': 'numEvaluationsAssigned',
            'num_evaluations_started': 'numEvaluationsStarted',
            'num_evaluations_completed': 'numEvaluationsCompleted',
            'num_calibrations_assigned': 'numCalibrationsAssigned',
            'num_calibrations_started': 'numCalibrationsStarted',
            'num_calibrations_completed': 'numCalibrationsCompleted',
            'num_evaluations_without_view_permission': 'numEvaluationsWithoutViewPermission',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._evaluator = None
        self._num_evaluations_assigned = None
        self._num_evaluations_started = None
        self._num_evaluations_completed = None
        self._num_calibrations_assigned = None
        self._num_calibrations_started = None
        self._num_calibrations_completed = None
        self._num_evaluations_without_view_permission = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this EvaluatorActivity.
        The globally unique identifier for the object.

        :return: The id of this EvaluatorActivity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EvaluatorActivity.
        The globally unique identifier for the object.

        :param id: The id of this EvaluatorActivity.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this EvaluatorActivity.


        :return: The name of this EvaluatorActivity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EvaluatorActivity.


        :param name: The name of this EvaluatorActivity.
        :type: str
        """
        
        self._name = name

    @property
    def evaluator(self):
        """
        Gets the evaluator of this EvaluatorActivity.


        :return: The evaluator of this EvaluatorActivity.
        :rtype: User
        """
        return self._evaluator

    @evaluator.setter
    def evaluator(self, evaluator):
        """
        Sets the evaluator of this EvaluatorActivity.


        :param evaluator: The evaluator of this EvaluatorActivity.
        :type: User
        """
        
        self._evaluator = evaluator

    @property
    def num_evaluations_assigned(self):
        """
        Gets the num_evaluations_assigned of this EvaluatorActivity.


        :return: The num_evaluations_assigned of this EvaluatorActivity.
        :rtype: int
        """
        return self._num_evaluations_assigned

    @num_evaluations_assigned.setter
    def num_evaluations_assigned(self, num_evaluations_assigned):
        """
        Sets the num_evaluations_assigned of this EvaluatorActivity.


        :param num_evaluations_assigned: The num_evaluations_assigned of this EvaluatorActivity.
        :type: int
        """
        
        self._num_evaluations_assigned = num_evaluations_assigned

    @property
    def num_evaluations_started(self):
        """
        Gets the num_evaluations_started of this EvaluatorActivity.


        :return: The num_evaluations_started of this EvaluatorActivity.
        :rtype: int
        """
        return self._num_evaluations_started

    @num_evaluations_started.setter
    def num_evaluations_started(self, num_evaluations_started):
        """
        Sets the num_evaluations_started of this EvaluatorActivity.


        :param num_evaluations_started: The num_evaluations_started of this EvaluatorActivity.
        :type: int
        """
        
        self._num_evaluations_started = num_evaluations_started

    @property
    def num_evaluations_completed(self):
        """
        Gets the num_evaluations_completed of this EvaluatorActivity.


        :return: The num_evaluations_completed of this EvaluatorActivity.
        :rtype: int
        """
        return self._num_evaluations_completed

    @num_evaluations_completed.setter
    def num_evaluations_completed(self, num_evaluations_completed):
        """
        Sets the num_evaluations_completed of this EvaluatorActivity.


        :param num_evaluations_completed: The num_evaluations_completed of this EvaluatorActivity.
        :type: int
        """
        
        self._num_evaluations_completed = num_evaluations_completed

    @property
    def num_calibrations_assigned(self):
        """
        Gets the num_calibrations_assigned of this EvaluatorActivity.


        :return: The num_calibrations_assigned of this EvaluatorActivity.
        :rtype: int
        """
        return self._num_calibrations_assigned

    @num_calibrations_assigned.setter
    def num_calibrations_assigned(self, num_calibrations_assigned):
        """
        Sets the num_calibrations_assigned of this EvaluatorActivity.


        :param num_calibrations_assigned: The num_calibrations_assigned of this EvaluatorActivity.
        :type: int
        """
        
        self._num_calibrations_assigned = num_calibrations_assigned

    @property
    def num_calibrations_started(self):
        """
        Gets the num_calibrations_started of this EvaluatorActivity.


        :return: The num_calibrations_started of this EvaluatorActivity.
        :rtype: int
        """
        return self._num_calibrations_started

    @num_calibrations_started.setter
    def num_calibrations_started(self, num_calibrations_started):
        """
        Sets the num_calibrations_started of this EvaluatorActivity.


        :param num_calibrations_started: The num_calibrations_started of this EvaluatorActivity.
        :type: int
        """
        
        self._num_calibrations_started = num_calibrations_started

    @property
    def num_calibrations_completed(self):
        """
        Gets the num_calibrations_completed of this EvaluatorActivity.


        :return: The num_calibrations_completed of this EvaluatorActivity.
        :rtype: int
        """
        return self._num_calibrations_completed

    @num_calibrations_completed.setter
    def num_calibrations_completed(self, num_calibrations_completed):
        """
        Sets the num_calibrations_completed of this EvaluatorActivity.


        :param num_calibrations_completed: The num_calibrations_completed of this EvaluatorActivity.
        :type: int
        """
        
        self._num_calibrations_completed = num_calibrations_completed

    @property
    def num_evaluations_without_view_permission(self):
        """
        Gets the num_evaluations_without_view_permission of this EvaluatorActivity.


        :return: The num_evaluations_without_view_permission of this EvaluatorActivity.
        :rtype: int
        """
        return self._num_evaluations_without_view_permission

    @num_evaluations_without_view_permission.setter
    def num_evaluations_without_view_permission(self, num_evaluations_without_view_permission):
        """
        Sets the num_evaluations_without_view_permission of this EvaluatorActivity.


        :param num_evaluations_without_view_permission: The num_evaluations_without_view_permission of this EvaluatorActivity.
        :type: int
        """
        
        self._num_evaluations_without_view_permission = num_evaluations_without_view_permission

    @property
    def self_uri(self):
        """
        Gets the self_uri of this EvaluatorActivity.
        The URI for this object

        :return: The self_uri of this EvaluatorActivity.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this EvaluatorActivity.
        The URI for this object

        :param self_uri: The self_uri of this EvaluatorActivity.
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

