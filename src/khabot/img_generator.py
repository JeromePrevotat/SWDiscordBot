###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import requests
from PIL import Image, ImageDraw, ImageFont


ASSETS_PATH = os.path.join(os.getcwd() + os.sep + 'assets')
CHARACTERS_ASSETS = os.path.join(ASSETS_PATH + os.sep + 'characters')
ABILITIES_ASSETS = os.path.join(ASSETS_PATH + os.sep + 'abilities')
FONTS_PATH = os.path.join(ASSETS_PATH + os.sep + 'fonts')
FILE_FORMAT = '.png'

if __name__ == '__main__':
    # Get ALL Image
        # Get Icon Image
        #filename = url[:len(url)-1].split('/')[-1]
    try:
        icon = Image.open(os.path.join(
        ABILITIES_ASSETS + os.sep + 'BOSSK'
        + os.sep + 'basicskill_BOSSK' + FILE_FORMAT))
    except OSError as error:
        print(error)
        # Get Title Image from Text
            #Create Image from Text
    abltTitle = Image.new('RGB', (200, 50), color=(25,25,25))
    d = ImageDraw.Draw(abltTitle)
    fnt = ImageFont.truetype(os.path.join(
        FONTS_PATH + os.sep + 'arial.ttf'), 20)
    d.text((10,35), 'Bossk Basic Skill',
        font=fnt, fill=(255,255,255), anchor='ms')


    abltTitle.save(os.path.join(
        ASSETS_PATH + os.sep + 'misc'
        + os.sep + 'abltTitle' + FILE_FORMAT))
        # Get Description Image
            # Create Image from Text
    # Create Template
    # Fill Template
