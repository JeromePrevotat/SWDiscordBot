###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import discord
import inspect
from dotenv import load_dotenv
from discord.ext import commands

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

load_dotenv(dotenv_path="./.env/config")
BOT_TOKEN = os.getenv("BOT_TOKEN")

###############################################################################
#                         CLASSES                                             #
###############################################################################

class KhaBot(commands.Bot):
    """KhaBot class to dominate Discord."""

    def __init__(self):
        super().__init__(command_prefix="%")
        self._intents = discord.Intents.default()
        self._intents.members=True
        self.chan = None;

        # Activates all Command instances of the Bot
        members = inspect.getmembers(self)
        for name, member in members:
            if isinstance(member, commands.Command):
                if member.parent is None:
                    self.add_command(member)

    # On connection
    # Find the khabot channel and check if the Bot has r/w permissions on it
    # Then send a message to the channel when ready to interact with users
    async def on_ready(self):
        gen = self.get_all_channels()
        for chan in gen:
            if(type(chan)==discord.TextChannel
                and chan.name.lower() == "khabot"
                and chan.permissions_for(
                    member = discord.utils.find(lambda m: m.id == self.user.id, chan.guild.members)).read_messages==True
                and chan.permissions_for(
                    member = discord.utils.find(lambda m: m.id == self.user.id, chan.guild.members)).send_messages==True):
                    self.chan = chan
                    await chan.send(f"{self.user.display_name} has awoken !")
                    break;

    # Delete the last 20 messages in the Bot channel and close the Bot if Owner
    @commands.is_owner()
    @commands.command()
    async def die(ctx):
        messagesList = await ctx.bot.chan.history(limit=20).flatten()
        await ctx.bot.chan.delete_messages(messagesList)
        await ctx.bot.logout()

if __name__ == "__main__":
    khabot = KhaBot()
    khabot.run(BOT_TOKEN)
