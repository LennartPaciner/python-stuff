import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get
import youtube_dl
import os
import asyncio
import random
import giphy_client
from giphy_client.rest import ApiException
from main import token


queue = []
client = commands.Bot(command_prefix="!")
next = False


@client.event
async def on_ready():
    print("Bot wurde gestartet.")

YTDL_OPTIONS = {
    'format': '250',
    'extractaudio': True,
    'audioformat': 'webm',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
}

@client.command()
async def gif(ctx, *, q="Bojack"):
    api_key = "6EVuFiKVwDgbM45Ayr3YwLfQUNr3QBwz"
    api_instance = giphy_client.DefaultApi()

    try:
        api_response = api_instance.gifs_search_get(api_key, q, limit=5)
        arr = list(api_response.data)
        giff = random.choice(arr)

        await ctx.channel.send(giff.embed_url)

    except ApiException as e:
        print(e)

@client.command()
async def join(ctx, channel):
    voicechannel = get(ctx.guild.voice_channels, name=channel)
    voice = get(client.voice_clients, guild=ctx.guild)
    await voicechannel.connect()

@client.command()
async def disconnect(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    await voice.disconnect()


@client.command()
async def add(ctx, name):
    global queue
    queue.append(name)
    print(queue)

@client.command()
async def stop(ctx):
    global queue
    queue = []
    voice = get(client.voice_clients, guild=ctx.guild)
    await voice.disconnect()

@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    try:
        await voice.pause()
    except TypeError as e:
        print(e)

@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    try:
        await voice.resume()
    except TypeError as e:
        print(e)

@client.command()
async def skip(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    try:
        await voice.stop()
    except TypeError as e:
        print(e)

@client.command()
async def play(ctx):
    global queue
    global next
    print(queue)
    voice = get(client.voice_clients, guild=ctx.guild)
    while len(queue) > 0:
        song = os.path.isfile("song.webm")
        try:
            if song:
                os.remove("song.webm")
                with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ydl:
                    print(queue[0])
                    ydl.download([queue[0]])
                    for file in os.listdir("./"):
                        if file.endswith(".webm"):
                            os.rename(file, "song.webm")
                    voice.play(discord.FFmpegOpusAudio(executable="C:/Users/wombo/github-privat/python-stuff/discord/ffmpeg/bin/ffmpeg.exe", source="song.webm"))
                    while voice.is_playing():
                        await asyncio.sleep(1)
                    print(queue)
                    queue.pop(0)
                    print(queue)
        except PermissionError:
            print("Spielt gerade.")
            return

@client.event
async def on_message(message):
    if message.content == "!waldmann":
        await message.channel.send("Sollte mir mal eine Fanta kaufen.")
    if message.content == "!chris":
        await message.channel.send("Sollte mal Statistik schreiben.")
    if message.content == "!maurice":
        await message.channel.send("Wann bekommen wir unsere erste Million für unsere App?")
    if message.content == "!patrick":
        await message.channel.send("Wann wieder in Mainz PepeHands.")
    if message.content == "!marco":
        await message.channel.send("Grundschulstudium scheint das schwerste Studium von allen zu sein.")
    if message.content == "!lennart":
        await message.channel.send("Der Ersteller von mir. Ziemlich lidl.")
    await client.process_commands(message)




#token aus main sonst schreit discord rum - auskommentieren für run mit eigenem token oder so
client.run(token)

