###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import requests

import swgohgg

import servers_locals

if __name__ == '__main__':
    swgoh = swgohgg.Swgohgg()
    abilities = swgoh.get_from_api('abilities')
    matches = []
    for charDict in abilities:
        if charDict['character_base_id'] == 'EZRABRIDGERS3'\
            and charDict['type'] != 5\
            and charDict['type'] == 1:
            matches.append(charDict)
    for ab in matches:
        print('{}\n'.format(ab))
