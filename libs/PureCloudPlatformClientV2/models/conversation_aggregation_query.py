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

class ConversationAggregationQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConversationAggregationQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interval': 'str',
            'granularity': 'str',
            'time_zone': 'str',
            'group_by': 'list[str]',
            'filter': 'ConversationAggregateQueryFilter',
            'metrics': 'list[str]',
            'flatten_multivalued_dimensions': 'bool',
            'views': 'list[ConversationAggregationView]',
            'alternate_time_dimension': 'str'
        }

        self.attribute_map = {
            'interval': 'interval',
            'granularity': 'granularity',
            'time_zone': 'timeZone',
            'group_by': 'groupBy',
            'filter': 'filter',
            'metrics': 'metrics',
            'flatten_multivalued_dimensions': 'flattenMultivaluedDimensions',
            'views': 'views',
            'alternate_time_dimension': 'alternateTimeDimension'
        }

        self._interval = None
        self._granularity = None
        self._time_zone = None
        self._group_by = None
        self._filter = None
        self._metrics = None
        self._flatten_multivalued_dimensions = None
        self._views = None
        self._alternate_time_dimension = None

    @property
    def interval(self):
        """
        Gets the interval of this ConversationAggregationQuery.
        Behaves like one clause in a SQL WHERE. Specifies the date and time range of data being queried. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :return: The interval of this ConversationAggregationQuery.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this ConversationAggregationQuery.
        Behaves like one clause in a SQL WHERE. Specifies the date and time range of data being queried. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :param interval: The interval of this ConversationAggregationQuery.
        :type: str
        """
        
        self._interval = interval

    @property
    def granularity(self):
        """
        Gets the granularity of this ConversationAggregationQuery.
        Granularity aggregates metrics into subpartitions within the time interval specified. The default granularity is the same duration as the interval. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :return: The granularity of this ConversationAggregationQuery.
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """
        Sets the granularity of this ConversationAggregationQuery.
        Granularity aggregates metrics into subpartitions within the time interval specified. The default granularity is the same duration as the interval. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :param granularity: The granularity of this ConversationAggregationQuery.
        :type: str
        """
        
        self._granularity = granularity

    @property
    def time_zone(self):
        """
        Gets the time_zone of this ConversationAggregationQuery.
        Time zone context used to calculate response intervals (this allows resolving DST changes). The interval offset is used even when timeZone is specified. Default is UTC. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London

        :return: The time_zone of this ConversationAggregationQuery.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this ConversationAggregationQuery.
        Time zone context used to calculate response intervals (this allows resolving DST changes). The interval offset is used even when timeZone is specified. Default is UTC. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London

        :param time_zone: The time_zone of this ConversationAggregationQuery.
        :type: str
        """
        
        self._time_zone = time_zone

    @property
    def group_by(self):
        """
        Gets the group_by of this ConversationAggregationQuery.
        Behaves like a SQL GROUPBY. Allows for multiple levels of grouping as a list of dimensions. Partitions resulting aggregate computations into distinct named subgroups rather than across the entire result set as if it were one group.

        :return: The group_by of this ConversationAggregationQuery.
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """
        Sets the group_by of this ConversationAggregationQuery.
        Behaves like a SQL GROUPBY. Allows for multiple levels of grouping as a list of dimensions. Partitions resulting aggregate computations into distinct named subgroups rather than across the entire result set as if it were one group.

        :param group_by: The group_by of this ConversationAggregationQuery.
        :type: list[str]
        """
        
        self._group_by = group_by

    @property
    def filter(self):
        """
        Gets the filter of this ConversationAggregationQuery.
        Behaves like a SQL WHERE clause. This is ANDed with the interval parameter. Expresses boolean logical predicates as well as dimensional filters

        :return: The filter of this ConversationAggregationQuery.
        :rtype: ConversationAggregateQueryFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this ConversationAggregationQuery.
        Behaves like a SQL WHERE clause. This is ANDed with the interval parameter. Expresses boolean logical predicates as well as dimensional filters

        :param filter: The filter of this ConversationAggregationQuery.
        :type: ConversationAggregateQueryFilter
        """
        
        self._filter = filter

    @property
    def metrics(self):
        """
        Gets the metrics of this ConversationAggregationQuery.
        Behaves like a SQL SELECT clause. Only named metrics will be retrieved.

        :return: The metrics of this ConversationAggregationQuery.
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this ConversationAggregationQuery.
        Behaves like a SQL SELECT clause. Only named metrics will be retrieved.

        :param metrics: The metrics of this ConversationAggregationQuery.
        :type: list[str]
        """
        
        self._metrics = metrics

    @property
    def flatten_multivalued_dimensions(self):
        """
        Gets the flatten_multivalued_dimensions of this ConversationAggregationQuery.
        Flattens any multivalued dimensions used in response groups (e.g. ['a','b','c']->'a,b,c')

        :return: The flatten_multivalued_dimensions of this ConversationAggregationQuery.
        :rtype: bool
        """
        return self._flatten_multivalued_dimensions

    @flatten_multivalued_dimensions.setter
    def flatten_multivalued_dimensions(self, flatten_multivalued_dimensions):
        """
        Sets the flatten_multivalued_dimensions of this ConversationAggregationQuery.
        Flattens any multivalued dimensions used in response groups (e.g. ['a','b','c']->'a,b,c')

        :param flatten_multivalued_dimensions: The flatten_multivalued_dimensions of this ConversationAggregationQuery.
        :type: bool
        """
        
        self._flatten_multivalued_dimensions = flatten_multivalued_dimensions

    @property
    def views(self):
        """
        Gets the views of this ConversationAggregationQuery.
        Custom derived metric views

        :return: The views of this ConversationAggregationQuery.
        :rtype: list[ConversationAggregationView]
        """
        return self._views

    @views.setter
    def views(self, views):
        """
        Sets the views of this ConversationAggregationQuery.
        Custom derived metric views

        :param views: The views of this ConversationAggregationQuery.
        :type: list[ConversationAggregationView]
        """
        
        self._views = views

    @property
    def alternate_time_dimension(self):
        """
        Gets the alternate_time_dimension of this ConversationAggregationQuery.
        Dimension to use as the alternative timestamp for data in the aggregate.  Choosing \"eventTime\" uses the actual time of the data event.

        :return: The alternate_time_dimension of this ConversationAggregationQuery.
        :rtype: str
        """
        return self._alternate_time_dimension

    @alternate_time_dimension.setter
    def alternate_time_dimension(self, alternate_time_dimension):
        """
        Sets the alternate_time_dimension of this ConversationAggregationQuery.
        Dimension to use as the alternative timestamp for data in the aggregate.  Choosing \"eventTime\" uses the actual time of the data event.

        :param alternate_time_dimension: The alternate_time_dimension of this ConversationAggregationQuery.
        :type: str
        """
        allowed_values = ["eventTime"]
        if alternate_time_dimension.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for alternate_time_dimension -> " + alternate_time_dimension)
            self._alternate_time_dimension = "outdated_sdk_version"
        else:
            self._alternate_time_dimension = alternate_time_dimension

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

