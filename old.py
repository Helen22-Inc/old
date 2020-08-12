import discord
from discord.ext import commands
from discord.utils import get
import inspect
import datetime
import random
import pymongo
import os

client = commands.Bot(command_prefix = "'")
client.remove_command("help")

tt = os.environ.get("TOKEN")

@client.command()
async def se(message, kuda = None, otkuda_channel = None, otkuda_msg = None, txt_channel = None, txt_msg = None):
    if message.author.id == 378559963494088707 or message.author.id == 414119169504575509:
        kuda = int(kuda.replace('<', '').replace('>', '').replace('#', ''))
        otkuda_channel = int(otkuda_channel.replace('<', '').replace('>', '').replace('#', ''))
        txt_channel = int(txt_channel.replace('<', '').replace('>', '').replace('#', ''))
        description = await client.get_channel(txt_channel).fetch_message(int(txt_msg))
        a = await client.get_channel(otkuda_channel).fetch_message(int(otkuda_msg))

        color, title = '000000', None
        for i in a.content.split('\n'):
            b = i.split(':::')
            if b[0] == 'color':
                color = b[1][1::]
            if b[0] == 'title':
                title = b[1][1::]
        embed = discord.Embed(title = title, description = description.content, colour = discord.Colour(int(color,16)))
        for i in a.content.split('\n'):
            b = i.split(':::')
            if b[0] == 'thumbnail':
                embed.set_thumbnail(url=b[1][1::])
            if b[0] == 'footer':
                b = b[1][1::].split('=>')
                embed.set_footer(text=b[0], icon_url=b[1])
            if b[0] == 'image':
                embed.set_image(url=b[1][1::])

        await client.get_channel(kuda).send(embed=embed)

@client.command()
async def ee(message, channel_edit = None, channel_msg = None, otkuda_channel = None, otkuda_msg = None, txt_channel = None, txt_msg = None):
    if message.author.id == 378559963494088707 or message.author.id == 414119169504575509:
        channel_edit = int(channel_edit.replace('<', '').replace('>', '').replace('#', ''))
        msg = await client.get_channel(channel_edit).fetch_message(int(channel_msg))
        otkuda_channel = int(otkuda_channel.replace('<', '').replace('>', '').replace('#', ''))
        txt_channel = int(txt_channel.replace('<', '').replace('>', '').replace('#', ''))
        description = await client.get_channel(txt_channel).fetch_message(int(txt_msg))
        a = await client.get_channel(otkuda_channel).fetch_message(int(otkuda_msg))

        color, title = '000000', None
        for i in a.content.split('\n'):
            b = i.split(':::')
            if b[0] == 'color':
                color = b[1][1::]
            if b[0] == 'title':
                title = b[1][1::]
        embed = discord.Embed(title = title, description = description.content, colour = discord.Colour(int(color,16)))
        for i in a.content.split('\n'):
            b = i.split(':::')
            if b[0] == 'thumbnail':
                embed.set_thumbnail(url=b[1][1::])
            if b[0] == 'footer':
                b = b[1][1::].split('=>')
                embed.set_footer(text=b[0], icon_url=b[1])
        await msg.edit(embed=embed)

client.run(tt)
