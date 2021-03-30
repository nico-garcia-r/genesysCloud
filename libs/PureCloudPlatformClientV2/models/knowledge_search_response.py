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

class KnowledgeSearchResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        KnowledgeSearchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'search_id': 'str',
            'total': 'int',
            'page_count': 'int',
            'page_size': 'int',
            'page_number': 'int',
            'results': 'list[KnowledgeSearchDocument]'
        }

        self.attribute_map = {
            'search_id': 'searchId',
            'total': 'total',
            'page_count': 'pageCount',
            'page_size': 'pageSize',
            'page_number': 'pageNumber',
            'results': 'results'
        }

        self._search_id = None
        self._total = None
        self._page_count = None
        self._page_size = None
        self._page_number = None
        self._results = None

    @property
    def search_id(self):
        """
        Gets the search_id of this KnowledgeSearchResponse.
        Search Id

        :return: The search_id of this KnowledgeSearchResponse.
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """
        Sets the search_id of this KnowledgeSearchResponse.
        Search Id

        :param search_id: The search_id of this KnowledgeSearchResponse.
        :type: str
        """
        
        self._search_id = search_id

    @property
    def total(self):
        """
        Gets the total of this KnowledgeSearchResponse.
        Total number of records returned

        :return: The total of this KnowledgeSearchResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this KnowledgeSearchResponse.
        Total number of records returned

        :param total: The total of this KnowledgeSearchResponse.
        :type: int
        """
        
        self._total = total

    @property
    def page_count(self):
        """
        Gets the page_count of this KnowledgeSearchResponse.
        Number of pages returned in the result calculated according to the pageSize and the total

        :return: The page_count of this KnowledgeSearchResponse.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this KnowledgeSearchResponse.
        Number of pages returned in the result calculated according to the pageSize and the total

        :param page_count: The page_count of this KnowledgeSearchResponse.
        :type: int
        """
        
        self._page_count = page_count

    @property
    def page_size(self):
        """
        Gets the page_size of this KnowledgeSearchResponse.
        Number of records according to the page size

        :return: The page_size of this KnowledgeSearchResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this KnowledgeSearchResponse.
        Number of records according to the page size

        :param page_size: The page_size of this KnowledgeSearchResponse.
        :type: int
        """
        
        self._page_size = page_size

    @property
    def page_number(self):
        """
        Gets the page_number of this KnowledgeSearchResponse.
        Current page number for the returned records

        :return: The page_number of this KnowledgeSearchResponse.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this KnowledgeSearchResponse.
        Current page number for the returned records

        :param page_number: The page_number of this KnowledgeSearchResponse.
        :type: int
        """
        
        self._page_number = page_number

    @property
    def results(self):
        """
        Gets the results of this KnowledgeSearchResponse.
        Results associated to the search response

        :return: The results of this KnowledgeSearchResponse.
        :rtype: list[KnowledgeSearchDocument]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this KnowledgeSearchResponse.
        Results associated to the search response

        :param results: The results of this KnowledgeSearchResponse.
        :type: list[KnowledgeSearchDocument]
        """
        
        self._results = results

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

