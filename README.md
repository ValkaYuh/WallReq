# Overview
WallReq is a simple discord bot that sends whatever wallpapers you want it to, powered by Wallhaven's API. You can request random or the top wallpapers from various
categories (people, general, anime and NSFW). You can also search for any wallpaper.
The "wr!help" command will help you get started with all the commands. They are also listed bellow:

> wr!r for a random image\
> wr!rg for a random image in the general category\
> wr!ra for a random image in the anime category\
> wr!rp for a random image in the people category\
> wr!t for the top image of the month\
> wr!tg for the top image of the month in the general category\
> wr!ta for the top image of the month in the anime category\
> wr!tp for the top image of the month in the people category\
> wr!rn for a random nsfw image\
> wr!tn for the top nsfw image of the month\
> wr!s to search for anything, e.g. "wr!s cars"

# Installation
- [Python 3.9+](https://www.python.org/downloads/)
- Install required packages (discord, requests)
> pip install discord.py
> pip install requests
- Create the Discord bot through the [Discord Portal](https://discord.com/developers/applications), you can use [this](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)guide.
  The guide explains everything from creating the bot, to inviting it to your server.
> If you read the guide you will know that you need a permission integer, it is "68608".
- Now you can put your bot's token in the WallReq.py script.
- Next if you want the NSFW features to work you will need to create a [Wallhaven](https://wallhaven.cc/join) account and put your [APIkey](https://wallhaven.cc/settings/account) in the script.
> If you don't put in an APIkey the bot will still work normally, it will just be family friendly.
- Now you can simply run the script
