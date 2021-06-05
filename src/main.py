###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os

from dotenv import load_dotenv

import khabot

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

ENV = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    '..', '.env', 'config')
load_dotenv(dotenv_path=ENV)

BOT_TOKEN = os.getenv('BOT_TOKEN')

if __name__ == '__main__':
    discordBot = khabot.bot.KhaBot()
    discordBot.run(BOT_TOKEN)
