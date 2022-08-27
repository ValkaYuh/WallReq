import discord
import requests
from discord.ext import commands

TOKEN = ''    # Your discord bot token goes here
ApiKey = ''   # Your wallhaven api key goes here

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

client = commands.Bot(command_prefix= ">", intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    user_message = str(message.content)
    wid = ''  # Need them both to be global
    uselink = ''  # ^^^
    baselink = 'https://wallhaven.cc/api/v1/'
    msg = user_message.lower()  # Mostly to help shorten the huge if statement needed for the search function

    if message.author == client.user:   # Making sure that the bot doesn't respond to its self
        return

    if user_message.lower() == 'wr!help':       # Help command to get users started
        await message.channel.send('Commands: \nwr!r for a random image \n'
                                   'wr!rg for a random image in the general category \n'
                                   'wr!ra for a random image in the anime category \n'
                                   'wr!rp for a random image in the people category \n'
                                   'wr!t for the top image of the month \n'
                                   'wr!tg for the top image of the month in the general category \n'
                                   'wr!ta for the top image of the month in the anime category \n'
                                   'wr!tp for the top image of the month in the people category \n'
                                   'wr!rn for a random nsfw image \n'
                                   'wr!tn for the top nsfw image of the month \n'
                                   'wr!s to search for anything, e.g. "wr!s cars"')

    if msg == 'wr!r':     # RANDOM ALL
        uselink = baselink + 'search?sorting=random'

    if msg == 'wr!rg':   # RANDOM GENERAL
        uselink = baselink + 'search?sorting=random&categories=100'

    if msg == 'wr!ra':   # RANDOM ANIME
        uselink = baselink + 'search?sorting=random&categories=010'

    if msg == 'wr!rp':   # RANDOM PEOPLE
        uselink = baselink + 'search?sorting=random&categories=001'

    if msg == 'wr!t':     # TOPLIST ALL
        uselink = baselink + 'search?sorting=toplist'

    if msg == 'wr!tg':   # TOPLIST GENERAL
        uselink = baselink + 'search?sorting=toplist&categories=100'

    if msg == 'wr!ta':     # TOPLIST ANIME
        uselink = baselink + 'search?sorting=toplist&categories=010'

    if msg == 'wr!tp':     # TOPLIST PEOPLE
        uselink = baselink + 'search?sorting=toplist&categories=001'

    if msg == 'wr!rn':     # RANDOM NSFW
        uselink = baselink + 'search?apikey=' + ApiKey + '&sorting=random&purity=001'  # ApiKey is needed for nsfw stuff

    if msg == 'wr!tn':     # TOPLIST NSFW
        uselink = baselink + 'search?apikey=' + ApiKey + '&sorting=toplist&purity=001'
    # ---------------------------- API CALLS -----------------------------------------------------------
    if msg == 'wr!r' or msg == 'wr!rg' or msg == 'wr!ra' or msg == 'wr!rp' or msg == 'wr!t' or msg == 'wr!tg' or\
            msg == 'wr!ta' or msg == 'wr!tp' or msg == 'wr!rn' or msg == 'wr!tn':
        api = requests.get(f"{uselink}")  # get data from wallhaven
        if api.status_code != 200:
            await message.channel.send('Request failed with code:' f'{api.status_code}')  # Check if the request is ok

        wid = str(api.content).split(':')[2]
        wid = wid.split(',')[0]  # cut everything out except the id
        wid = wid.replace('"', '')

        msg = 'https://wallhaven.cc/w/' + wid
        await message.channel.send(f'{msg}')  # send msg with the link of the wallpaper
        return
    substring = 'wr!s'
    # ------------------------------ SEARCH -----------------------------------------------------------
    if substring in msg:  # SEARCH FUNCTION
        search = user_message[5:]  # Isolate search keywords from wr!s command

        uselink = baselink + 'search?apikey=' + ApiKey + '&sorting=random&purity=111&q=' + search
        api = requests.get(f"{uselink}")  # get data from wallhaven
        if api.status_code != 200:
            await message.channel.send('Request failed with code:' f'{api.status_code}')  # Check if the request is ok

        wid = str(api.content).split(':')[2]
        wid = wid.split(',')[0]  # cut everything out except the id
        wid = wid.replace('"', '')
        print(wid)

        msg = 'https://wallhaven.cc/w/' + wid

        if wid == '{current_page':       # Just checking if wallhaven actually found the wallpaper that we searched for
            msg = "I couldn't find a wallpaper matching that description."

        await message.channel.send(f'{msg}')  # send msg with the link of the wallpaper
        return

client.run(TOKEN)