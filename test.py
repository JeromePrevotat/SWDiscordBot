###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import requests

import swgohgg

import servers_locals

if __name__ == '__main__':
    swgoh = swgohgg.Swgohgg()
    charList = swgoh.get_from_api('characters')
    matches = []
    for character in charList:
        for ablt in character['ability_classes']:
            if ablt not in matches:
                matches.append(ablt)
    with open('trash', 'w+') as f:
        for ablt in matches:
            f.write(ablt + '\n')
