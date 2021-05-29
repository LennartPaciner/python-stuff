import urllib, re
import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import asyncio
import random
import giphy_client
from giphy_client.rest import ApiException
from main import token
from urllib.parse import urlencode
from urllib.request import urlopen
from discord import Spotify

#Benötigte Sachen initialisieren
queue = []
anhalten = False
intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=intents)


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

#TODO ändern/testen in dass er checkt ob ich noch spotify höre oder nicht bevor er in die schleife geht
#TODO voreingestellte playlists drin haben z.b. bei !playlist rock, !playlist elektro und co ?
#TODO anleitung embedded? schreiben für befehle und features
#TODO spiele ala tic tac toe oder polls?
#TODO hardcoded sound snippets z.b. uganda stuff oder forsen bei den commands? (soundboards mäßig)
#TODO yt video zsm gucken über bot in discord - die werden ja embedded angezeigt wenn man link postet? zb. bot sagt link in chat immer der grad spielt
#TODO Autoplay - nach genre? dieser yt befehl mit info die man bekommt


@client.command()
async def spot(ctx, user: discord.Member=None):
    global queue
    global skippen
    titel = "platzhalter"
    art = "platzhalter"
    user = user or ctx.author
    voice = get(client.voice_clients, guild=ctx.guild)
    while True:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                if titel != activity.title:
                    titel = activity.title
                    art = activity.artist
                    print(f"{user} hört {activity.title} von {activity.artist}")

                    query_string = urllib.parse.urlencode({'search_query': titel + " " + art})

                    html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)

                    search_content= html_content.read().decode()

                    search_results = re.findall(r'/watch\?v=(.{11})', search_content)

                    video = (search_results[0])
                    #print(video)

                    name = ('https://www.youtube.com/watch?v=' + video)
                    await ctx.channel.send("Spielt gerade " + name)
                    queue.append(name)
                    print(queue)
                    try:
                        await voice.stop()
                        await asyncio.sleep(1)
                    except TypeError as e:
                        print(e)
                else:
                    await asyncio.sleep(5)
                    continue

@client.command()
async def gif(ctx, *, q="Bojack"):
    api_key = "6EVuFiKVwDgbM45Ayr3YwLfQUNr3QBwz"
    api_instance = giphy_client.DefaultApi()

    try:
        api_response = api_instance.gifs_search_get(api_key, q, limit=10)
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
async def add(ctx, *, name):
    global queue

    if name[:3] != "http":
        query_string = urllib.parse.urlencode({'search_query': name})

        html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)

        search_content= html_content.read().decode()

        search_results = re.findall(r'/watch\?v=(.{11})', search_content)

        video = random.choice(search_results)

        name = ('https://www.youtube.com/watch?v=' + video)

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
    global anhalten
    voice = get(client.voice_clients, guild=ctx.guild)
    try:
        anhalten = True
        await voice.pause()
    except TypeError as e:
        print(e)

@client.command()
async def resume(ctx):
    global anhalten
    voice = get(client.voice_clients, guild=ctx.guild)
    try:
        anhalten = False
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
async def playlist(ctx, name):
    global queue
    liste = []
    html_content = urllib.request.urlopen(name)

    search_content = html_content.read().decode()

    search_results = re.findall(r'/watch\?v=(.{11})', search_content)

    for i in range(0, len(search_results)):
        if search_results[i] not in liste:
            liste.append(search_results[i])

    for i in range(0, len(liste)):
        queue.append('https://www.youtube.com/watch?v=' + liste[i])


@client.command()
async def play(ctx):
    global queue
    global anhalten
    global skippen
    print(queue)
    voice = get(client.voice_clients, guild=ctx.guild)
    while len(queue) > 0:
        song = os.path.isfile("song.webm")
        print("will neues lied haben")
        try:
            if song:
                os.remove("song.webm")
                with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ydl:
                    print(queue[0])
                    try:
                        ydl.download([queue[0]])
                    except youtube_dl.utils.DownloadError as e:
                        await asyncio.sleep(3)
                        print(e)
                        ydl.download([queue[0]])
                    for file in os.listdir("./"):
                        if file.endswith(".webm"):
                            os.rename(file, "song.webm")
                    voice.play(discord.FFmpegOpusAudio(executable="C:/Users/wombo/github-privat/python-stuff/discord/ffmpeg/bin/ffmpeg.exe", source="song.webm"))
                    while voice.is_playing() or anhalten == True:
                        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=queue[0]))
                        await asyncio.sleep(1)
                    print("ist raus aus aktuellem lied")
                    print(queue)
                    queue.pop(0)
                    print(queue)
        except PermissionError as e:
            print(e)
            print("Spielt gerade.")
            #return

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
        await message.channel.send("Wann Studio offen.")
    if message.content == "!lennart":
        await message.channel.send("Der Ersteller von mir. Ziemlich lidl.")
    await client.process_commands(message)




#token aus main sonst schreit discord rum - auskommentieren für run mit eigenem token oder so
client.run(token)

