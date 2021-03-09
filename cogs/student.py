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

    #Name of the class to import in setup
class student(commands.Cog):
    #Initialisation of class
    def __init__(self, client):
        self.client = client
    #This is a event command
    @commands.Cog.listener()
    async def on_ready(self):
        print("Student is loaded")

    @commands.command()
    async def libft(self, ctx):
        embed = discord.Embed (
            colour = discord.Colour.dark_gold()
        )
        embed.add_field(name = "Libft", value = "[PDF Libft](https://cdn.intra.42.fr/pdf/pdf/17405/fr.subject.pdf)")
        await ctx.send(embed = embed)

    @commands.command()
    async def netwhat(self, ctx):
        embed = discord.Embed (
            colour = discord.Colour.dark_gold()
        )
        embed.add_field(name = "Netwhat", value = "[PDF Netwhat](https://cdn.intra.42.fr/pdf/pdf/13268/fr.subject.pdf)")
        await ctx.send(embed = embed)

    @commands.command()
    async def getnextline(self, ctx):
        embed = discord.Embed (
            colour = discord.Colour.dark_gold()
        )
        embed.add_field(name = "Get Next Line", value = "[PDF Get Next Line](https://cdn.intra.42.fr/pdf/pdf/13324/fr.subject.pdf)")
        await ctx.send(embed = embed)

    @commands.command()
    async def printf(self, ctx):
        embed = discord.Embed (
            colour = discord.Colour.dark_gold()
        )
        embed.add_field(name = "Printf", value = "[PDF Printf](https://cdn.intra.42.fr/pdf/pdf/19314/fr.subject.pdf)")
        await ctx.send(embed = embed)

    @commands.command()
    async def maxvalue(self, ctx):
        embed = discord.Embed (
            colour = discord.Colour.dark_gold()
        )
        embed.add_field(name = "C Max Values", value = "[Docs Microsoft Link](https://docs.microsoft.com/en-us/cpp/c-language/cpp-integer-limits?view=msvc-160)")
        await ctx.send(embed = embed)
    #This is a command
def setup(client):
    client.add_cog(student(client))