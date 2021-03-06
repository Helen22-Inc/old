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

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd,activity=discord.Game(f"Находится в доме престарелых | {len(client.get_guild(711118908081569793).members)}"))
    
@client.command()
async def se(message, kuda = None, otkuda_msg = None, txt_msg = None, fm1 = None, fm2 = None, fm3 = None, fm4 = None, fm5 = None):
    if message.author.id == 378559963494088707 or message.author.id == 414119169504575509:
        kuda = int(kuda.replace('<', '').replace('>', '').replace('#', ''))
        description = await client.get_channel(743198152403714129).fetch_message(int(txt_msg))
        a = await client.get_channel(742376455329284177).fetch_message(int(otkuda_msg))

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
                try:
                    embed.set_footer(text=b[0], icon_url=b[1])
                except:
                    embed.set_footer(text=b[0])
            if b[0] == 'image':
                embed.set_image(url=b[1][1::])
        if not fm1 is None:
            fo1 = await client.get_channel(743198152403714129).fetch_message(int(fm1))
            embed.add_field(name = fo1.content.split('\n\n\n')[0], value = fo1.content.split('\n\n\n')[1], inline = False)
        if not fm2 is None:
            fo2 = await client.get_channel(743198152403714129).fetch_message(int(fm2))
            embed.add_field(name = fo2.content.split('\n\n\n')[0], value = fo2.content.split('\n\n\n')[1], inline = False)
        if not fm3 is None:
            fo3 = await client.get_channel(743198152403714129).fetch_message(int(fm3))
            embed.add_field(name = fo3.content.split('\n\n\n')[0], value = fo3.content.split('\n\n\n')[1], inline = False)
        if not fm4 is None:
            fo3 = await client.get_channel(743198152403714129).fetch_message(int(fm4))
            embed.add_field(name = fo3.content.split('\n\n\n')[0], value = fo3.content.split('\n\n\n')[1], inline = False)
        if not fm5 is None:
            fo3 = await client.get_channel(743198152403714129).fetch_message(int(fm5))
            embed.add_field(name = fo3.content.split('\n\n\n')[0], value = fo3.content.split('\n\n\n')[1], inline = False)
        await client.get_channel(kuda).send(embed=embed)

@client.command()
async def ee(message, channel_edit = None, channel_msg = None, otkuda_msg = None, txt_msg = None, fm1 = None, fm2 = None, fm3 = None, fm4 = None, fm5 = None):
    if message.author.id == 378559963494088707 or message.author.id == 414119169504575509:
        channel_edit = int(channel_edit.replace('<', '').replace('>', '').replace('#', ''))
        msg = await client.get_channel(channel_edit).fetch_message(int(channel_msg))
        description = await client.get_channel(743198152403714129).fetch_message(int(txt_msg))
        a = await client.get_channel(742376455329284177).fetch_message(int(otkuda_msg))

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
                try:
                    embed.set_footer(text=b[0], icon_url=b[1])
                except:
                    embed.set_footer(text=b[0])
        if not fm1 is None:
            fo1 = await client.get_channel(743198152403714129).fetch_message(int(fm1))
            embed.add_field(name = fo1.content.split('\n\n\n')[0], value = fo1.content.split('\n\n\n')[1], inline = False)
        if not fm2 is None:
            fo2 = await client.get_channel(743198152403714129).fetch_message(int(fm2))
            embed.add_field(name = fo2.content.split('\n\n\n')[0], value = fo2.content.split('\n\n\n')[1], inline = False)
        if not fm3 is None:
            fo3 = await client.get_channel(743198152403714129).fetch_message(int(fm3))
            embed.add_field(name = fo3.content.split('\n\n\n')[0], value = fo3.content.split('\n\n\n')[1], inline = False)
        if not fm4 is None:
            fo3 = await client.get_channel(743198152403714129).fetch_message(int(fm4))
            embed.add_field(name = fo3.content.split('\n\n\n')[0], value = fo3.content.split('\n\n\n')[1], inline = False)
        if not fm5 is None:
            fo3 = await client.get_channel(743198152403714129).fetch_message(int(fm5))
            embed.add_field(name = fo3.content.split('\n\n\n')[0], value = fo3.content.split('\n\n\n')[1], inline = False)
        await msg.edit(embed=embed)
        
@client.command() 
async def ev(message,*command):
  if message.author.id == 414119169504575509 or message.author.id === 571006178444836875:
    command = " ".join(command)
    res = eval(command)
    if inspect.isawaitable(res): 
      await message.channel.send('```py\n' + str(await res) + '```')
    else:
      await message.channel.send('```py\n' + str(res) + '```')
    
@client.command()
async def server(message):
    gg = client.get_guild(711118908081569793)
    embed = discord.Embed(title = gg.name, colour = message.author.colour, timestamp = datetime.datetime.utcnow())
    embed.add_field(name='Эмодзи', value=len(gg.emojis))
    embed.add_field(name='Владелец', value=str(gg.owner.mention))
    embed.add_field(name='Уровень верификации', value=gg.verification_level)
    embed.add_field(name='Текстовых каналов', value=len(gg.text_channels))
    embed.add_field(name='Голосовых каналов', value=len(gg.voice_channels))
    embed.add_field(name='Категорий', value=len(gg.categories))
    embed.add_field(name='<:offline:743187158398926989> Участников', value=gg.member_count)
    k = 0
    for i in gg.members:
        if str(i.status) != 'offline':
            k += 1
    embed.add_field(name='<:online:743187158205988925> Участников онлайн', value=k)
    k = 0
    for i in gg.roles:
        if i.permissions.administrator:
            k += 1
    embed.add_field(name='Ролей администрации', value=k)
    embed.add_field(name='Бустов', value=gg.premium_subscription_count)
    embed.add_field(name='Дата создания', value=str(gg.created_at).split('.')[0], inline=False)
    embed.add_field(name='឵឵឵', value=f'**[{gg.name}](https://discord.gg/pRyYNPE)**')

    embed.set_thumbnail(url=gg.icon_url)
    embed.set_footer(text='Пожилые человеки ^^', icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

client.run(tt)
