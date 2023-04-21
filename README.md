# Overview
WallReq is a simple discord bot that sends whatever wallpapers you want it to, powered by Wallhaven's API. You can request random or the top wallpapers from various
categories (people, general, anime and NSFW). You can also search for any wallpaper.
The "wr!help" or "/help" commands will help you get started with all the commands (the bot works both with the old command method and the new slash commands).

**Note: you can get NSFW images ONLY if you put a WallHaven API key in the script, otherwise the bot remains family friendly!**

# Installation
- [Python 3.9+](https://www.python.org/downloads/)
- Install required packages (discord, requests)
> pip install discord.py\
> pip install requests
- Create the Discord bot through the [Discord Portal](https://discord.com/developers/applications), you can use [this](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) guide.
  The guide explains everything from creating the bot, to inviting it to your server.
> If you read the guide you will know that you need a permission integer, it is "68608".
- Now you can put your bot's token in the WallReq.py script.
- Next if you want the NSFW features to work you will need to create a [Wallhaven](https://wallhaven.cc/join) account and put your [APIkey](https://wallhaven.cc/settings/account) in the script.
> If you don't put in an APIkey the bot will still work normally, it will just be family friendly (wr!rn and wr!tn commands won't work, search functionality will still work, just won't show NSFW results).
- Now you can simply run the script
