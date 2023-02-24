import discord
import requests
from discord import app_commands

TOKEN = ''    # Your discord bot token goes here
ApiKey = ''   # Your wallhaven api key goes here

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = intents)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")


client = aclient()
tree = app_commands.CommandTree(client)


def top(category):
    if category == "people":
        category = category.replace("people", "001")
    elif category == "anime":
        category = category.replace("anime", "010")
    elif category == "general":
        category = category.replace("general", "100")
    elif category == "nsfw":
        category = category.replace("nsfw", "111&purity=001")
    elif category == "all":
        category = category.replace("all", "111")
    else:
        msg = "Wrong category, the only categories are: general, people, anime, nsfw and all"
        return msg

    baselink = 'https://wallhaven.cc/api/v1/'
    uselink = baselink + 'search?apikey=' + ApiKey + '&sorting=toplist&categories=' + category
    api = requests.get(f"{uselink}")  # get data from wallhaven
    response = api.json()
    if api.status_code != 200:
        msg = 'Request failed with code:' f'{api.status_code}'  # Check if the request is ok

    msg = response['data'][0]['path']  # get the id of the wallpaper from the json file
    return msg


def random(category):
    if category == "people":
        category = category.replace("people", "001")
    elif category == "anime":
        category = category.replace("anime", "010")
    elif category == "general":
        category = category.replace("general", "100")
    elif category == "nsfw":
        category = category.replace("nsfw", "111&purity=001")
    elif category == "all":
        category = category.replace("all", "111")
    else:
        msg = "Wrong category, the only categories are: general, people, anime, nsfw and all"
        return msg

    baselink = 'https://wallhaven.cc/api/v1/'
    uselink = baselink + 'search?apikey=' + ApiKey + '&sorting=random&categories=' + category
    api = requests.get(f"{uselink}")  # get data from wallhaven
    response = api.json()
    if api.status_code != 200:
        msg = 'Request failed with code:' f'{api.status_code}'  # Check if the request is ok

    msg = response['data'][0]['path']  # get the id of the wallpaper from the json file
    return msg


def search(query):
    baselink = 'https://wallhaven.cc/api/v1/'
    uselink = baselink + 'search?apikey=' + ApiKey + '&sorting=random&purity=111&q=' + query
    api = requests.get(f"{uselink}")  # get data from wallhaven
    response = api.json()
    if api.status_code != 200:
        msg = 'Request failed with code:' f'{api.status_code}'  # Check if the request is ok

    msg = response['data'][0]['path']
    return msg


@tree.command(name = "top", description = "Send the top viewed image of the month, of the specified category.(people, general, anime, nsfw)")
async def self(interaction: discord.Interaction, category: str):
    await interaction.response.send_message(top(category))


@tree.command(name = "random", description = "Send a random image of the specified category.(people, general, anime, nsfw)")
async def self(interaction: discord.Interaction, category: str):
    await interaction.response.send_message(random(category))


@tree.command(name = "search", description = "Search for a specific image.")
async def self(interaction: discord.Interaction, query: str):
    await interaction.response.send_message(search(query))


@tree.command(name = "help", description = "Send a message with instructions on how to use the bot")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("You can use the following commands: \n"
                                            "/top followed by the category \n"
                                            "/random followed by the category \n"
                                            "/search followed by your query \n"
                                            "Categories: general, people, anime, nsfw, all \n"
                                            "The top command sends the top viewed image of the month in the specific category, if you choose 'all' it will"
                                            " show the most viewed image across all categories \n"
                                            "The random command will send a randomly selected image of the specified category \n"
                                            "With the search command you can search for any type of image, just like in Goole for example :)")


@client.event
async def on_message(message):
    user_message = str(message.content)
    uselink = ''  # needs to be global
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
        response = api.json()
        if api.status_code != 200:
            await message.channel.send('Request failed with code:' f'{api.status_code}')  # Check if the request is ok

        msg = response['data'][0]['path']

        await message.channel.send(f'{msg}')  # send msg with the link of the wallpaper
        return
    # ------------------------------ SEARCH -----------------------------------------------------------
    substring = 'wr!s'
    if substring in msg:  # SEARCH FUNCTION
        search = user_message[5:]  # Isolate search keywords from wr!s command

        uselink = baselink + 'search?apikey=' + ApiKey + '&sorting=random&purity=111&q=' + search
        api = requests.get(f"{uselink}")  # get data from wallhaven
        response = api.json()
        if api.status_code != 200:
            await message.channel.send('Request failed with code:' f'{api.status_code}')  # Check if the request is ok

        msg = response['data'][0]['path']

        await message.channel.send(f'{msg}')  # send msg with the link of the wallpaper
        return

client.run(TOKEN)