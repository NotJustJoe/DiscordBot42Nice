import discord
from discord.ext import commands
from discord.utils import get
import random
import asyncio
from discord.ext.commands import Bot
import datetime
from datetime import timedelta
from datetime import date
import json
from pathlib import Path
import time
import math
import os

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin is loaded")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Wrong command, try !help for more info")

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.send(f"Hey {ctx.author.mention}, I am now logging out :wave:")
        await self.client.logout()

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def clear(self, ctx, amount= 5):
        await ctx.channel.purge(limit=amount)

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(colour=discord.Colour.dark_gold())
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name="Pool Subjects", value = "\u200b", inline=False)
        embed.add_field(name="!pool", value = "All PDFs of C Pool", inline=False)
        embed.add_field(name="Students Subjects", value = "\u200b", inline=False)
        embed.add_field(name="!libft", value = "Libft PDF")
        embed.add_field(name="!netwhat", value = "NetWhat PDF")
        embed.add_field(name="!getnextline", value = "GetNextLine PDF")
        embed.add_field(name="!ft_printf", value = "Ft_Printf PDF")
        embed.add_field(name="!cub3D", value = "Cub3D PDF")
        embed.add_field(name="!miniRT", value = "MiniRT PDF")
        embed.add_field(name="!ft_server", value = "Ft_Server PDF")
        embed.add_field(name="\u200b", value = "\u200b")
        embed.add_field(name="!intra LOGIN", value = "Vous donne accès au Discord et à votre Role.")
        embed.set_author(name = 'All commands of 42 Bot')
        await ctx.send(embed=embed)

    @commands.command()
    async def cleardm(self, amount):
        async for message in self.client.get_user(189816540089024512).history(limit=(int(amount))):
            if message.author.id == self.client.user.id:
                amount = int(amount) + 1
                await message.delete()
                await asyncio.sleep(0.5)
            elif message.author.id == self.client.user.id:
                amount = int(amount) + 1

def setup(client):
    client.add_cog(Admin(client))