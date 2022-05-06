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
import feats

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
        cmd, argList, optList = await ctx.bot.get_cmd_arg(ctx)
        charName = ''
        embedContent = embed.init_embed()
        if argList is not None:
            mainArg = ctx.bot.get_main_arg(argList, optList)
            charName = mainArg
            # Find all Characters matching Arg
            charList = ctx.bot.client.get_from_api('characters')
            abltList = ctx.bot.client.get_from_api('abilities')
            basic = ''
            charBaseId = ''
            # Retrieve Character name from Aliases
            charName = ctx.bot.get_charname_from_aliases(ctx, charName)
            # Retrieve Charater Base ID
            for character in charList:
                if character['name'].lower() == charName.lower():
                    charBaseId = character['base_id']
                    charName = character['name']
            # Retrieve Character Ability
            if charBaseId != '':
                for ablt in abltList:
                    if ablt['character_base_id'] == charBaseId\
                        and ablt['type'] != swgohgg.SHIP_ABLT\
                        and ablt['type'] == swgohgg.BASIC_ABLT:
                        basic = ablt
                # Retrieve Ability Description from Swgoh.gg website
                abltHtmlDoc = webscrapper.get_html_doc('', 'ability',
                basic['url'])
                abltDesc = webscrapper.get_ablt_desc(abltHtmlDoc, basic['url'])
                # Create Embed
                embedContent = embed.add_embed_content(
                    embedContent, 'Thumbnail', basic['image'])
                embedContent = embed.add_embed_content(
                    embedContent, 'Description', cmd + ' ' + mainArg)
                fieldContent = abltDesc
                embedContent = embed.add_embed_content(
                    embedContent, 'Fields', embed.create_field(
                        ctx.bot.get_localized_str(ctx, 'basic_success')\
                        + ctx.bot.get_localized_character(ctx, charName) +\
                        ': ' + basic['name'] + '\n', fieldContent))
            # No match found
            if charBaseId == '' and len(argList[0]) < ARG_CHAR_LIMIT:
                    embedContent = embed.add_embed_content(embedContent,
                        'Description', ctx.bot.get_localized_str(ctx,
                        'basic_fail') + mainArg + '\n')
        # Invalid/Missing Args
        else:
            embedContent = embed.add_embed_content(embedContent, 'Description',
                ctx.bot.get_localized_str(ctx, 'missing_wrong_arg'))
        # Send the Embed
        e = embed.create_embed(ctx, embedContent)
        await ctx.bot.send_embed(ctx, e, cmd)

    @commands.command(
        brief=locals.HELP_LOCAL['special_brief'],
        help=locals.HELP_LOCAL['special_help'])
    async def special(self, ctx):
        cmd, argList, optList = await ctx.bot.get_cmd_arg(ctx)
        charName = ''
        matches = []
        special = ''
        charBaseId = ''
        embedContent = embed.init_embed()
        if argList is not None:
            mainArg = ctx.bot.get_main_arg(argList, optList)
            for arg in mainArg.split():
                try:
                    intArg = int(arg)
                except ValueError:
                    charName += arg + ' '
            charName = charName.strip()
            # Find all Characters matching Arg
            charList = ctx.bot.client.get_from_api('characters')
            abltList = ctx.bot.client.get_from_api('abilities')
            # Retrieve Character name from Aliases
            charName = ctx.bot.get_charname_from_aliases(ctx, charName)
            # Retrieve Charater Base ID
            for character in charList:
                if character['name'].lower() == charName.lower():
                    charBaseId = character['base_id']
                    charName = character['name']
            # Retrieve Character Special Abilities
            if charBaseId != '':
                for ablt in abltList:
                    if ablt['character_base_id'] == charBaseId\
                        and ablt['type'] != swgohgg.SHIP_ABLT\
                        and ablt['type'] == swgohgg.SPECIAL_ABLT:
                        matches.append(ablt)
            # Find the corresponding Special Ability number
            if optList is not None:
                for specialAblt in matches:
                    if specialAblt['base_id'][-1] == optList[0]:
                        special = specialAblt
                if special != '':
                    # Retrieve Ability Description from Swgoh.gg website
                    abltHtmlDoc = webscrapper.get_html_doc('', 'ability',
                    special['url'])
                    abltDesc = webscrapper.get_ablt_desc(abltHtmlDoc,
                        special['url'])
                    # Create Embed
                    embedContent = embed.add_embed_content(
                        embedContent, 'Thumbnail', special['image'])
                    embedContent = embed.add_embed_content(
                        embedContent, 'Description', cmd + ' ' + mainArg)
                    fieldContent = abltDesc
                    embedContent = embed.add_embed_content(
                        embedContent, 'Fields', embed.create_field(
                            ctx.bot.get_localized_str(ctx, 'special_success')\
                            + ctx.bot.get_localized_character(ctx, charName) +\
                            ': '+ special['name'] + '\n', fieldContent))
            # No match found
            # No character match
            if charBaseId == '' and len(argList[0]) < ARG_CHAR_LIMIT:
                embedContent = embed.add_embed_content(embedContent,
                    'Description', ctx.bot.get_localized_str(ctx,
                    'special_fail') + mainArg + '\n')
            # No ability match
            elif special == '' and optList[0] in ctx.bot.optionsNumbers:
                embedContent = embed.add_embed_content(embedContent,
                    'Description', ctx.bot.get_localized_str(ctx,
                    'less_special_fail') + '\n')
            # Out of range
            else:
                try:
                    argToInt = int(argList[0])
                    if argToInt not in ctx.bot.optionsNumbers:
                        embedContent = embed.add_embed_content(embedContent,
                            'Description', ctx.bot.get_localized_str(ctx,
                            'special_incorrect_arg'))
                except ValueError:
                    embedContent = embed.add_embed_content(embedContent,
                    'Description',ctx.bot.get_localized_str(ctx,
                    'missing_wrong_arg'))
        # Missing Arg
        else:
            embedContent = embed.add_embed_content(embedContent,
            'Description',ctx.bot.get_localized_str(ctx,'missing_wrong_arg'))
        # Send the Embed
        e = embed.create_embed(ctx, embedContent)
        await ctx.bot.send_embed(ctx, e, cmd)

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
        cmd, argList, optList = await ctx.bot.get_cmd_arg(ctx)
        effect = ''
        if argList is not None:
            effect = ctx.bot.get_main_arg(argList, optList)
        fieldContent = ''
        embedContent = embed.init_embed()
        matches = []
        charList = ctx.bot.client.get_from_api('characters')
        if charList is None:
            embedContent = embed.add_embed_content(embedContent, 'Description',
                ctx.bot.get_localized_str(ctx, 'something_went_wrong'))
            e = embed.create_embed(ctx, embedContent)
            await ctx.bot.send_embed(ctx, e, cmd)
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
                embedContent = embed.add_embed_content(embedContent,
                    'Description', cmd + ' ' + effect)
                embedContent = embed.add_embed_content(embedContent,
                    'Thumbnail', webscrapper.get_ablt_img(effect))
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
                ctx.bot.get_localized_str(ctx, 'missing_wrong_arg'))
        # Send the Embed
        e = embed.create_embed(ctx, embedContent)
        await ctx.bot.send_embed(ctx, e, cmd)

    @commands.command(
        brief=locals.HELP_LOCAL['feat_brief'],
        help=locals.HELP_LOCAL['feat_help'])
    async def feat(self, ctx):
        cmd, argList, optList = await ctx.bot.get_cmd_arg(ctx)
        filter = ''
        if argList is not None:
            filter = ctx.bot.get_main_arg(argList, optList)
        fieldTitle = ''
        fieldContent = ''
        embedContent = embed.init_embed()
        embedContent = embed.add_embed_content(embedContent, 'Description',
            cmd + ' ' + filter)
        if (filter in ['1', '2', '3', '4', '5', 'g']):
            # Sets FieldTitle & Content
            if (filter in ['1', '2', '3', '4', '5']):
                for key,value in feats.FEATS[filter].items():
                    fieldTitle = ''
                    fieldContent = ''
                    embedContent = embed.init_embed()
                    embedContent = embed.add_embed_content(embedContent,
                    'Description', cmd + ' ' + filter)
                    if key == 'Sector':
                        fieldTitle = ctx.bot.get_localized_str(
                        ctx, 'feat_success') + 'Sector ' + filter + ':\n'
                    else:
                        fieldTitle = key
                    fieldContent = value
                    embedContent = embed.add_embed_content(
                            embedContent, 'Fields', embed.create_field(
                            fieldTitle, fieldContent))
                    # Send the Embed
                    e = embed.create_embed(ctx, embedContent)
                    await ctx.bot.send_embed(ctx, e, cmd)
            elif filter == 'g':
                fieldTitle = ctx.bot.get_localized_str(ctx, 'feat_general')
                for key,value in feats.FEATS[filter].items():
                    fieldContent = value
                    embedContent = embed.add_embed_content(
                    embedContent, 'Fields', embed.create_field(
                    fieldTitle, fieldContent))
                # Send the Embed
                e = embed.create_embed(ctx, embedContent)
                await ctx.bot.send_embed(ctx, e, cmd)
        # Invalid/Missing Args
        else:
            if (argList is None or filter == ''):
                embedContent = embed.add_embed_content(embedContent,
                'Description', ctx.bot.get_localized_str(ctx, 'missing_wrong_arg'))
                # Send the Embed
                e = embed.create_embed(ctx, embedContent)
                await ctx.bot.send_embed(ctx, e, cmd)
            elif (filter not in ['1', '2', '3', '4', '5', 'g']):
                embedContent = embed.add_embed_content(embedContent,
                'Description', ctx.bot.get_localized_str(ctx, 'feat_fail'))
                # Send the Embed
                e = embed.create_embed(ctx, embedContent)
                await ctx.bot.send_embed(ctx, e, cmd)

    @commands.command(
        brief=locals.HELP_LOCAL['effects_brief'],
        help=locals.HELP_LOCAL['effects_help'])
    async def effects(self, ctx):
        cmd, argList, optList = await ctx.bot.get_cmd_arg(ctx)
        fieldContent = ''
        embedContent = embed.init_embed()
        embedContent = embed.add_embed_content(embedContent, 'Description',cmd)
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
            msg = ctx.bot.get_localized_str(ctx, 'missing_wrong_arg')
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
