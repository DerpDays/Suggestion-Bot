import discord
from discord.ext import commands
from discord import utils
import asyncio
import time
import json

extensions = ["settings", "developer", "suggest", "general"]

def get_prefix(bot, message):
    """Get the prefixes."""
    gprefix = client.config["GLOBAL"]["PREFIX"]
    if message.guild is None:
        extras = gprefix
        return commands.when_mentioned_or(*extras)(bot, message)
    prefix = client.config["GUILDS"][str(message.guild.id)]["PREFIX"]
    extras = [prefix, gprefix]
    return commands.when_mentioned_or(*extras)(bot, message)


client = commands.Bot(command_prefix=get_prefix, case_insensitive=True)

with open('settings.json', 'r') as f:
    client.config = json.load(f)


async def add_guild():
    if not "GUILDS" in client.config:
            client.config["GUILDS"] = {}
    for guild in client.guilds:
        gid = str(guild.id)
        if gid not in client.config["GUILDS"]:
            client.config["GUILDS"][gid] = {
            "TOGGLED": "ON",
            "TOGGLEPM": "OFF",
            "OUTPUT": None,
            "ID": "1",
            "PREFIX": "!"
            }
            print(f"Added new server to the config file ({guild.name})")
            with open('settings.json', 'w') as f:
                json.dump(client.config, f, indent=2)



@client.event
async def on_guild_join(guild):
    await add_guild()
    embed = discord.Embed(title=f':tools: Suggestion Bot', color=0xffffff)
    embed.add_field(name=f'Thanks for adding suggestion bot {guild.owner.name}!', value=f'To configure the bot use **!settings** in a server text channel. To see the available commands do: **!help**, \nplease make sure the bot has the following permission: `Administrator` or the following: `Manage messages`, `Add reactions`, `Read messages`, `Send messages`, `Read message history`, `Embed links` and `Attach file`')
    await guild.owner.send(embed=embed)


@client.event
async def on_ready():
    print('-------------------------------------------------------------')
    print('Bot created by @DerpDays')
    print('Updated to the discord rewrite by @AdamAtomus')
    print('You may not remove the credit,')
    print('However you can expand the bot.')
    print('If you have any issues please contact me on discord')
    print('Or create a issue on GitHub')
    print('-------------------------------------------------------------')
    await add_guild()


if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension("extensions." + extension)
        except Exception as e:
            print("")
            print("TRACEBACK")
            print("--------------------------------")
            print(e)
            print("--------------------------------")
            print('Failed to load extension {}'.format(extension))
            print("")

try:
    client.run(client.config["GLOBAL"]["TOKEN"], bot=True, reconnect=True)
except:
    print("---------------------------------------------------------------------")
    print("INVALID TOKEN, PLEASE EDIT THE TOKEN FIELD IN SETTINGS.JSON")
    print("---------------------------------------------------------------------")
    time.sleep(10)
