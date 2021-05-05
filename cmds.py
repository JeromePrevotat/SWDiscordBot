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

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

ARG_CHAR_LIMIT = 50
CWD = os.getcwd()

###############################################################################
#                         CLASSES                                             #
###############################################################################

class Game_cmds(commands.Cog, name='Game Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        brief=locals.HELP_LOCAL['who_brief'],
        help=locals.HELP_LOCAL['who_help'])
    async def who(self, ctx):
        msg = 'Working on it.'
        await ctx.channel.send(msg)

    @commands.command(
        brief=locals.HELP_LOCAL['basic_brief'],
        help=locals.HELP_LOCAL['basic_help'])
    async def basic(self, ctx):
        msg = 'Working on it.'
        await ctx.channel.send(msg)

    @commands.command(
        brief=locals.HELP_LOCAL['kit_brief'],
        help=locals.HELP_LOCAL['kit_help'])
    async def kit(self, ctx):
        msg = 'Working on it.'
        await ctx.channel.send(msg)

    @commands.command(
        brief=locals.HELP_LOCAL['have_brief'],
        help=locals.HELP_LOCAL['have_help'])
    async def have(self, ctx):
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


class Bot_cmds(commands.Cog, name='Bot Commands'):
    def __init__(self, bot):
        self.bot = bot

    # Set Localisation
    @commands.command(
        brief=locals.HELP_LOCAL['local_brief'],
        help=locals.HELP_LOCAL['local_help'])
    async def local(self, ctx):
        msg = ''
        argList = await ctx.bot.get_cmd_arg(ctx)
        if len(argList) > 0:
            for key in locals.LOCALS.keys():
                if argList[0].lower() == key.lower():
                    ctx.bot.guildLocals[str(ctx.guild.id)] = key
                    newEntry = ctx.bot.get_local_entry(
                        str(ctx.guild.id), newLocal=key)
                    ctx.bot.update_locals_file(
                        str(ctx.guild.id), newEntry=newEntry, update=True)
                    msg = await ctx.bot.build_msg(
                        ctx, msg,
                        ctx.bot.get_guild_local(
                        ctx.guild)['set_local_success'])
        if len(msg) > 0:
            await ctx.channel.send(msg)
        else:
            msg = await ctx.bot.build_msg(
                ctx, msg, ctx.bot.get_guild_local(
                ctx.guild)['set_local_fail'])
            await ctx.channel.send(msg)


    # Delete the last 20 messages in the Bot channel and close the Bot if Owner
    @commands.is_owner()
    @commands.command(
        brief='Delete last 20 messages then close khabot.',
        help="Delete the last 20 messages from the channel then close the \
            bot if you are it's owner.")
    async def die(self, ctx):
        if (ctx.bot.check_channel_permissions(ctx)
            and ctx.channel.permissions_for(
            member = discord.utils.find(
                lambda m: m.id == ctx.bot.user.id, ctx.channel.guild.members)
            ).manage_messages==True):
            messagesList = await ctx.channel.history(limit=20).flatten()
            await ctx.channel.delete_messages(messagesList)
        await ctx.bot.logout()
