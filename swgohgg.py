#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module to communicate with the swgoh.gg API.
"""

###############################################################################
#                         IMPORTS                                             #
###############################################################################

import requests
from json import loads, dumps

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

BASIC_ABLT = 1
SPECIAL_ABLT = 2
LEADER_ABLT = 3
UNIQUE_ABLT = 4
SHIP_ABLT = 5

###############################################################################
#                         CLASSES                                             #
###############################################################################

class Swgohgg():
    def __init__(self):
        self.baseUrl = 'https://swgoh.gg/api/'
        self.categoryUrl = {
            'abilities':'abilities/',
            'characters':'characters/',
            'ships':'ships/',
            'token-balance':'token-balance/',
        }

    def get_from_api(self, category):
        fullUrl = self.baseUrl + self.categoryUrl[category]
        request = requests.request('GET', fullUrl, timeout=10)
        if request.status_code != 200:
            return {'status_code':request.status_code, 'message':'Error'}
        result = loads(request.content.decode('utf-8'))
        return result

    def get_character(self, charName, charList):
        character = []
        for character in charList:
            if charName.lower().strip() == character['name'].lower().strip():
                return character

    def get_ability_class_list(self, charList):
        abltClassList = []
        for character in charList:
            for abltClass in character['ability_classes']:
                if abltClass not in abltClassList:
                    abltClassList.append(abltClass)
        return abltClassList
