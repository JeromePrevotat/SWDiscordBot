###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import inspect
import requests
from dotenv import load_dotenv

import discord
from discord.ext import commands

import servers_locals
from khabot import swgohgg, webscrapper, locals, interactions, embed

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

ARG_CHAR_LIMIT = 50
CWD = os.getcwd()
###############################################################################
#                         CLASSES                                             #
###############################################################################

class Game_cmds(commands.Cog, name='Game Commands'):
    """Commands related directly to the Game."""

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

    # DONE
    @commands.command(
        brief=locals.HELP_LOCAL['have_brief'],
        help=locals.HELP_LOCAL['have_help'])
    async def have(self, ctx):
        msg = await ctx.bot.get_channel_last_msg(ctx)
        cmd, argList, optList = ctx.bot.get_cmd_arg(msg)
        effect = ''
        if argList is not None:
            effect = ctx.bot.get_main_arg(argList, optList)
        fieldContent = ''
        embedContent = {
            'Header':None,
            'Description': cmd + ' ' + effect,
            'Fields':[],
            'Footer':None,
            'Img':None,
            'Thumbnail':webscrapper.get_ablt_img(effect),
        }
        matches = []
        charList = ctx.bot.client.get_from_api('characters')
        # Find all Characters matching Arg
        if argList is not None:
            for charBaseId, charAbltList in interactions.ABLT_CLASSES.items():
                for ablt in charAbltList:
                    if effect.lower() == ablt.lower():
                        matches.append(charBaseId)
            for charBaseId in matches:
                for character in charList:
                    if charBaseId == character['base_id']:
                        fieldContent += '- ' + ctx.bot.get_localized_character(
                        ctx, character['name']) + '\n'
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
        # Send the Embed
        e = embed.create_embed(ctx, embedContent)
        await ctx.bot.send_embed(ctx, e, cmd)

    # DONE
    @commands.command(
        brief=locals.HELP_LOCAL['effects_brief'],
        help=locals.HELP_LOCAL['effects_help'])
    async def effects(self, ctx):
        msg = await ctx.bot.get_channel_last_msg(ctx)
        cmd, argList, optList = ctx.bot.get_cmd_arg(msg)
        fieldContent = ''
        embedContent = {
            'Header':None,
            'Description': cmd,
            'Fields':[],
            'Footer':None,
            'Img':None,
            'Thumbnail':None,
        }
        matches = []
        # Find all Matches
        for k,v in interactions.ABLT_CLASSES_LIST.items():
            matches.clear()
            fieldContent = ''
            effectType = ctx.bot.get_localized_str(ctx, k)
            fieldTitle = ctx.bot.get_localized_str(ctx, 'effects_success')
            for effect in v:
                matches.append(effect)
            # Add all matches to a new Embed Field
            for effect in matches:
                fieldContent += '- ' + ctx.bot.get_localized_effect(
                    ctx, effect) + '\n'
            embedContent = embed.add_embed_content(
                embedContent, 'Fields', embed.create_field(
                    fieldTitle + effectType + ':\n', fieldContent))
        # Send the Embed
        e = embed.create_embed(ctx, embedContent)
        await ctx.bot.send_embed(ctx, e, cmd)

class Bot_cmds(commands.Cog, name='Bot Commands'):
    """Commands related to the Bot."""
    def __init__(self, bot):
        self.bot = bot

    # Set Localisation
    @commands.command(
        brief=locals.HELP_LOCAL['local_brief'],
        help=locals.HELP_LOCAL['local_help'])
    async def local(self, ctx):
        msg = await ctx.bot.get_channel_last_msg(ctx)
        cmd, argList, optList = ctx.bot.get_cmd_arg(msg)
        fieldContent = ''
        embedContent = {
            'Header':None,
            'Description': ' '.join(cmd, argList),
            'Fields':[],
            'Footer':None,
            'Img':None,
            'Thumbnail':None,
        }
        if argList is not None and len(argList) > 0:
            args = ' '.join(s for s in argList)
            # Local exists
            if args.lower() in [key.lower() for key in locals.LOCALS.keys()]:
                ctx.bot.guildLocals[str(ctx.guild.id)] = key
                newEntry = ctx.bot.get_local_entry(
                    str(ctx.guild.id), newLocal=key)
                ctx.bot.update_locals_file(
                    str(ctx.guild.id), newEntry=newEntry, update=True)
                embedContent = embed.add_embed_content(
                    embedContent, 'Fields', embed.create_field(
                        ctx.bot.get_localized_str(ctx, 'local_success')\
                        + args.capitalize() + '.', fieldContent))
            # Local is not yet implemented
            else:
                embedContent = embed.add_embed_content(
                    embedContent, 'Fields', embed.create_field(
                        ctx.bot.get_localized_str(ctx, 'local_fail')\
                        + args.capitalize() + '.\n', fieldContent))
        # Missing arguments
        else:
            embedContent = embed.add_embed_content(embedContent, 'Description',
                ctx.bot.get_localized_str(ctx, 'missing_arg'))
        # Send the embed
        e = embed.create_embed(ctx, embedContent)
        await ctx.bot.send_embed(ctx, e, cmd)

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
