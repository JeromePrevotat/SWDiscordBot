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
import interactions
import embed

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
        argList = await ctx.bot.get_cmd_arg(ctx)
        effect = ''
        if argList is not None:
            effect = ' '.join(str(s) for s in argList).lower()
        fieldContent = ''
        embedContent = {
            'Header':None,
            'Description':'%have ' + effect,
            'Fields':[],
            'Footer':None,
            'Img':None,
        }
        matches = []
        charList = ctx.bot.client.get_from_api('characters')
        # Find all Characters matching Arg
        if argList is not None:
            for charBaseId, charAbltList in interactions.ABLT_CLASSES.items():
                for ablt in charAbltList:
                    if effect == ablt.lower():
                        matches.append(charBaseId)
            for charBaseId in matches:
                for character in charList:
                    if charBaseId == character['base_id']:
                        fieldContent += '- ' + character['name'] + '\n'
            # Add all matches to a new Embed Field
            if len(matches) > 0:
                embedContent = embed.add_embed_content(
                    embedContent, 'Fields', embed.create_field(
                        ctx.bot.get_localized_str(ctx, 'have_success')\
                        + effect.capitalize() + ':\n', fieldContent))
            # No match found
            if len(matches) == 0 and len(argList[0]) < ARG_CHAR_LIMIT:
                embedContent = embed.add_embed_content(embedContent,
                    'Description', ctx.bot.get_localized_str(ctx, 'have_fail')\
                    + effect.capitalize() + ':\n')
        # Invalid/Missing Args
        else:
            embedContent = embed.add_embed_content(embedContent, 'Description',
                ctx.bot.get_localized_str(ctx, 'missing_arg'))
        e = embed.create_embed(ctx, embedContent)
        if e is not None:
            await ctx.channel.send(embed=e)


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
        if argList is not None and len(argList) > 0:
            args = ' '.join(s for s in argList)
            for key in locals.LOCALS.keys():
                if args.lower() == key.lower():
                    ctx.bot.guildLocals[str(ctx.guild.id)] = key
                    newEntry = ctx.bot.get_local_entry(
                        str(ctx.guild.id), newLocal=key)
                    ctx.bot.update_locals_file(
                        str(ctx.guild.id), newEntry=newEntry, update=True)
                    msg = await ctx.bot.build_msg(
                        ctx, msg,
                        ctx.bot.get_localized_str(ctx, 'local_success')
                            + ctx.bot.get_guild_local(
                        ctx.guild)[args.upper()] + '.')
            if len(msg) > 0:
                await ctx.channel.send(msg)
            else:
                msg = await ctx.bot.build_msg(
                ctx, msg, ctx.bot.get_localized_str(ctx, 'local_fail')
                    + args + '.')
                await ctx.channel.send(msg)
        else:
            msg = ctx.bot.get_localized_str(ctx, 'missing_arg')
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

    # Delete the last 20 messages in the Bot channel and close the Bot if Owner
    @commands.is_owner()
    @commands.command(
        brief='Test Command for dev purposes.',
        help="Test Command for dev purposes.")
    async def test(self, ctx):
        await ctx.channel.send(embed=embed.create_embed(ctx, ''))
