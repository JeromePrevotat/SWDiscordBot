import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path="./.env/config")
BOT_TOKEN = os.getenv("BOT_TOKEN")

class KhaBot(commands.Bot):
    """KhaBot class to dominate Discord."""

    def __init__(self):
        super().__init__(command_prefix="%")
        self._intents = discord.Intents.default()
        self._intents.members=True
        self.chan = None;

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

    async def on_message(self, message):
        if (message.author.id != self.user.id and message.channel == self.chan):
            if (message.content.lower() == "kha"):
                await message.channel.send("Tar")

khabot = KhaBot()
khabot.run(BOT_TOKEN)
