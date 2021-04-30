###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import requests

import swgohgg

import interactions

if __name__ == '__main__':
    client = swgohgg.Swgohgg()
    charList = client.get_from_api('characters')

    wrecker = {}
    for character in charList:
        if character['base_id'] == 'BADBATCHWRECKER':
            wrecker = dict(character)
    pcwd = os.getcwd()
    with open(os.path.join(pcwd + os.sep + 'interactions.py'), 'a+') as f:
        f.write(str(wrecker))
