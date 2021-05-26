import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get
import youtube_dl
import os

#client = commands.Bot(command_prefix="!")
client = discord.Client()
queue = []


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

@client.event
async def on_ready():
    # print("Hallo, ich bin ein {}.".format(client.user.name))
    #client.loop.create_task(self.status_task())
    print("Bot wurde gestartet.")

async def status_task():
    while (True):
        await client.change_presence(activity=discord.Game("und schaut Hentai"))

#@client.command()
async def join(ctx):
    where = ctx.content.split(" ")[1]
    print("Trete {} bei.".format(where))
    channel = get(ctx.guild.channels, name=where)
    await channel.connect()

#!@client.command()
async def start(ctx):
    global queue
    voice = get(client.voice_clients, guild=ctx.guild)
    print(voice)
    if voice == None:
        await ctx.channel.send("Bot muss erst Voicechannel joinen.")
    song = os.path.isfile("song.webm")
    try:
        if song:
            os.remove("song.webm")
    except PermissionError:
        await ctx.channel.send("Musik spielt gerade.")
        return

    while len(queue) != 0:
        with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ydl:
            print(queue[0])
            print(queue)
            ydl.download([queue[0]])
            for file in os.listdir("./"):
                if file.endswith(".webm"):
                    os.rename(file, "song.webm")
            voice.play(discord.FFmpegOpusAudio(executable="C:/Users/wombo/github-privat/python-stuff/discord/ffmpeg/bin/ffmpeg.exe", source="song.webm"))
        queue.pop(0)


async def on_message(message):
    global queue

    if message.content == "!help":
        await message.channel.send("hilfe ist da")

    if message.content == "!disconnect":
        await message.guild.voice_client.disconnect()
        await message.channel.send('Gehe aus {}.'.format(message.channel.name))  #noch anpassen

    if message.content.startswith("!add"):
        was = message.content.split(" ")[1]
        queue.append(was)
        print(queue)


    if message.content.startswith("!play"):
        was = message.content.split(" ")[1]
        #print(was)
        queue.append(was)
        #print(queue)
        '''
        voice = get(client.voice_clients, guild=message.guild)
        print(voice)
        if voice == None:
            await message.channel.send("Bot muss erst Voicechannel joinen.")
        song = os.path.isfile("song.webm")
        try:
            if song:
                os.remove("song.webm")
        except PermissionError:
            await message.channel.send("Musik spielt gerade.")
            return

        
        while len(queue) != 0:
            with youtube_dl.YoutubeDL(self.YTDL_OPTIONS) as ydl:
                print(queue[0])
                print(queue)
                ydl.download([queue[0]])
                for file in os.listdir("./"):
                    if file.endswith(".webm"):
                        os.rename(file, "song.webm")
                voice.play(discord.FFmpegOpusAudio(executable="C:/Users/wombo/github-privat/python-stuff/discord/ffmpeg/bin/ffmpeg.exe", source="song.webm"))
            queue.pop(0)
        '''
    if message.content == "!stop":
        voice = get(client.voice_clients, guild=message.guild)
        voice.stop()

    if message.content == "!pause":
        voice = get(client.voice_clients, guild=message.guild)
        voice.pause()

    if message.content == "!resume":
        voice = get(client.voice_clients, guild=message.guild)
        voice.resume()




    #await Bot.process_commands(message)



client.run('ODQ2MTExNTUwNDg1MTY4MTkx.YKqwyQ.27PRFBImGJRRCCRq72y2F1SecAo')
