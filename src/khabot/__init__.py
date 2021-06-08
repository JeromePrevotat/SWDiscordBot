import os
import sys
if os.path.abspath(os.path.dirname(__file__)) not in sys.path:
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import servers_locals

from khabot import bot
from khabot import swgohgg
from khabot import webscrapper
from khabot import locals
from khabot import cmds
from khabot import embed
from khabot import logs
