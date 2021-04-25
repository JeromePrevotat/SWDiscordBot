###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import inspect
import requests
from dotenv import load_dotenv

import discord
from discord.ext import commands

import swgohgg
import webscrapper

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

load_dotenv(dotenv_path='./.env/config')
BOT_TOKEN = os.getenv('BOT_TOKEN')
ARG_CHAR_LIMIT = 50

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

    async def get_cmd_arg(self, ctx):
        channel = ctx.channel
        arg = await channel.history(limit=1).flatten()
        arg = arg[0].content
        i = 0
        while arg[i] != ' ':
            i += 1
        return arg[i + 1:].split(' ')

    async def build_msg(self, ctx, msg, *arg):
        msg = msg
        for argument in arg:
            if len(msg) + len(arg) + 2 < 2000:
                msg = msg + argument + '\n'
            else:
                await arg[0].channel.send(msg)
                msg = ''
        return msg

    def check_channel_permissions(self, ctx):
        if(type(ctx.channel)==discord.TextChannel
            and ctx.channel.permissions_for(
                member = discord.utils.find(
                    lambda m: m.id == self.user.id, ctx.channel.guild.members)
                ).read_messages==True
            and ctx.channel.permissions_for(
                member = discord.utils.find(
                    lambda m: m.id == self.user.id, ctx.channel.guild.members)
                ).send_messages==True):
                return True
        return False

    async def send_msg(self, ctx, msg):
        if check_channel_permissions(ctx):
            await ctx.channel.send(msg)

    # Delete the last 20 messages in the Bot channel and close the Bot if Owner
    @commands.is_owner()
    @commands.command(
        brief='Delete last 20 messages then close khabot.',
        help="Delete the last 20 messages from the channel then close the \
            bot if you are it's owner.")
    async def die(ctx):
        if (ctx.bot.check_channel_permissions(ctx)
            and ctx.channel.permissions_for(
            member = discord.utils.find(
                lambda m: m.id == ctx.bot.user.id, ctx.channel.guild.members)
            ).manage_messages==True):
            messagesList = await ctx.channel.history(limit=20).flatten()
            await ctx.channel.delete_messages(messagesList)
        await ctx.bot.logout()

    @commands.command(
        brief='Returns a Character.',
        help='Returns a Character.')
    async def who(ctx):
        msg = 'Working on it.'
        await ctx.channel.send(msg)

    @commands.command(
        brief='Returns the Basic Ability of a specified Character.',
        help='Returns the Basic Ability of a specified Character.')
    async def basic(ctx):
        msg = 'Working on it.'
        await ctx.channel.send(msg)

    @commands.command(
        brief='Returns all the Abilities of a specified Character.',
        help='Returns all the Abilities of a specified Character.')
    async def kit(ctx):
        msg = 'Working on it.'
        await ctx.channel.send(msg)

    @commands.command(
        brief='Who interacts with a specified Status Effect.',
        help='Returns a List of Characters that have an interaction with the\
        specified Status Effect.')
    async def have(ctx):
        msg = ''
        matches = []
        charList = ctx.bot.client.get_from_api('characters')
        abltClassList = ctx.bot.client.get_ability_class_list(charList)
        argList = await ctx.bot.get_cmd_arg(ctx)
        for character in charList:
            for abltClass in character['ability_classes']:
                if argList[0].lower() == abltClass.lower():
                    matches.append(character['name'])
        if len(matches) == 0 and len(argList[0]) < ARG_CHAR_LIMIT:
            msg = 'No Character seems to interact with ' + argList[0] + '.'
        for character in matches:
            msg = await ctx.bot.build_msg(ctx, msg, character)
        if len(msg) > 0:
            await ctx.channel.send(msg)


if __name__ == '__main__':
    khabot = KhaBot()
    khabot.run(BOT_TOKEN)
