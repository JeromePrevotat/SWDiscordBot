###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import requests
from PIL import Image

import swgohgg

ASSETS_PATH = os.path.join(os.getcwd() + os.sep + 'assets')
CHARACTERS_ASSETS = os.path.join(ASSETS_PATH + os.sep + 'characters')
ABILITIES_ASSETS = os.path.join(ASSETS_PATH + os.sep + 'abilities')
FILE_FORMAT = '.png'

if __name__ == '__main__':
    def checkMissing(refList, newList, verbal):
        refTotal = len(refList)
        newTotal = len(newList)
        missing = []
        if verbal:
            print('There is {} Elements and {} were created.'.format(
                len(refList), len(newList)))
        if len(refList) != len(newList):
            if verbal:
                print('Here are the missing Elements :')
            for element in refList:
                if element not in newList:
                    missing.append(element)
                    if verbal:
                        print(element['base_id'])
        return refTotal, newTotal, missing

    def mkCharDirs(charList):
        print('Creating Folders...')
        for character in charList:
            if not os.path.isdir(ABILITIES_ASSETS
                + os.sep + character['base_id']):
                os.mkdir(ABILITIES_ASSETS + os.sep + character['base_id'])
        checkMissing([character['base_id'] for character in charList],
            os.listdir(ABILITIES_ASSETS), verbal=True)

    def getCharAssets(charList):
        for character in charList:
            url = 'https://swgoh.gg' + character['image']
            filename = url[:len(url)-1].split('/')[-1]
            response = requests.request('GET', url)
            if response.status_code == 200:
                with open(os.path.join(
                    CHARACTERS_ASSETS + os.sep + filename + FILE_FORMAT),
                    'w+b') as f:
                    f.write(response.content)
        checkMissing([character['base_id'] for character in charList],
            os.listdir(CHARACTERS_ASSETS), verbal=True)

    def getAbilitiesAssets(charList, abilitiesList):
        refTotal = 0
        newTotal = 0
        missingTotal = []
        for character in charList:
            charKit = []
            path = os.path.join(ABILITIES_ASSETS
                + os.sep + character['base_id'])
            for ability in abilitiesList:
                if ability['character_base_id'] == character['base_id']:
                    charKit.append(ability)
            for ability in charKit:
                url = 'https://swgoh.gg' + ability['image']
                response = requests.request('GET', url)
                filename = url[:len(url)-1].split('/')[-1]
                if response.status_code == 200:
                    with open(os.path.join(
                    ABILITIES_ASSETS + os.sep
                    + character['base_id'] + os.sep
                    + filename + FILE_FORMAT), 'w+b') as f:
                        f.write(response.content)
            # Final Check Lists
            r, n, m = checkMissing(charKit,
                os.listdir(ABILITIES_ASSETS + os.sep
                + character['base_id']), verbal = False)
            refTotal += r
            newTotal += n
            for element in m:
                missingTotal.append(element)
        # Print Missing Items
        print('There is {} Elements and {} were created.'.format(
            refTotal, newTotal))
        print('Here are the missing Elements :')
        for element in m:
            print(element['base_id'])

    client = swgohgg.Swgohgg()
    charList = client.get_from_api('characters')
    abilitiesList = client.get_from_api('abilities')
    mkCharDirs(charList)
    getCharAssets(charList)
    getAbilitiesAssets(charList, abilitiesList)
