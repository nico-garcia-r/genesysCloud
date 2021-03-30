# coding: utf-8

"""
AlertingApi.py
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
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AlertingApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_alerting_interactionstats_alert(self, alert_id, **kwargs):
        """
        Delete an interaction stats alert
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_alerting_interactionstats_alert(alert_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str alert_id: Alert ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alert_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_alerting_interactionstats_alert" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params) or (params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `delete_alerting_interactionstats_alert`")


        resource_path = '/api/v2/alerting/interactionstats/alerts/{alertId}'.replace('{format}', 'json')
        path_params = {}
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_alerting_interactionstats_rule(self, rule_id, **kwargs):
        """
        Delete an interaction stats rule.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_alerting_interactionstats_rule(rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str rule_id: Rule ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_alerting_interactionstats_rule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params) or (params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `delete_alerting_interactionstats_rule`")


        resource_path = '/api/v2/alerting/interactionstats/rules/{ruleId}'.replace('{format}', 'json')
        path_params = {}
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_alerting_alerts_active(self, **kwargs):
        """
        Gets active alert count for a user.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_alerting_alerts_active(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ActiveAlertCount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alerting_alerts_active" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/alerting/alerts/active'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ActiveAlertCount',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_alerting_interactionstats_alert(self, alert_id, **kwargs):
        """
        Get an interaction stats alert
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_alerting_interactionstats_alert(alert_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str alert_id: Alert ID (required)
        :param list[str] expand: Which fields, if any, to expand
        :return: InteractionStatsAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alert_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alerting_interactionstats_alert" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params) or (params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `get_alerting_interactionstats_alert`")


        resource_path = '/api/v2/alerting/interactionstats/alerts/{alertId}'.replace('{format}', 'json')
        path_params = {}
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InteractionStatsAlert',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_alerting_interactionstats_alerts(self, **kwargs):
        """
        Get interaction stats alert list.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_alerting_interactionstats_alerts(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] expand: Which fields, if any, to expand
        :return: InteractionStatsAlertContainer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alerting_interactionstats_alerts" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/alerting/interactionstats/alerts'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InteractionStatsAlertContainer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_alerting_interactionstats_alerts_unread(self, **kwargs):
        """
        Gets user unread count of interaction stats alerts.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_alerting_interactionstats_alerts_unread(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UnreadMetric
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alerting_interactionstats_alerts_unread" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/alerting/interactionstats/alerts/unread'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UnreadMetric',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_alerting_interactionstats_rule(self, rule_id, **kwargs):
        """
        Get an interaction stats rule.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_alerting_interactionstats_rule(rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str rule_id: Rule ID (required)
        :param list[str] expand: Which fields, if any, to expand
        :return: InteractionStatsRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alerting_interactionstats_rule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params) or (params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `get_alerting_interactionstats_rule`")


        resource_path = '/api/v2/alerting/interactionstats/rules/{ruleId}'.replace('{format}', 'json')
        path_params = {}
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InteractionStatsRule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_alerting_interactionstats_rules(self, **kwargs):
        """
        Get an interaction stats rule list.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_alerting_interactionstats_rules(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] expand: Which fields, if any, to expand
        :return: InteractionStatsRuleContainer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alerting_interactionstats_rules" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/alerting/interactionstats/rules'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InteractionStatsRuleContainer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_alerting_interactionstats_rules(self, body, **kwargs):
        """
        Create an interaction stats rule.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_alerting_interactionstats_rules(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param InteractionStatsRule body: AlertingRule (required)
        :param list[str] expand: Which fields, if any, to expand
        :return: InteractionStatsRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_alerting_interactionstats_rules" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_alerting_interactionstats_rules`")


        resource_path = '/api/v2/alerting/interactionstats/rules'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InteractionStatsRule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_alerting_interactionstats_alert(self, alert_id, body, **kwargs):
        """
        Update an interaction stats alert read status
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_alerting_interactionstats_alert(alert_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str alert_id: Alert ID (required)
        :param UnreadStatus body: InteractionStatsAlert (required)
        :param list[str] expand: Which fields, if any, to expand
        :return: UnreadStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alert_id', 'body', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_alerting_interactionstats_alert" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'alert_id' is set
        if ('alert_id' not in params) or (params['alert_id'] is None):
            raise ValueError("Missing the required parameter `alert_id` when calling `put_alerting_interactionstats_alert`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_alerting_interactionstats_alert`")


        resource_path = '/api/v2/alerting/interactionstats/alerts/{alertId}'.replace('{format}', 'json')
        path_params = {}
        if 'alert_id' in params:
            path_params['alertId'] = params['alert_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UnreadStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_alerting_interactionstats_rule(self, rule_id, body, **kwargs):
        """
        Update an interaction stats rule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_alerting_interactionstats_rule(rule_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str rule_id: Rule ID (required)
        :param InteractionStatsRule body: AlertingRule (required)
        :param list[str] expand: Which fields, if any, to expand
        :return: InteractionStatsRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_id', 'body', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_alerting_interactionstats_rule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params) or (params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `put_alerting_interactionstats_rule`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_alerting_interactionstats_rule`")


        resource_path = '/api/v2/alerting/interactionstats/rules/{ruleId}'.replace('{format}', 'json')
        path_params = {}
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InteractionStatsRule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
