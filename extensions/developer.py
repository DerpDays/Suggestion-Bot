import discord
from discord.ext import commands
from discord import utils
import asyncio
import json


class Developers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot




    @commands.group()
    @commands.is_owner()
    async def extension(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f':tools: Extensions', color=0xffffff)
            embed.add_field(name=f'Invalid syntax! **{ctx.prefix}extension <sub-command>**', value=f'Valid sub-commands: *reload*, *load*, *load*')
            await ctx.send(embed=embed)
            return


    @extension.command(name='load')
    @commands.is_owner()
    async def load(self, ctx, *, extension: str = None):
        """Load a extension!"""

        if extension == None:
            embed = discord.Embed(title=f':tools: Extensions', color=0xffffff)
            embed.add_field(name=f'Invalid syntax! **{ctx.prefix}extension load <extension>**', value=f'Please enter a valid extension ex: **suggest**')
            await ctx.send(embed=embed)
            return

        try:
            self.bot.load_extension(f'extensions.' + extension)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** Could not load {extension}')
            await ctx.send(f'=========================================')
            await ctx.send(f'```{e}```')
        else:
            await ctx.send('**`SUCCESS`** Loaded extension: *{extension}*')

    @extension.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx, *, extension: str = None):
        """Unload a extension!"""

        if extension == None:
            embed = discord.Embed(title=f':tools: Extensions', color=0xffffff)
            embed.add_field(name=f'Invalid syntax! **{ctx.prefix}extension unload <extension>**', value=f'Please enter a valid extension ex: **suggest**')
            await ctx.send(embed=embed)
            return

        try:
            self.bot.unload_extension(f'extensions.' + extension)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** Could not unload {extension}')
            await ctx.send(f'=========================================')
            await ctx.send(f'```{e}```')
        else:
            await ctx.send(f'**`SUCCESS`** Unloaded extension: *{extension}*')

    @extension.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx, *, extension: str = None):
        """Reload a extension!"""

        if extension == None:
            embed = discord.Embed(title=f':tools: Extensions', color=0xffffff)
            embed.add_field(name=f'Invalid syntax! **{ctx.prefix}extension reload <extension>**', value=f'Please enter a valid extension ex: **suggest**')
            await ctx.send(embed=embed)
            return

        try:
            self.bot.unload_extension(f'extensions.' + extension)
            self.bot.load_extension(f'extensions.' + extension)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** Could not reload {extension}')
            await ctx.send(f'=========================================')
            await ctx.send(f'```{e}```')
        else:
            await ctx.send(f'**`SUCCESS`** Reloaded extension: *{extension}*')

    @commands.group(name="bot")
    @commands.is_owner()
    async def bots(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f':tools: Bot Tools', color=0xffffff)
            embed.add_field(name=f'Invalid syntax! **{ctx.prefix}bot <sub-command>**', value=f'Valid sub-commands: *stop*')
            await ctx.send(embed=embed)
            return


    @bots.command(name='stop', alias="restart")
    @commands.is_owner()
    async def stop(self, ctx):
        """Stops/Restarts the bot."""

        await ctx.send(f'Stopping the bot!')
        await self.bot.logout()


    @bots.command(name="prefix")
    async def prefix(self, ctx, newprefix: str = None):

        if newprefix == None:
            embed = discord.Embed(title=f':tools: Settings', color=0xffffff)
            embed.add_field(name=f'Invalid syntax! **{ctx.prefix}bot prefix <newprefix>**', value=f'Sets the global backup prefix, please enter a valid prefix ex: **!**')
            await ctx.send(embed=embed)
            return



        self.bot.config["GLOBAL"]["PREFIX"] = newprefix
        with open('settings.json', 'w') as f:
            json.dump(selg.bot.config, f, indent=2)
            await ctx.send('Changed the global backup prefix to: **{}**'.format(newprefix))
            return

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, discord.ext.commands.NoPrivateMessage):
            await ctx.send(f':no_entry: This command can only be used inside a server!')
            return
        if isinstance(error, discord.ext.commands.NotOwner):
            await ctx.send(f':no_entry: You do not have permission to use this command!')
            return
        if isinstance(error, discord.ext.commands.MissingPermissions):
            await ctx.send(f':no_entry: You do not have permission to use this command!')
            return
        if isinstance(error, discord.ext.commands.BotMissingPermissions):
            await ctx.send(":no_entry: The bot does not have sufficient permissions to run this command, please contact the guild owner about this!")
            await ctx.guild.owner.send(f':no_entry: The bot does not have sufficient permissions to run command: {ctx.prefix}{ctx.name}, please make sure the bot has the following permissions: `Administrator` or the following: `Manage messages`, `Add reactions`, `Read messages`, `Send messages`, `Read message history`, `Embed links` and `Attach file`')
            return

        await ctx.send(f'**`ERROR:`** Error while running the command **{ctx.prefix}{ctx.command.qualified_name}**')
        await ctx.send(f'=========================================')
        await ctx.send(f'```{error}```')


def setup(bot):
    bot.add_cog(Developers(bot))
