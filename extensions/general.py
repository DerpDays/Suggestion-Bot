import discord
from discord.ext import commands
from discord import utils
import asyncio
import json


class General:

    def __init__(self, bot):
        self.bot = bot


    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:

            if ctx.guild == None:
                embed = discord.Embed(color=0xffffff)
                embed.set_author(name=f'🛠 Help', icon_url=ctx.author.avatar_url)
                embed.set_footer(text=f'Type !help <command> for more info on a command • Bot made by DerpDays')
                output=""
                output += f'• `suggest` - *Suggest a improvement for the server!*\n'
                embed.add_field(name=f'General', value=output, inline=False)
                output=""
                output += f'• *Commands currently hidden, please use the command in a server!*\n'
                embed.add_field(name=f'Admin', value=output, inline=False)
                if self.bot.is_owner(ctx.author):
                    output=""
                    output += f'• `extension` - *Manage all the extensions/cogs!*\n'
                    output += f'• `bot` - *Manage the bot ex: restart/stop!*\n'
                    embed.add_field(name=f'Owner', value=output, inline=False)
                await ctx.send(embed=embed)
                return

            embed = discord.Embed(color=0xffffff)
            embed.set_author(name=f'🛠 Help', icon_url=ctx.author.avatar_url)
            embed.set_footer(text=f'Type !help <command> for more info on a command.')
            output=""
            output += f'• `suggest` - *Suggest a improvement for the server!*\n'
            embed.add_field(name=f'General', value=output, inline=False)
            if ctx.author.guild_permissions.administrator == True:
                output=""
                output += f'• `settings` - *Set the bots settings for the guild that the command is sent in!*\n'
                embed.add_field(name=f'Admin', value=output, inline=False)
            if self.bot.is_owner(ctx.author):
                output=""
                output += f'• `extension` - *Manage all the extensions/cogs!*\n'
                output += f'• `bot` - *Manage the bot ex: restart/stop!*\n'
                embed.add_field(name=f'Owner', value=output, inline=False)
            await ctx.send(embed=embed)


    @help.command(name='suggest')
    async def suggest(self, ctx):

        embed = discord.Embed(color=0xffffff)
        embed.set_author(name=f'🛠 Help', icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f'Type !help <command> for more info on a command • Bot made by DerpDays')
        embed.add_field(name=f'Suggest', value=f'Sends the command author a form to complete and the results are posted in the desired channel!', inline=False)
        await ctx.send(embed=embed)


    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @help.command(name='settings', alias="suggestsettings")
    async def suggest(self, ctx):

        embed = discord.Embed(color=0xffffff)
        embed.set_author(name=f'🛠 Help', icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f'Type !help <command> for more info on a command • Bot made by DerpDays')
        embed.add_field(name=f'settings', value=f'Configure the bots settings! \nValid Sub Commands: *output*, *toggle*, *togglepm*, *prefix*', inline=False)
        await ctx.send(embed=embed)

    @commands.is_owner()
    @help.command(name='extension')
    async def suggest(self, ctx):

        embed = discord.Embed(color=0xffffff)
        embed.set_author(name=f'🛠 Help', icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f'Type !help <command> for more info on a command • Bot made by DerpDays')
        embed.add_field(name=f'extension', value=f'Manage certain features of the bot! \nValid Sub Commands: *reload*, *load*, *unload*', inline=False)
        await ctx.send(embed=embed)


    @commands.is_owner()
    @help.command(name='bot')
    async def suggest(self, ctx):

        embed = discord.Embed(color=0xffffff)
        embed.set_author(name=f'🛠 Help', icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f'Type !help <command> for more info on a command • Bot made by DerpDays')
        embed.add_field(name=f'bot', value=f'Manage the bot! \nValid Sub Commands: *stop, *prefix*', inline=False)
        await ctx.send(embed=embed)



def setup(bot):
    bot.remove_command('help')
    bot.add_cog(General(bot))
