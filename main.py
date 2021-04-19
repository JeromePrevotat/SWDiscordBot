###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import inspect
from dotenv import load_dotenv

import discord
from discord.ext import commands

import swgohgg


###############################################################################
#                         CONSTANTS                                           #
###############################################################################

load_dotenv(dotenv_path='./.env/config')
BOT_TOKEN = os.getenv('BOT_TOKEN')

###############################################################################
#                         CLASSES                                             #
###############################################################################
class KhaBot(commands.Bot):
    '''KhaBot class to dominate Discord.'''

    def __init__(self):
        #Discord related stuff
        super().__init__(command_prefix='%')
        self._intents = discord.Intents.default()
        self._intents.members=True
        self.chanList = {}
        #Swgoh.gg related stuff
        self.client = swgohgg.Swgohgg()
        # Activates all Command instances of the Bot
        members = inspect.getmembers(self)
        for name, member in members:
            if isinstance(member, commands.Command):
                if member.parent is None:
                    self.add_command(member)

    # On connection
    async def on_ready(self):
        for g in self.guilds:
            for c in g.channels:
                if(type(c)==discord.TextChannel
                    and c.name.lower() == 'khabot'
                    and c.permissions_for(
                        member = discord.utils.find(
                            lambda m: m.id == self.user.id, c.guild.members)
                        ).read_messages==True
                    and c.permissions_for(
                        member = discord.utils.find(
                            lambda m: m.id == self.user.id, c.guild.members)
                        ).send_messages==True):
                        self.chanList[g] = c
                        await c.send(f'{self.user.display_name} has awoken !')

    def get_channel(self, ctx):
        return ctx.bot.chanList[ctx.message.channel.guild]

    async def get_cmd_arg(self, ctx):
        channel = ctx.bot.get_channel(ctx)
        charName = await channel.history(limit=1).flatten()
        charName = charName[0].content
        i = 0
        while charName[i] != ' ':
            i += 1
        return charName[i:]

    # Delete the last 20 messages in the Bot channel and close the Bot if Owner
    @commands.is_owner()
    @commands.command(
        brief='Delete last 20 messages then close khabot.',
        help="Delete the last 20 messages from khabot channel then close the \
            bot if you are it's owner. Can raise RuntimeError on Windows.")
    async def die(ctx):
        channel = ctx.bot.get_channel(ctx)
        messagesList = await channel.history(limit=20).flatten()
        await channel.delete_messages(messagesList)
        await ctx.bot.logout()

    @commands.command(
        brief='Returns a Character.',
        help='Returns a Character.')
    async def who(ctx):
        msg = ''
        charName = await ctx.bot.get_cmd_arg(ctx)
        charList = ctx.bot.client.get_from_api('characters')
        character = ctx.bot.client.get_character(charName, charList)
        for k,v in character.items():
            msg = msg + k.__str__() + ': ' + v.__str__() + '\n'
        await ctx.channel.send(msg)

    @commands.command(
        brief='Returns all the Abilities of a specified Character.',
        help='Returns all the Abilities of a specified Character.')
    async def kit(ctx):
        charKit = []
        msg = ''
        charName = await ctx.bot.get_cmd_arg(ctx)
        charList = ctx.bot.client.get_from_api('characters')
        charId = ctx.bot.client.get_character(charName, charList)['base_id']
        abilitiesList = ctx.bot.client.get_from_api('abilities')
        for ability in abilitiesList:
            if (ability['character_base_id'] == charId
                and ability['type'] in [1,2,3,4]):
                charKit.append(ability)
        for ability in charKit:
            for k,v in ability.items():
                msg = msg + k.__str__() + v.__str__() + '\n'
            msg = msg + '\n'
        await ctx.channel.send(msg)

if __name__ == '__main__':
    khabot = KhaBot()
    khabot.run(BOT_TOKEN)
