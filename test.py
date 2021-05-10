###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import requests

import swgohgg

import servers_locals

if __name__ == '__main__':
    client = swgohgg.Swgohgg()
    charList = client.get_from_api('characters')
    with open(os.path.join(os.getcwd() + os.sep + 'characters'), 'w+') as f:
        for character in charList:
            f.write('\'' + character['name'] + '\':\'' + character['name'] + '\',\n')
