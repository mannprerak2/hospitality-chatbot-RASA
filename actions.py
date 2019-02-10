# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)

url = 'http://192.168.43.186:8000/api'

class ActionEvent(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_event"

    def run(self, dispatcher, tracker, domain):
        print('============================')
        # name = next(tracker.get_latest_entity_values('event_name'),None)
        name = tracker.get_slot('event_name')
        print(name)
        print('============================')

        # what your action should do
        request = json.loads(requests.get(f'{url}/event?name={name}').text)  # make an api call
        dispatcher.utter_message(f"{name}, {request[0]['time']}, at, {request[0]['location']}")

        # dispatcher.utter_message(f"{request[0]['name']}\n{request[0]['location']}")
        # # dispatcher.utter_message(joke)  # send the message back to the user

class ActionEventLocation(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_event_location"

    def run(self, dispatcher, tracker, domain):
        print('============================')
        # name = next(tracker.get_latest_entity_values('event_name'),None)
        name = tracker.get_slot('event_name')
        print(name)
        print('============================')

        # what your action should do
        request = json.loads(requests.get(f'{url}/event?name={name}').text)  # make an api call
        dispatcher.utter_message(f"{name}is at, {request[0]['location']}")

class ActionEventTime(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_event_time"

    def run(self, dispatcher, tracker, domain):
        print('============================')
        # name = next(tracker.get_latest_entity_values('event_name'),None)
        name = tracker.get_slot('event_name')
        print(name)
        print('============================')

        # what your action should do
        request = json.loads(requests.get(f'{url}/event?name={name}').text)  # make an api call
        dispatcher.utter_message(f"{name} timing : {request[0]['time']}")

class ActionWashroom(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_washroom"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('{url}/').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

class ActionFoodLocation(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_food_location"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('{url}/').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []
