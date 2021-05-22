###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os

import discord

import locals
import servers_locals
from datetime import datetime

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

CWD = os.getcwd()

def create_embed(ctx, dictContent):
    embed = discord.Embed(
        type='rich',
        color=discord.Colour.dark_blue(),
        #title='Test Title',
        description='placeholder',
        #url='https://cdn.discordapp.com/avatars/269317546040229889/82d89071abee5cca81606a3e0ed663a4.png?size=512',
        #timestamp = datetime.now(tz=datetime.timezone),
    )

    #embed.set_image(url='https://cdn.discordapp.com/avatars/269317546040229889/82d89071abee5cca81606a3e0ed663a4.png?size=128')
    #embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/269317546040229889/82d89071abee5cca81606a3e0ed663a4.png?size=256')
    #embed.set_author(name=ctx.bot.user.display_name, icon_url='https://cdn.discordapp.com/avatars/269317546040229889/82d89071abee5cca81606a3e0ed663a4.png?size=64')
    for k,v in dictContent.items():
        if k == 'Description' and v is not None:
            embed.description = v
        if k == 'Fields':
            for field in v:
                embed.add_field(name=field[0], value=field[1], inline=field[2])
        if k == 'Footer' and v is not None:
            embed.set_footer(
                text=v[0],
                icon_url=v[1]
            )
        if k == 'Img' and v is not None:
            embed.set_image(url=v)
        if k == 'Thumbnail' and v is not None:
            embed.set_thumbnail(url=v)
    return embed

def add_embed_content(currentContent, key, value):
    content = currentContent
    if key == 'Fields':
        content[key].append(value)
    else:
        content[key] = value
    return content

def create_field(fieldTitle, fieldContent, inline=False):
    return [fieldTitle, fieldContent, inline]
