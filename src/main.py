###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
from dotenv import load_dotenv

import khabot

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

load_dotenv(dotenv_path='../.env/config')
BOT_TOKEN = os.getenv('BOT_TOKEN')

if __name__ == '__main__':
    discordBot = khabot.bot.KhaBot()
    discordBot.run(BOT_TOKEN)
