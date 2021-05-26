'''
#erste
x = 1
y = 2
l = [x, y]
x += 42
l3 = [x, y]

a = [1]
b = [2]
l2 = [a, b]
a.append(42)

#print(l)
#print(l2)
#print(a)
#print(l3)
'''

#zweite
def longestSubstring(s):
    head = 0
    tail = 0
    max = 0
    altes_max = 0
    text = ""
    for i in range(0, len(s)):
        head += 1
        if i < len(s) - 1 and s[i+1] in text:
            print(head)
            if max < head:
                max = head
            text += s[i]
            head = 0
        else:
            text += s[i]
        #print(text)

    print(text)
    print(max)


#print(longestSubstring("riwerhjrwethngounhgngngweptriüwetgweütewitetwetietjejtjtejjtjekitjewpgjsgsdg"))

print(longestSubstring("abcdearrqweklmrtzqvvb"))



#######
import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import asyncio


queue = []
client = commands.Bot(command_prefix="!")


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

###queue geht nocht nicht - aber ein lied
@client.command()
async def play(ctx):
    global queue
    sID = "t99ULJjCsaM"
    print(queue)

    voice = get(client.voice_clients, guild=ctx.guild)
    while len(queue) > 0:
        song = os.path.isfile("song.webm")
        print("am anfang der while schleife")
        try:
            if song:
                print("überprüfe ob song spielt")
                os.remove("song.webm")
                with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ydl:
                    print(queue[0])
                    #dictMeta = ydl.extract_info(queue[0].format(sID=sID),download=False)
                    #print(dictMeta)
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
                    #break

        except PermissionError:
            print("Spielt gerade")
            return






client.run('ODQ2MTExNTUwNDg1MTY4MTkx.YKqwyQ.27PRFBImGJRRCCRq72y2F1SecAo')




















