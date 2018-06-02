import discord
from discord.ext import commands
from discord import utils
import asyncio
import json

class Settings():

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='settings', aliases=["suggestsettings", "suggestsetting"])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def settings(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f':tools: Settings', color=0xffffff)
            embed.add_field(name=f'Invalid syntax! **{ctx.prefix}settings <sub-command>**', value=f'Valid sub-commands: *toggle*, *output*, *prefix*, *togglepm*')
            await ctx.send(embed=embed)
            return


    @settings.command(name="toggle")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def toggle(self, ctx):
            if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLED"] == "ON":
                self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLED"] = "OFF"
                with open('settings.json', 'w') as f:
                    json.dump(self.bot.config, f, indent=2)
                    await ctx.send(f'Disabled suggestions for the public!')
                    return

            if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLED"] == "OFF":
                self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLED"] = "ON"
                with open('settings.json', 'w') as f:
                    json.dump(self.bot.config, f, indent=2)
                    await ctx.send(f'Opened suggestions to the public!')
                    return

    @settings.command(name="togglepm")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def togglepm(self, ctx):

        if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLEPM"] == "ON":
            self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLEPM"] = "OFF"
            with open('settings.json', 'w') as f:
                json.dump(self.bot.config, f, indent=2)
                await ctx.send(f'Suggestions will now be made in the command author''s private messages.')
                return

        if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLEPM"] == "OFF":
            self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLEPM"] = "ON"
            with open('settings.json', 'w') as f:
                json.dump(self.bot.config, f, indent=2)
                await ctx.send(f'Suggestions will now be made in the text channel the command was executed from.')
                return


    @settings.command(name="output")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def output(self, ctx, output: str = None):

        if output == None:
            embed = discord.Embed(title=":tools: Settings", color=0xffffff)
            embed.add_field(name=f'Invalid syntax! **{ctx.prefix}settings output <channel-id>**', value=f'The channel you entered was invalid. Please try again! [**How to get a channel id!**](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-server-ID-)')
            await ctx.send(embed=embed)
            return

        try:
            channel = discord.utils.get(ctx.guild.text_channels, id=int(output))
            await channel.send(f'Suggestions will now be sent here!')
        except:
            embed = discord.Embed(title=f':tools: Settings', color=0xffffff)
            embed.add_field(name=f'Invalid syntax! **{ctx.prefix}settings output <channel-id>**', value=f'The channel you entered was invalid. Please try again! [**How to get a channel id!**](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-server-ID-)')
            await ctx.send(embed=embed)
            return

        self.bot.config["GUILDS"][str(ctx.guild.id)]["OUTPUT"] = output
        with open('settings.json', 'w') as f:
            json.dump(self.bot.config, f, indent=2)
            channel = discord.utils.get(ctx.guild.text_channels, id=int(self.bot.config["GUILDS"][str(ctx.guild.id)]["OUTPUT"]))
            await ctx.send(f'The output channel was changed to: {channel.mention}')
            return


    @settings.command(name="prefix")
    @commands.guild_only()
    async def prefix(self, ctx, newprefix: str = None):

        if newprefix == None:
            embed = discord.Embed(title=f':tools: Settings', color=0xffffff)
            embed.add_field(name=f'Invalid syntax! **{ctx.prefix}settings prefix <newprefix>**', value=f'Please enter a valid prefix ex: **!**')
            await ctx.send(embed=embed)
            return


        self.bot.config["GUILDS"][str(ctx.guild.id)]["PREFIX"] = newprefix
        with open('settings.json', 'w') as f:
            json.dump(self.bot.config, f, indent=2)
            await ctx.send(f'Changed **{ctx.guild.name}**''s prefix to: **{}**'.format(newprefix))
            return

def setup(bot):
    bot.add_cog(Settings(bot))
