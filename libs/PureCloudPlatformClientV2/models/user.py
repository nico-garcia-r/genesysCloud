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

class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'division': 'Division',
            'chat': 'Chat',
            'department': 'str',
            'email': 'str',
            'primary_contact_info': 'list[Contact]',
            'addresses': 'list[Contact]',
            'state': 'str',
            'title': 'str',
            'username': 'str',
            'manager': 'User',
            'images': 'list[UserImage]',
            'version': 'int',
            'certifications': 'list[str]',
            'biography': 'Biography',
            'employer_info': 'EmployerInfo',
            'routing_status': 'RoutingStatus',
            'presence': 'UserPresence',
            'conversation_summary': 'UserConversationSummary',
            'out_of_office': 'OutOfOffice',
            'geolocation': 'Geolocation',
            'station': 'UserStations',
            'authorization': 'UserAuthorization',
            'profile_skills': 'list[str]',
            'locations': 'list[Location]',
            'groups': 'list[Group]',
            'team': 'Team',
            'skills': 'list[UserRoutingSkill]',
            'languages': 'list[UserRoutingLanguage]',
            'acd_auto_answer': 'bool',
            'language_preference': 'str',
            'last_token_issued': 'OAuthLastTokenIssued',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'chat': 'chat',
            'department': 'department',
            'email': 'email',
            'primary_contact_info': 'primaryContactInfo',
            'addresses': 'addresses',
            'state': 'state',
            'title': 'title',
            'username': 'username',
            'manager': 'manager',
            'images': 'images',
            'version': 'version',
            'certifications': 'certifications',
            'biography': 'biography',
            'employer_info': 'employerInfo',
            'routing_status': 'routingStatus',
            'presence': 'presence',
            'conversation_summary': 'conversationSummary',
            'out_of_office': 'outOfOffice',
            'geolocation': 'geolocation',
            'station': 'station',
            'authorization': 'authorization',
            'profile_skills': 'profileSkills',
            'locations': 'locations',
            'groups': 'groups',
            'team': 'team',
            'skills': 'skills',
            'languages': 'languages',
            'acd_auto_answer': 'acdAutoAnswer',
            'language_preference': 'languagePreference',
            'last_token_issued': 'lastTokenIssued',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._chat = None
        self._department = None
        self._email = None
        self._primary_contact_info = None
        self._addresses = None
        self._state = None
        self._title = None
        self._username = None
        self._manager = None
        self._images = None
        self._version = None
        self._certifications = None
        self._biography = None
        self._employer_info = None
        self._routing_status = None
        self._presence = None
        self._conversation_summary = None
        self._out_of_office = None
        self._geolocation = None
        self._station = None
        self._authorization = None
        self._profile_skills = None
        self._locations = None
        self._groups = None
        self._team = None
        self._skills = None
        self._languages = None
        self._acd_auto_answer = None
        self._language_preference = None
        self._last_token_issued = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this User.
        The globally unique identifier for the object.

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        The globally unique identifier for the object.

        :param id: The id of this User.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this User.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.


        :param name: The name of this User.
        :type: str
        """
        
        self._name = name

    @property
    def division(self):
        """
        Gets the division of this User.
        The division to which this entity belongs.

        :return: The division of this User.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division):
        """
        Sets the division of this User.
        The division to which this entity belongs.

        :param division: The division of this User.
        :type: Division
        """
        
        self._division = division

    @property
    def chat(self):
        """
        Gets the chat of this User.


        :return: The chat of this User.
        :rtype: Chat
        """
        return self._chat

    @chat.setter
    def chat(self, chat):
        """
        Sets the chat of this User.


        :param chat: The chat of this User.
        :type: Chat
        """
        
        self._chat = chat

    @property
    def department(self):
        """
        Gets the department of this User.


        :return: The department of this User.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """
        Sets the department of this User.


        :param department: The department of this User.
        :type: str
        """
        
        self._department = department

    @property
    def email(self):
        """
        Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.


        :param email: The email of this User.
        :type: str
        """
        
        self._email = email

    @property
    def primary_contact_info(self):
        """
        Gets the primary_contact_info of this User.
        Auto populated from addresses.

        :return: The primary_contact_info of this User.
        :rtype: list[Contact]
        """
        return self._primary_contact_info

    @primary_contact_info.setter
    def primary_contact_info(self, primary_contact_info):
        """
        Sets the primary_contact_info of this User.
        Auto populated from addresses.

        :param primary_contact_info: The primary_contact_info of this User.
        :type: list[Contact]
        """
        
        self._primary_contact_info = primary_contact_info

    @property
    def addresses(self):
        """
        Gets the addresses of this User.
        Email addresses and phone numbers for this user

        :return: The addresses of this User.
        :rtype: list[Contact]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this User.
        Email addresses and phone numbers for this user

        :param addresses: The addresses of this User.
        :type: list[Contact]
        """
        
        self._addresses = addresses

    @property
    def state(self):
        """
        Gets the state of this User.
        The current state for this user.

        :return: The state of this User.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this User.
        The current state for this user.

        :param state: The state of this User.
        :type: str
        """
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def title(self):
        """
        Gets the title of this User.


        :return: The title of this User.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this User.


        :param title: The title of this User.
        :type: str
        """
        
        self._title = title

    @property
    def username(self):
        """
        Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this User.


        :param username: The username of this User.
        :type: str
        """
        
        self._username = username

    @property
    def manager(self):
        """
        Gets the manager of this User.


        :return: The manager of this User.
        :rtype: User
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this User.


        :param manager: The manager of this User.
        :type: User
        """
        
        self._manager = manager

    @property
    def images(self):
        """
        Gets the images of this User.


        :return: The images of this User.
        :rtype: list[UserImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this User.


        :param images: The images of this User.
        :type: list[UserImage]
        """
        
        self._images = images

    @property
    def version(self):
        """
        Gets the version of this User.
        Required when updating a user, this value should be the current version of the user.  The current version can be obtained with a GET on the user before doing a PATCH.

        :return: The version of this User.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this User.
        Required when updating a user, this value should be the current version of the user.  The current version can be obtained with a GET on the user before doing a PATCH.

        :param version: The version of this User.
        :type: int
        """
        
        self._version = version

    @property
    def certifications(self):
        """
        Gets the certifications of this User.


        :return: The certifications of this User.
        :rtype: list[str]
        """
        return self._certifications

    @certifications.setter
    def certifications(self, certifications):
        """
        Sets the certifications of this User.


        :param certifications: The certifications of this User.
        :type: list[str]
        """
        
        self._certifications = certifications

    @property
    def biography(self):
        """
        Gets the biography of this User.


        :return: The biography of this User.
        :rtype: Biography
        """
        return self._biography

    @biography.setter
    def biography(self, biography):
        """
        Sets the biography of this User.


        :param biography: The biography of this User.
        :type: Biography
        """
        
        self._biography = biography

    @property
    def employer_info(self):
        """
        Gets the employer_info of this User.


        :return: The employer_info of this User.
        :rtype: EmployerInfo
        """
        return self._employer_info

    @employer_info.setter
    def employer_info(self, employer_info):
        """
        Sets the employer_info of this User.


        :param employer_info: The employer_info of this User.
        :type: EmployerInfo
        """
        
        self._employer_info = employer_info

    @property
    def routing_status(self):
        """
        Gets the routing_status of this User.
        ACD routing status

        :return: The routing_status of this User.
        :rtype: RoutingStatus
        """
        return self._routing_status

    @routing_status.setter
    def routing_status(self, routing_status):
        """
        Sets the routing_status of this User.
        ACD routing status

        :param routing_status: The routing_status of this User.
        :type: RoutingStatus
        """
        
        self._routing_status = routing_status

    @property
    def presence(self):
        """
        Gets the presence of this User.
        Active presence

        :return: The presence of this User.
        :rtype: UserPresence
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this User.
        Active presence

        :param presence: The presence of this User.
        :type: UserPresence
        """
        
        self._presence = presence

    @property
    def conversation_summary(self):
        """
        Gets the conversation_summary of this User.
        Summary of conversion statistics for conversation types.

        :return: The conversation_summary of this User.
        :rtype: UserConversationSummary
        """
        return self._conversation_summary

    @conversation_summary.setter
    def conversation_summary(self, conversation_summary):
        """
        Sets the conversation_summary of this User.
        Summary of conversion statistics for conversation types.

        :param conversation_summary: The conversation_summary of this User.
        :type: UserConversationSummary
        """
        
        self._conversation_summary = conversation_summary

    @property
    def out_of_office(self):
        """
        Gets the out_of_office of this User.
        Determine if out of office is enabled

        :return: The out_of_office of this User.
        :rtype: OutOfOffice
        """
        return self._out_of_office

    @out_of_office.setter
    def out_of_office(self, out_of_office):
        """
        Sets the out_of_office of this User.
        Determine if out of office is enabled

        :param out_of_office: The out_of_office of this User.
        :type: OutOfOffice
        """
        
        self._out_of_office = out_of_office

    @property
    def geolocation(self):
        """
        Gets the geolocation of this User.
        Current geolocation position

        :return: The geolocation of this User.
        :rtype: Geolocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """
        Sets the geolocation of this User.
        Current geolocation position

        :param geolocation: The geolocation of this User.
        :type: Geolocation
        """
        
        self._geolocation = geolocation

    @property
    def station(self):
        """
        Gets the station of this User.
        Effective, default, and last station information

        :return: The station of this User.
        :rtype: UserStations
        """
        return self._station

    @station.setter
    def station(self, station):
        """
        Sets the station of this User.
        Effective, default, and last station information

        :param station: The station of this User.
        :type: UserStations
        """
        
        self._station = station

    @property
    def authorization(self):
        """
        Gets the authorization of this User.
        Roles and permissions assigned to the user

        :return: The authorization of this User.
        :rtype: UserAuthorization
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """
        Sets the authorization of this User.
        Roles and permissions assigned to the user

        :param authorization: The authorization of this User.
        :type: UserAuthorization
        """
        
        self._authorization = authorization

    @property
    def profile_skills(self):
        """
        Gets the profile_skills of this User.
        Profile skills possessed by the user

        :return: The profile_skills of this User.
        :rtype: list[str]
        """
        return self._profile_skills

    @profile_skills.setter
    def profile_skills(self, profile_skills):
        """
        Sets the profile_skills of this User.
        Profile skills possessed by the user

        :param profile_skills: The profile_skills of this User.
        :type: list[str]
        """
        
        self._profile_skills = profile_skills

    @property
    def locations(self):
        """
        Gets the locations of this User.
        The user placement at each site location.

        :return: The locations of this User.
        :rtype: list[Location]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """
        Sets the locations of this User.
        The user placement at each site location.

        :param locations: The locations of this User.
        :type: list[Location]
        """
        
        self._locations = locations

    @property
    def groups(self):
        """
        Gets the groups of this User.
        The groups the user is a member of

        :return: The groups of this User.
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this User.
        The groups the user is a member of

        :param groups: The groups of this User.
        :type: list[Group]
        """
        
        self._groups = groups

    @property
    def team(self):
        """
        Gets the team of this User.
        The team the user is a member of

        :return: The team of this User.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this User.
        The team the user is a member of

        :param team: The team of this User.
        :type: Team
        """
        
        self._team = team

    @property
    def skills(self):
        """
        Gets the skills of this User.
        Routing (ACD) skills possessed by the user

        :return: The skills of this User.
        :rtype: list[UserRoutingSkill]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """
        Sets the skills of this User.
        Routing (ACD) skills possessed by the user

        :param skills: The skills of this User.
        :type: list[UserRoutingSkill]
        """
        
        self._skills = skills

    @property
    def languages(self):
        """
        Gets the languages of this User.
        Routing (ACD) languages possessed by the user

        :return: The languages of this User.
        :rtype: list[UserRoutingLanguage]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """
        Sets the languages of this User.
        Routing (ACD) languages possessed by the user

        :param languages: The languages of this User.
        :type: list[UserRoutingLanguage]
        """
        
        self._languages = languages

    @property
    def acd_auto_answer(self):
        """
        Gets the acd_auto_answer of this User.
        acd auto answer

        :return: The acd_auto_answer of this User.
        :rtype: bool
        """
        return self._acd_auto_answer

    @acd_auto_answer.setter
    def acd_auto_answer(self, acd_auto_answer):
        """
        Sets the acd_auto_answer of this User.
        acd auto answer

        :param acd_auto_answer: The acd_auto_answer of this User.
        :type: bool
        """
        
        self._acd_auto_answer = acd_auto_answer

    @property
    def language_preference(self):
        """
        Gets the language_preference of this User.
        preferred language by the user

        :return: The language_preference of this User.
        :rtype: str
        """
        return self._language_preference

    @language_preference.setter
    def language_preference(self, language_preference):
        """
        Sets the language_preference of this User.
        preferred language by the user

        :param language_preference: The language_preference of this User.
        :type: str
        """
        
        self._language_preference = language_preference

    @property
    def last_token_issued(self):
        """
        Gets the last_token_issued of this User.


        :return: The last_token_issued of this User.
        :rtype: OAuthLastTokenIssued
        """
        return self._last_token_issued

    @last_token_issued.setter
    def last_token_issued(self, last_token_issued):
        """
        Sets the last_token_issued of this User.


        :param last_token_issued: The last_token_issued of this User.
        :type: OAuthLastTokenIssued
        """
        
        self._last_token_issued = last_token_issued

    @property
    def self_uri(self):
        """
        Gets the self_uri of this User.
        The URI for this object

        :return: The self_uri of this User.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this User.
        The URI for this object

        :param self_uri: The self_uri of this User.
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

