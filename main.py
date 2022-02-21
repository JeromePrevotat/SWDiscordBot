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
import locals
import servers_locals
import cmds
import embed

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

CWD = os.getcwd()
load_dotenv(dotenv_path=CWD + os.sep + '.env')
BOT_TOKEN = os.getenv('BOT_TOKEN')
ARG_CHAR_LIMIT = 50
DEFAULT_LOCAL = 'EN-US'
MAX_EMBED_LENGTH = 6000
OPTIONS_NUMBERS = ['1', '2', '3']
OPTIONS_LIST = ['-a','-t', OPTIONS_NUMBERS]
PREFIX = '%k'

###############################################################################
#                         CLASSES                                             #
###############################################################################
class KhaBot(commands.Bot):
    '''KhaBot class to dominate Discord.'''

    def __init__(self):
        #Discord related stuff
        super().__init__(command_prefix=PREFIX + ' ')
        self._intents = discord.Intents.default()
        self._intents.members=True
        self.chanList = {}
        self.guildLocals = servers_locals.SERVER_LOCALS
        #Swgoh.gg related stuff
        self.client = swgohgg.Swgohgg()
        #Activates Commands
        self.optionsNumbers = OPTIONS_NUMBERS
        self.optionsList = OPTIONS_LIST
        self.add_cog(cmds.Bot_cmds(self))
        self.add_cog(cmds.Game_cmds(self))

    # On connection
    async def on_ready(self):
        for guild in self.guilds:
            self.set_guild_locals(guild)
            for c in guild.channels:
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
                        self.chanList[guild] = c
                        await c.send(f'{self.user.display_name} has awoken !')

    async def on_guild_join(self, guild):
        """On joining a new server, sets the default local."""
        self.set_guild_locals(guild)

    def get_local_entry(self, guildId, newLocal):
        """Return a formated string to fill in servers_locals file."""
        newEntry = '\t\'{}\':\'{}\',\n'.format(
            guildId, newLocal)
        return newEntry

    def set_guild_locals(self, guild):
        """Sets locals of all server either from the server_locals file,
        or default it to EN-US if this is the first connection."""
        guildId = str(guild.id)
        # New entry if this is a new server
        if guildId not in self.guildLocals.keys():
            self.guildLocals[guildId] = locals.EN_US
            # Update the file where entries are stored
            newEntry = self.get_local_entry(guildId, self.guildLocals[guildId])
            self.update_locals_file(guildId, newEntry)

    def update_locals_file(self, guildId, newEntry=None, update=None):
        """Update the server_locals file."""
        line = ''
        #Set default Local to EN-US
        if newEntry is None:
            newEntry = get_local_entry(guildId, locals.EN_US)
        with open(os.path.join(CWD + os.sep + 'servers_locals.py'), 'r') as f:
            with open(os.path.join(
                    CWD + os.sep + 'new_servers_locals.py'), 'w+') as new_f:
                line = f.readline()
                while line != '':
                    if (update and line.strip()[1:len(guildId)+1] == guildId):
                        line = f.readline()
                    if line == '}' or line == '}\n':
                        line = f.readline()
                    new_f.write(line)
                    line = f.readline()
                new_f.write(newEntry)
                new_f.write('}')
        # Replace the old file by the new one
        os.remove(os.path.join(CWD + os.sep + 'servers_locals.py'))
        os.rename(os.path.join(CWD + os.sep + 'new_servers_locals.py'),
            os.path.join(CWD + os.sep + 'servers_locals.py'))

    def get_guild_local(self, guild):
        currentLocal = ''
        for k,v in self.guildLocals.items():
            if k == str(guild.id):
                currentLocal = v
        return locals.LOCALS[currentLocal]

    def get_localized_str(self, ctx, key):
        """Returns a localized String for Success/Failure of a Command."""
        return ctx.bot.get_guild_local(ctx.guild)[key]

    def get_localized_character(self, ctx, charName):
        """Returns the Localized Character Name.
        Default to EN-US if not yet translated."""
        name = ''
        name = ctx.bot.get_guild_local(ctx.guild)['Characters'][charName][0]
        if name == '':
            name = locals.LOCALS[DEFAULT_LOCAL]['Characters'][charName][0]
        return name

    def get_charname_from_aliases(self, ctx, charName):
        """Look up for charName into Characters Aliases.
        Returns the full name if it matches."""
        name = ''
        for c, a in ctx.bot.get_guild_local(ctx.guild)['Characters'].items():
            if charName.lower() in [alias.lower() for alias in a]:
                name = a[0]
        if name == '':
            for c, a in locals.LOCALS[DEFAULT_LOCAL]['Characters'].items():
                    if charName.lower() in [alias.lower() for alias in a]:
                        name = a[0]
        return name

    def get_localized_effect(self, ctx, effect):
        """Returns the Localized Status Effect.
        Default to EN-US if not yet translated."""
        name = ''
        name = ctx.bot.get_guild_local(ctx.guild)['Status Effects'][effect]
        if name == '':
            name = locals.LOCALS[DEFAULT_LOCAL]['Status Effects'][effect]
        return name

    async def get_cmd_arg(self, ctx):
        """Returns a list of all Arguments passed to the Command, if any.
        This list includes Options. If no Arguments, returns None."""
        channel = ctx.channel
        arg = await channel.history(limit=1).flatten()
        arg = arg[0].content
        arg = arg.split(' ')
        argList = []
        optList = []
        cmd = arg[0] + ' ' + arg[1]
        if len(arg) == 2:
            argList = None
            optList = None
        else:
            argList = arg[2:]
            optList = self.get_cmd_options(argList, ctx)
        return cmd, argList, optList

    def get_cmd_options(self, argList, ctx):
        """Returns a list of all Options passed to the Command, if any.
        Return None if no Options are passed."""
        options = []
        for arg in argList:
            if arg.startswith('-'):
                options.append(arg)
            elif arg in ctx.bot.optionsNumbers:
                options.append(arg)
            else:
                try:
                    intArg = int(arg)
                    options.append(arg)
                except ValueError:
                    pass
        if options != []:
            return options
        else:
            return None

    def get_main_arg(self, argList, optList):
        """Returns the Main Argument passed to the Command."""
        mainArg = ''
        if optList is None:
            mainArg = ' '.join(a for a in argList)
        else:
            i = 0
            while i < len(argList):
                if argList[i] not in optList:
                    mainArg += argList[i].lower() + ' '
                i += 1
        print('ARGLIST : ', argList)
        print('OPTLIST : ', optList)
        print('MAINARG : ', mainArg.strip())
        return mainArg.strip()

    async def send_embed(self, ctx, e, cmd):
        embedContent = {
            'Header':None,
            'Description': cmd,
            'Fields':[],
            'Footer':None,
            'Img':None,
            'Thumbnail':None,
        }
        if e is None:
            embedContent = embed.add_embed_content(embedContent, 'Description',
                ctx.bot.get_localized_str(ctx, 'something_went_wrong'))
            e = embed.create_embed(ctx, embedContent)
        if len(e) >= MAX_EMBED_LENGTH:
            embedContent = embed.add_embed_content(embedContent, 'Description',
                ctx.bot.get_localized_str(ctx, 'embed_too_long'))
            e = embed.create_embed(ctx, embedContent)
        await ctx.channel.send(embed=e)

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


if __name__ == '__main__':
    khabot = KhaBot()
    khabot.run(BOT_TOKEN)
