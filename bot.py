import discord
import asyncio
from random import randint, choice
from discord.utils import get
import db
from selenium import webdriver
from discord.ext import commands
import json
import requests
from discord.ext.commands import Bot

des = "Someone's gotta clean up those drugs."
pref = "!"
client = discord.Client()
bot = commands.Bot(description=des, command_prefix=pref)
url = 'https://randomall.ru/api/custom/gen/758/'

@bot.event
async def on_ready():
    print("Commander, your favourite cleaner bot is now online!")
    print("Name:", bot.user.name)
    print("ID:", bot.user.id)


@bot.event
async def on_message(message):
    print(message.author, "|", message.channel, ">", message.content)
    await bot.process_commands(message)


@bot.command()
async def random(ctx):
    lst = [i for i in range(4)]
    # db = get_db()
    # quote = db.get_random_quote()
    await ctx.channel.send(lst)


@bot.command(pass_context=True) #разрешаем передавать агрументы
async def test(ctx, arg): #создаем асинхронную фунцию бота
    author = ctx.message.author
    await ctx.send(arg + author.mention) #отправляем обратно аргумент


@bot.command()
async def info(ctx):
    emb = discord.Embed(title='Info about BUNKER GAME', color=0x39d0d6)
    emb.set_author(name='Bunker-BOT')
    emb.set_thumbnail(url='https://static.mk.ru/upload/entities/2020/03/24/15/articles/detailPicture/6f/d3/83/94/e1e1b343624f272a58ab25f49576761a.jpg')
    emb.add_field(name='!send_location', value='Генерация локации')
    emb.add_field(name='!send_all', value='Отправка карточек')
    emb.add_field(name='!give_age', value='Новый возраст')
    emb.add_field(name='!give_baggage', value='Новый багаж')
    emb.add_field(name='!give_charact', value='Новая характеристика')
    emb.add_field(name='!give_dopinfa', value='Новая доп.инфа')
    emb.add_field(name='!give_gender', value='Новый пол')
    emb.add_field(name='!give_health', value='Новое здоровье')
    emb.add_field(name='!give_hobby', value='Новое хобби')
    emb.add_field(name='!give_phobia', value='Новая фобия')
    emb.add_field(name='!give_plod', value='Новая способность к детерождению')
    emb.add_field(name='!give_prof', value='Новая профессия')

    await ctx.send(embed=emb)


@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color= 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url= json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed= embed) # Отправляем Embed


####

@bot.command()
async def send_a(ctx):
    await ctx.author.send('Hello world')


@bot.command()
async def send_m(ctx, member:discord.Member):
    await member.send(f'{member.name}, priver ot')


@bot.command()
async def send_all(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        response = requests.get('https://randomall.ru/api/custom/gen/758/')
        json_data = json.loads(response.text)

        await i.send(json_data['text'])


@bot.command()
async def send_location(ctx):
    response = requests.get('https://randomall.ru/api/custom/gen/1324/')
    json_data = json.loads(response.text)
    await ctx.send(json_data['text'])


def spline(url):
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['text'].split('\n')


@bot.command()
async def give_gender(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        lst = spline(url)
        await i.send(lst[0])


@bot.command()
async def give_age(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        lst = spline(url)
        await i.send(lst[1])


@bot.command()
async def give_prof(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        lst = spline(url)
        await i.send(lst[2])


@bot.command()
async def give_plod(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        lst = spline(url)
        await i.send(lst[3])


@bot.command()
async def give_health(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        lst = spline(url)
        await i.send(lst[4])


@bot.command()
async def give_phobia(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        lst = spline(url)
        await i.send(lst[5])


@bot.command()
async def give_hobby(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        lst = spline(url)
        await i.send(lst[6])


@bot.command()
async def give_charact(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        lst = spline(url)
        await i.send(lst[7])


@bot.command()
async def give_dopinfa(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        lst = spline(url)
        await i.send(lst[8])


@bot.command()
async def give_baggage(ctx):
    channel = ctx.message.author.voice.channel

    for i in channel.members:
        lst = spline(url)
        await i.send(lst[9])


@bot.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Bot is connected {channel}')


@bot.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
        await ctx.send(f'Bot is disconnected {channel}')

@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)



if __name__ == "__main__":
    keyfile = open("key.txt", "r")
    key = keyfile.readline()
    keyfile.close()
    bot.run(key)


